#!/usr/bin/env python3
"""
postflight_runner.py

Deterministic postflight state machine.
Each step is a labelled checkpoint. The agent calls Feishu tools directly
(using its own auth). This script only:
  - Records plan inputs and state
  - Validates outputs of each step
  - Handles retry/cleanup logic
  - Computes final audit result

Usage (agent):
  cd /root/.openclaw/workspace/ai_blog
  python3 tools/daily_post/postflight_runner.py \
    --step list-nodes \
    --nodes-json /tmp/wiki_nodes.json

  python3 tools/daily_post/postflight_runner.py \
    --step plan \
    --nodes-json /tmp/wiki_nodes.json \
    --render-missing-review-dir /tmp/daily-blog-review-docs \
    > /tmp/draft_postflight_plan.json

  python3 tools/daily_post/postflight_runner.py \
    --step send-notifications \
    --plan-json /tmp/draft_postflight_plan.json \
    --notify-state /tmp/notify_state.json

  python3 tools/daily_post/postflight_runner.py \
    --step audit \
    --nodes-json /tmp/wiki_nodes.json

Exit code 0 = success / pass, 1 = failure / needs retry.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── constants ────────────────────────────────────────────────────────────────

REPO = Path("/root/.openclaw/workspace/ai_blog")
STATE_FILE = Path("/root/.openclaw/workspace/.daily_ai_blog_review_notified.json")


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(level: str, msg: str) -> None:
    print(f"[{now()}] [{level}] {msg}", flush=True)


def info(msg: str) -> None:
    log("INFO", msg)


def warn(msg: str) -> None:
    log("WARN", msg)


def error(msg: str) -> None:
    log("ERROR", msg)


# ── step: list-nodes ────────────────────────────────────────────────────────

def cmd_list_nodes(args) -> int:
    """Just validates that the nodes JSON was written; prints summary."""
    nodes_path = Path(args.nodes_json)
    if not nodes_path.exists():
        error(f"nodes JSON not found: {nodes_path}")
        return 1
    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    info(f"nodes file OK: {len(nodes)} nodes")
    return 0


# ── step: plan ──────────────────────────────────────────────────────────────

def cmd_plan(args) -> int:
    """Runs draft_postflight plan, writes output."""
    import urllib.request

    nodes_path = Path(args.nodes_json)
    state_path = Path(args.state or str(STATE_FILE))
    render_dir = Path(args.render_missing_review_dir) if args.render_missing_review_dir else None

    cmd = [
        "python3", str(REPO / "tools/daily_post/draft_postflight.py"),
        "plan",
        "--nodes-json", str(nodes_path),
        "--state", str(state_path),
    ]
    if render_dir:
        cmd += ["--render-missing-review-dir", str(render_dir)]

    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if r.stdout:
        sys.stdout.write(r.stdout)
    if r.returncode != 0:
        warn(f"plan non-zero: {r.stderr[:300]}")
    return r.returncode


# ── step: send-notifications ─────────────────────────────────────────────────

NOTIFY_STATE_FILE = Path("/tmp/postflight_notify_state.json")


def cmd_send_notifications(args) -> int:
    """Reads plan JSON, prints notification items as JSON lines.
    Caller (agent) is responsible for sending each via Feishu tools.
    After all sent, writes /tmp/postflight_notify_state.json with sent items."""
    plan_path = Path(args.plan_json)
    if not plan_path.exists():
        error(f"plan JSON not found: {plan_path}")
        return 1

    plan = json.loads(plan_path.read_text(encoding="utf-8"))

    # Read existing notify state
    notify_state: dict = {}
    if NOTIFY_STATE_FILE.exists():
        notify_state = json.loads(NOTIFY_STATE_FILE.read_text(encoding="utf-8"))

    to_notify = [
        d for d in plan.get("drafts", [])
        if d.get("needs_notification")
    ]

    if not to_notify:
        info("no pending notifications")
        # Write empty sent record
        NOTIFY_STATE_FILE.write_text(json.dumps({
            "sent": [], "at": now()
        }, ensure_ascii=False), encoding="utf-8")
        return 0

    info(f"{len(to_notify)} notifications to send")
    for draft in to_notify:
        slug = draft.get("slug", "")
        item = {
            "slug": slug,
            "title": draft.get("title", ""),
            "node_token": draft.get("node_token", ""),
            "doc_url": draft.get("doc_url", ""),
            "github_path": draft.get("github_path", ""),
            "review_message": draft.get("review_message", ""),
            "ts": now(),
            "sent": False,
        }
        print(json.dumps(item), flush=True)
        notify_state[slug] = item

    NOTIFY_STATE_FILE.write_text(
        json.dumps(notify_state, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    return 0


def cmd_mark_notified(args) -> int:
    """Marks a single slug as notified in the state file."""
    slug = args.slug
    title = args.title
    node_token = args.node_token
    doc_url = args.doc_url

    cmd = [
        "python3", str(REPO / "tools/daily_post/draft_postflight.py"),
        "mark-notified",
        "--state", str(STATE_FILE),
        "--slug", slug,
        "--title", title,
        "--node-token", node_token,
        "--doc-url", doc_url,
    ]
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        warn(f"mark-notified failed: {r.stderr[:200]}")
    else:
        info(f"marked notified: {slug}")
    return r.returncode


# ── step: audit ─────────────────────────────────────────────────────────────

def cmd_audit(args) -> int:
    """Runs draft_postflight audit. Exit 0 = pass, 1 = fail."""
    nodes_path = Path(args.nodes_json)
    state_path = Path(args.state or str(STATE_FILE))

    cmd = [
        "python3", str(REPO / "tools/daily_post/draft_postflight.py"),
        "audit",
        "--nodes-json", str(nodes_path),
        "--state", str(state_path),
    ]
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    try:
        result = json.loads(r.stdout) if r.stdout.strip() else {}
        info(f"audit: ok={result.get('ok')}, "
             f"pending={result.get('pending_count')}, "
             f"needs_notif={result.get('needs_notification_count')}, "
             f"no_wiki_draft={result.get('pending_without_wiki_draft_count')}")
    except Exception as exc:
        warn(f"audit parse error: {exc}")

    if r.returncode != 0:
        warn(f"audit exit {r.returncode}")
    return r.returncode


# ── main ───────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="postflight_runner step executor")
    sub = parser.add_subparsers(dest="step", required=True)

    p_nodes = sub.add_parser("list-nodes")
    p_nodes.add_argument("--nodes-json", required=True)

    p_plan = sub.add_parser("plan")
    p_plan.add_argument("--nodes-json", required=True)
    p_plan.add_argument("--state", default=None)
    p_plan.add_argument("--render-missing-review-dir", default=None)

    p_notify = sub.add_parser("send-notifications")
    p_notify.add_argument("--plan-json", required=True)

    p_mark = sub.add_parser("mark-notified")
    p_mark.add_argument("--slug", required=True)
    p_mark.add_argument("--title", required=True)
    p_mark.add_argument("--node-token", required=True)
    p_mark.add_argument("--doc-url", required=True)

    p_audit = sub.add_parser("audit")
    p_audit.add_argument("--nodes-json", required=True)
    p_audit.add_argument("--state", default=None)

    args = parser.parse_args()

    steps = {
        "list-nodes": cmd_list_nodes,
        "plan": cmd_plan,
        "send-notifications": cmd_send_notifications,
        "mark-notified": cmd_mark_notified,
        "audit": cmd_audit,
    }

    info(f"postflight_runner step={args.step}")
    return steps[args.step](args)


if __name__ == "__main__":
    sys.exit(main())
