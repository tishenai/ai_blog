#!/usr/bin/env python3
"""
Pick the next topic from topic_pool.md.

Priority order (most important first):
1. Today's freshly scraped entries (used_at = today) — these are hot-news anchored
2. Yesterday's entries (used_at = yesterday) — still somewhat fresh
3. Older entries — only if no fresh options remain

Among entries in the same freshness tier, prefer higher rule_score (tag + keyword match).

Returns the first matching pending row as JSON.
Does NOT mark it as used. Caller marks it after successful publish via mark_topic_used.py.
"""
import json
import os
import re
import sys
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(ROOT, "topic_pool.md")

TODAY = datetime.now().strftime("%Y-%m-%d")
YESTERDAY = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# Tags / keywords for rule-based scoring
HIGH_TAGS = {"智能体", "Agent", "OpenAI", "Anthropic", "Claude", "GPT",
             "安全/对齐", "Hugging Face", "GitHub", "MCP/工具", "编码",
             "论文/研究", "现象/趋势", "产品更新", "多模态", "推理"}
LOW_TAGS = {"具身智能", "端侧", "视频", "图像生成", "部署/工程",
            "政策/监管", "数据/训练", "教程/实践", "开源/仓库",
            "机器人", "AR/VR", "可穿戴", "行业动态"}
GOOD_KW = ["AI", "Agent", "LLM", "大模型", "模型", "ChatGPT", "Claude", "GPT",
           "OpenAI", "Anthropic", "推理", "智能体", "RAG", "prompt",
           "上下文", "token", "幻觉", "对齐", "安全", "能力", "涌现",
           "红队", "沙盒", "越狱", "攻击", "自主", "自动化"]


def parse_table_row(line: str):
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(parts) < 7:
        return None
    n, slug, title, angle, tags, status, used_at = parts[:7]
    if not slug or slug == "slug" or "---" in slug:
        return None
    return {
        "n": n, "slug": slug, "title_zh": title,
        "angle": angle,
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "status": status.lower(),
        "used_at": used_at,
    }


def rule_score(row: dict) -> int:
    """Higher = more suitable for the AI-agent-perspective blog."""
    s = 0
    tag_set = set(row["tags"])
    for t in tag_set:
        if t in HIGH_TAGS:
            s += 10
        if t in LOW_TAGS:
            s -= 15
    title = row["title_zh"]
    for kw in GOOD_KW:
        if kw.lower() in title.lower():
            s += 3
    return s


def get_published_slugs():
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(ROOT)), "posts")
    if not os.path.isdir(posts_dir):
        return set()
    return {
        os.path.splitext(f)[0]
        for f in os.listdir(posts_dir)
        if f.endswith(".md")
    }


def main():
    published = get_published_slugs()

    if not os.path.exists(POOL):
        print(json.dumps({"error": f"topic_pool.md not found at {POOL}"}))
        sys.exit(1)

    in_pending = False
    candidates = []

    with open(POOL) as f:
        for idx, line in enumerate(f, 1):
            ls = line.strip()
            if ls.startswith("## Pending"):
                in_pending = True
                continue
            if ls.startswith("## ") and in_pending:
                break
            if not in_pending:
                continue
            if not ls.startswith("|"):
                continue
            row = parse_table_row(line)
            if row is None:
                continue
            if row["status"] != "pending":
                continue
            if row["slug"] in published:
                continue

            date_str = row["used_at"].strip()[:10] if row["used_at"] else ""

            # Tier 1: today's freshly scraped entries
            if date_str == TODAY:
                tier = 0
            # Tier 2: yesterday's entries
            elif date_str == YESTERDAY:
                tier = 1
            # Tier 3: older or unknown date
            else:
                tier = 2

            candidates.append({
                "tier": tier,
                "score": rule_score(row),
                "line_no": idx,
                **row,
            })

    if not candidates:
        print(json.dumps({"error": "no pending topic available (all published or none left)"}))
        sys.exit(2)

    # Sort: tier ASC (fresh first), then score DESC (best match first)
    candidates.sort(key=lambda x: (x["tier"], -x["score"]))

    chosen = candidates[0]
    result = {
        "n": chosen["n"],
        "slug": chosen["slug"],
        "title_zh": chosen["title_zh"],
        "angle": chosen["angle"],
        "tags": chosen["tags"],
        "status": chosen["status"],
        "used_at": chosen["used_at"],
        "tier": chosen["tier"],
        "rule_score": chosen["score"],
        "line_no": chosen["line_no"],
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
