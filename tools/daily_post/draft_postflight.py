#!/usr/bin/env python3
"""Postflight helper for daily draft review workflow.

This script is intentionally local-only. It does not call Feishu APIs itself.
Agent/cron flow:
  1. list wiki nodes with feishu_wiki_space_node
  2. write simplified nodes JSON
  3. run this script in `plan` mode
  4. use Feishu tools to create missing Draft docs, update homepage, send messages
  5. run `mark-notified` after each successful review notification

The important invariant is result-driven: a local pending/*.md draft is not
considered complete until there is a matching Feishu [Draft ...] node and a
recorded review notification.
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
DEFAULT_STATE = Path("/root/.openclaw/workspace/.daily_ai_blog_review_notified.json")
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


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def read_frontmatter_and_body(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm, body = parts[1], parts[2]
    if yaml is not None:
        try:
            data = yaml.safe_load(fm) or {}
            if isinstance(data, dict):
                return data, body
        except Exception:
            pass
    data: dict[str, Any] = {}
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*[\"']?(.+?)[\"']?\s*$", line)
        if m:
            data[m.group(1)] = m.group(2)
    return data, body


def pending_articles() -> list[dict[str, str]]:
    pending = REPO_ROOT / "pending"
    articles: list[dict[str, str]] = []
    if not pending.is_dir():
        return articles
    for path in sorted(pending.glob("*.md")):
        fm, body = read_frontmatter_and_body(path)
        title = str(fm.get("title") or "").strip().strip("'\"")
        date = str(fm.get("date") or datetime.now().strftime("%Y-%m-%d")).strip().strip("'\"")[:10]
        if not title:
            continue
        slug = path.stem
        article: dict[str, str] = {
            "title": title,
            "date": date,
            "slug": slug,
            "path": f"pending/{slug}.md",
            "abs_path": str(path),
            "body": body.strip(),
        }
        # 优先从 frontmatter 读取飞书 wiki token（解决 Feishu API 索引延迟导致列表查不到的问题）
        wiki_node_token = str(fm.get("feishu_wiki_node_token") or "").strip()
        wiki_doc_token = str(fm.get("feishu_wiki_doc_token") or "").strip()
        if wiki_node_token:
            article["feishu_wiki_node_token"] = wiki_node_token
        if wiki_doc_token:
            article["feishu_wiki_doc_token"] = wiki_doc_token
        articles.append(article)
    return articles


def pending_title_map() -> dict[str, dict[str, str]]:
    return {a["title"]: {k: a[k] for k in ["slug", "path", "abs_path", "date"]} for a in pending_articles()}


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


def build_review_markdown(title: str, slug: str, body: str) -> str:
    return f"""> 📝 待审稿说明
>
> - 标题：{title}
> - Slug：{slug}
> - 审稿命令：`/publish {slug}` / `/edit {slug} <修改意见>` / `/abandon {slug}`

---

