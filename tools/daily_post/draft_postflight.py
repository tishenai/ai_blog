#!/usr/bin/env python3
"""Postflight helper for daily draft review workflow.

This script is intentionally local-only. It does not call Feishu APIs itself.
Agent/cron flow:
  1. list wiki nodes with feishu_wiki_space_node
  2. write simplified nodes JSON
  3. run this script in `plan` mode
  4. use Feishu tools to update homepage / send messages
  5. run `mark-notified` after each successful review notification
"""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_STATE = Path("/root/.openclaw/workspace/.daily_ai_blog_review_notified.json")
FEISHU_WIKI_URL_PREFIX = "https://vcnd3kpj0wx8.feishu.cn/wiki"
OWNER_OPEN_ID = "ou_106a0b92c4a08afd40abec947337313a"
DRAFT_RE = re.compile(r"^\[Draft (\d{4}-\d{2}-\d{2})\]\s+(.+)$")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


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


def pending_title_map() -> dict[str, dict[str, str]]:
    pending = REPO_ROOT / "pending"
    mapping: dict[str, dict[str, str]] = {}
    if not pending.is_dir():
        return mapping
    for path in sorted(pending.glob("*.md")):
        fm = read_frontmatter(path)
        title = str(fm.get("title") or "").strip()
        if not title:
            continue
        slug = path.stem
        mapping[title] = {
            "slug": slug,
            "path": f"pending/{slug}.md",
        }
    return mapping


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
    state_path = Path(args.state)
    state = load_json(state_path, {"notified": {}})
    notified: dict[str, Any] = state.get("notified") if isinstance(state, dict) else {}
    if not isinstance(notified, dict):
        notified = {}

    titles = pending_title_map()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    drafts: list[dict[str, Any]] = []
    missing_pending: list[dict[str, str]] = []

    for node in nodes:
        title = str(node.get("title", ""))
        token = str(node.get("node_token", ""))
        if not title or not token:
            continue
        m = DRAFT_RE.match(title)
        if not m:
            continue
        date_str, real_title = m.group(1), m.group(2)
        info = titles.get(real_title)
        doc_url = str(node.get("url") or f"{FEISHU_WIKI_URL_PREFIX}/{token}")
        if not info:
            missing_pending.append({"date": date_str, "title": real_title, "node_token": token, "doc_url": doc_url})
            continue
        slug = info["slug"]
        already = bool(notified.get(slug, {}).get("node_token") == token)
        draft = {
            "date": date_str,
            "title": real_title,
            "slug": slug,
            "github_path": info["path"],
            "node_token": token,
            "doc_url": doc_url,
            "notified": already,
            "needs_notification": not already,
            "review_message": build_review_message(real_title, slug, doc_url, now, token),
        }
        drafts.append(draft)

    drafts.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
    output = {
        "owner_open_id": OWNER_OPEN_ID,
        "state_path": str(state_path),
        "draft_count": len(drafts),
        "needs_notification_count": sum(1 for d in drafts if d["needs_notification"]),
        "drafts": drafts,
        "missing_pending_for_wiki_drafts": missing_pending,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def mark_notified(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_json(state_path, {"notified": {}})
    if not isinstance(state, dict):
        state = {"notified": {}}
    notified = state.setdefault("notified", {})
    if not isinstance(notified, dict):
        state["notified"] = notified = {}
    notified[args.slug] = {
        "title": args.title,
        "node_token": args.node_token,
        "doc_url": args.doc_url,
        "notified_at": datetime.now().isoformat(timespec="seconds"),
    }
    save_json(state_path, state)
    print(f"marked notified: {args.slug}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan/mark draft review postflight notifications")
    parser.add_argument("--state", default=str(DEFAULT_STATE), help="notification state JSON path")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan")
    p_plan.add_argument("--nodes-json", required=True)
    p_plan.set_defaults(func=plan)

    p_mark = sub.add_parser("mark-notified")
    p_mark.add_argument("--slug", required=True)
    p_mark.add_argument("--title", required=True)
    p_mark.add_argument("--node-token", required=True)
    p_mark.add_argument("--doc-url", required=True)
    p_mark.set_defaults(func=mark_notified)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
