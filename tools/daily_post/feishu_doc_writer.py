#!/usr/bin/env python3
"""
feishu_doc_writer.py - write content to Feishu doc (overwrite mode)

Problem: --content starting with "---" causes argparse "bad flag syntax" error
when passed as a subprocess list arg.

Solution: write content to a temp file in WORK_DIR, then pass
"@./_feishu_write_tmp.md" as --content. Run subprocess with cwd=WORK_DIR
so lark-cli can read the relative path.

Usage:
  feishu_doc_writer.py <profile> <doc_id> <content_file>
  feishu_doc_writer.py <profile> <doc_id> -   (read from stdin)
"""
import sys, subprocess, json, os, tempfile, shutil

WORK_DIR = "/root/.openclaw/workspace/ai_blog"
TMP_FILE = "_feishu_write_tmp.md"

def write_doc(profile, doc_id, content, doc_format="markdown"):
    tmp_path = os.path.join(WORK_DIR, TMP_FILE)
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(content)
        cmd = [
            "lark-cli", "--profile", profile, "--as", "user",
            "docs", "+update",
            "--doc", doc_id,
            "--command", "overwrite",
            "--content", f"@{TMP_FILE}",
            "--doc-format", doc_format,
            "--format", "json"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=WORK_DIR)
        if result.returncode != 0:
            print(f"write_doc failed rc={result.returncode}: {result.stderr[:200]}", file=sys.stderr)
            return False
        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            print(f"JSON parse error: {result.stdout[:200]}", file=sys.stderr)
            return False
        if not data.get("ok"):
            print(f"lark-cli ok=false: {result.stdout[:200]}", file=sys.stderr)
            return False
        return True
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: feishu_doc_writer.py <profile> <doc_id> [content_file|-]", file=sys.stderr)
        sys.exit(1)
    profile, doc_id = sys.argv[1], sys.argv[2]
    content = open(sys.argv[3], encoding="utf-8").read() if len(sys.argv) > 3 and sys.argv[3] != "-" else sys.stdin.read()
    ok = write_doc(profile, doc_id, content)
    sys.exit(0 if ok else 1)
