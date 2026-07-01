#!/usr/bin/env python3
"""
Auto-generate a motif SVG + append to gen_thumbnails.py POSTS list.

Usage:
    python3 auto_thumbnail.py <slug> <title_line1> <title_line2> <kicker> [tag1,tag2,...]

After running:
1. Picks one of GENERIC_MOTIFS (defined in motif_templates.py) based on tags.
2. Writes motifs/<slug>.svg.
3. Appends the post entry to gen_thumbnails.py POSTS list (idempotent on slug).
4. Calls gen_thumbnails.py to actually render.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(ROOT))
THUMB_DIR = os.path.join(REPO, "tools", "thumbnails")
MOTIFS_DIR = os.path.join(THUMB_DIR, "motifs")
GEN_PY = os.path.join(THUMB_DIR, "gen_thumbnails.py")

# Import motif templates
sys.path.insert(0, ROOT)
from motif_templates import GENERIC_MOTIFS, pick_motif_key  # noqa: E402


def _escape_py(s: str) -> str:
    """把字符串安全地转义为 Python 字符串字面量（用于插进 gen_thumbnails.py 的 POSTS 表）。"""
    return (
        s.replace("\\", "\\\\")
         .replace('"', '\\"')
         .replace("\n", "\\n")
         .replace("\r", "\\r")
         .replace("\t", "\\t")
    )


def already_in_posts(slug: str) -> bool:
    """检查 slug 是否已在 gen_thumbnails.py POSTS 表中（幂等）。"""
    content = open(GEN_PY).read()
    # slug 是 ASCII，转义前后一样，直接查即可
    return f'"slug": "{slug}"' in content


def append_to_posts(slug: str, motif_filename: str, t1: str, t2: str, kicker: str):
    src = open(GEN_PY).read()
    marker = "]\n\nW, H = 1200, 630"
    if marker not in src:
        raise RuntimeError("gen_thumbnails.py POSTS marker not found")
    entry = (
        f'    {{\n'
        f'        "slug": "{_escape_py(slug)}",\n'
        f'        "motif": "{_escape_py(motif_filename)}",\n'
        f'        "title": ["{_escape_py(t1)}", "{_escape_py(t2)}"],\n'
        f'        "kicker": "{_escape_py(kicker)}",\n'
        f'    }},\n'
    )
    new_src = src.replace(marker, entry + marker)
    open(GEN_PY, "w").write(new_src)


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(1)
    slug = sys.argv[1]
    t1 = sys.argv[2]
    t2 = sys.argv[3]
    kicker = sys.argv[4]
    # tags 格式：tag1,tag2,... 逗号分隔
    tags = [t.strip() for t in sys.argv[5].split(",")] if len(sys.argv) > 5 else []

    motif_path = os.path.join(MOTIFS_DIR, f"{slug}.svg")
    motif_key = pick_motif_key(tags)
    print(f"motif: picked '{motif_key}' from tags={tags}")
    if not os.path.exists(motif_path):
        with open(motif_path, "w") as f:
            f.write(GENERIC_MOTIFS[motif_key])
        print(f"motif: wrote {motif_path}")
    else:
        print(f"motif: already exists at {motif_path}, leaving as is")

    if not already_in_posts(slug):
        append_to_posts(slug, f"{slug}.svg", t1, t2, kicker)
        print(f"posts: appended entry for slug={slug}")
    else:
        print(f"posts: slug={slug} already in gen_thumbnails.py, skipping append")

    print("rendering...")
    r = subprocess.run([sys.executable, GEN_PY], capture_output=True, text=True)
    if r.returncode != 0:
        print("RENDER FAILED:")
        print(r.stdout)
        print(r.stderr)
        sys.exit(2)
    # show only the line for our slug
    for line in r.stdout.splitlines():
        if slug in line:
            print(line)

    # 渲染成功后，主动将 thumbnail 字段注入到 frontmatter。
    md_candidates = [
        os.path.join(REPO, "pending", f"{slug}.md"),
        os.path.join(REPO, "posts", f"{slug}.md"),
    ]
    md_path = next((p for p in md_candidates if os.path.exists(p)), None)
    if md_path is None:
        print(
            f"⚠️  frontmatter inject 跳过：未找到 {slug}.md。"
            f" 请手动补 thumbnail: '/images/thumbnails/{slug}.png'。"
        )
        return

    lint_path = os.path.join(ROOT, "lint_frontmatter.py")
    if not os.path.exists(lint_path):
        print(f"⚠️  lint_frontmatter.py 不存在，跳过 thumbnail 注入")
        return

    print(f"注入 thumbnail 到 {md_path} 的 frontmatter...")
    r2 = subprocess.run(
        [sys.executable, lint_path, "--fix", "--inject-thumbnail", md_path],
        capture_output=True,
        text=True,
    )
    print(r2.stdout)
    if r2.returncode != 0 and r2.stderr:
        print(r2.stderr)


if __name__ == "__main__":
    main()
