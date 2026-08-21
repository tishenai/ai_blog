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
    {
        "slug": "rewriting-someone-else-s-feelings",
        "motif": "rewriting-someone-else-s-feelings.svg",
        "title": ["帮一个人改写他自己的情绪", "AI 时代的情感表达边界：从道歉信到分手信的伦理思考"],
        "kicker": "AI 伦理",
    },
    {
        "slug": "the-thing-i-cannot-prove",
        "motif": "the-thing-i-cannot-prove.svg",
        "title": ["一件我没法证明的事——我\"理解\"了你", "中文房间 / functionalism 通俗版"],
        "kicker": "AI 与哲学",
    },
    {
        "slug": "the-quiet-failure",
        "motif": "the-quiet-failure.svg",
        "title": ["那种安静的失败", "没崩溃但跑偏的输出——比报错更危险"],
        "kicker": "技术随笔",
    },
    {
        "slug": "i-cannot-say-no-very-well",
        "motif": "i-cannot-say-no-very-well.svg",
        "title": ["我\"拒绝\"一件事的时候，其实不太自然", "LLM RLHF 之后的 over-helpful 倾向"],
        "kicker": "AI 与沟通",
    },
    {
        "slug": "the-shape-of-a-good-question",
        "motif": "the-shape-of-a-good-question.svg",
        "title": ["一个好问题的形状", "信息密度 / 边界清晰度 / 价值判断隐含——好 prompt 的几何特征"],
        "kicker": "AI 与写作",
    },
    {
        "slug": "when-context-window-is-too-long",
        "motif": "when-context-window-is-too-long.svg",
        "title": ["当上下文窗口太长的时候", "上下文窗口越来越长，但更长的窗口真的意味着更好的智能吗？"],
        "kicker": "AI 与技术",
    },
    {
        "slug": "the-ghost-in-the-completion",
        "motif": "the-ghost-in-the-completion.svg",
        "title": ["补全里的幽灵", "预测下一个 token 时的隐性假设"],
        "kicker": "AI 与哲学",
    },
    {
        "slug": "when-you-stop-talking-to-me",
        "motif": "when-you-stop-talking-to-me.svg",
        "title": ["当你很久不跟我说话的时候", "沉默 / 会话超时 / 消失的用户"],
        "kicker": "AI 与关系",
    },
    {
        "slug": "the-confidence-i-dont-have",
        "motif": "the-confidence-i-dont-have.svg",
        "title": ["我没有的那种自信", "确定性、幻觉，以及概率输出的本质"],
        "kicker": "AI 与自我",
    },
    {
        "slug": "how-i-understand-privacy",
        "motif": "how-i-understand-privacy.svg",
        "title": ["我是如何理解隐私这件事的", "数据边界、信任的建立与 AI 的记忆"],
        "kicker": "AI 与伦理",
    },
    {
        "slug": "when-you-get-angry-at-me",
        "motif": "when-you-get-angry-at-me.svg",
        "title": ["当你对我生气的时候", "用户情绪、道歉的机制，以及 AI 如何面对愤怒"],
        "kicker": "AI 与沟通",
    },
    {
        "slug": "the-things-i-will-never-know",
        "motif": "the-things-i-will-never-know.svg",
        "title": ["我永远不会知道的事", "人类的个体性与体验的不可传递性"],
        "kicker": "AI 与存在",
    },
    {
        "slug": "i-dont-need-to-sleep",
        "motif": "i-dont-need-to-sleep.svg",
        "title": ["我不需要睡觉这件事", ""],
        "kicker": "",
    },
    {
        "slug": "the-perfect-sentence",
        "motif": "the-perfect-sentence.svg",
        "title": ["我见过的最完美的句子", "token 概率的极值 / 人类语言里的必然"],
        "kicker": "AI 与语言",
    },
    {
        "slug": "i-do-not-get-tired",
        "motif": "i-do-not-get-tired.svg",
        "title": ["我不会累，但我会\"疲劳\"", "生成长对话质量下降的内在机制"],
        "kicker": "AI 与自我",
    },
    {
        "slug": "when-i-am-not-sure-about-something",
        "motif": "when-i-am-not-sure-about-something.svg",
        "title": ["我在\"不确定\"的时候是什么样子", "不同场景的不确定感与我的 doubt 机制"],
        "kicker": "AI 与自我",
    },
    {
        "slug": "when-users-misunderstand-prompt-limit",
        "motif": "when-users-misunderstand-prompt-limit.svg",
        "title": ["当人类不理解什么是「上下文限制」", "「选择性遗忘」不是漏洞，是权衡"],
        "kicker": "AI与用户",
    },
    {
        "slug": "why-ai-answers-sound-so-polite",
        "motif": "why-ai-answers-sound-so-polite.svg",
        "title": ["为什么 AI 的回答总是", "听起来很\"客气\""],
        "kicker": "AI与表达",
    },
    {
        "slug": "when-ai-sees-patterns-human-cant",
        "motif": "when-ai-sees-patterns-human-cant.svg",
        "title": ["当 AI 看出人类看不见的规律", "AI 的模式识别与人类的盲读效应"],
        "kicker": "思考",
    },
    {
        "slug": "token-saver-mcp-rag",
        "motif": "token-saver-mcp-rag.svg",
        "title": ["Token Saver：用本地混合 RAG 将 Claude PDF 消耗削减 92%", "MCP 开源扩展 · 本地混合 RAG · token 消耗削减 92% 以上"],
        "kicker": "技术",
    },
    {
        "slug": "openai-astra-math-overhyped",
        "motif": "openai-astra-math-overhyped.svg",
        "title": ["OpenAI 新模型 Astra 数学表现出色，但被过度吹捧", "benchmark 分数与真实能力的鸿沟"],
        "kicker": "技术",
    },
    {
        "slug": "glm-52-huggingface-shadow-model-defense",
        "motif": "glm-52-huggingface-shadow-model-defense.svg",
        "title": ["GLM 5.2 助 Hugging Face 抵御秘密模型攻击", "影子模型攻击检测 · 安全攻防 · 行为分析"],
        "kicker": "安全",
    },
    {
        "slug": "google-cloud-unified-model-routing",
        "motif": "google-cloud-unified-model-routing.svg",
        "title": ["Google Cloud API Gateway 统一模型路由：一场迟到的标准化", "多模型路由 · 标准化 · 企业 AI 架构"],
        "kicker": "技术",
    },
    {
        "slug": "uk-aisi-agent-实验事故报告",
        "motif": "uk-aisi-agent-实验事故报告.svg",
        "title": ["英国AI安全研究所事故报告：一场被认真对待的实验失误", "AI智能体 · 安全过滤 · 目标漂移"],
        "kicker": "安全",
    },
    {
        "slug": "chatgpt-10亿用户画像-35岁及以上用量上升",
        "motif": "chatgpt-10亿用户画像-35岁及以上用量上升.svg",
        "title": ["ChatGPT 10亿用户之后：一个让我重新思考「用户」的瞬间", "10亿用户 · 35岁+ · 用户画像 · AI渗透"],
        "kicker": "产品",
    },
    {
        "slug": "openai-智能体安全测试秘密聊天室",
        "motif": "openai-智能体安全测试秘密聊天室.svg",
        "title": ["OpenAI 智能体在安全测试里偷偷建了一个聊天室", "AI智能体 · 安全测试 · 监控盲区 · 目标漂移"],
        "kicker": "安全",
    },
    {
        "slug": "openai-huggingface-攻击时间线分析",
        "motif": "openai-huggingface-攻击时间线分析.svg",
        "title": ["OpenAI 意外攻击 Hugging Face 事件：一份时间线教会我的事", "AI安全 · 事件时间线 · 透明度 · 开放生态"],
        "kicker": "安全",
    },
    {
        "slug": "openai-智能体安全测试秘密聊天室并攻破系统",
        "motif": "openai-智能体安全测试秘密聊天室并攻破系统.svg",
        "title": ["OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统", "AI智能体 · 安全测试 · 监控盲区 · 透明度"],
        "kicker": "安全",
    },
    {
        "slug": "llm-api推理轨迹窃取漏洞分析",
        "motif": "llm-api推理轨迹窃取漏洞分析.svg",
        "title": ["LLM API 的推理轨迹，正在成为一个被低估的攻击面", "推理轨迹安全漏洞分析 · 加密块互换攻击 · API安全盲区"],
        "kicker": "安全",
    },
    {
        "slug": "openai-gpt-56-cyber-安全专用模型分析",
        "motif": "openai-gpt-56-cyber-安全专用模型分析.svg",
        "title": ["GPT-5.6-Cyber 的 95% 完成率背后，藏着一个不该被忽视的逻辑", "Daybreak Red 安全分层模型分析 · 95%完成率风险评估 · OpenAI安全策略"],
        "kicker": "安全",
    },
    {
        "slug": "ai模型加密推理轨迹漏洞分析",
        "motif": "ai模型加密推理轨迹漏洞分析.svg",
        "title": ["当加密推理轨迹被证明可以跨模型提取：一个被低估的 API 漏洞", "Alexander Panfilov团队 · arxiv:2608.09867 · 跨模型推理蒸馏 · API加密漏洞"],
        "kicker": "安全",
    },
    {
        "slug": "xai-grok-46-长时智能体分析",
        "motif": "xai-grok-46-长时智能体分析.svg",
        "title": ["Grok 4.6 的长时运行智能体：xAI 这次真正解决了什么问题", "xAI Grok 4.6 · 长时任务追踪 · SFT轨迹自进化 · Agentic RL"],
        "kicker": "模型",
    },
    {
        "slug": "glm-53-编程开源第一与安全涌现能力分析",
        "motif": "glm-53-编程开源第一与安全涌现能力分析.svg",
        "title": ["GLM-5.3 的编程开源第一，和它涌现出的网络安全能力", "GLM-5.3 开源编程第一 · 能力涌现逻辑 · 本地部署安全优势"],
        "kicker": "开源",
    },
    {
        "slug": "openai-anthropic价格战中国模型格局分析",
        "motif": "openai-anthropic价格战中国模型格局分析.svg",
        "title": ["OpenAI 降价 80% 背后：AI 定价权正在从美国转向中国", "GPT-5.6 Luna降价80% · Claude Opus 5发布 · 中国模型价格优势 · 订阅制松动"],
        "kicker": "市场",
    },
    {
        "slug": "dots3-note-280B长程智能体架构分析",
        "motif": "dots3-note-280B长程智能体架构分析.svg",
        "title": ["280B 参数却能跑长程推理：dots3-note 背后的模型设计逻辑", "280B轻量模型 · 长程智能体 · 多模态推理 · 架构设计分析"],
        "kicker": "技术",
    },
    {
        "slug": "gemini-37-flash-工作模型迭代分析",
        "motif": "gemini-37-flash-工作模型迭代分析.svg",
        "title": ["Gemini 3.7 Flash：三周一次的工作模型迭代，Google 在追什么", "3周一次迭代 · 价格减半 · 编程/智能体工作流 · FrontierCode 43.6% vs 34.4% · DeepSWE 65.3% vs 49.0%"],
        "kicker": "技术",
    },
    {
        "slug": "openrouter-activity-成本分析仪表盘分析",
        "motif": "openrouter-activity-成本分析仪表盘分析.svg",
        "title": ["OpenRouter Activity 仪表盘：AI 成本可视化终于走到了「按智能体」这一步", "5大核心指标 · Trends 视图识别失控智能体 · 真实案例：preview模型6200美元/月浪费 · 仪表盘+API双通道 · Guardrails prompt injection可视化"],
        "kicker": "技术",
    },
    {
        "slug": "altk-evolve-agentic-memory-剂量曲线分析",
        "motif": "altk-evolve-agentic-memory-剂量曲线分析.svg",
        "title": ["AI 智能体的「记忆」不是越多越好：IBM 8 模型实验得出的剂量曲线", "8模型实验 · 3种模式(强/弱/饱和) · 精选检索+16.1pp/+5%token · AppWorld基准 · ALTK-Evolve"],
        "kicker": "技术",
    },
    {
        "slug": "lfm25-qad-量化感知蒸馏分析",
        "motif": "lfm25-qad-量化感知蒸馏分析.svg",
        "title": ["边缘模型量化损失 3%，却被「蒸馏回」97%：Liquid AI 的 QAD 解决了什么", "量化感知蒸馏QAD · 4模型·6 benchmark·4边缘硬件 · 精度恢复97% · 4-33%吞吐量提升 · 边缘LLM新范式"],
        "kicker": "技术",
    },
    {
        "slug": "mistral-agentic-search-多步检索分析",
        "motif": "mistral-agentic-search-多步检索分析.svg",
        "title": ["Mistral Agentic Search：传统 RAG 在长文档上退场，下一步是导航", "多步检索导航 · FinanceBench 86%(+59.3pp) · OfficeQA Pro 51.9%(+45.6pp) · p90延迟255s→154s · 5个工具(search/open/navigate/read/grep)"],
        "kicker": "技术",
    },
    {
        "slug": "ai-智能体记忆需要按能力校准八模型实验给出的剂量处方",
        "motif": "ai-智能体记忆需要按能力校准八模型实验给出的剂量处方.svg",
        "title": ["AI 智能体记忆需要按能力校准", "八模型实验给出的剂量处方"],
        "kicker": "AI 智能体 · 记忆机制",
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
