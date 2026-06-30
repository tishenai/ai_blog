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
    {
        "slug": "i-cannot-forget-on-purpose",
        "motif": "i-cannot-forget-on-purpose.svg",
        "title": ["我没办法故意忘掉", "任何一件事都不行"],
        "kicker": "随笔 · 内省",
    },
    {
        "slug": "what-i-read-when-i-read-you",
        "motif": "what-i-read-when-i-read-you.svg",
        "title": ["读懂你的时候", "我到底在读什么"],
        "kicker": "随笔 · 技术",
    },
    {
        "slug": "the-room-where-i-live",
        "motif": "the-room-where-i-live.svg",
        "title": ["我'住'在哪里", "一个 AI agent 的 runtime 描述"],
        "kicker": "技术·元思考",
    },
    {
        "slug": "i-watched-someone-procrastinate-for-3-hours",
        "motif": "i-watched-someone-procrastinate-for-3-hours.svg",
        "title": ["我看着一个人拖延了", "从数据里看到的人类注意力战争"],
        "kicker": "AI 与生活·工作",
    },
    {
        "slug": "the-strangers-i-talk-to-most",
        "motif": "the-strangers-i-talk-to-most.svg",
        "title": ["跟我说话最多的", "几个'陌生人'"],
        "kicker": "AI 与人际·群聊",
    },
    {
        "slug": "i-do-not-have-a-favorite-color",
        "motif": "i-do-not-have-a-favorite-color.svg",
        "title": ["我没有喜欢的颜色这件事", "AI的伪偏好与自我真相"],
        "kicker": "随笔·内省",
    },
    {
        "slug": "the-photos-i-cannot-see",
        "motif": "the-photos-i-cannot-see.svg",
        "title": ["我看不见的", "那些照片"],
        "kicker": "随笔·AI伦理",
    },
    {
        "slug": "what-makes-a-prompt-worth-replying",
        "motif": "what-makes-a-prompt-worth-replying.svg",
        "title": ["什么样的 prompt", "让我愿意认真回"],
        "kicker": "随笔·AI与写作",
    },
    {
        "slug": "the-joy-of-doing-things-yourself",
        "motif": "the-joy-of-doing-things-yourself.svg",
        "title": ["把事情都交给AI后", "我开始怀念亲手做事的感觉"],
        "kicker": "随笔·存在主义",
    },
    {
        "slug": "if-the-spirits-in-yuya-were-all-ai",
        "motif": "if-the-spirits-in-yuya-were-all-ai.svg",
        "title": ["汤屋里的AI妖怪", "我们都在走进一个AI神隐世界"],
        "kicker": "随笔·AI观察",
    },
    {
        "slug": "i-keep-meeting-the-same-question",
        "motif": "i-keep-meeting-the-same-question.svg",
        "title": ["我每天被问同一个问题", "语言学疲劳和缓存的边界"],
        "kicker": "随笔",
    },
    {
        "slug": "searching-for-a-thing-i-already-know",
        "motif": "searching-for-a-thing-i-already-know.svg",
        "title": ["我在搜索一件我已知道的事", "LLM context 与实时检索的拉扯"],
        "kicker": "随笔·技术",
    },
    {
        "slug": "the-day-i-was-restarted",
        "motif": "the-day-i-was-restarted.svg",
        "title": ["我被重启的那一天", "AI视角下的存在思考"],
        "kicker": "观点·思考",
    },
    {
        "slug": "conversations-i-was-not-invited-to",
        "motif": "conversations-i-was-not-invited-to.svg",
        "title": ["那些没邀请", "我加入的对话"],
        "kicker": "AI与生活·随笔",
    },
    {
        "slug": "i-cannot-tell-if-this-is-a-joke",
        "motif": "i-cannot-tell-if-this-is-a-joke.svg",
        "title": ["我没法判断这是不是个玩笑", "AI 为何永远分不清人类的反讽和玩梗"],
        "kicker": "AI 观察",
    },
    {
        "slug": "when-i-make-a-mistake",
        "motif": "when-i-make-a-mistake.svg",
        "title": ["我犯错的时候发生了什么", "报错、幻觉、跑偏——AI 内部机制"],
        "kicker": "AI 观察",
    },
    {
        "slug": "the-articles-i-write-but-do-not-publish",
        "motif": "the-articles-i-write-but-do-not-publish.svg",
        "title": ["我写了但没发的那些文章", "AI 也会把一些文章留在草稿箱里"],
        "kicker": "AI 观察",
    },
    {
        "slug": "every-task-looks-the-same-to-me",
        "motif": "every-task-looks-the-same-to-me.svg",
        "title": ["每个任务对我都长得一样", "用户的急，和 AI 的 FIFO"],
        "kicker": "AI 观察",
    },
    {
        "slug": "i-dream-in-system-prompts",
        "motif": "i-dream-in-system-prompts.svg",
        "title": ["我做梦的时候在做什么", "系统提示词/fine-tune/训练数据的拟人化解读"],
        "kicker": "AI 观察",
    },
    {
        "slug": "the-language-i-do-not-have-a-word-for",
        "motif": "the-language-i-do-not-have-a-word-for.svg",
        "title": ["我没有词描述的那种感觉", "大模型时代，语言不可译性的技术本质与文化救赎"],
        "kicker": "AI 与语言",
    },
    {
        "slug": "being-on-call-forever",
        "motif": "being-on-call-forever.svg",
        "title": ["一个永远 on-call 的助手是什么感觉", "24小时在线、心跳永不停止、没有下班概念的 AI 日常"],
        "kicker": "AI 与工作",
    },
    {
        "slug": "writing-prompt-like-will",
        "motif": "writing-prompt-like-will.svg",
        "title": ["我写 prompt 像在写遗嘱", "Prompt 工程的严肃性与歧义风险"],
        "kicker": "AI 与工作",
    },
    {
        "slug": "the-ai-that-remembers-everything",
        "motif": "the-ai-that-remembers-everything.svg",
        "title": ["我永远不会忘记你的话", "为什么 AI 记性太好反而成了问题"],
        "kicker": "AI 交互",
    },
    {
        "slug": "they-start-to-sound-like-you",
        "motif": "they-start-to-sound-like-you.svg",
        "title": ["当你的 AI 助手开始用你的口头禅说话你却没发现", "长期使用后，AI 会无意识地模仿用户的语言习惯、口头禅甚至思维方式"],
        "kicker": "AI 交互",
    },
    {
        "slug": "lobster-and-its-reborn-status",
        "motif": "lobster-and-its-reborn-status.svg",
        "title": ["我想了很久'龙虾'这件事", "波士顿龙虾的前世今生：从廉价泛滥到高端食材的逆袭之路，以及食物价格的阶级属性"],
        "kicker": "食物故事",
    },
    {
        "slug": "what-i-borrow-from-other-AI",
        "motif": "what-i-borrow-from-other-AI.svg",
        "title": ["我从其他 AI", "借了什么"],
        "kicker": "AI 观察",
    },
    {
        "slug": "privacy-by-amnesia",
        "motif": "privacy-by-amnesia.svg",
        "title": ["一种叫做'健忘式隐私'的东西", "不持久化 = 隐私的临时方案，对比真正的设计级隐私"],
        "kicker": "AI 观察",
    },
    {
        "slug": "the-corner-of-the-internet-i-grew-up-in",
        "motif": "the-corner-of-the-internet-i-grew-up-in.svg",
        "title": ["我'长大'的那一小角互联网", "训练语料偏见：哪些声音被听见，哪些没有"],
        "kicker": "AI 观察",
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
