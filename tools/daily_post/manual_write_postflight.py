#!/usr/bin/env python3
"""Manual /write_blog postflight planner.

This script is intentionally API-free. It inspects local ai_blog files plus a
simplified Feishu wiki node list produced by the agent, then emits a JSON plan.
The main-session agent performs external actions (create/update docs, send IMs).

Why this exists:
- The isolated writing cron is good at long-form generation, but its final
  delivery can be partial: local draft may exist while Feishu doc / homepage /
  notification are missing.
- /write_blog should not leave the user guessing. A main-session watchdog can
  run this planner and complete visible postflight work.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = Path("/root/.openclaw/workspace/.daily_ai_blog_review_notified.json")
MANUAL_TOPIC_FILE = Path("/root/.openclaw/workspace/.daily_ai_blog_manual_topic.md")
MANUAL_TOPIC_ARCHIVE = Path("/root/.openclaw/workspace/.daily_ai_blog_manual_topic_archive")
FEISHU_WIKI_URL_PREFIX = "https://vcnd3kpj0wx8.feishu.cn/wiki"
OWNER_OPEN_ID = "user:ou_12cafe83f620117e40728ef5cd4687eb"
DRAFT_RE = re.compile(r"^\[Draft (\d{4}-\d{2}-\d{2})\]\s+(.+)$")
PUBLISHED_RE = re.compile(r"^\[Published (\d{4}-\d{2}-\d{2})\]\s+(.+)$")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = parts[1]
    if yaml is not None:
        try:
            data = yaml.safe_load(fm) or {}
            if isinstance(data, dict):
                return data
        except Exception:
            pass
    data: dict[str, Any] = {}
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*[\"']?(.+?)[\"']?\s*$", line)
        if m:
            data[m.group(1)] = m.group(2)
    return data


def body_without_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip()
    return text


def review_markdown(slug: str, body: str) -> str:
    return (
        "> 审稿说明：这是待审草稿。\n"
        ">\n"
        f"> 发布：`/publish {slug}`\n"
        f"> 修改：`/edit {slug} <修改意见>`\n"
        f"> 放弃：`/abandon {slug}`\n"
        "\n---\n\n"
        + body
    )


def load_local_pending() -> list[dict[str, Any]]:
    pending_dir = REPO_ROOT / "pending"
    out: list[dict[str, Any]] = []
    if not pending_dir.is_dir():
        return out
    for path in sorted(pending_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
        fm = read_frontmatter(path)
        title = str(fm.get("title") or "").strip()
        if not title:
            continue
        slug = path.stem
        date = str(fm.get("date") or "").strip().strip("'\"")[:10] or datetime.now().strftime("%Y-%m-%d")
        review_path = Path("/tmp") / f"manual-write-review-{slug}.md"
        review_path.write_text(review_markdown(slug, body_without_frontmatter(path)), encoding="utf-8")
        out.append({
            "slug": slug,
            "title": title,
            "date": date,
            "github_path": f"pending/{slug}.md",
            "abs_path": str(path),
            "review_markdown_path": str(review_path),
            "mtime": path.stat().st_mtime,
        })
    return out


def node_maps(nodes: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    drafts: dict[str, dict[str, Any]] = {}
    published: dict[str, dict[str, Any]] = {}
    for node in nodes:
        raw_title = str(node.get("title") or "")
        token = str(node.get("node_token") or "")
        if not raw_title or not token:
            continue
        url = str(node.get("url") or f"{FEISHU_WIKI_URL_PREFIX}/{token}")
        m = DRAFT_RE.match(raw_title)
        if m:
            title = m.group(2)
            drafts[title] = {"date": m.group(1), "title": title, "node_token": token, "doc_url": url, "raw_title": raw_title}
            continue
        m = PUBLISHED_RE.match(raw_title)
        if m:
            title = m.group(2)
            published[title] = {"date": m.group(1), "title": title, "node_token": token, "doc_url": url, "raw_title": raw_title}
    return drafts, published


def build_review_message(title: str, slug: str, doc_url: str, generated_at: str, node_token: str) -> str:
    return f"""📝 【待审文章】《{title}》

🔗 [飞书文档]({doc_url})
🐙 GitHub 草稿：pending/{slug}.md
📅 生成时间：{generated_at}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 直接复制命令执行：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/publish {slug}
/edit {slug} <修改意见>
/abandon {slug}

---
【内部参数】
SLUG: {slug}
TITLE: {title}
FEISHU_DOC_ID: {node_token}"""


def plan(args: argparse.Namespace) -> None:
    nodes = load_json(Path(args.nodes_json), [])
    state = load_json(STATE_PATH, {"notified": {}})
    notified = state.get("notified", {}) if isinstance(state, dict) else {}
    if not isinstance(notified, dict):
        notified = {}

    drafts_by_title, published_by_title = node_maps(nodes)
    pending = load_local_pending()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    create_doc_tasks: list[dict[str, Any]] = []
    notify_tasks: list[dict[str, Any]] = []
    already_published_local_pending: list[dict[str, Any]] = []

    for item in pending:
        title = item["title"]
        slug = item["slug"]
        if title in published_by_title:
            already_published_local_pending.append(item)
            continue
        draft_node = drafts_by_title.get(title)
        if not draft_node:
            create_doc_tasks.append({
                **item,
                "doc_title": f"[Draft {item['date']}] {title}",
                "wiki_space": "7650738808775330774",
            })
            continue
        already = bool(notified.get(slug, {}).get("node_token") == draft_node["node_token"])
        if not already:
            notify_tasks.append({
                **item,
                "node_token": draft_node["node_token"],
                "doc_url": draft_node["doc_url"],
                "review_message": build_review_message(title, slug, draft_node["doc_url"], now, draft_node["node_token"]),
            })

    output = {
        "owner_open_id": OWNER_OPEN_ID,
        "state_path": str(STATE_PATH),
        "manual_topic_file": str(MANUAL_TOPIC_FILE),
        "manual_topic_file_exists": MANUAL_TOPIC_FILE.exists() and MANUAL_TOPIC_FILE.read_text(encoding="utf-8", errors="ignore").strip() != "",
        "manual_topic_archive_dir": str(MANUAL_TOPIC_ARCHIVE),
        "pending_count": len(pending),
        "create_doc_count": len(create_doc_tasks),
        "notify_count": len(notify_tasks),
        "create_doc_tasks": create_doc_tasks,
        "notify_tasks": notify_tasks,
        "already_published_local_pending": already_published_local_pending,
        "next_steps_for_agent": [
            "For each create_doc_task, read review_markdown_path and call feishu_create_doc(wiki_space, title=doc_title, markdown=file_content).",
            "After creating docs, re-list wiki nodes and rebuild homepage with build_wiki_index.py, then update homepage doc.",
            "For every new or existing draft notification sent, run draft_postflight.py mark-notified with slug/title/node-token/doc-url.",
            "If all pending drafts are handled and manual_topic_file_exists is true, archive the manual topic file after successful notification.",
        ],
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan manual write-blog postflight repairs")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--nodes-json", required=True)
    p.set_defaults(func=plan)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
