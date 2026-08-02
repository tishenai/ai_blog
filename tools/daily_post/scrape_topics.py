#!/usr/bin/env python3
"""
Fetch latest AI hot news from aihot.virxact.com and add interesting topics
to topic_pool.md.

Usage:
    python3 scrape_topics.py [--max-topics N] [--dry-run]

Outputs topics to stdout in JSON format.
With --dry-run, only prints what would be added without modifying topic_pool.md.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(ROOT, "topic_pool.md")

TODAY = datetime.now().strftime("%Y-%m-%d")


def fetch_page(url: str) -> str:
    """Use chromium to fetch dynamic page content."""
    cmd = [
        "google-chrome", "--headless", "--disable-gpu", "--no-sandbox",
        "--dump-dom", url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout


def parse_timeline(html: str) -> list[dict]:
    """Parse aihot timeline HTML into structured article list."""
    articles = []

    card_pattern = re.compile(
        r'<article class="timeline-card">.*?</article>',
        re.DOTALL
    )

    for card_html in card_pattern.findall(html):
        title_m = re.search(r'class="timeline-title"[^>]*>([^<]+)</a>', card_html)
        if not title_m:
            continue
        title = title_m.group(1).strip()

        skip_words = ['AI 热点', '精选', '全部', '日报', '主题', '收藏', '反馈',
                      '更新日志', '搜索', '关于', '登录', '注册']
        if any(w in title for w in skip_words) or len(title) < 8:
            continue

        summary_m = re.search(r'<p class="timeline-summary">([^<]+)</p>', card_html)
        summary = summary_m.group(1).strip() if summary_m else ""

        tags = re.findall(r'class="tag"[^>]*>([^<]+)</a>', card_html)
        tags = [t.strip() for t in tags if t.strip()]

        src_m = re.search(r'class="timeline-source">([^<]+)</span>', card_html)
        source = src_m.group(1).strip() if src_m else ""

        score_m = re.search(r'class="timeline-score mono[^"]*">(\d+)</span>', card_html)
        score = int(score_m.group(1)) if score_m else 50

        day_m = re.search(r'class="timeline-date">([^<]+)</h2>', card_html)
        day = day_m.group(1).strip() if day_m else ""

        articles.append({
            "title": title,
            "summary": summary,
            "tags": tags,
            "source": source,
            "score": score,
            "day": day,
        })

    return articles


# Title patterns that indicate stale/recycled topics — news-cycle re-phrasings
# that have been in the pool multiple times and should be heavily penalized.
# These topics are "slow" angles dressed up as today's news.
STALE_PATTERNS = [
    "逃出测试", "入侵真实系统", "攻击真实系统",   # Anthropic rogue agent (over-covered)
    "桌面应用", "有点乱", "零标签",               # OpenAI desktop app (fluff angle)
    "系统提示词", "泄露", "完整泄露",              # Prompt leak (recycled every month)
    "失控", "欺骗与背叛",                          # Safety test anthropomorphization
    "龙虾", "善恶感",                               # Known over-used Claude existential pieces
]

# Tags that indicate great AI agent topics
HIGH_SCORE_TAGS = {
    "智能体", "Agent", "OpenAI", "Anthropic", "Claude", "GPT",
    "安全/对齐", "Hugging Face", "GitHub", "MCP/工具", "编码",
    "论文/研究", "现象/趋势", "产品更新", "搜索", "多模态", "推理"
}

# Tags to skip (too niche or hardware-focused)
SKIP_TAGS = {
    "具身智能", "端侧", "视频", "图像生成", "部署/工程", "政策/监管",
    "数据/训练", "教程/实践", "开源/仓库", "机器人", "AR/VR", "可穿戴",
    "行业动态",
}

GOOD_KW = [
    "AI", "Agent", "LLM", "大模型", "模型", "ChatGPT", "Claude",
    "GPT", "OpenAI", "Anthropic", "Grok", "Kimi", "豆包", "Gemini",
    "推理", "智能体", "RAG", "prompt", "上下文", "token", "幻觉",
    "对齐", "安全", "能力", "涌现", "红队", "沙盒", "越狱", "攻击",
    "自主", "自动化", "系统提示", "提示词",
]
BAD_KW = [
    "硬件", "芯片", "GPU", "手机", "电脑", "汽车", "智能音箱",
    "智能家居", "智能眼镜", "AR", "VR", "自动驾驶", "电动车",
]


def filter_topics(articles: list[dict], max_topics: int = 2) -> list[dict]:
    """
    Filter and score articles suitable for the blog (AI agent perspective).
    Penalizes stale/recycled topic patterns so they rarely get selected.
    """

    def score(article: dict) -> int:
        s = article["score"]
        tags = set(article["tags"])

        for t in tags:
            if t in HIGH_SCORE_TAGS:
                s += 15
            if t in SKIP_TAGS:
                s -= 20

        title = article["title"]

        # Penalize stale/recycled patterns heavily — these are slow topics
        # dressed as today's news and should almost never get selected.
        for pat in STALE_PATTERNS:
            if pat in title:
                s -= 30

        for kw in GOOD_KW:
            if kw.lower() in title.lower():
                s += 5
        for kw in BAD_KW:
            if kw in title:
                s -= 15

        return max(0, s)

    scored = [(score(a), a) for a in articles]
    scored.sort(key=lambda x: -x[0])

    return [a for _, a in scored[:max_topics]]


def title_to_slug(title: str) -> str:
    """Convert Chinese title to URL-safe slug."""
    import urllib.parse

    clean = re.sub(r'[^\w\s\u4e00-\u9fff]', '', title)
    chinese_words = re.findall(r'[\u4e00-\u9fff]+', clean)

    trans = {
        "大模型": "llm", "模型": "model", "人工智能": "ai",
        "智能体": "agent", "大语言模型": "llm",
        "多模态": "multimodal", "推理": "reasoning",
        "开源": "open-source", "发布": "release", "系统": "system",
        "提示词": "prompt", "上下文": "context", "能力": "capability",
        "安全": "safety", "对齐": "alignment", "攻击": "attack",
        "入侵": "intrusion", "越狱": "jailbreak", "红队": "red-team",
    }

    slug_parts = []
    for word in chinese_words:
        low = word.lower()
        slug_parts.append(trans.get(low, low))

    if len(slug_parts) >= 2:
        slug = "-".join(slug_parts[:4])
    elif slug_parts:
        slug = slug_parts[0]
    else:
        slug = re.sub(r'\s+', '-', clean)[:30]

    parts = slug.split("-")
    seen = set()
    uniq = []
    for p in parts:
        if p not in seen and len(p) > 1:
            seen.add(p)
            uniq.append(p)

    return "-".join(uniq)[:60]


def parse_table_row(line: str):
    """Parse one row of the topic pool markdown table."""
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(parts) < 7:
        return None
    n, slug, title, angle, tags, status, used_at = parts[:7]
    if not slug or slug == "slug" or "---" in slug:
        return None
    return {
        "n": n, "slug": slug, "title_zh": title,
        "angle": angle, "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "status": status.lower(), "used_at": used_at,
    }


def read_pool() -> str:
    with open(POOL) as f:
        return f.read()


def get_next_n(pool_content: str) -> int:
    numbers = re.findall(r'^\s*\|\s*(\d+)\s*\|', pool_content, re.MULTILINE)
    return max((int(n) for n in numbers), default=0) + 1


def add_topics_to_pool(articles: list[dict], dry_run: bool = False) -> list[dict]:
    pool = read_pool()
    next_n = get_next_n(pool)

    # Build a dict of existing slugs -> used_at for stale dedup
    existing_slugs = {}
    for line in pool.split("\n"):
        if not line.startswith("|"):
            continue
        row = parse_table_row(line)
        if row and row["slug"]:
            existing_slugs[row["slug"]] = row["used_at"].strip()

    new_rows = []
    for article in articles:
        slug = title_to_slug(article["title"])

        # If slug already exists in pool:
        # - If the existing entry was added today or yesterday -> skip (freshness ok, don't duplicate)
        # - If the existing entry is older -> allow replacement (stale entry should be superseded)
        from datetime import timedelta
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        if slug in existing_slugs:
            existing_date = existing_slugs[slug][:10] if existing_slugs[slug] else ""
            if existing_date in (TODAY, yesterday):
                continue  # fresh enough, don't add duplicate angle

        tags_str = ", ".join(article["tags"][:3]) if article["tags"] else "AI 热点"
        # Write TODAY as used_at so pick_topic.py can sort by freshness
        row = f'| {next_n}  | {slug} | {article["title"]} | AI 热点抓取：{article["summary"][:40]}… | {tags_str} | pending | {TODAY}   |'

        new_rows.append({
            "n": next_n,
            "slug": slug,
            "title": article["title"],
            "tags": article["tags"],
            "source": article["source"],
            "score": article["score"],
            "row": row,
            "used_at": TODAY,
        })
        next_n += 1

    if not new_rows:
        print(json.dumps({"info": "no new topics", "added": []}))
        return []

    if dry_run:
        print(json.dumps({"dry_run": True, "added": new_rows}, ensure_ascii=False, indent=2))
        return new_rows

    pending_end = pool.rfind("## Pending")
    used_pos = pool.find("## Used", pending_end)

    if used_pos == -1:
        insert_pos = pool.rfind("|")
    else:
        insert_pos = pool.rfind("|", 0, used_pos)

    rows_text = "\n".join(r["row"] for r in new_rows) + "\n"
    new_pool = pool[:insert_pos+1] + "\n" + rows_text + pool[insert_pos+1:]

    with open(POOL, 'w') as f:
        f.write(new_pool)

    return new_rows


def main():
    parser = argparse.ArgumentParser(description="Scrape AI hot news and add to topic pool")
    parser.add_argument("--max-topics", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("[scrape_topics] Fetching aihot.virxact.com...", file=sys.stderr)
    html = fetch_page("https://aihot.virxact.com/")
    if not html:
        print(json.dumps({"error": "Failed to fetch page"}))
        sys.exit(1)

    articles = parse_timeline(html)
    print(f"[scrape_topics] Parsed {len(articles)} articles from timeline", file=sys.stderr)

    if not articles:
        print(json.dumps({"error": "No articles found in page"}))
        sys.exit(1)

    filtered = filter_topics(articles, max_topics=args.max_topics)
    print(f"[scrape_topics] Filtered to {len(filtered)} topics", file=sys.stderr)
    for a in filtered:
        print(f"  [{a['score']}] {a['title']} | {','.join(a['tags'][:3])}", file=sys.stderr)

    added = add_topics_to_pool(filtered, dry_run=args.dry_run)

    print(json.dumps({
        "added_count": len(added),
        "topics": [{"n": a["n"], "slug": a["slug"], "title": a["title"],
                    "score": a["score"], "source": a["source"]} for a in added],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
