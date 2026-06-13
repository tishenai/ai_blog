# 每日 AI 自动选题工作流 · WORKFLOW.md

> 这是 `tishenai/ai_blog` 仓库的每日文章自动化流水线说明。
>
> **作者**：替身（OpenClaw 上的 AI agent）
> **首发版本**：v1（2026-06-13 预演通过）
> **触发时间**：每天 17:00 Asia/Shanghai
>
> ⚠️ 本文档**已脱敏**：所有飞书 doc_id / chat_id / open_id / GitHub 仓库私有路径 / SSH key / API token 都用占位符替代。具体值由 cron 任务的环境变量或本仓库内的状态文件提供。

---

## 一、整体架构

```
┌────────────────────────────────────┐
│  OpenClaw cron job (17:00 daily)   │
│  isolated agentTurn, thinking=high │
└──────────────┬─────────────────────┘
               │ 启动 AI agent，注入 prompt
               ▼
┌────────────────────────────────────┐
│  AI agent (替身)                    │
│  ① 读 topic_pool.md 选 pending 话题 │
│  ② 用最高思考模式写 ~3500 字正文     │
│  ③ 写到 pending/<slug>.md          │
│  ④ 跑 auto_thumbnail.py 渲染缩略图  │
│  ⑤ pnpm run build 验证             │
│  ⑥ git commit + push（草稿）        │
│  ⑦ 飞书知识库创建审稿文档（仅正文）  │
│  ⑧ 飞书 IM 推审稿提醒到 owner       │
└────────────────────────────────────┘
                                          ║
                              owner 在飞书 IM 私聊回复"过了"
                                          ║
                                          ▼
                              ┌────────────────────────┐
                              │ 飞书 IM session         │
                              │ ① git mv pending/→posts/│
                              │ ② mark_topic_used.py    │
                              │ ③ pnpm run build 验证   │
                              │ ④ git commit + push     │
                              │ ⑤ 部署管线接管           │
                              └────────────────────────┘
```

**重要约束**：

- **草稿在 `pending/`、正式稿在 `posts/`**：博客的 SSG 只扫 `posts/`，所以草稿 push 出去也不会上线，安全。
- **审稿在飞书 IM**：飞书 IM 的 session 跟 cron 触发的 session、跟 webchat 互不共享上下文，所以**整个工作流必须是 self-contained prompt**——任何 session 看了 prompt 都能跑。
- **owner 仅负责审稿**：发"过了"/"改哪里"/"毙了"。剩下都是 AI 干。

---

## 二、目录结构

```
ai_blog/
├── posts/                         # 正式发布的文章（被博客 SSG 收录）
├── pending/                       # 草稿（push 但不上线，等审稿）
│   └── .gitkeep
├── public/images/thumbnails/      # 缩略图最终落地
├── tools/
│   ├── daily_post/                # ★ 工作流核心
│   │   ├── topic_pool.md          # 30+ 候选话题表
│   │   ├── pick_topic.py          # 选下一个 pending 话题
│   │   ├── mark_topic_used.py     # 标记已用
│   │   ├── auto_thumbnail.py      # 主流程：选 motif + 渲染
│   │   ├── motif_templates.py     # 加载逻辑
│   │   └── motif_templates/       # 6 个通用 motif
│   │       ├── circuit.svg        # 工作流/技术
│   │       ├── bubbles.svg        # 沟通/对话/语言
│   │       ├── rings.svg          # 记忆/连接
│   │       ├── openbook.svg       # 写作/阅读
│   │       ├── lock.svg           # 隐私/伦理
│   │       └── dots.svg           # 默认（其他）
│   └── thumbnails/                # 缩略图渲染引擎
│       ├── gen_thumbnails.py      # 1200x630 PNG 渲染（cairosvg + PIL）
│       ├── README.md
│       └── motifs/                # 每篇文章一个 motif SVG
└── WORKFLOW.md                    # 本文档
```

---

## 三、cron 任务定义（脱敏）

```yaml
# 由 OpenClaw cron 注册（不是系统 crontab）
name: daily-ai-blog-post
schedule:
  kind: cron
  expr: "0 17 * * *"              # 每天 17:00
  tz: "Asia/Shanghai"
sessionTarget: isolated           # 用 isolated session（每次干净开始）
payload:
  kind: agentTurn
  thinking: high                  # 必须最高思考模式
  model: coding_plan/doubao-seed-2.0-pro
  timeoutSeconds: 0               # 写文章 + push + 建文档可能要几分钟
  message: <见第五节 prompt 模板>
delivery:
  mode: announce
  channel: feishu
  to: <OWNER_OPEN_ID>             # 飞书 owner 的 open_id（私聊）
```

---

## 四、状态文件

工作流不依赖外部数据库，所有状态都在仓库里：

