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

# ==================== 配置 ====================
WORK_DIR = "/root/.openclaw/workspace/ai_blog"
PARAMS_FILE = os.path.join(WORK_DIR, ".publish_params.json")
WIKI_SPACE_ID = "7650738808775330774"
OWNER_OPEN_ID = "ou_106a0b92c4a08afd40abec947337313a"


def run_cmd(cmd, shell=True, cwd=WORK_DIR, capture_output=False):
    """执行 shell 命令，失败则退出"""
    print(f"$ {cmd}")
    try:
        result = subprocess.run(
            cmd,
            shell=shell,
            cwd=cwd,
            capture_output=capture_output,
            text=True,
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
    
    # git pull
    run_cmd("git pull --rebase")
    
    # 验证 pending 文件存在
    pending_path = f"pending/{params['slug']}.md"
    if not os.path.exists(os.path.join(WORK_DIR, pending_path)):
        print(f"❌ 草稿文件不存在: {pending_path}")
        sys.exit(1)
    
    print(f"✅ 草稿文件存在: {pending_path}")


def step2_move_to_posts(params):
    """步骤 2: 移到正式发布目录"""
    print("\n" + "=" * 60)
    print("步骤 2: 移到正式发布目录")
    print("=" * 60)
    
    src = f"pending/{params['slug']}.md"
    dst = f"posts/{params['slug']}.md"
    run_cmd(f"git mv {src} {dst}")
    print(f"✅ 已移动: {src} → {dst}")


def step3_mark_topic_used(params):
    """步骤 3: 标记话题已用"""
    print("\n" + "=" * 60)
    print("步骤 3: 标记话题已用")
    print("=" * 60)
    
    today = datetime.now().strftime("%Y-%m-%d")
    run_cmd(
        f"python3 tools/daily_post/mark_topic_used.py "
        f"{params['slug']} {today} /{params['slug']}"
    )
    print("✅ 话题已标记为已用")


def step4_build_verify():
    """步骤 4: 构建验证"""
    print("\n" + "=" * 60)
    print("步骤 4: 构建验证")
    print("=" * 60)
    
    run_cmd("pnpm run build")
    print("✅ 构建验证通过")


def step5_git_commit_and_push(params):
    """步骤 5: Git 提交并推送"""
    print("\n" + "=" * 60)
    print("步骤 5: Git 提交并推送")
    print("=" * 60)
    
    run_cmd("git add -A")
    run_cmd(f"git commit -m \"feat(posts): 发布《{params['title']}》\"")
    run_cmd("HUSKY=0 git push")
    print("✅ 已提交并推送到 main 分支")


def step6_update_feishu_doc(params):
    """步骤 6: 更新飞书审稿文档状态"""
    print("\n" + "=" * 60)
    print("步骤 6: 更新飞书审稿文档状态")
    print("=" * 60)
    
    if "feishu_doc_id" not in params:
        print("⚠️  缺少 feishu_doc_id，跳过飞书文档更新")
        return
    
    # 读取文章内容
    post_path = os.path.join(WORK_DIR, f"posts/{params['slug']}.md")
    with open(post_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 去掉 frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    
    # 构建新的文档内容（Published 状态）
    today = datetime.now().strftime("%Y-%m-%d")
    new_title = f"[Published {today}] {params['title']}"
    github_url = f"https://github.com/tishenai/ai_blog/blob/main/posts/{params['slug']}.md"
    
    new_content = f"""✅ **已发布到博客 main 分支**

✅ GitHub: [{github_url}]({github_url})

---

{content}
"""
    
    # 调用 feishu_update_doc（通过 OpenClaw 的工具机制，这里打印让 agent 调用）
    print(f"📝 需要调用 feishu_update_doc:")
    print(f"   doc_id: {params['feishu_doc_id']}")
    print(f"   title: {new_title}")
    print(f"   content_length: {len(new_content)} 字符")
    
    # 保存到临时文件供 agent 读取
    tmp_file = os.path.join(WORK_DIR, ".feishu_doc_update.json")
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump({
            "doc_id": params["feishu_doc_id"],
            "title": new_title,
            "content": new_content,
            "github_url": github_url,
        }, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 飞书文档更新参数已保存到 {tmp_file}")


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
    """步骤 8: 发飞书消息通知 owner"""
    print("\n" + "=" * 60)
    print("步骤 8: 发飞书消息通知 owner")
    print("=" * 60)
    
    github_url = f"https://github.com/tishenai/ai_blog/blob/main/posts/{params['slug']}.md"
    msg = f"""✅ 《{params['title']}》已发布成功！

🔗 GitHub: {github_url}
"""
    
    if "feishu_doc_id" in params:
        doc_url = f"https://vcnd3kpj0wx8.feishu.cn/wiki/{params['feishu_doc_id']}"
        msg += f"📑 飞书文档: {doc_url}\n"
    
    # 保存通知内容供 agent 发送
    notify_file = os.path.join(WORK_DIR, ".publish_notify.txt")
    with open(notify_file, "w", encoding="utf-8") as f:
        f.write(msg)
    
    print(f"✅ 通知内容已保存到 {notify_file}")
    print(f"\n{msg}")


def step9_cleanup():
    """步骤 9: 清理参数文件"""
    print("\n" + "=" * 60)
    print("步骤 9: 清理参数文件")
    print("=" * 60)
    
    if os.path.exists(PARAMS_FILE):
        os.remove(PARAMS_FILE)
        print(f"✅ 已删除: {PARAMS_FILE}")
    else:
        print("⚠️  参数文件已不存在，跳过清理")


def main():
    print("🚀 博客文章发布流程启动")
    print(f"⏰ 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 1. 读取参数
    params = load_params()
    
    # 2. 执行所有步骤
    step1_prepare_env(params)
    step2_move_to_posts(params)
    step3_mark_topic_used(params)
    step4_build_verify()
    step5_git_commit_and_push(params)
    step6_update_feishu_doc(params)
    step7_update_wiki_index(params)
    step8_send_notification(params)
    
    # 注意：step9_cleanup 由 agent 在所有步骤成功后执行
    # （因为飞书文档更新和发送通知需要 agent 调用工具）
    
    print("\n" + "=" * 60)
    print("✅ 脚本执行完成！")
    print("=" * 60)
    print("\n📋 剩余步骤（agent 执行）：")
    print("   1. 调用 feishu_update_doc 更新审稿文档状态")
    print("   2. 调用 feishu_wiki_space_node list + feishu_update_doc 更新知识库首页")
    print("   3. 调用 message 工具发送飞书通知")
    print("   4. 删除 .publish_params.json")
    print("\n💡 状态文件：")
    print(f"   - {WORK_DIR}/.feishu_doc_update.json (飞书文档更新参数)")
    print(f"   - {WORK_DIR}/.publish_notify.txt (通知内容)")


if __name__ == "__main__":
    main()
