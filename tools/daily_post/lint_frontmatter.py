#!/usr/bin/env python3
"""
Frontmatter 规范校验工具（适配 SuzuBlog: https://suzu.zla.app/guide/posts/）

使用方式：
    python3 tools/daily_post/lint_frontmatter.py <md_path>                       # 仅校验
    python3 tools/daily_post/lint_frontmatter.py --fix <md_path>                 # 校验并尝试自动修复
    python3 tools/daily_post/lint_frontmatter.py --inject-thumbnail <md_path>    # 修正 thumbnail 路径
    （可与 --fix 组合使用）

校验规则（适配 SuzuBlog frontmatter 规范）：

  必填字段：
    - title (str)
    - date  (str, 形如 'YYYY-MM-DD' 或 'YYYY-MM-DD HH:MM:SS'，必须加引号)

  推荐字段：
    - tags        (list[str])
    - categories  (list[str])
    - thumbnail   (str)

  可选字段：
    - author, redirect, showComments, showLicense, showThumbnail, autoSlug, status

  常见错误（会警告，--fix 时自动修复）：
    - 'category' → 应该用 'categories' (list)
    - 'tag'      → 应该用 'tags' (list)
    - tags/categories 写成字符串 → 应该是数组

  非标字段（不在 SuzuBlog 规范里，会被忽略，--fix 时清理）：
    - subtitle, summary, excerpt

退出码：
    0 = 全部 OK（可能有 warnings 但没有错误）
    1 = 有错误（必填字段缺失或格式错误）
    2 = 文件不存在或无 frontmatter
"""

import sys
import os
import argparse
from datetime import datetime, date as date_cls

try:
    import yaml
except ImportError:
    print("❌ 需要 pyyaml: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ============== Suzu 规范 ==============
REQUIRED_FIELDS = {"title", "date"}
RECOMMENDED_FIELDS = {"tags", "categories", "thumbnail"}
OPTIONAL_FIELDS = {
    "author", "redirect", "showComments", "showLicense", "showThumbnail",
    "autoSlug", "status",
}
KNOWN_FIELDS = REQUIRED_FIELDS | RECOMMENDED_FIELDS | OPTIONAL_FIELDS

# 字段类型期望
LIST_FIELDS = {"tags", "categories"}
BOOL_FIELDS = {"showComments", "showLicense", "showThumbnail", "autoSlug"}

VALID_STATUS = {"published", "unlisted", "draft", "hidden"}

# 常见错误字段 → 推荐替换
COMMON_TYPOS = {
    "category": "categories",
    "tag": "tags",
}

# SuzuBlog 不支持的非标字段
NON_STANDARD = {"subtitle", "summary", "excerpt"}


def split_frontmatter(text):
    """从 markdown 文本里抽出 frontmatter 字符串和 body。
    返回 (fm_str, body_str)，若无 frontmatter 返回 (None, text)"""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1].strip(), parts[2]


def _slug_from_path(path):
    """从 md 文件路径推断 slug（去掉目录和 .md 后缀）。"""
    return os.path.splitext(os.path.basename(path))[0]