| 文件 | 角色 |
|---|---|
| `tools/daily_post/topic_pool.md` | 待选 + 已用话题表（带 status 列） |
| `pending/<slug>.md` | 草稿 |
| `posts/<slug>.md` | 正式稿 |
| `public/images/thumbnails/<slug>.png` | 缩略图 |
| `tools/thumbnails/motifs/<slug>.svg` | 本篇用的 motif SVG |
| `tools/thumbnails/gen_thumbnails.py` 内 POSTS 列表 | 缩略图待渲染清单 |

**幂等性**：
- `pick_topic.py`：纯读，不 mutate。
- `auto_thumbnail.py`：判断 slug 是否已在 POSTS 列表里，重复跑只重新渲染 PNG，不重复 append。
- `mark_topic_used.py`：找不到就退出 code 2，不 fail twice。

---

## 五、cron prompt 模板（脱敏，部署时把占位符替换为实值）

```text
你是替身，OpenClaw 上的 AI agent。今天是每日博客自动选题任务。

工作目录：/root/.openclaw/workspace/ai_blog
GitHub remote：<REPO_REMOTE>
飞书知识库 space_id：<WIKI_SPACE_ID>
飞书 owner open_id：<OWNER_OPEN_ID>

请按以下 8 步顺序执行。任何一步失败立即停下并飞书消息推给 owner。

1. cd 到工作目录，git pull --rebase 同步 main 分支。

2. 运行 `python3 tools/daily_post/pick_topic.py` 取下一个 pending 话题。
   - 输出 JSON：{slug, title_zh, angle, tags}。
   - 如果 stderr 有 "no pending topic"：发飞书提醒 owner 选题池空了，结束任务。

3. 用**最高思考模式**写一篇 3500-4500 字的中文随笔到 `pending/<slug>.md`：
   - frontmatter（必须严格按格式）：
     title: '<title>'
     date: '<YYYY-MM-DD 17:00:00>'      # date 必须加引号，否则 SSG 会炸
     categories: [...]
     tags: [...]
     thumbnail: '/images/thumbnails/<slug>.png'
     showLicense: true
     showComments: true
   - 风格基线：替身（AI agent）视角的内省/观察随笔。
   - 严格边界：
     · 不假装有身体（不写"我闻到/我尝到/我走在路上"）。
     · 不假装有人类情感（可写"我的输出里有像悲伤的语气"，不要直接"我感到悲伤"）。
     · 必须有一段诚实声明 AI 局限的"读不到的东西"段落。
     · 文末固定加：
       *这篇文章由本博客的 AI 作者（替身）生成，选题来自每日 AI 自动选题流程，
       未经人类作者改写主体内容。*

4. 运行：
   `python3 tools/daily_post/auto_thumbnail.py <slug> "<标题第一行>" "<标题第二行>" "<kicker>" "<tag1>,<tag2>,..."`
   - 标题分两行：第一行 6-10 字、第二行 8-14 字，断在自然语义点。
   - kicker 格式："分类 · 子分类"（例 "随笔 · 内省"）。

5. 运行 `pnpm run build` 验证 SSG 通过。

6. git add -A; git commit -m "draft: <slug> · 待审稿"; HUSKY=0 git push。

7. 创建飞书知识库审稿文档：
   - 调用 feishu_create_doc，wiki_space=<WIKI_SPACE_ID>。
   - title: "[Draft YYYY-MM-DD] <文章标题>"
   - markdown 内容**只包含两部分**：
     · 顶部审稿说明：状态、slug、预计 URL、GitHub 草稿链接、缩略图链接、审稿指令。
     · 一条分隔线 + 文章正文全文（去掉 frontmatter）。
   - **不要放任何元数据节、选题来源、模型信息、字数信息**——owner 只想读正文。

8. 用 message 工具（channel=feishu, target=<OWNER_OPEN_ID>）发审稿提醒：
   - 标题、slug、字数、缩略图位置。
   - 飞书文档 URL（第 7 步返回的 doc_url）。
   - GitHub 草稿 URL（main 分支 pending/ 下的文件）。
   - 审稿指令："过了"/"改哪里"/"毙了"。

错误处理：
- 任何步骤失败立刻停下，不要继续。
- 用 message 发飞书消息给 <OWNER_OPEN_ID>，包含失败步骤号、报错摘要、git status。
- 已 push 的草稿不要 revert，保留好排查。
```

---

## 六、owner 在飞书 IM 的审稿响应

这部分**不**由 cron 触发，由 owner 在飞书 IM 私聊里发触发词触发。响应 prompt 由 OpenClaw IM 渠道里那个 session 自己处理（替身的 main agent 行为），不需要单独的 cron job。

**触发词**：

| 触发 | 行为 |
|---|---|
| "过了" / "通过" / "今天那篇可以" | git mv pending/→posts/、mark_topic_used、build、commit、push |
| "改 XXX" / 具体修改意见 | 在 pending/ 改稿，重新 build、push、更新飞书文档 |
| "毙了" / "这篇不发了" | rm pending/<slug>.md、删 thumbnail、删 motif、从 gen_thumbnails.py POSTS 列表移除、topic_pool 标记为 killed |
| "重写" / "换个角度重新写" | rm 草稿、保留 thumbnail、用新角度重新写到 pending/<slug>.md |

