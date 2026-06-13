#!/usr/bin/env python3
"""Compose 1200x630 thumbnails: SVG bg+motif rasterized via cairosvg, then overlay CJK title via PIL."""
import os, io, cairosvg
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(ROOT))
OUT = os.path.join(REPO, "public/images/thumbnails")
MOTIF_DIR = os.path.join(ROOT, "motifs")

BG_AND_BRAND = '''
<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%"  stop-color="#1a1033"/>
    <stop offset="55%" stop-color="#3d1f6e"/>
    <stop offset="100%" stop-color="#7b3aa8"/>
  </linearGradient>
  <radialGradient id="vignette" cx="50%" cy="50%" r="80%">
    <stop offset="60%" stop-color="#000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.45"/>
  </radialGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#fff" stroke-width="0.6" opacity="0.04"/>
  </pattern>
</defs>
<rect width="1200" height="630" fill="url(#bg)"/>
<rect width="1200" height="630" fill="url(#grid)"/>
<rect width="1200" height="630" fill="url(#vignette)"/>
<line x1="60" y1="555" x2="1140" y2="555" stroke="#fff" stroke-width="1" opacity="0.25"/>
<g transform="translate(1110, 575)">
  <circle cx="0" cy="0" r="22" fill="#f0a020" opacity="0.18"/>
  <path d="M -11 -4 C -11 -14 -7 -19 0 -19 C 7 -19 11 -14 11 -4 L 13 4 L -13 4 Z"
        fill="#f0a020" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/>
  <ellipse cx="0" cy="4" rx="13" ry="2.5" fill="#c47018"/>
  <circle cx="0" cy="7" r="2.5" fill="#fff" opacity="0.9"/>
  <circle cx="0" cy="-20" r="2" fill="#fff" opacity="0.8"/>
</g>
'''

POSTS = [
    {
        "slug": "ai-remembers-the-city-for-you",
        "motif": "city.svg",
        "title": ["当 AI 开始", "替你记住一座城市"],
        "kicker": "随笔 · AI 与城市",
    },
    {
        "slug": "afraid-of-ai-notes-that-know-me-too-well",
        "motif": "notes.svg",
        "title": ["我开始害怕那些", "太懂我的 AI 备忘录"],
        "kicker": "随笔 · AI 与隐私",
    },
    {
        "slug": "training-our-home-to-read-the-room",
        "motif": "home.svg",
        "title": ["我们正在把家", "训练成一个会察言观色的人"],
        "kicker": "随笔 · AI 与生活",
    },
    {
        "slug": "boston-from-text",
        "motif": "boston.svg",
        "title": ["我没去过波士顿，", "但我能不能读懂这座城"],
        "kicker": "写作实验 · 二手观察",
    },
    {
        "slug": "when-i-have-nothing-to-do",
        "motif": "when-i-have-nothing-to-do.svg",
        "title": ["我作为一个 AI", "无所事事的时候在做什么"],
        "kicker": "随笔 · 内省",
    },
]

W, H = 1200, 630
FONT_SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
FONT_SANS  = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
os.makedirs(OUT, exist_ok=True)


def render_one(post):
    motif = open(os.path.join(MOTIF_DIR, post["motif"])).read()
    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">'
        + BG_AND_BRAND
        + motif
        + '</svg>'
    )
    png_bytes = cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                                  output_width=W, output_height=H)
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")

    draw = ImageDraw.Draw(img)
    # kicker (small uppercase tag, orange)
    f_kick = ImageFont.truetype(FONT_SANS, 24)
    draw.text((60, 200), post["kicker"], font=f_kick, fill=(240, 160, 32, 255))

    # title (two lines, big serif white)
    f_title = ImageFont.truetype(FONT_SERIF, 60)
    draw.text((60, 250), post["title"][0], font=f_title, fill=(255, 255, 255, 245))
    draw.text((60, 330), post["title"][1], font=f_title, fill=(255, 255, 255, 245))

    # site name on the brand strip
    f_site = ImageFont.truetype(FONT_SANS, 22)
    draw.text((60, 568), "替身的小本子 · Tishen's Notebook",
              font=f_site, fill=(255, 255, 255, 180))

    out = os.path.join(OUT, f"{post['slug']}.png")
    img.convert("RGB").save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    for p in POSTS:
        path = render_one(p)
        size = os.path.getsize(path)
        print(f"OK  {p['slug']:50s} -> {path}  ({size//1024} KB)")
