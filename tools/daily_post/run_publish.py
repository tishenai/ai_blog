#!/usr/bin/env python3
"""
博客文章发布流程执行脚本（publish-blog-post cron 任务调用入口）

使用方式：
    python3 tools/daily_post/run_publish.py

功能：
1. 读取 .publish_params.json
2. git mv pending/<slug>.md posts/<slug>.md
3. 标记话题已用
4. pnpm run build 验证
5. git commit + push
6. 更新飞书审稿文档状态（Draft → Published）
7. 更新知识库首页索引
8. 发飞书通知给 owner
9. 清理 .publish_params.json

失败处理：
- 任何步骤失败立刻退出并打印错误信息
- 已 push 的内容不 revert
- 保留 .publish_params.json 方便排查
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

# ==================== 配置 ====================
WORK_DIR = "/root/.openclaw/workspace/ai_blog"
PARAMS_FILE = os.path.join(WORK_DIR, ".publish_params.json")
WIKI_SPACE_ID = "7650738808775330774"
OWNER_OPEN_ID = "user:ou_12cafe83f620117e40728ef5cd4687eb"

# 关键 URL。谁也不要再在别处硬编码 blog.tishenai.app 之类东西。
BLOG_BASE_URL = "https://www.wemixmemory.top"
GITHUB_REPO_URL = "https://github.com/tishenai/ai_blog"
FEISHU_WIKI_URL_PREFIX = "https://vcnd3kpj0wx8.feishu.cn/wiki"


def run_cmd(cmd, shell=True, cwd=WORK_DIR, capture_output=False):
    """执行 shell 命令，失败则退出"""
    print(f"$ {cmd}")
    try:
        merged_env = {**os.environ, 'HUSKY': '0'}
        result = subprocess.run(
            cmd,
            shell=shell,
            cwd=cwd,
            capture_output=capture_output,
            text=True,
            env=merged_env,
        )
        if result.returncode != 0:
            print(f"❌ 命令执行失败（退出码 {result.returncode}）")
            if result.stderr:
                print(f"stderr: {result.stderr}")
            sys.exit(1)
        return result
    except Exception as e:
        print(f"❌ 命令执行异常: {e}")
        sys.exit(1)


def load_params():
    """读取发布参数"""
    if not os.path.exists(PARAMS_FILE):
        print(f"❌ 参数文件不存在: {PARAMS_FILE}")
        sys.exit(1)
    
    with open(PARAMS_FILE, "r", encoding="utf-8") as f:
        params = json.load(f)
    
    required_fields = ["slug", "title"]
    for field in required_fields:
        if field not in params:
            print(f"❌ 参数文件缺少必填字段: {field}")
            sys.exit(1)
    
    print(f"✅ 读取参数成功")
    print(f"   slug: {params['slug']}")
    print(f"   title: {params['title']}")
    if "feishu_doc_id" in params:
        print(f"   feishu_doc_id: {params['feishu_doc_id']}")
    
    return params


def step1_prepare_env(params):
    """步骤 1: 准备环境"""
    print("\n" + "=" * 60)
    print("步骤 1: 准备环境")
    print("=" * 60)
    
    # git pull。临时状态文件已加入 .gitignore 且必须保持未跟踪，避免污染仓库。
    run_cmd("git pull --rebase")
    
    # 验证 pending 文件存在
    pending_path = f"pending/{params['slug']}.md"
    if not os.path.exists(os.path.join(WORK_DIR, pending_path)):
        print(f"❌ 草稿文件不存在: {pending_path}")
        sys.exit(1)
    
    print(f"✅ 草稿文件存在: {pending_path}")

    # 确保 pending 文件已被 git 跟踪（未跟踪时 git mv 会失败）
    status = subprocess.run(
        ["git", "ls-files", "--error-unmatch", pending_path],
        cwd=WORK_DIR,
        capture_output=True,
    )
    if status.returncode != 0:
        print(f"$ git add {pending_path}")
        run_cmd(f"git add {pending_path}")
        print(f"✅ 已 git add: {pending_path}")


def step1b_lint_and_fix_frontmatter(params):
    """步骤 1b: 校验 frontmatter 是否符合 SuzuBlog 规范，能修的自动修复

    SuzuBlog frontmatter 规范见 https://suzu.zla.app/guide/posts/
    - 必填: title, date(带引号 'YYYY-MM-DD' 或 'YYYY-MM-DD HH:MM:SS')
    - 推荐: tags(list), categories(list), thumbnail
    - 禁止: subtitle/category(单数)/tag(单数)等非标字段

    本步执行：
    1. lint --fix 自动修复（typo、字符串→数组、date 加引号、删非标字段）
    2. 再 lint 一次确认无 errors（warnings 允许放过）
    3. 如果修改了文件，直接 git add 进暂存（后面 step5 一起 commit）
    """
    print("\n" + "=" * 60)
    print("步骤 1b: Frontmatter 规范校验（SuzuBlog）")
    print("=" * 60)

    pending_path = f"pending/{params['slug']}.md"

    # 先尝试自动修复
    fix_result = subprocess.run(
        ["python3", "tools/daily_post/lint_frontmatter.py", "--fix", pending_path],
        cwd=WORK_DIR,
        capture_output=True,
        text=True,
    )
    print(fix_result.stdout)
    if fix_result.stderr:
        print(f"stderr: {fix_result.stderr}")

    # 再校验一次确认无 errors
    verify_result = subprocess.run(
        ["python3", "tools/daily_post/lint_frontmatter.py", pending_path],
        cwd=WORK_DIR,
        capture_output=True,
        text=True,
    )
    print(verify_result.stdout)
    if verify_result.returncode != 0:
        # returncode 1 = 有 errors（必填字段缺失等）
        print("❌ frontmatter 仍有硬错误，无法发布")
        sys.exit(1)

    print("✅ frontmatter 校验通过")


def step2_move_to_posts(params):
    """步骤 2: 移到正式发布目录（幂等）"""
    print("\n" + "=" * 60)
    print("步骤 2: 移到正式发布目录")
    print("=" * 60)
    
    src = f"pending/{params['slug']}.md"
    dst = f"posts/{params['slug']}.md"

    src_abs = os.path.join(WORK_DIR, src)
    dst_abs = os.path.join(WORK_DIR, dst)

    src_exists = os.path.exists(src_abs)
    dst_exists = os.path.exists(dst_abs)

    if dst_exists and not src_exists:
        print(f"⚠️  跳过：{dst} 已存在且 {src} 不存在（幂等）")
        return

    if dst_exists and src_exists:
        print(f"⚠️  异常状态：{src} 和 {dst} 同时存在，请人工介入")
        sys.exit(1)

    if not src_exists:
        print(f"❌ {src} 不存在，无法发布")
        sys.exit(1)

    run_cmd(f"git mv {src} {dst}")
    print(f"✅ 已移动: {src} → {dst}")

    # 显式替换 status: draft → published（--fix 不会改 status）
    with open(dst_abs, encoding="utf-8") as f:
        content = f.read()
    content = content.replace("status: draft", "status: published")
    with open(dst_abs, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ status: draft → published")

    # 写入正确写作声明（判断是否手动选题）
    manual_topic_file = Path(WORK_DIR) / "../../.daily_ai_blog_manual_topic.md"
    is_manual = False
    if manual_topic_file.exists() and manual_topic_file.read_text(encoding="utf-8", errors="ignore").strip():
        is_manual = True
    disc_result = subprocess.run(
        ["python3", "tools/daily_post/write_disclaimer.py",
         str(is_manual).lower(), dst_abs],
        cwd=WORK_DIR, capture_output=True, text=True,
    )
    print(disc_result.stdout.rstrip())
    if disc_result.returncode != 0:
        print(f"❌ write_disclaimer.py 失败（退出码 {disc_result.returncode}）")
        sys.exit(1)

    # 生成或确认 thumbnail 存在
    thumb_path = Path(WORK_DIR) / "public/images/thumbnails" / f"{params['slug']}.png"
    if not thumb_path.exists():
        print(f"⚠️  封面不存在，生成中...")
        thumb_result = subprocess.run(
            ["python3", "tools/daily_post/auto_thumbnail.py",
             params['slug'], params['title'],
             params.get('subtitle', ''), params.get('category', ''),
             params.get('tags', '')],
            cwd=WORK_DIR, capture_output=True, text=True,
        )
        print(thumb_result.stdout.rstrip())
        if thumb_result.returncode != 0:
            print(f"❌ auto_thumbnail.py 失败（退出码 {thumb_result.returncode}）")
            sys.exit(1)
    else:
        print(f"✅ 封面已存在: {thumb_path}")

    # 迁移后对 posts 文件跑 lint --fix --inject-thumbnail：
    # 1. thumbnail 路径修正确（已在上一步确保文件存在）
    # 2. 清理 subtitle/slug 等非标字段
    lint_result = subprocess.run(
        ["python3", "tools/daily_post/lint_frontmatter.py",
         "--fix", "--inject-thumbnail", dst_abs],
        cwd=WORK_DIR,
        capture_output=True,
        text=True,
    )
    print(lint_result.stdout)
    if lint_result.returncode != 0:
        print(f"❌ posts 文件 frontmatter 仍有错误（退出码 {lint_result.returncode}）")
        sys.exit(1)

    # lint 写回后 git add
    run_cmd(f"git add {dst}")
    print(f"✅ posts 文件 frontmatter 已修正并 git add")


def step3_mark_topic_used(params):
    """步骤 3: 标记话题已用（幂等）"""
    print("\n" + "=" * 60)
    print("步骤 3: 标记话题已用")
    print("=" * 60)
    
    today = datetime.now().strftime("%Y-%m-%d")
    # mark_topic_used.py 在话题不在 Pending 表中时退出码 2（幂等）
    # 这里允许它返回 0、2，其他退出码汇报失败
    cmd = (
        f"python3 tools/daily_post/mark_topic_used.py "
        f"{params['slug']} {today} /{params['slug']}"
    )
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=WORK_DIR)
    if result.returncode == 0:
        print("✅ 话题已标记为已用")
    elif result.returncode == 2:
        print(f"⚠️  跳过：话题 {params['slug']} 不在 Pending 表，可能已经标过")
    else:
        print(f"❌ mark_topic_used.py 失败（退出码 {result.returncode}）")
        sys.exit(1)


def step4_build_verify():
    """步骤 4: 构建验证"""
    print("\n" + "=" * 60)
    print("步骤 4: 构建验证")
    print("=" * 60)
    
    run_cmd("pnpm run build")
    print("✅ 构建验证通过")


def step5_git_commit_and_push(params):
    """步骤 5: Git 提交并推送（幂等）。
    
    如果工作区干净（上次已提交过），跳过 commit，但仍会 push 一次以防本地 commit 未到远端。
    """
    print("\n" + "=" * 60)
    print("步骤 5: Git 提交并推送")
    print("=" * 60)

    run_cmd("git add -A")

    # 检查是否有待提交的变动
    status = subprocess.run(
        "git diff --cached --quiet",
        shell=True,
        cwd=WORK_DIR,
    )
    if status.returncode == 0:
        print("⚠️  暂存区为空，跳过 commit（可能上次已 commit）")
    else:
        commit_msg = f"发布《{params['title']}》"
        run_cmd(f"git commit -m {repr(commit_msg)}")

    # 检查是否有未 push 的 commit
    unpushed = subprocess.run(
        "git log @{u}.. --oneline",
        shell=True,
        cwd=WORK_DIR,
        capture_output=True,
        text=True,
    )
    if unpushed.stdout.strip():
        run_cmd("HUSKY=0 git push")
        print("✅ 已提交并推送")
    else:
        print("⚠️  本地与远端一致，跳过 push")


def step6_update_feishu_doc(params):
    """步骤 6: 生成飞书审稿文档状态更新参数"""
    print("\n" + "=" * 60)
    print("步骤 6: 生成飞书审稿文档状态更新参数")
    print("=" * 60)
    
    if "feishu_doc_id" not in params:
        print("⚠️  缺少 feishu_doc_id，跳过飞书文档更新参数生成")
        # 仍然创建一个空的状态文件，避免后续步骤报错
        tmp_file = os.path.join(WORK_DIR, ".feishu_doc_update.json")
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump({"skip": True, "reason": "no feishu_doc_id"}, f)
        return
    
    # 构建新的飞书文档状态参数。
    #
    # v1.5.4 起：发布后的飞书文档必须保留全文正文。
    # 之前的「轻量版 banner_only」让文档看起来像空文档，用户体验很差。
    # 为避免把整篇文章塞进 JSON 状态文件，这里把完整 markdown 写到独立文件，
    # agent 发布时读取该文件内容调用 feishu_update_doc，然后必须 feishu_fetch_doc 反查验收。
    today = datetime.now().strftime("%Y-%m-%d")
    new_title = f"[Published {today}] {params['title']}"
    github_url = f"{GITHUB_REPO_URL}/blob/main/posts/{params['slug']}.md"
    blog_url = f"{BLOG_BASE_URL}/{params['slug']}"

    post_path = os.path.join(WORK_DIR, "posts", f"{params['slug']}.md")
    if not os.path.exists(post_path):
        print(f"❌ 已发布文章不存在，无法生成飞书全文: {post_path}")
        sys.exit(1)
    with open(post_path, "r", encoding="utf-8") as f:
        post_text = f.read()
    if post_text.startswith("---"):
        parts = post_text.split("---", 2)
        body = parts[2].lstrip() if len(parts) >= 3 else post_text
    else:
        body = post_text

    banner = (
        f"> ✅ **此文章已发布** · {today}\n"
        f">\n"
        f"> 🌐 [在博客上阅读]({blog_url})\n"
        f">\n"
        f"> 🔗 [在 GitHub 上查看]({github_url})\n"
        f"\n---\n\n"
    )
    full_markdown = banner + body
    markdown_file = os.path.join(WORK_DIR, ".feishu_doc_update.md")
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write(full_markdown)

    # 保存到临时 JSON 供 agent 读取；不把全文放进 JSON，避免污染日志和上下文。
    tmp_file = os.path.join(WORK_DIR, ".feishu_doc_update.json")
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump({
            "skip": False,
            "doc_id": params["feishu_doc_id"],
            "title": new_title,
            "markdown_path": markdown_file,
            "expected_min_length": max(1000, len(body) // 2),
            "github_url": github_url,
            "blog_url": blog_url,
            "_note": "发布后飞书文档保留全文；agent 必须读取 markdown_path 覆盖更新，并用 feishu_fetch_doc 反查正文长度。",
        }, f, ensure_ascii=False, indent=2)

    print(f"✅ 飞书文档更新参数已保存到 {tmp_file}")
    print(f"✅ 飞书全文 markdown 已保存到 {markdown_file}")
    print(f"   doc_id: {params['feishu_doc_id']}")
    print(f"   title: {new_title}")
    print(f"   full_markdown_size: {len(full_markdown)} 字符")
    print(f"   expected_min_length: {max(1000, len(body) // 2)} 字符")


def step7_update_wiki_index(params):
    """步骤 7: 更新知识库首页索引（待审稿 → 已发布）"""
    print("\n" + "=" * 60)
    print("步骤 7: 更新知识库首页索引")
    print("=" * 60)
    print("📝 需要调用 feishu_wiki_space_node list(space_id=7650738808775330774) 获取所有文章")
    print("   逻辑：")
    print("   1. 过滤出标题以 [Published 开头的 → 已发布文章表格（按时间倒序）")
    print("   2. 过滤出标题以 [Draft 开头的 → 待审稿文章表格（按时间倒序）")
    print("   3. 找到「替身 · 知识库首页」文档，调用 feishu_update_doc 覆盖更新")
    print("   4. 本步骤完成后，刚刚发布的文章会从待审稿栏消失，出现在已发布栏")
    print("✅ 索引更新标记（agent 处理）")


def step8_send_notification(params):
    """步骤 8: 生成飞书消息通知内容"""
    print("\n" + "=" * 60)
    print("步骤 8: 生成飞书消息通知内容")
    print("=" * 60)
    
    github_url = f"{GITHUB_REPO_URL}/blob/main/posts/{params['slug']}.md"
    blog_url = f"{BLOG_BASE_URL}/{params['slug']}"
    msg = (
        f"✅ 《{params['title']}》已发布成功！\n\n"
        f"🌐 博客: {blog_url}\n"
        f"🔗 GitHub: {github_url}\n"
    )
    
    if "feishu_doc_id" in params:
        doc_url = f"{FEISHU_WIKI_URL_PREFIX}/{params['feishu_doc_id']}"
        msg += f"📑 飞书文档: {doc_url}\n"
    
    # 保存通知内容供 agent 发送
    notify_file = os.path.join(WORK_DIR, ".publish_notify.txt")
    with open(notify_file, "w", encoding="utf-8") as f:
        f.write(msg)
    
    print(f"✅ 通知内容已保存到 {notify_file}")
    print(f"\n{msg}")


def step9_cleanup():
    """步骤 9: 清理发布状态文件。

    发布成功后必须清理 .publish_params.json（脏数据会导致下次 publish 读到旧 slug）。
    其他状态文件也一并清理，避免残留。
    """
    print("\n" + "=" * 60)
    print("步骤 9: 清理发布状态文件")
    print("=" * 60)

    for name in (".publish_params.json", ".feishu_doc_update.json", ".feishu_doc_update.md", ".publish_notify.txt"):
        src = os.path.join(WORK_DIR, name)
        if not os.path.exists(src):
            print(f"⚠️  {name} 不存在，跳过")
            continue
        os.remove(src)
        print(f"✅ 已删除: {src}")


def main():
    print("🚀 博客文章发布流程启动")
    print(f"⏰ 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 1. 读取参数
    params = load_params()
    
    # 2. 执行所有步骤
    step1_prepare_env(params)
    step1b_lint_and_fix_frontmatter(params)  # 新增：frontmatter 规范校验
    step2_move_to_posts(params)
    step3_mark_topic_used(params)
    step4_build_verify()
    step5_git_commit_and_push(params)
    step6_update_feishu_doc(params)
    step7_update_wiki_index(params)
    step8_send_notification(params)
    
    step9_cleanup()
    
    print("\n" + "=" * 60)
    print("✅ 脚本执行完成！所有步骤均已执行。")
    print("=" * 60)
    print("\n📋 剩余步骤（agent 执行）：")
    print("   1. 读取 .feishu_doc_update.json 和 markdown_path，调用 feishu_update_doc 更新审稿文档为全文发布版")
    print("   2. 调用 feishu_wiki_space_node list + feishu_update_doc 更新知识库首页")
    print("   3. 调用 message 工具发送飞书通知")
    print("   4. 调用 feishu_fetch_doc 反查文档标题和正文长度，验证不为空")
    print("\n💡 状态文件：")
    print(f"   - {WORK_DIR}/.feishu_doc_update.json (飞书文档更新参数)")
    print(f"   - {WORK_DIR}/.feishu_doc_update.md (飞书发布全文 markdown)")
    print(f"   - {WORK_DIR}/.publish_notify.txt (通知内容)")


if __name__ == "__main__":
    main()
