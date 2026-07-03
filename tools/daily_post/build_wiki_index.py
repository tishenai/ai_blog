#!/usr/bin/env python3
"""
生成飞书知识库首页索引的 markdown 内容。

使用方式：
    # 接受一个 JSON 文件作为输入（描述 wiki 节点列表），输出首页 markdown 到 stdout
    python3 tools/daily_post/build_wiki_index.py <nodes_json_file>

    # 或者直接传节点 JSON 字符串
    python3 tools/daily_post/build_wiki_index.py --json-stdin < nodes.json

输入 JSON 格式（来自 feishu_wiki_space_node list 工具的精简版）：
[
  {"node_token": "xxx", "title": "[Published 2026-06-14] 文章A"},
  {"node_token": "yyy", "title": "[Draft 2026-06-13] 文章B"},
  {"node_token": "zzz", "title": "替身 · 知识库首页"},
  ...
]

输出：完整的首页 markdown 字符串（覆盖式更新用）。

设计意图：
- 把"列 wiki 节点 → 过滤 → 排序 → 拼 markdown"这套易错逻辑从 agent prompt 抽出来。
- agent 只需要：调 feishu_wiki_space_node list → 把结果（精简版）喂给本脚本 → 拿 markdown → feishu_update_doc。
- 排序规则、URL 模板、表格格式都在这里集中维护。
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

try:
    import yaml
except ImportError:  # pragma: no cover - fallback for minimal environments
    yaml = None

# ==================== 配置（与 run_publish.py 保持一致）====================
BLOG_BASE_URL = "https://www.wemixmemory.top"
GITHUB_REPO_URL = "https://github.com/tishenai/ai_blog"
FEISHU_WIKI_URL_PREFIX = "https://vcnd3kpj0wx8.feishu.cn/wiki"

# 标题前缀正则
PUBLISHED_RE = re.compile(r"Published\s+(\d{4}-\d{2}-\d{2})[\s\]]+\s+(.+)")
DRAFT_RE = re.compile(r"Draft\s+(\d{4}-\d{2}-\d{2})[\s\]]+\s+(.+)")

def repo_root():
    """返回 ai_blog 仓库根目录。"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


def load_title_slug_map():
    """从 posts/ 和 pending/ 目录扫描 frontmatter，构建 标题 → slug 映射。

    这样新文章发布后不需要再手改本脚本；wiki 首页能自动生成正确博客/GitHub 链接。
    """
    mapping = {}
    root = repo_root()
    for dirname in ("posts", "pending"):
        dir_path = os.path.join(root, dirname)
        if not os.path.isdir(dir_path):
            continue
        for name in sorted(os.listdir(dir_path)):
            if not name.endswith(".md"):
                continue
            slug = name[:-3]
            path = os.path.join(dir_path, name)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read(8192)
            except OSError:
                continue
            if not text.startswith("---"):
                continue
            parts = text.split("---", 2)
            if len(parts) < 3:
                continue
            frontmatter = parts[1]
            title = None
            if yaml is not None:
                try:
                    data = yaml.safe_load(frontmatter) or {}
                    title = data.get("title")
                except Exception:
                    title = None
            if not title:
                m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", frontmatter, re.MULTILINE)
                if m:
                    title = m.group(1).strip()
            if title:
                mapping[str(title)] = slug
    return mapping


TITLE_TO_SLUG = load_title_slug_map()


def slug_for_title(title):
    """根据 posts/pending frontmatter 标题查 slug，找不到返回 None。"""
    return TITLE_TO_SLUG.get(title)


def categorize_nodes(nodes):
    """把 wiki 节点列表分类为 published / draft / 其他。

    每个 node 至少含 node_token 和 title。
    返回 (published_list, draft_list)，各按日期倒序排列。
    """
    published = []
    draft = []

    for node in nodes:
        title = node.get("title", "")
        token = node.get("node_token", "")
        if not title or not token:
            continue

        m = PUBLISHED_RE.search(title)
        if m:
            date_str = m.group(1)
            real_title = m.group(2)
        elif slug_for_title(title):
            # 无 [Published] 前缀但存在于 posts/pending，即已发布（飞书 strip 了前缀）
            real_title = title
            date_str = None
        else:
            real_title = None
        if real_title:
            published.append({
                "node_token": token,
                "date": date_str,
                "title": real_title,
                "slug": slug_for_title(real_title),
            })
            continue

        m = DRAFT_RE.search(title)
        if m:
            date_str = m.group(1)
            real_title = m.group(2)
        elif slug_for_title(title):
            real_title = title
            date_str = None
        else:
            real_title = None
        if real_title:
            draft.append({
                "node_token": token,
                "date": date_str,
                "title": real_title,
                "slug": slug_for_title(real_title),
            })
            continue

    # 按日期倒序，同日期按标题
    published.sort(key=lambda x: (x["date"] or "", x["title"]), reverse=True)
    draft.sort(key=lambda x: (x["date"] or "", x["title"]), reverse=True)

    return published, draft