def lint(path, fix=False, inject_thumbnail=False):
    """
    校验单个 md 文件的 frontmatter。
    返回: (errors: list[str], warnings: list[str], fixed_text: str | None)
    """
    errors = []
    warnings = []

    if not os.path.isfile(path):
        return [f"文件不存在: {path}"], [], None

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    fm_str, body = split_frontmatter(text)
    if fm_str is None:
        return [f"缺少 frontmatter（必须以 --- 开头并有结束 ---）"], [], None

    try:
        data = yaml.safe_load(fm_str)
    except yaml.YAMLError as e:
        return [f"frontmatter YAML 解析失败: {e}"], [], None

    if not isinstance(data, dict):
        return [f"frontmatter 必须是 YAML 字典"], [], None

    # 必填字段
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"缺少必填字段: {field}")

    # title 类型
    if "title" in data and not isinstance(data["title"], str):
        errors.append("title 必须是字符串")

    # title 含中文/curly 引号时禁止套外层双引号（会导致 YAML 解析成嵌套引号字符串）
    # 正确写法：title: 我从其他 AI 那里"借"了什么
    # 错误写法：title: "我从其他 AI 那里"借"了什么"
    if "title" in data and isinstance(data["title"], str):
        t = data["title"]
        # 检查是否含有中文引号或 curly double quotes
        if any(c in t for c in ['"', '"', '"', '"']):
            # 用 source 直接检查 frontmatter 原文是否用了 "title: \"...\"" 的格式
            fm_lines = fm_str.split("\n")
            for line in fm_lines:
                stripped = line.strip()
                if stripped.startswith("title:"):
                    # 外层有双引号包裹 → 错误格式
                    after_colon = stripped[len("title:"):].strip()
                    if after_colon.startswith('"') and after_colon.endswith('"') and len(after_colon) >= 2:
                        errors.append(
                            "title 含中文/curly 引号时禁止套外层双引号。"
                            "正确格式：title: 我从其他 AI 那里\"借\"了什么"
                            "（去掉 title: 后面的引号，直接裸写）"
                        )
                    break

    # date 格式
    if "date" in data:
        date_val = data["date"]
        if not isinstance(date_val, str):
            # PyYAML 把没引号的 'YYYY-MM-DD' 解析成 date 对象
            warnings.append(
                f"date 没加引号（被 YAML 解析为 {type(date_val).__name__}），"
                f"应该写成 '{date_val}'（带引号）"
            )
        else:
            ok = False
            for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
                try:
                    datetime.strptime(date_val, fmt)
                    ok = True
                    break
                except ValueError:
                    continue
            if not ok:
                errors.append(
                    f"date 格式错误（应该是 YYYY-MM-DD 或 YYYY-MM-DD HH:MM:SS）：{date_val!r}"
                )

    # tags / categories 必须是 list
    for field in LIST_FIELDS:
        if field in data and not isinstance(data[field], list):
            warnings.append(
                f"{field} 应该是数组，当前: {type(data[field]).__name__}（值: {data[field]!r}）"
            )

    # status 枚举
    if "status" in data and data["status"] not in VALID_STATUS:
        errors.append(
            f"status 必须是 {sorted(VALID_STATUS)} 之一，当前: {data['status']!r}"
        )

    # bool 字段
    for field in BOOL_FIELDS:
        if field in data and not isinstance(data[field], bool):
            warnings.append(f"{field} 应该是 true/false，当前: {data[field]!r}")

    # typo
    for typo, correct in COMMON_TYPOS.items():
        if typo in data:
            warnings.append(
                f"字段名错误：'{typo}' 应该改成 '{correct}'（数组类型）"
            )

    # 非标字段
    for field in NON_STANDARD:
        if field in data:
            warnings.append(f"非 SuzuBlog 标准字段（会被忽略）：{field}")

    # 推荐字段缺失
    for field in RECOMMENDED_FIELDS:
        if field not in data:
            warnings.append(f"建议补充推荐字段: {field}")

    # 未知字段
    unknown = set(data.keys()) - KNOWN_FIELDS - set(COMMON_TYPOS.keys()) - NON_STANDARD
    for field in unknown:
        warnings.append(f"未识别字段（请确认拼写）: {field}")

    # 自动修复
    fixed_text = None
    if fix or inject_thumbnail:
        fixed_data = dict(data)
        changed = False

        # typo 修复
        for typo, correct in COMMON_TYPOS.items():
            if typo in fixed_data:
                val = fixed_data.pop(typo)
                if not isinstance(val, list):
                    if isinstance(val, str):
                        val = [v.strip() for v in val.split(",") if v.strip()]
                    else:
                        val = [val]
                if correct in fixed_data and isinstance(fixed_data[correct], list):
                    fixed_data[correct] = list(dict.fromkeys(fixed_data[correct] + val))
                else:
                    fixed_data[correct] = val
                changed = True

        # tags/categories 字符串 → list
        for field in LIST_FIELDS:
            if field in fixed_data and not isinstance(fixed_data[field], list):
                val = fixed_data[field]
                if isinstance(val, str):
                    fixed_data[field] = [v.strip() for v in val.split(",") if v.strip()]
                else:
                    fixed_data[field] = [val]
                changed = True

        # date 没加引号 → 转 str
        if "date" in fixed_data and not isinstance(fixed_data["date"], str):
            d = fixed_data["date"]
            if isinstance(d, datetime):
                fixed_data["date"] = d.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(d, date_cls):
                fixed_data["date"] = d.strftime("%Y-%m-%d")
            else:
                fixed_data["date"] = str(d)
            changed = True

        # 删除非标字段（仅在 --fix 模式下）
        if fix:
            for field in NON_STANDARD:
                if field in fixed_data:
                    fixed_data.pop(field)
                    changed = True

        # 注入 / 修正 thumbnail 路径（--inject-thumbnail 模式）
        # 只修 thumbnail，不注入 showLicense/showComments（字段名错误，SuzuBlog
        # 读取 yaml 时会自动注入默认值）
        if inject_thumbnail:
            slug = _slug_from_path(path)
            correct_thumb = f"/images/thumbnails/{slug}.png"
            existing = fixed_data.get("thumbnail", "")
            if existing != correct_thumb:
                fixed_data["thumbnail"] = correct_thumb
                changed = True

        if changed:
            new_fm = yaml.dump(
                fixed_data,
                allow_unicode=True,
                sort_keys=False,
                default_flow_style=False,
            ).strip()
            fixed_text = f"---\n{new_fm}\n---{body}"

    return errors, warnings, fixed_text


def main():
    parser = argparse.ArgumentParser(description="SuzuBlog frontmatter 校验工具")
    parser.add_argument("path", help="要校验的 markdown 文件路径")
    parser.add_argument("--fix", action="store_true", help="自动修复可修复的问题（typo/类型/非标字段）")
    parser.add_argument(
        "--inject-thumbnail",
        action="store_true",
        help="自动注入 / 修正 thumbnail 路径为 /images/thumbnails/<slug>.png（--fix 也清理 subtitle/slug 等非标字段）",
    )
    parser.add_argument("--quiet", action="store_true", help="只在出错时输出")
    args = parser.parse_args()

    errors, warnings, fixed_text = lint(
        args.path,
        fix=args.fix,
        inject_thumbnail=args.inject_thumbnail,
    )

    if not args.quiet or errors or warnings:
        print(f"📝 校验文件: {args.path}")

    if errors:
        print(f"\n❌ 错误 ({len(errors)}):")
        for e in errors:
            print(f"   - {e}")

    if warnings:
        print(f"\n⚠️  警告 ({len(warnings)}):")
        for w in warnings:
            print(f"   - {w}")

    if (args.fix or args.inject_thumbnail) and fixed_text is not None:
        with open(args.path, "w", encoding="utf-8") as f:
            f.write(fixed_text)
        print(f"\n✅ 已自动修复并写回 {args.path}")

    if not errors and not warnings:
        if not args.quiet:
            print("✅ frontmatter 规范无问题")
        return 0

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
