#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/daily_post/draft_postflight.py"
PENDING = ROOT / "pending"


def run_cmd(*args: str, check: bool = True):
    return subprocess.run(
        ["python3", str(SCRIPT), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=check,
    )


def write_pending(slug: str = "postflight-test-draft", title: str = "测试草稿标题") -> Path:
    PENDING.mkdir(exist_ok=True)
    path = PENDING / f"{slug}.md"
    path.write_text(
        "---\n"
        f"title: '{title}'\n"
        "date: '2026-06-14 17:00:00'\n"
        "tags:\n  - 测试\n"
        "categories:\n  - 测试\n"
        "---\n\n"
        "这是一篇用于 postflight 测试的草稿正文。\n",
        encoding="utf-8",
    )
    return path


def test_detects_pending_without_wiki_draft():
    path = write_pending()
    try:
        with tempfile.TemporaryDirectory() as td:
            state = Path(td) / "state.json"
            review_dir = Path(td) / "reviews"
            result = run_cmd(
                "--state", str(state),
                "plan",
                "--nodes-json", "tests/fixtures/draft_postflight/nodes-empty.json",
                "--render-missing-review-dir", str(review_dir),
            )
            data = json.loads(result.stdout)
            assert data["pending_without_wiki_draft_count"] == 1
            missing = data["pending_without_wiki_draft"][0]
            assert missing["slug"] == "postflight-test-draft"
            assert missing["draft_doc_title"] == "[Draft 2026-06-14] 测试草稿标题"
            assert Path(missing["review_markdown_path"]).exists()
            audit = run_cmd(
                "--state", str(state),
                "audit",
                "--nodes-json", "tests/fixtures/draft_postflight/nodes-empty.json",
                check=False,
            )
            assert audit.returncode == 2
    finally:
        path.unlink(missing_ok=True)


def test_detects_unnotified_existing_wiki_draft_and_mark_notified():
    path = write_pending()
    try:
        with tempfile.TemporaryDirectory() as td:
            state = Path(td) / "state.json"
            result = run_cmd(
                "--state", str(state),
                "plan",
                "--nodes-json", "tests/fixtures/draft_postflight/nodes-with-draft.json",
            )
            data = json.loads(result.stdout)
            assert data["pending_without_wiki_draft_count"] == 0
            assert data["needs_notification_count"] == 1
            draft = data["drafts"][0]
            assert draft["slug"] == "postflight-test-draft"
            assert "/publish postflight-test-draft" in draft["review_message"]

            run_cmd(
                "--state", str(state),
                "mark-notified",
                "--slug", "postflight-test-draft",
                "--title", "测试草稿标题",
                "--node-token", "wikidraft123",
                "--doc-url", "https://vcnd3kpj0wx8.feishu.cn/wiki/wikidraft123",
            )
            result2 = run_cmd(
                "--state", str(state),
                "plan",
                "--nodes-json", "tests/fixtures/draft_postflight/nodes-with-draft.json",
            )
            data2 = json.loads(result2.stdout)
            assert data2["needs_notification_count"] == 0
            assert data2["ok"] is True
    finally:
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    test_detects_pending_without_wiki_draft()
    test_detects_unnotified_existing_wiki_draft_and_mark_notified()
    print("draft_postflight tests passed")