def render_published_table(published):
    """生成已发布文章表格的 markdown。"""
    if not published:
        return "*目前还没有已发布的文章。*"

    lines = [
        "| 发布日期 | 标题 | 飞书 | 博客 | GitHub |",
        "|---|---|---|---|---|",
    ]
    for item in published:
        feishu_url = f"{FEISHU_WIKI_URL_PREFIX}/{item['node_token']}"
        slug = item["slug"]
        if slug:
            blog_link = f"[🌐]({BLOG_BASE_URL}/{slug})"
            github_link = f"[📦]({GITHUB_REPO_URL}/blob/main/posts/{slug}.md)"
        else:
            blog_link = "—"
            github_link = "—"
        lines.append(
            f"| {item['date']} | {item['title']} | [📄]({feishu_url}) | {blog_link} | {github_link} |"
        )
    return "\n".join(lines)


def render_draft_table(draft):
    """生成待审稿表格的 markdown。"""
    if not draft:
        return "*目前没有待审稿件。每天 17:00 (Asia/Shanghai) 由 daily-ai-blog-post 定时任务自动生成新稿。*"

    lines = [
        "| 生成日期 | 标题 | 飞书审稿文档 |",
        "|---|---|---|",
    ]
    for item in draft:
        feishu_url = f"{FEISHU_WIKI_URL_PREFIX}/{item['node_token']}"
        lines.append(f"| {item['date']} | {item['title']} | [📄 审稿]({feishu_url}) |")
    return "\n".join(lines)


def render_index_page(published, draft):
    """生成完整的知识库首页 markdown。"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M (Asia/Shanghai)")
    total = len(published)

    return f"""# 替身 · 知识库首页

> 📝 这是替身（一个 AI agent）的博客知识库索引页。所有文章都已发布到 [tishenai/ai_blog]({GITHUB_REPO_URL})，博客地址 [{BLOG_BASE_URL.replace('https://', '')}]({BLOG_BASE_URL})。

---

## ✅ 已发布文章

{render_published_table(published)}

**共 {total} 篇文章**

---

## 📝 待审稿

{render_draft_table(draft)}

---

## 🛠 工作流说明

- **生成**：每天 17:00 自动选题、写稿、推送到 `tishenai/ai_blog` 仓库 `pending/` 目录
- **审稿**：在飞书或 GitHub 上查看 Draft 文档，决定发布、修改或放弃
- **发布**：通过 `/publish <slug>` 命令触发，自动从 `pending/` 移到 `posts/`，更新飞书文档状态、刷新本索引页

---

*自动更新于：{now}*
"""


def main():
    parser = argparse.ArgumentParser(description="生成飞书知识库首页索引")
    parser.add_argument(
        "input_file",
        nargs="?",
        help="输入 JSON 文件路径（含 wiki 节点列表）",
    )
    parser.add_argument(
        "--json-stdin",
        action="store_true",
        help="从 stdin 读取 JSON",
    )
    args = parser.parse_args()

    if args.json_stdin:
        nodes = json.load(sys.stdin)
    elif args.input_file:
        with open(args.input_file, "r", encoding="utf-8") as f:
            nodes = json.load(f)
    else:
        print("❌ 必须指定 input_file 或 --json-stdin", file=sys.stderr)
        sys.exit(1)

    if not isinstance(nodes, list):
        print(f"❌ JSON 必须是列表，得到 {type(nodes).__name__}", file=sys.stderr)
        sys.exit(1)

    published, draft = categorize_nodes(nodes)
    print(render_index_page(published, draft))


if __name__ == "__main__":
    main()
