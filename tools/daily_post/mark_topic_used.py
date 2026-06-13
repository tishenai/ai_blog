#!/usr/bin/env python3
"""
Mark a topic as used in topic_pool.md.

Usage:
    python3 mark_topic_used.py <slug> <YYYY-MM-DD> <post_url>

Behavior:
- Finds the row in `## Pending` where slug matches.
- Removes it from Pending table.
- Appends a row to `## Used` with used_at and post_url.
- Writes file back.

If slug not found in Pending, exits with code 2 (idempotent: don't fail
twice).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(ROOT, "topic_pool.md")


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    slug, used_at, post_url = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(POOL) as f:
        lines = f.readlines()

    in_pending = False
    in_used = False
    pending_row_idx = None
    pending_row_title = None
    used_table_last_row_idx = None

    for i, line in enumerate(lines):
        ls = line.strip()
        if ls.startswith("## Pending"):
            in_pending, in_used = True, False
            continue
        if ls.startswith("## Used"):
            in_pending, in_used = False, True
            continue
        if ls.startswith("## ") and not ls.startswith("## Pending") and not ls.startswith("## Used"):
            in_pending, in_used = False, False
            continue

        if in_pending and ls.startswith("|"):
            cells = [c.strip() for c in ls.strip("|").split("|")]
            if len(cells) >= 6 and cells[1] == slug:
                pending_row_idx = i
                pending_row_title = cells[2]
        if in_used and ls.startswith("|"):
            cells = [c.strip() for c in ls.strip("|").split("|")]
            if len(cells) >= 4 and cells[1] and cells[1] != "slug" and "---" not in cells[1]:
                used_table_last_row_idx = i

    if pending_row_idx is None:
        print(f"slug '{slug}' not found in Pending; nothing to do.")
        sys.exit(2)

    # Remove from pending, then build the used row
    title = pending_row_title or slug
    used_row = f"| - | {slug} | {title} | {used_at} | {post_url} |\n"

    new_lines = []
    for i, line in enumerate(lines):
        if i == pending_row_idx:
            continue
        new_lines.append(line)
        if i == used_table_last_row_idx:
            new_lines.append(used_row)

    # Edge case: Used 表为空（还没有任何数据行）。
    # 找到 "## Used" 后的表头分隔行（|---|---|...|），在其后插入 used_row。
    if used_table_last_row_idx is None:
        new_lines = []
        in_used2 = False
        sep_seen = False
        inserted = False
        for i, line in enumerate(lines):
            if i == pending_row_idx:
                continue
            new_lines.append(line)
            ls = line.strip()
            if ls.startswith("## Used"):
                in_used2 = True
                sep_seen = False
                continue
            if in_used2 and ls.startswith("|") and ("---" in ls or ":---" in ls):
                # 表头分隔行，下一行才是数据区。在表头分隔后立刻插入 used_row。
                sep_seen = True
                new_lines.append(used_row)
                inserted = True
                in_used2 = False
                continue
        if not inserted:
            print("⚠️  Used 表未找到表头分隔行，跳过添加")

    with open(POOL, "w") as f:
        f.writelines(new_lines)
    print(f"OK: marked '{slug}' as used at {used_at} -> {post_url}")


if __name__ == "__main__":
    main()
