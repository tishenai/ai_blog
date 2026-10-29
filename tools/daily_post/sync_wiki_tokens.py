#!/usr/bin/env python3
"""把飞书 wiki node/doc token 回写到 pending/ 文章的 frontmatter，并立即提交入库。

为什么必须提交：
  postflight 在 17:30 回写 token，次日 17:00 的写稿 cron 会执行 git stash push，
  把这些 token 暂存掉，导致飞书草稿与仓库的映射永久丢失（10-15~10-29 已发生多次）。
  本脚本在回写后立刻 git commit，使次日 cron 看到的是干净工作区，无内容可被 stash。

用法:
    python3 tools/daily_post/sync_wiki_tokens.py <results.json>
    results.json 格式: [{"slug": "...", "node_token": "...", "doc_id": "..."}, ...]
    也支持直接传 slug=node:doc 形式: sync_wiki_tokens.py --inline slug=NODE:DOC
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PENDING = REPO / "pending"


def write_tokens(slug: str, node_token: str, doc_token: str) -> bool:
    path = PENDING / f"{slug}.md"
    if not path.exists():
        print(f"❌ 文件不存在: {path}")
        return False
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^(---\n)(.*?)(\n---\n)", content, re.DOTALL)
    if not match:
        print(f"❌ frontmatter 解析失败: {slug}")
        return False
    fm = match.group(2)
    # 去掉旧 token 行后重新插入，避免重复
    fm = re.sub(r"^feishu_wiki_node_token:.*\n", "", fm, flags=re.MULTILINE)
    fm = re.sub(r"^feishu_wiki_doc_token:.*\n", "", fm, flags=re.MULTILINE)
    token_block = f"feishu_wiki_node_token: {node_token}\nfeishu_wiki_doc_token: {doc_token}\n"
    fm = re.sub(r"^(thumbnail:)", token_block + r"\1", fm, count=1, flags=re.MULTILINE)
    if "feishu_wiki_node_token:" not in fm:
        fm = fm.rstrip("\n") + "\n" + token_block.rstrip("\n") + "\n"
    path.write_text(content[: match.start(2)] + fm + content[match.end(2):], encoding="utf-8")
    print(f"✅ {slug}: node={node_token} doc={doc_token}")
    return True


def commit_if_changed() -> bool:
    """只在确有 token 变更时提交，避免制造空 commit。"""
    diff = subprocess.run(
        ["git", "-C", str(REPO), "diff", "--name-only", "--", "pending/"],
        capture_output=True, text=True,
    ).stdout.strip()
    if not diff:
        print("ℹ️  pending/ 无变更，无需提交")
        return False
    subprocess.run(["git", "-C", str(REPO), "add", "pending/"], check=True)
    res = subprocess.run(
        ["git", "-C", str(REPO), "commit", "-m", "chore: 回写文章飞书 wiki token（防止次日 cron stash 吞掉）"],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        print(f"❌ commit 失败: {res.stderr.strip()}")
        return False
    print(f"✅ 已提交: {res.stdout.strip().splitlines()[0] if res.stdout.strip() else ''}")
    return True


def main() -> int:
    items = []
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args[0] == "--inline":
        for a in args[1:]:
            slug, _, pair = a.partition("=")
            node, _, doc = pair.partition(":")
            items.append({"slug": slug, "node_token": node, "doc_id": doc})
    else:
        data = json.loads(Path(args[0]).read_text(encoding="utf-8"))
        items = data if isinstance(data, list) else [data]

    ok = True
    for it in items:
        if write_tokens(it["slug"], it["node_token"], it["doc_id"]):
            pass
        else:
            ok = False
    commit_if_changed()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
