#!/usr/bin/env python3
"""
check_chinese_in_code.py — pre-commit gate

Block Chinese characters in code/config/URL-path files. Chinese is allowed ONLY in:
  1. Markdown body (posts/, pending/, content/, source/_posts/)
  2. Feishu wiki content
  3. IM / commit message text

This is a hard rule. If this script exits non-zero, husky will block the commit.

Usage:
  python3 tools/check_chinese_in_code.py [--staged] [--paths PATH ...]

Default mode (no args): scan staged files that are about to be committed.
Exit codes:
  0 — no Chinese in any code/config file
  1 — at least one forbidden file contains Chinese; commit blocked
  2 — internal error
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Files where Chinese IS allowed (markdown body)
ALLOWED_DIRS = ("posts/", "pending/", "content/", "source/_posts/", "docs/content/")

# File extensions where Chinese MUST NOT appear (code/config/URL)
CODE_EXTENSIONS = {
    ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".json", ".jsonc", ".json5",
    ".yaml", ".yml",
    ".toml",
    ".scss", ".css", ".less",
    ".html", ".vue", ".svelte",
}

# Top-level config files (no extension or special names) that must be ASCII-only
TOP_LEVEL_CONFIG = {
    "next.config.ts", "next.config.js", "next.config.mjs",
    "vite.config.ts", "vite.config.js", "vite.config.mjs",
    "tsconfig.json", "jsconfig.json",
    "package.json", "pnpm-lock.yaml", "yarn.lock",
    ".eslintrc", ".eslintrc.js", ".eslintrc.json",
    ".prettierrc", ".prettierrc.js", ".prettierrc.json",
    "robots.txt", "sitemap.xml",
    "Dockerfile", "Makefile",
    ".gitignore", ".gitattributes", ".editorconfig",
    "vercel.json", "netlify.toml", "wrangler.toml",
}

CHINESE_RE = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\uff00-\uffef]")


def is_allowed_markdown(path: str) -> bool:
    """Markdown files inside specific content dirs are allowed to contain Chinese."""
    p = path.replace("\\", "/")
    if not p.endswith(".md"):
        return False
    return any(p.startswith(d) for d in ALLOWED_DIRS)


def get_staged_files() -> list[str]:
    """Return list of files staged for commit (added/copied/modified/renamed)."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True,
    )
    return [f for f in result.stdout.splitlines() if f]


def has_chinese(path: Path) -> tuple[bool, str]:
    """Return (has_chinese, offending_line). Reads file as utf-8 with errors='replace'."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeDecodeError) as e:
        return False, f"<read error: {e}>"
    m = CHINESE_RE.search(text)
    if not m:
        return False, ""
    # find line of first hit
    idx = m.start()
    line_no = text.count("\n", 0, idx) + 1
    line = text.splitlines()[line_no - 1] if line_no <= len(text.splitlines()) else ""
    return True, f"line {line_no}: {line.strip()[:120]}"


def should_check(path: str) -> bool:
    """Decide if this file path must be ASCII-only."""
    p = Path(path)
    # Whitelist: markdown content files
    if is_allowed_markdown(path):
        return False
    # Whitelist: this very script + check scripts dir
    if "check_chinese_in_code" in p.name:
        return False
    if p.name.startswith("check_") and p.suffix == ".py":
        return False  # other check scripts may contain Chinese in comments
    # Whitelist: i18n locale dictionaries
    if any(part in p.parts for part in ("locales", "i18n", "translations", "locale")):
        return False
    # Whitelist: 404/error pages (i18n dicts are the long-term fix, not this gate)
    if p.suffix in {".tsx", ".jsx"} and p.name in {
        "not-found.tsx", "error.tsx", "global-error.tsx", "loading.tsx"
    }:
        return False
    # Top-level config files
    if path in TOP_LEVEL_CONFIG or p.name in TOP_LEVEL_CONFIG:
        return True
    # Code files by extension
    if p.suffix.lower() in CODE_EXTENSIONS:
        return True
    # Files inside routes/, pages/, app/, src/ (URL paths)
    if any(part in p.parts for part in ("routes", "pages", "app", "src", "lib", "components")):
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--staged", action="store_true",
                    help="Scan git staged files (default when no --paths)")
    ap.add_argument("--paths", nargs="*", default=[],
                    help="Explicit file paths to scan")
    args = ap.parse_args()

    if args.paths:
        files = args.paths
    elif args.staged or not args.paths:
        files = get_staged_files()
    else:
        files = args.paths

    if not files:
        return 0

    violations: list[tuple[str, str]] = []
    for f in files:
        if not should_check(f):
            continue
        p = Path(f)
        if not p.exists():
            continue
        bad, detail = has_chinese(p)
        if bad:
            violations.append((f, detail))

    if violations:
        print("=" * 60)
        print("BLOCKED: commit contains Chinese in code/config files")
        print("=" * 60)
        print()
        print("Rule: code / config / route / URL path files must be ASCII-only.")
        print("Chinese is allowed only in:")
        print("  - markdown body (posts/, pending/)")
        print("  - Feishu wiki content")
        print("  - IM / commit message text")
        print()
        for f, detail in violations:
            print(f"  X {f}")
            print(f"      {detail}")
        print()
        print("Fix:")
        print("  1. Move Chinese strings to markdown body content")
        print("  2. URL / route / redirect: use ASCII or URL-encoded (%XX)")
        print("  3. i18n: use next-intl / i18next dictionaries, not TS literals")
        print()
        print("If this is a false positive (e.g. comment): git commit --no-verify")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