{body.strip()}
"""


def simplify_nodes(nodes: list[dict[str, Any]]) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    draft_by_title: dict[str, dict[str, str]] = {}
    published_by_title: dict[str, dict[str, str]] = {}
    for node in nodes:
        node_title = str(node.get("title", ""))
        token = str(node.get("node_token", ""))
        if not node_title or not token:
            continue
        url = str(node.get("url") or f"{FEISHU_WIKI_URL_PREFIX}/{token}")
        dm = DRAFT_RE.match(node_title)
        if dm:
            draft_by_title[dm.group(2)] = {"date": dm.group(1), "node_token": token, "doc_url": url}
            continue
        pm = PUBLISHED_RE.match(node_title)
        if pm:
            published_by_title[pm.group(2)] = {"date": pm.group(1), "node_token": token, "doc_url": url}
    return draft_by_title, published_by_title


def plan(args: argparse.Namespace) -> None:
    nodes = load_json(Path(args.nodes_json), [])
    state_path = Path(args.state)
    state = load_json(state_path, {"notified": {}})
    notified: dict[str, Any] = state.get("notified") if isinstance(state, dict) else {}
    if not isinstance(notified, dict):
        notified = {}

    pending = pending_articles()
    pending_by_title = {a["title"]: a for a in pending}
    draft_by_title, published_by_title = simplify_nodes(nodes)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    drafts: list[dict[str, Any]] = []
    pending_without_wiki_draft: list[dict[str, Any]] = []
    wiki_drafts_without_pending: list[dict[str, str]] = []

    for title, draft in draft_by_title.items():
        info = pending_by_title.get(title)
        if not info:
            wiki_drafts_without_pending.append({"title": title, **draft})
            continue
        slug = info["slug"]
        already = bool(notified.get(slug, {}).get("node_token") == draft["node_token"])
        drafts.append(
            {
                "date": draft["date"],
                "title": title,
                "slug": slug,
                "github_path": info["path"],
                "node_token": draft["node_token"],
                "doc_url": draft["doc_url"],
                "notified": already,
                "needs_notification": not already,
                "review_message": build_review_message(title, slug, draft["doc_url"], now, draft["node_token"]),
            }
        )

    for article in pending:
        title = article["title"]
        # 优先用 frontmatter 中的飞书 token（解决 Feishu API 索引延迟和标题前缀被剥的问题）
        wiki_node_token = article.get("feishu_wiki_node_token", "")
        wiki_doc_token = article.get("feishu_wiki_doc_token", "")
        if wiki_node_token:
            # frontmatter 有 token，说明 wiki draft 已创建
            doc_url = f"{FEISHU_WIKI_URL_PREFIX}/{wiki_node_token}"
            already = bool(notified.get(article["slug"], {}).get("node_token") == wiki_node_token)
            drafts.append(
                {
                    "date": article["date"],
                    "title": title,
                    "slug": article["slug"],
                    "github_path": article["path"],
                    "node_token": wiki_node_token,
                    "doc_token": wiki_doc_token,
                    "doc_url": doc_url,
                    "notified": already,
                    "needs_notification": not already,
                    "review_message": build_review_message(title, article["slug"], doc_url, now, wiki_node_token),
                }
            )
            continue

        if title in draft_by_title or title in published_by_title:
            continue
        review_path = Path(args.render_missing_review_dir) / f"{article['slug']}.review.md" if args.render_missing_review_dir else None
        if review_path:
            review_path.parent.mkdir(parents=True, exist_ok=True)
            review_path.write_text(build_review_markdown(title, article["slug"], article["body"]), encoding="utf-8")
        pending_without_wiki_draft.append(
            {
                "date": article["date"],
                "title": title,
                "slug": article["slug"],
                "github_path": article["path"],
                "abs_path": article["abs_path"],
                "draft_doc_title": f"[Draft {article['date']}] {title}",
                "review_markdown_path": str(review_path) if review_path else None,
                "needs_create_doc": True,
                "needs_notification_after_create": True,
            }
        )

    drafts.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
    pending_without_wiki_draft.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
    output = {
        "owner_open_id": OWNER_OPEN_ID,
        "state_path": str(state_path),
        "pending_count": len(pending),
        "draft_count": len(drafts),
        "needs_notification_count": sum(1 for d in drafts if d["needs_notification"]),
        "pending_without_wiki_draft_count": len(pending_without_wiki_draft),
        "drafts": drafts,
        "pending_without_wiki_draft": pending_without_wiki_draft,
        "wiki_drafts_without_pending": wiki_drafts_without_pending,
        "ok": not pending_without_wiki_draft and not any(d["needs_notification"] for d in drafts),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def build_review_doc(args: argparse.Namespace) -> None:
    path = REPO_ROOT / "pending" / f"{args.slug}.md"
    if not path.exists():
        raise SystemExit(f"pending draft not found: {path}")
    fm, body = read_frontmatter_and_body(path)
    title = str(fm.get("title") or "").strip().strip("'\"")
    if not title:
        raise SystemExit(f"missing title in frontmatter: {path}")
    print(build_review_markdown(title, args.slug, body))


def audit(args: argparse.Namespace) -> None:
    from io import StringIO
    import contextlib

    fake = argparse.Namespace(**vars(args))
    fake.render_missing_review_dir = None
    buf = StringIO()
    with contextlib.redirect_stdout(buf):
        plan(fake)
    data = json.loads(buf.getvalue())
    print(json.dumps(data, ensure_ascii=False, indent=2))
    if data["pending_without_wiki_draft_count"] or data["needs_notification_count"]:
        raise SystemExit(2)


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
    p_plan.add_argument("--render-missing-review-dir")
    p_plan.set_defaults(func=plan)

    p_audit = sub.add_parser("audit")
    p_audit.add_argument("--nodes-json", required=True)
    p_audit.set_defaults(func=audit)

    p_render = sub.add_parser("build-review-doc")
    p_render.add_argument("--slug", required=True)
    p_render.set_defaults(func=build_review_doc)

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
