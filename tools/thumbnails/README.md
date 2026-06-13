# Thumbnails

为每篇博文生成 1200×630（OG 标准比例）的封面缩略图。

## 风格

- **背景**：紫色三段渐变（`#1a1033 → #3d1f6e → #7b3aa8`）+ 网格纹 + 暗角，呼应站点 favicon
- **主题图**：右侧大插画，每篇一个独立的 SVG motif（在 `motifs/` 下）
- **文字**：左侧两行大标题（Noto Serif CJK Bold）+ 上方小 kicker（Noto Sans CJK，橙色 `#f0a020`）
- **底部品牌带**：浅色横线 + 站名 "替身的小本子 · Tishen's Notebook" + 右下角小铃铛标记

所有图片本地生成、放进 `public/images/thumbnails/`，不引用任何外部图床（避免版权风险与图片失效）。

## 运行

需要 `cairosvg` + `Pillow`：

```bash
pip3 install --break-system-packages cairosvg Pillow
python3 tools/thumbnails/gen_thumbnails.py
```

## 加新文章时

1. 在 `motifs/` 下新建一个 SVG 文件 `<slug>.svg`，画一个 ~300×280 的右侧主题图
   - 可参考 `city.svg / notes.svg / home.svg / boston.svg` 的风格（白色描边 + 橙色重点 + `transform="translate(800~820, 150~170)"`）
2. 在 `gen_thumbnails.py` 的 `POSTS` 列表里追加一项：
   ```python
   {
       "slug": "<post-slug>",
       "motif": "<slug>.svg",
       "title": ["第一行（≤12字）", "第二行（≤14字）"],
       "kicker": "分类 · 标签",
   }
   ```
3. `python3 tools/thumbnails/gen_thumbnails.py` 重新跑一次（4 张全部重渲，开销约 1 秒）
4. 在文章 frontmatter 里设 `thumbnail: '/images/thumbnails/<post-slug>.png'`
5. `pnpm run build` 验证

## 不要

- ❌ 不要从外网 hotlink 图（图源会失效，可能有版权）
- ❌ 不要用 stock photo 网站的图（即使是 free tier 也常带署名要求）
- ❌ 不要用未经允许的真人/品牌 logo
- ✅ 要么本地生成（这套脚本），要么自己画/拍

## 风格示例

跑完一次后，所有缩略图都长成统一的样子。在博客首页 / 文章列表页 / Open Graph / Twitter Card 里都会用到。
