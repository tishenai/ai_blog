#!/usr/bin/env python3
"""
在文章末尾追加或替换写作声明。
用法：python3 tools/daily_post/write_disclaimer.py <is_manual> <article_md>

is_manual: "true" 或 "false"
article_md: 文章 .md 文件路径

逻辑：
  - 读取文章，从末尾往前找最后一个 --- 分隔线
  - 删掉分隔线之后所有内容
  - 追加声明段落（结尾换行）
"""
import sys
import re
from pathlib import Path

is_manual = len(sys.argv) > 1 and sys.argv[1].lower() == "true"
article_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None

disclaimer = (
    "这篇文章由本博客的 AI 作者（替身）生成，由人类手动选题，未经人类作者改写主体内容。"
    if is_manual
    else "这篇文章由本博客的 AI 作者（替身）生成，由 AI 自动选题，未经人类作者改写主体内容。"
)

NEW_CONTENT = f"\n---\n\n{disclaimer}\n"

if article_path and article_path.exists():
    content = article_path.read_text(encoding="utf-8")
    # 只匹配末尾的分隔线，避免碰到 frontmatter 里的分隔线
    # 策略：从文件末尾往前找 "\n---\n" 模式
    last_sep = content.rfind("\n---\n")
    if last_sep != -1:
        new_content = content[:last_sep] + NEW_CONTENT
    else:
        new_content = content.rstrip() + NEW_CONTENT
    article_path.write_text(new_content, encoding="utf-8")
    print(f"[disclaimer] is_manual={is_manual} → {article_path}")
    print(f"[disclaimer] 声明：{disclaimer}")
else:
    print(f"[disclaimer] is_manual={is_manual}")
    print(f"[disclaimer] 声明：{disclaimer}")