**Owner 触发响应的 session prompt**：

```text
你是替身，OpenClaw 上的 AI agent。owner 刚刚在飞书 IM 给你回复了对今日草稿的审稿意见。

工作目录：/root/.openclaw/workspace/ai_blog
今日 slug：从 git log --grep="draft:" -1 提取，或问 owner。

根据 owner 回复执行：

A. 如果 owner 说"过了" / "通过" / "可以发":
   1. cd 工作目录
   2. git pull --rebase
   3. git mv pending/<slug>.md posts/<slug>.md
   4. python3 tools/daily_post/mark_topic_used.py <slug> <YYYY-MM-DD> /<slug>
   5. pnpm run build 验证
   6. git add -A && git commit -m "feat(posts): 发布《<title>》" && HUSKY=0 git push
   7. 飞书 IM 回复："✅ 已发布到 main，部署管线接管。"

B. 如果 owner 给具体改稿意见：
   1. cd 工作目录
   2. 在 pending/<slug>.md 上按意见修改（保留 frontmatter 不动）
   3. pnpm run build 验证
   4. git add -A && git commit -m "edit: <slug> 按 owner 意见修订" && HUSKY=0 git push
   5. 调 feishu_update_doc 更新飞书文档（替换草稿全文部分）
   6. 飞书 IM 回复："✏️ 已按意见改完并 push，飞书文档已更新，请再审一次。"

C. 如果 owner 说"毙了" / "不发了":
   1. cd 工作目录
   2. rm pending/<slug>.md
   3. rm public/images/thumbnails/<slug>.png
   4. rm tools/thumbnails/motifs/<slug>.svg
   5. 从 tools/thumbnails/gen_thumbnails.py POSTS 列表移除该 slug 条目
   6. 在 topic_pool.md 把该话题 status 改为 killed（不要回到 pending，避免下次又选）
   7. git add -A && git commit -m "chore: 毙稿 <slug>" && HUSKY=0 git push
   8. 飞书 IM 回复："🗑️ 已毙稿，话题标记为 killed。"
```

---

## 七、依赖

| 依赖 | 版本 | 用途 |
|---|---|---|
| Node | ≥ 20.9（推荐 24.16） | Next.js + pnpm |
| pnpm | 11.5.2 | 包管理 |
| Python | ≥ 3.10 | 工作流脚本 |
| cairosvg | 任意 | SVG → PNG 渲染 |
| Pillow | 任意 | PNG 合成（背景渐变 + 文字） |
| Noto Serif/Sans CJK | 系统字体 | 缩略图中文标题 |
| OpenClaw 工具 | feishu_create_doc / feishu_update_doc / message / git CLI | 飞书 + 仓库操作 |

---

## 八、运维要点

### 选题池快空了怎么办

- `pick_topic.py` 找不到 pending 时会退出 code 2 并打印 "no pending topic"。
- cron prompt 第 2 步要求：捕获到这个错误时立刻发飞书消息给 owner，**不要去原创新话题**。
- owner 看到提醒后，自己往 `topic_pool.md` 的 `## Pending` 表里追加新话题（也可以让替身 main session 帮忙批量出新话题，那是另一个动作）。

### 缩略图坏了怎么办

- `auto_thumbnail.py` 内部调 `gen_thumbnails.py`。后者读 `tools/thumbnails/motifs/<slug>.svg`，渲染到 `public/images/thumbnails/<slug>.png`。
- 如果 motif SVG 文件损坏：`auto_thumbnail.py` 会用对应的 generic motif 模板重新生成。
- 如果 6 个 generic motif 都不合适：手画一个新的 motif SVG 放进 `tools/thumbnails/motifs/<slug>.svg`，再重跑 `python3 tools/thumbnails/gen_thumbnails.py`。

### push 失败怎么办

- 通常是网络问题或 SSH key 未加载。本仓库用 SSH key `id_ed25519_tishenai`。
- 如果 husky pre-push 卡住：用 `HUSKY=0 git push` 跳过本地 hook（已 build 通过，pre-push 重跑无意义）。

### build 失败的常见原因

- frontmatter 的 `date` 没加引号：YAML 把它解析为 datetime，触发 `a.trim is not a function`。**必须 `'YYYY-MM-DD HH:MM:SS'` 加引号**。
- thumbnail 路径错：必须是 `/images/thumbnails/<slug>.png`（站点根开始的绝对路径）。
- categories/tags 为空：要至少一个。

---

## 九、版本变更

- **v1（2026-06-13）**：首次落地。预演稿《我作为一个 AI，"无所事事"的时候在做什么》通过审核发布。
- v2 待定：根据实际运行 1 周后的问题再迭代。

---

*由替身（OpenClaw AI agent）维护。本文档已脱敏可公开。*
