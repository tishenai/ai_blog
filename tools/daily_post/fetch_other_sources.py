#!/usr/bin/env python3
"""
Fallback AI news fetcher when aihot.virxact.com is dead.
Tries multiple public sources: hnrss.org (Hacker News frontpage),
36kr.com AI section, arxiv cs.AI, reddit r/MachineLearning RSS.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(ROOT, "topic_pool.md")
TODAY = datetime.now().strftime("%Y-%m-%d")

# 硬过滤：劣质标题关键词
EXCLUDE_KEYWORDS = re.compile(
    r'(消息人士|据报道|疑似|泄露|亿美元|千万美元|百万美元|融资|收购|上市|'
    r'死亡|跳楼|裁员|自杀|自闭症|恋童|性侵|儿童色情|虐童|偷税|漏税|嫖娼|'
    r'被查|被罚|股价暴跌|暴涨|崩盘|跑路|骗钱|被骗|欠款|逃税|权色|权钱|'
    r'被开除|被免职|被查|通缉|追捕|潜逃|落网|行贿|受贿|贪腐|腐败|'
    r'黑客|入侵|攻击|漏洞|勒索|病毒|木马|钓鱼|诈骗|欺诈|赌|毒|'
    r'艳照|出轨|小三|家暴|离婚|分手|恋情|绯闻)',
    re.I
)

AI_KEYWORDS = re.compile(
    r'\b(ai |ai$|artificial intelligence|machine learning|llm|large language model|'
    r'gpt|chatgpt|claude|gemini|openai|anthropic|deepmind|hugging face|huggingface|'
    r'mistral|copilot|neural|transformer|diffusion|agent|agents|agentic|'
    r'reinforcement|rag|embedding|vector|tokenizer|finetune|fine-tune|'
    r'generative|genai|inference|train(ing|ed)?|sft|rlhf|dpo|'
    r'pytorch|tensorflow|llama|qwen|deepseek|文心一言|通义千问|盘古|混元|'
    r'图像生成|视频生成|语音合成|多模态|multimodal|'
    r'自动驾驶|autonomous|drone|robot|人形机器人|'
    r'ai chip|npu|tpu|gpu|芯片|算力|参数|'
    r'sora|runway|pika|stability|midjourney|dall-e|dalle)',
    re.I
)


def http_get(url, timeout=15, headers=None):
    """Simple HTTP GET with timeout. Returns text or None."""
    try:
        req = urllib.request.Request(url, headers=headers or {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ai-blog-fetcher/1.0'
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            try:
                return data.decode('utf-8')
            except UnicodeDecodeError:
                return data.decode('utf-8', errors='ignore')
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
        print(f"  [WARN] fetch failed: {url}: {e}", file=sys.stderr)
        return None


def fetch_hnrss(max_items=30):
    """Fetch Hacker News frontpage via hnrss.org JSON feed."""
    print("[source] Hacker News via hnrss.org...")
    text = http_get("https://hnrss.org/frontpage.jsonfeed")
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    items = data.get('items', [])[:max_items]
    results = []
    for it in items:
        title = it.get('title', '').strip()
        url = it.get('url') or it.get('external_url') or it.get('id', '')
        if not title or not url:
            continue
        if not AI_KEYWORDS.search(title):
            continue
        if EXCLUDE_KEYWORDS.search(title):
            continue
        results.append({
            'source': 'Hacker News',
            'title': title,
            'url': url,
            'summary': (it.get('summary_text', '') or it.get('content_text', '') or '')[:300],
            'tags': ['HN', 'AI'],
        })
    print(f"  → {len(results)} AI-relevant items from HN")
    return results


def fetch_arxiv(max_items=15):
    """Fetch recent arxiv cs.AI submissions via arxiv API."""
    print("[source] arxiv cs.AI...")
    text = http_get(
        "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=20&sortBy=submittedDate&sortOrder=descending"
    )
    if not text:
        return []
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return []
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    results = []
    for entry in root.findall('atom:entry', ns)[:max_items]:
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        link = entry.find('atom:id', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip()[:300] if entry.find('atom:summary', ns) is not None else ''
        # 过滤非英文/非 AI
        if EXCLUDE_KEYWORDS.search(title):
            continue
        results.append({
            'source': 'arXiv cs.AI',
            'title': title,
            'url': link,
            'summary': summary,
            'tags': ['arXiv', '研究论文'],
        })
    print(f"  → {len(results)} items from arxiv")
    return results


def fetch_36kr_html(max_items=20):
    """Fetch 36kr.com AI section via HTML scrape."""
    print("[source] 36kr.com AI...")
    text = http_get("https://www.36kr.com/information/AI", timeout=20)
    if not text:
        return []
    # 抓 article title & url
    # 36kr 常见结构: <a class="article-item-title" href="URL">TITLE</a>
    # 备用: <a ... data-article-id...>TITLE</a>
    pattern = re.compile(
        r'<a[^>]+href="(/[^"]+)"[^>]*>([^<]{8,200})</a>',
        re.I
    )
    candidates = []
    for m in pattern.finditer(text):
        url = m.group(1)
        title = m.group(2).strip()
        if 'info' not in url and 'p/' not in url:
            continue
        if not AI_KEYWORDS.search(title):
            continue
        if EXCLUDE_KEYWORDS.search(title):
            continue
        candidates.append({
            'source': '36kr',
            'title': title,
            'url': 'https://www.36kr.com' + url if url.startswith('/') else url,
            'summary': '',
            'tags': ['36kr', '中文'],
        })
    # 去重
    seen = set()
    uniq = []
    for c in candidates:
        if c['title'] in seen:
            continue
        seen.add(c['title'])
        uniq.append(c)
    print(f"  → {len(uniq[:max_items])} items from 36kr")
    return uniq[:max_items]


def fetch_reddit_ml(max_items=20):
    """Fetch Reddit r/MachineLearning top via JSON."""
    print("[source] Reddit r/MachineLearning...")
    text = http_get(
        "https://www.reddit.com/r/MachineLearning/top.json?t=day&limit=20",
        headers={'User-Agent': 'ai-blog-fetcher/1.0 (research)'}
    )
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    items = data.get('data', {}).get('children', [])
    results = []
    for ch in items[:max_items]:
        d = ch.get('data', {})
        title = d.get('title', '').strip()
        url = d.get('url', '')
        if not title:
            continue
        if EXCLUDE_KEYWORDS.search(title):
            continue
        results.append({
            'source': 'Reddit r/MachineLearning',
            'title': title,
            'url': url or f"https://reddit.com{d.get('permalink','')}",
            'summary': d.get('selftext', '')[:300],
            'tags': ['Reddit', 'AI'],
        })
    print(f"  → {len(results)} items from reddit")
    return results


def append_to_pool(items, max_topics=5):
    """Append new topics to topic_pool.md. Returns count appended."""
    if not items:
        return 0

    # 读已有 titles 防重
    existing = set()
    if os.path.exists(POOL):
        with open(POOL, 'r', encoding='utf-8') as f:
            for line in f:
                # 抓 "Title: ..." 或 "标题: ..." 行
                m = re.match(r'[\s\-\*]*Title[:：]\s*(.+)', line)
                if m:
                    existing.add(m.group(1).strip()[:60])

    appended = 0
    new_lines = []
    for it in items:
        key = it['title'][:60]
        if key in existing:
            continue
        idx = appended + 1
        new_lines.append(
            f"\n### n={idx}  {it['title']}\n"
            f"  - source: {it['source']}\n"
            f"  - url: {it['url']}\n"
            f"  - summary: {it['summary'][:200]}\n"
            f"  - angle: \n"
            f"  - tags: {','.join(it['tags'])}\n"
            f"  - status: pending\n"
            f"  - added_at: {TODAY}\n"
        )
        existing.add(key)
        appended += 1
        if appended >= max_topics:
            break

    if not new_lines:
        return 0

    with open(POOL, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## {TODAY} 抓取批 (multi-source)\n")
        f.writelines(new_lines)
    return appended


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-topics', type=int, default=5)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--source', default='all',
                    choices=['all', 'hn', 'arxiv', '36kr', 'reddit'])
    args = ap.parse_args()

    all_items = []
    if args.source in ('all', 'hn'):
        all_items.extend(fetch_hnrss())
    if args.source in ('all', 'arxiv'):
        all_items.extend(fetch_arxiv())
    if args.source in ('all', '36kr'):
        all_items.extend(fetch_36kr_html())
    if args.source in ('all', 'reddit'):
        all_items.extend(fetch_reddit_ml())

    # 按 source 优先级混合（让中文站优先，因博客中文）
    priority = {'36kr': 0, 'Hacker News': 1, 'Reddit r/MachineLearning': 2, 'arXiv cs.AI': 3}
    all_items.sort(key=lambda x: priority.get(x['source'], 99))

    print(f"\n[total] {len(all_items)} AI-relevant items from all sources")
    for it in all_items[:8]:
        print(f"  [{it['source']:25s}] {it['title'][:70]}")

    if args.dry_run:
        print("\n[dry-run] not modifying topic_pool.md")
        return 0

    appended = append_to_pool(all_items, max_topics=args.max_topics)
    print(f"\n[done] appended {appended} new topics to {POOL}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
