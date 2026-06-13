#!/usr/bin/env python3
"""
Pick the next topic from topic_pool.md.
- Reads the markdown table.
- Returns the first row in `## Pending` whose status is `pending`.
- Prints JSON: {slug, title_zh, angle, tags, line_no_in_pool}

Does NOT mark it as used. The caller (cron agent) marks it after a successful
publish via mark_topic_used.py.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(ROOT, "topic_pool.md")


def parse_table_row(line: str):
    # | 1 | slug | title-zh | angle | tags | status | used_at |
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(parts) < 7:
        return None
    n, slug, title, angle, tags, status, used_at = parts[:7]
    if not slug or slug == "slug" or "---" in slug:
        return None
    return {
        "n": n,
        "slug": slug,
        "title_zh": title,
        "angle": angle,
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "status": status.lower(),
        "used_at": used_at,
    }


def main():
    if not os.path.exists(POOL):
        print(json.dumps({"error": f"topic_pool.md not found at {POOL}"}))
        sys.exit(1)
    in_pending_section = False
    with open(POOL) as f:
        for idx, line in enumerate(f, 1):
            ls = line.strip()
            if ls.startswith("## Pending"):
                in_pending_section = True
                continue
            if ls.startswith("## ") and in_pending_section:
                break
            if not in_pending_section:
                continue
            if not ls.startswith("|"):
                continue
            row = parse_table_row(line)
            if row is None:
                continue
            if row["status"] == "pending":
                row["line_no"] = idx
                print(json.dumps(row, ensure_ascii=False))
                return
    print(json.dumps({"error": "no pending topic available"}))
    sys.exit(2)


if __name__ == "__main__":
    main()
