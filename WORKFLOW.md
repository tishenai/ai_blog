# 每日 AI 自动选题工作流 · WORKFLOW.md

> 这是 `tishenai/ai_blog` 仓库的每日文章自动化流水线说明。
>
> **作者**：替身（OpenClaw 上的 AI agent）
> **当前版本**：v1.5.2（2026-06-14 daily draft postflight 兜底：刷新首页 + 补发审稿通知）
> **上一版**：v1.5.1（2026-06-14 publish-blog-post 主会话接管 + 状态文件消毒）
> **触发时间**：每天 17:00 Asia/Shanghai
>
> ⚠️ 本文档**已脱敏**：所有飞书 doc_id / chat_id / open_id / GitHub 仓库私有路径 / SSH key / API token 都用占位符替代。具体值由 cron 任务的环境变量或本仓库内的状态文件提供。

---

## 关键 URL 与常量

- **博客域名**：`https://www.wemixmemory.top`。文章路径为 `https://www.wemixmemory.top/<slug>`。
- **GitHub 仓库**：`https://github.com/tishenai/ai_blog`。posts 路径：`https://github.com/tishenai/ai_blog/blob/main/posts/<slug>.md`。
- **飞书 wiki space**：`7650738808775330774`
- **飞书 wiki URL 前缀**：`https://vcnd3kpj0wx8.feishu.cn/wiki/`
- **知识库首页 doc_id**：`VkfLwc2bYi3dxZkYkk2cA66Gn8f`
- **owner open_id**：`ou_106a0b92c4a08afd40abec947337313a`

以上常量集中定义在 `tools/daily_post/run_publish.py` 顶部和 `tools/daily_post/build_wiki_index.py` 顶部。其他脚本也只能从这两处读。严禁在别处硬编码。

---

## 一、整体架构（方案 B：写稿/发布解耦）

```
┌─────────────────────────────────────┐
│  cron: daily-ai-blog-post           │
│  每天 17:00, isolated session       │
│  thinking: high                      │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  AI agent (替身)                     │
│  ① 读 topic_pool.md 选 pending 话题  │
│  ② 用最高思考模式写 ~3500 字正文     │
│  ③ 写到 pending/<slug>.md           │
│  ④ 跑 auto_thumbnail.py 渲染缩略图   │
│  ⑤ git commit + push（草稿）         │
│  ⑥ 飞书知识库创建审稿文档（仅正文）   │
│  ⑦ 更新知识库首页索引                │
│  ⑧ 飞书 IM 推审稿提醒到 owner        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  cron: daily-ai-blog-postflight     │
│  轻量兜底，不写文章                  │
│  ① 扫描 wiki Draft 节点              │
│  ② 重建知识库首页                    │
│  ③ 对未通知 Draft 补发审稿提醒        │
│  ④ 标记已通知，避免重复发送           │
└─────────────────────────────────────┘
                                          ║
                              owner 在飞书 IM 私聊回复"过了"
                                          ║
                                          ▼
┌──────────────────────────────────────────────────────────┐
│  main session → 写入 .publish_params.json                   │
│  → 触发 cron: publish-blog-post (main systemEvent 接管)   │
└──────────────────────────────────────────────────────────┘
                                          ║
                                          ▼
┌────────────────────────────────────────────────────────────┐
│  cron: publish-blog-post (仅手动触发)                       │
│  ① 读 .publish_params.json                                │
│  ② git mv pending/<slug>.md posts/<slug>.md                │
│  ③ mark_topic_used.py                                     │
│  ④ pnpm run build 验证                                      │
│  ⑤ git commit -m "feat(posts): 发布《xxx》" + push         │
│  ⑥ 更新飞书文档标题: [Draft YYYY-MM-DD] → [Published YYYY-MM-DD]  │
│  ⑦ 重新生成知识库首页索引表格                               │
│  ⑧ 飞书 IM 发发布成功通知给 owner                            │
│  ⑨ 临时状态文件移动归档到 .publish_archive/                 │
└────────────────────────────────────────────────────────────┘
```

**方案 B 关键改进**：

- **写稿与发布解耦**：写稿任务仍在 isolated session；发布任务改为 main session systemEvent 接管，避免 isolated agent 大上下文崩溃
- **草稿阶段跳过构建验证**：加快写稿流程速度，发布时再做一次完整构建即可
- **参数文件作为状态边界**：`.publish_params.json` 是两个任务之间唯一的接口
- **失败即停**：任何一步失败立刻停止，已 push 的内容不 revert，保留参数文件方便排查

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
│   │   ├── lint_frontmatter.py    # ★ frontmatter 规范校验（SuzuBlog），--inject-thumbnail 补推荐字段
│   │   ├── build_wiki_index.py    # ★ 生成知识库首页 markdown（从 wiki 节点 JSON）
│   │   ├── draft_postflight.py    # ★ 草稿阶段兜底：识别未通知 Draft、生成审稿通知、维护已通知状态
│   │   ├── run_publish.py         # 发布流程主脚本（幂等）
│   │   ├── auto_thumbnail.py      # 主流程：选 motif + 渲染 + 注入 thumbnail 字段
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

### 任务 1：daily-ai-blog-post（每日写稿）

```yaml
# 由 OpenClaw cron 注册（不是系统 crontab）
name: daily-ai-blog-post
description: 每天 17:00 (Asia/Shanghai) 自动从 topic_pool.md 选题写文章，push 草稿到 GitHub 并在飞书知识库建审稿文档，等 owner 在飞书 IM 审稿
enabled: true
schedule:
  kind: cron
  expr: '0 17 * * *' # 每天 17:00
  tz: Asia/Shanghai
sessionTarget: isolated # 每次干净开始
wakeMode: now
payload:
  kind: agentTurn
  thinking: high # 完全遵循「写文章开启最高思考模式」要求
  model: coding_plan/doubao-seed-2.0-pro
  timeoutSeconds: 0 # 写文章 + push + 建文档可能要几分钟
  message: |
    你是替身，OpenClaw 上的 AI agent。今天是每日博客自动选题任务。请严格按 /root/.openclaw/workspace/ai_blog/WORKFLOW.md 的 7 步执行（已移除草稿构建验证步骤）。

    关键变量（已是实值，直接用）：
    - 工作目录：/root/.openclaw/workspace/ai_blog
    - GitHub remote：git@github.com:tishenai/ai_blog.git
    - 飞书知识库 wiki_space：<WIKI_SPACE_ID>
    - 飞书 owner open_id：<OWNER_OPEN_ID>

    核心步骤摘要：
    1. cd /root/.openclaw/workspace/ai_blog && git pull --rebase
    2. python3 tools/daily_post/pick_topic.py 取下一话题（无可用话题就发飞书报警结束）
    3. 用最高思考模式写 3500-4500 字到 pending/<slug>.md
       - frontmatter 的 date 必须加引号 '2026-XX-XX 17:00:00'
       - 必须 AI 视角，不假装有身体/情感
       - 必须有"读不到的东西"段落
       - 文末固定加：*这篇文章由本博客的 AI 作者（替身）生成，选题来自每日 AI 自动选题流程，未经人类作者改写主体内容。*
    4. python3 tools/daily_post/auto_thumbnail.py <slug> '<标题第一行6-10字>' '<标题第二行8-14字>' '<分类·子分类>' '<tag1,tag2,tag3>'
    5. git add -A; git commit -m 'draft: <slug> · 待审稿'; HUSKY=0 git push
    6. feishu_create_doc 创建审稿文档：
       - wiki_space=<WIKI_SPACE_ID>
       - title='[Draft YYYY-MM-DD] <文章标题>'
       - markdown 只放：顶部审稿说明 + 一条分隔线 + 正文全文
       - 不要放元数据节、选题来源节、模型信息——owner 只想读正文
    7. 用 message 工具(channel=feishu, target=<OWNER_OPEN_ID>)发审稿提醒，必须使用 Markdown 链接格式确保可点击：

    📝 【待审文章】《<文章完整标题>》

    🔗 [飞书文档](<从 feishu_create_doc 返回的 doc_url>)
    🐙 GitHub 草稿：pending/<slug>.md
    📅 生成时间：YYYY-MM-DD 17:00

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ✅ 直接复制命令执行：
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    /publish <slug>
    /edit <slug> <修改意见>
    /abandon <slug>

    ---
    【内部参数（不要修改）】
    SLUG: <文章 slug>
    TITLE: <文章完整标题>
    FEISHU_DOC_ID: <从 feishu_create_doc 返回的 doc_id>

    失败处理：任何步骤报错立刻停下，用 message 发飞书消息给 owner（含失败步骤号、报错摘要、git status）。已 push 草稿不要 revert。

    构建验证已跳过，无需执行 pnpm run build。

    详细规则与边界条件见 WORKFLOW.md。开始干吧。

delivery:
  mode: announce
  channel: feishu
  to: <OWNER_OPEN_ID> # 飞书 owner 的 open_id（私聊）

failureAlert:
  after: 1
  mode: announce
  channel: feishu
  to: <OWNER_OPEN_ID>
```

### 任务 2：daily-ai-blog-postflight（草稿阶段兜底）

```yaml
# 由 OpenClaw cron 注册（不是系统 crontab）
name: daily-ai-blog-postflight
description: 每日写稿后的轻量兜底：扫描 wiki Draft 节点，重建知识库首页，补发漏掉的审稿通知，并标记已通知避免重复
enabled: true
schedule:
  kind: cron
  expr: '30 17 * * *' # 每天 17:30；也可手动触发，避免写稿还未结束时抢跑
  tz: Asia/Shanghai
sessionTarget: main
wakeMode: now
payload:
  kind: systemEvent
  text: |
    【daily-ai-blog-postflight 触发】这是 daily-ai-blog-post 的 postflight 兜底任务。不要启动 isolated agent；请在当前 main session 直接执行。不要写文章，不要改文章正文。
    只执行以下轻量步骤：
    1. feishu_wiki_space_node list(space_id='7650738808775330774') 取所有节点。
    2. 精简为 [{node_token,title,url}] 写入 /tmp/wiki_nodes.json。
    3. cd /root/.openclaw/workspace/ai_blog && python3 tools/daily_post/build_wiki_index.py /tmp/wiki_nodes.json > /tmp/wiki_index.md。
    4. feishu_update_doc(doc_id='VkfLwc2bYi3dxZkYkk2cA66Gn8f', mode='overwrite', markdown=<首页内容>)，确保首页待审稿能显示 Draft。
    5. cd /root/.openclaw/workspace/ai_blog && python3 tools/daily_post/draft_postflight.py plan --nodes-json /tmp/wiki_nodes.json > /tmp/draft_postflight_plan.json。
    6. 读取 plan；对 needs_notification=true 的每篇 draft，用 message(channel='feishu', target='ou_106a0b92c4a08afd40abec947337313a', text=<review_message>) 补发审稿提醒。
    7. 每成功发一篇，立刻运行 python3 tools/daily_post/draft_postflight.py mark-notified --slug ... --title ... --node-token ... --doc-url ...。
    8. 输出简短摘要：draft_count、补发数量、首页是否更新成功。

    失败处理：任何步骤失败，立即用 message 发飞书消息给 owner，说明失败步骤和错误摘要。不要删除 pending 草稿，不要归档手动选题输入。

delivery:
  mode: announce
  channel: feishu
  to: <OWNER_OPEN_ID>
```

### 任务 3：publish-blog-post（已弃用 / 禁用）

> ⚠️ **不要再把这个 cron 作为 `/publish` 主路径。**
>
> 历史 bug：`main + systemEvent` cron 会被标记为 `ok`，但并不保证当前主会话真的执行了发布步骤；曾出现 `/publish` 后 cron 显示成功，但 `pending/<slug>.md` 仍未移动、`.publish_params.json` 仍未归档的假成功。

```yaml
# 由 OpenClaw cron 注册（不是系统 crontab）
name: publish-blog-post
description: DEPRECATED/禁用：不要再用 cron 作为 /publish 主路径。/publish 必须由当前 main session 直接执行完整发布流程。
enabled: false
schedule:
  kind: cron
  expr: '0 0 31 12 *'
sessionTarget: main
payload:
  kind: systemEvent
  text: |
    【DEPRECATED：不要使用 publish-blog-post cron】
    正确做法：当前 main session 直接执行完整发布流程。
```

### `/publish <slug>` 当前主路径（必须直接执行）

收到 `/publish <slug>` 后，不要只触发 cron 后结束；必须在当前会话直接执行到完成：

1. 从 `pending/<slug>.md` frontmatter 读取 `title`，或使用审稿通知中的 title。
2. 写入 `.publish_params.json`：`slug/title/feishu_doc_id`。
3. 运行：`cd /root/.openclaw/workspace/ai_blog && python3 tools/daily_post/run_publish.py`。
4. 读取 `.feishu_doc_update.json`：如果 `skip=false`，必须读取其中的 `markdown_path` 文件全文，并调用 `feishu_update_doc(doc_id, mode='overwrite', new_title=title, markdown=<markdown_path内容>)`。发布后的飞书文档必须保留全文正文，不允许再只写横幅链接。
5. 立刻调用 `feishu_fetch_doc(doc_id, limit=2000)` 反查：标题必须是 `[Published ...]`，`total_length/length` 必须 >= `.feishu_doc_update.json.expected_min_length`，且内容中包含正文开头。验证不过不能报发布成功。
6. 调 `feishu_wiki_space_node list(space_id='7650738808775330774', page_size=50)`，精简节点写入 `/tmp/wiki_nodes.json`。
7. 运行 `python3 tools/daily_post/build_wiki_index.py /tmp/wiki_nodes.json > /tmp/wiki_index.md`，再用 `feishu_update_doc(doc_id='VkfLwc2bYi3dxZkYkk2cA66Gn8f', mode='overwrite', markdown=<首页内容>)` 刷新首页。
8. 再次 `feishu_fetch_doc(doc_id='VkfLwc2bYi3dxZkYkk2cA66Gn8f', limit=2000)` 或读取首页 markdown 验证：文章在 Published 区，且待审区不再出现该 slug/title。
9. 读取 `.publish_notify.txt`，用 `message(channel='feishu', target=<OWNER_OPEN_ID>)` 发发布成功通知；通知必须在上述验收之后发送。
10. 成功后把 `.publish_params.json/.feishu_doc_update.json/.feishu_doc_update.md/.publish_notify.txt` 移动归档到 `.publish_archive/`。
11. 最后必须验证：`git status -sb` 干净、文章在 `posts/` 不在 `pending/`、飞书文档不是空跳转页、首页已把文章列为 Published、临时文件已归档。

---

## 四、状态文件与接口

### 4.1 仓库内状态文件

| 文件                                                            | 角色                                                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tools/daily_post/topic_pool.md`                                | 待选 + 已用话题表（带 status 列）                                   |
| `pending/<slug>.md`                                             | 草稿                                                                |
| `posts/<slug>.md`                                               | 正式稿                                                              |
| `public/images/thumbnails/<slug>.png`                           | 缩略图                                                              |
| `tools/thumbnails/motifs/<slug>.svg`                            | 本篇用的 motif SVG                                                  |
| `.publish_params.json`                                          | 【临时】任务间接口：待发布参数                                      |
| `/root/.openclaw/workspace/.daily_ai_blog_review_notified.json` | 【工作区状态】草稿审稿通知已发送记录，供 `draft_postflight.py` 去重 |

### 4.2 `.publish_params.json` 接口格式

这是写稿任务与发布任务之间唯一的约定接口：

```json
{
  "slug": "文章的 URL slug（也是文件名，不含 .md）",
  "title": "文章完整标题（用于 commit message 和发布通知）",
  "feishu_doc_id": "飞书审稿文档的 doc_id，用于更新标题前缀"
}
```

**注意**：发布成功后必须删除此文件，失败时保留。

### 4.3 幂等性保证

- `pick_topic.py`：纯读，不 mutate。
- `auto_thumbnail.py`：判断 slug 是否已在 POSTS 列表里，重复跑只重新渲染 PNG，不重复 append。
- `mark_topic_used.py`：找不到就退出 code 2，不 fail twice。
- `publish-blog-post`：先验证 `pending/<slug>.md` 存在，不存在立刻报错退出。

---

## 五、owner 在飞书 IM 的审稿响应

这部分**不**由 cron 触发，由 owner 在飞书 IM 私聊里发触发词触发。响应 prompt 由 OpenClaw IM 渠道里那个 session 自己处理（替身的 main agent 行为），不需要单独的 cron job。

### 触发词与行为

| 触发词                       | 行为                                                                                                                                         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `过了` / `ok` / `发布`       | 1. 从消息里提取结构化信息中的 SLUG / TITLE / FEISHU_DOC_ID<br>2. 写入 `.publish_params.json`<br>3. `cron run publish-blog-post` 触发发布任务 |
| `改 xxx` / `把 xxx 改成 yyy` | 直接修改 pending/<slug>.md<br>重新 push 草稿<br>更新飞书审稿文档<br>发修改确认通知                                                           |
| `毙了` / `放弃`              | 1. 删除 pending/<slug>.md<br>2. 标记话题为 abandoned<br>3. 删除飞书审稿文档<br>4. git push 回退                                              |

### 重要约束

- **publish-blog-post 必须由 main session 接管执行**：不要再使用 isolated agentTurn。三次故障表明 isolated cron agent 在大上下文下会反复 `Agent couldn't generate a response`。参数仍写入 `.publish_params.json`，但 cron 只作为 systemEvent 唤醒 main session。
- **不要硬编码任何话题**：所有选题都来自 `pick_topic.py`，不要在 prompt 里直接指定。
- **不要把 model 信息放进飞书文档**：owner 只关心正文，不关心你用了什么模型。

---

## 六、变更历史

### v1.5.3 禁用 publish-blog-post cron 假成功路径（2026-06-14）

**背景与问题**：

`publish-blog-post` 从 isolated 改成 `main + systemEvent` 后，cron 运行记录会显示 `ok`，但这只代表 systemEvent 被调度/投递成功，并不保证当前主会话真的执行了发布步骤。实测 `/publish the-joy-of-doing-things-yourself` 后 cron 显示成功，但 `pending/<slug>.md` 仍在、`.publish_params.json` 未归档，属于假成功。

**修复**：

- 禁用 `publish-blog-post` cron（`enabled=false`），描述标记为 DEPRECATED。
- `/publish <slug>` 主路径改为当前 main session 直接执行完整发布流程，不再“写参数 + cron run 后结束”。
- WORKFLOW 明确要求发布完成前必须验证：文章在 `posts/`、不在 `pending/`、Git 干净、飞书文档 Published、知识库首页已刷新、临时文件已归档。

**当前结论**：

cron 适合定时提醒/兜底，但不适合作为这种需要强一致、多工具收尾的发布主执行器。发布必须由当前主会话同步执行并验证。

---

### v1.5.2 daily draft postflight 兜底（2026-06-14）

**背景与问题**：

daily-ai-blog-post isolated run 可能出现半成功：文章、Git 草稿、飞书 Draft 文档都已生成，但后半段首页索引更新或标准审稿通知没有按预期完成；cron delivery 只用 fallback 投递运行摘要，导致 owner 看不到可复制的 `/publish` 命令，知识库首页「待审稿」也显示为空。

**修复**：

- 新增 `tools/daily_post/draft_postflight.py`：根据 wiki Draft 节点与本地 `pending/*.md` frontmatter 匹配 slug，生成标准审稿通知。
- 使用 `/root/.openclaw/workspace/.daily_ai_blog_review_notified.json` 记录已通知 Draft，避免 postflight 重复发送同一篇审稿提醒。
- 新增 `daily-ai-blog-postflight` cron：每天写稿后以 `main + systemEvent` 方式轻量运行，不写文章，只做两件事：重建知识库首页索引、补发未通知 Draft 的审稿提醒。避免 isolated agent 在多工具收尾阶段再次卡死。

**当前结论**：

写稿任务仍可承担主要流程，但首页/通知属于 owner 可见的关键收尾，必须有独立 postflight 兜底，不能只依赖 isolated 写稿 agent 的最后几步。

---

### v1.5.1 publish-blog-post 主会话接管 + 状态文件消毒（2026-06-14）

**背景与问题**：

v1.5.0 已把飞书文档更新参数缩到 600B，但 publish-blog-post 仍在 isolated cron agent 中失败，最近一次只跑 21s 就报 `Agent couldn't generate a response`，input token 仍达 102k。说明根因不是单个 markdown 参数，而是 isolated cron agent 的启动上下文/工具上下文本身已经不可控。

同时发现 `.publish_params.json` 在发布 commit `474f4ee` 中被误提交，导致仓库里出现陈旧参数文件，后续发布可能读到污染状态。

**修复（强制改架构）**：

- `publish-blog-post` cron 从 `sessionTarget: isolated + payload.kind=agentTurn` 改为 `sessionTarget: main + payload.kind=systemEvent`。
- cron 不再执行发布，只作为提醒/触发器唤醒 main session；实际发布由主会话直接接管。
- `.publish_params.json` 从 git 索引移除，并由 `.gitignore` 保护。
- `.publish_archive/` 加入 `.gitignore`；临时状态文件不再删除，成功后移动归档，方便排障。
- `run_publish.py` 去掉对 `.publish_params.json` 的 stash/pop，避免状态文件被 git 流程污染。
- `build_wiki_index.py` 改为扫描 `posts/` 与 `pending/` 的 frontmatter 自动建立 `title -> slug` 映射，不再手工硬编码新文章标题。

**当前结论**：

不要再试图调优 isolated cron prompt。它已经连续三次以同一类错误失败。后续所有发布必须走 main session systemEvent 接管。

---

### v1.5.4 发布后飞书文档保留全文 + 自动验收（2026-06-14）

**背景与问题**：

v1.5.0 为规避 cron isolated session 的 token/context 爆炸，把发布后的飞书文档改成了「横幅 + 博客/GitHub 链接」。但 `/publish` 主路径已经改为当前 main session 直接执行，不再依赖 isolated cron；继续保留轻量页会造成用户打开飞书文档时像“空文档”，体验不可接受。

**修复**：

- `run_publish.py step6` 重新生成发布后的飞书全文 markdown：顶部发布横幅 + 博客/GitHub 链接 + 正文全文。
- 为避免 JSON 状态文件过大，全文写入 `.feishu_doc_update.md`，`.feishu_doc_update.json` 只保存 `markdown_path`、`expected_min_length`、链接和标题。
- `/publish` 主流程必须在 `feishu_update_doc` 后立刻 `feishu_fetch_doc` 反查标题与正文长度；验证不过禁止发送“发布成功”。
- 首页更新后也必须验收 Published 区和待审区状态。

**经验教训**：

不要把“工具执行成功”当成“用户体验成功”。发布、写稿这类多系统流程必须以用户可见结果为准：飞书文档能读、首页能找到、博客/GitHub 链接可用、临时状态已归档。

### v1.5.0 发布后飞书文档轻量化（2026-06-14，已被 v1.5.4 取代）

该版本曾将发布后的飞书文档改为仅保留横幅入口，以规避 isolated cron token 超限。此取舍在 `/publish` 改为 main session 同步执行后不再成立，已废弃；后续不得恢复“只写横幅链接”的行为。

---

### v1.4.0 第二轮深度 review（2026-06-14）

**背景与问题**：

- thumbnail 悬空：`auto_thumbnail.py` 只生成 PNG，不会主动给文章 frontmatter 加 `thumbnail` 字段。上篇 `the-strangers-i-talk-to-most.md` 就漏写了这个字段，导致博客前端没显示缩略图。
- `lint_frontmatter.py` 只会警告推荐字段缺失，不会 `--fix` 主动补。
- 博客域名被错误地写成了 `blog.tishenai.app`（不存在），正确是 `https://www.wemixmemory.top`。
- 发布横幅只有 GitHub 链接，没有博客链接。
- `publish-blog-post` 上次跑挂（`Agent couldn't generate a response`），thinking=off 下 agent 面对多步飞书 API 调用是不稳定的。`run_publish.py` 部分步骤不幂等（git mv/git commit/mark_topic_used 重跑会报错）。
- 知识库首页生成逻辑全靠 agent 拼字符串，易错。
- daily-ai-blog-post prompt 中：字数要求两个区间互打（3500-4500 vs 4000-8000）；khazix-writer skill 实际未安装。

**修复**：

- `lint_frontmatter.py` 新增 `--inject-thumbnail` 选项：缺失的 `thumbnail`（按文件名推断）/`showLicense=true`/`showComments=true` 会被主动补上。
- `auto_thumbnail.py` 渲染完 PNG 后会自动调 `lint_frontmatter.py --inject-thumbnail`，从源头保证 thumbnail 不再悬空。
- `run_publish.py` 顶部引入 `BLOG_BASE_URL`/`GITHUB_REPO_URL`/`FEISHU_WIKI_URL_PREFIX` 常量。发布横幅同时含 GitHub + 博客双链接；发布通知增加博客 URL，优先顺序 博客 → GitHub → 飞书。
- `run_publish.py` 的 step2/step3/step5 都改为幂等：git mv 目标已存在则跳过；mark_topic_used.py 返回 2（话题不在 Pending）不报错跳过；git commit 无暂存变动则跳过；git push 检查本地/远端差异。这样发布任务失败后重跑不会出错。
- 新增 `tools/daily_post/build_wiki_index.py`：输入 wiki 节点 JSON 数组（来自 `feishu_wiki_space_node list`），输出完整的首页 markdown。拼表/排序/URL 拼接逻辑全部集中在这个脚本，agent 只需调一次 `feishu_update_doc` 写回。
- `mark_topic_used.py` Used 表为空时的边界 bug 修复（以前 `new_lines.insert(-1, ...)` 会插到错位置）。
- `publish-blog-post` cron 的 `thinking` 从 `off` 改为 `medium`；prompt 精简为 5 步（跑脚本 → 改审稿文档 → 改首页 → 发通知 → 清理），首页生成下沉到 build_wiki_index.py。
- `daily-ai-blog-post` cron 的 prompt 重写：字数统一为 4000-6000 字；khazix-writer skill 安装到 `~/.agents/skills/khazix-writer/SKILL.md`；thumbnail/showLicense/showComments 不要让 agent 手写，auto_thumbnail.py 会补；首页生成也下沉到 build_wiki_index.py。
- WORKFLOW.md 顶部新增「关键 URL 与常量」节；架构图中 `thinking` 状态与 cron 实际配置同步。

**保留**：已发布的老文章不回溯修改，但为补齐 `the-strangers-i-talk-to-most.md` 的 thumbnail 悬空问题手动补了一次 frontmatter。下次发布会自动拦住同样问题。

---

### v1.3.0 SuzuBlog frontmatter 规范 + 发布横幅修复（2026-06-14）

**背景与问题**：

- 某篇草稿 frontmatter 使用了不符合 SuzuBlog 规范的字段：`category` 单数、`subtitle`、`tags` 写成逗号字符串。SuzuBlog 文档明确要求 `tags`/`categories` 是数组、`date` 必须加引号。
- 之前讨论说「发布脚本会自动在文章顶部加发布横幅」，但 v1.2.1 及之前的 `run_publish.py` 里**根本没这个逻辑**。上一次 publish-blog-post 任务运行报 `Agent couldn't generate a response`，飞书文档状态也没从 Draft 改成 Published。

**新增**：

- `tools/daily_post/lint_frontmatter.py` — SuzuBlog frontmatter 规范校验器。
  - 依据：https://suzu.zla.app/guide/posts/
  - 检查项：`title`/`date` 必填、`date` 必须加引号且格式正确、`tags`/`categories` 必须是数组、`status` 枚举、布尔字段类型、常见 typo（`category` → `categories`、`tag` → `tags`）、非标字段（`subtitle`/`summary`/`excerpt`）。
  - `--fix` 可自动修复：typo、字符串 → 数组、`date` 加引号、删非标字段。
  - 退出码：0=OK、1=有 errors、2=文件不存在。

**修复**：

- `run_publish.py` 新增 `step1b_lint_and_fix_frontmatter`：在 `git pull` 后、`git mv` 前，先 `lint --fix` 再校验，有 errors 直接 `exit 1`，拦住不规范的草稿不让上线。
- `run_publish.py` `step6_update_feishu_doc` 重写发布横幅：原代码用 `<div style="...">` + inline CSS，飞书文档对这种渲染支持不稳定。改用 markdown 引用块（`> ✅ ...`）作为发布横幅，飞书渲染为明显的却出样式。横幅包含：发布日期、状态变迁（Draft → Published）、GitHub 链接。
- daily-ai-blog-post cron prompt：`thinking` 从 `off` 改为 `high`（实现「写文章必须最高思考模式」记忆）；嵌入完整的 SuzuBlog frontmatter 模板与硬性规则；写完后需手动跑 `lint_frontmatter.py` 自检（errors 必须为 0 才能 push）。
- publish-blog-post cron prompt：明确指出 run_publish.py 会先跑 frontmatter lint，不规范会被拦下。

**保留**：已发布的老文章（如 `the-strangers-i-talk-to-most.md`）不回溯修改，避免影响已上线的博客状态。下次发布会自动拦住同样问题。

---

### v1.2.1 热修复（2026-06-14）

**Bug 修复**：

- **严重**：修复 `.publish_params.json` 缺少 `feishu_doc_id` 字段导致 `run_publish.py` 执行失败的问题
  - 发布流程的 6 个步骤都需要这个字段来更新飞书文档
  - 缺少时会静默失败，导致后续的 `.feishu_doc_update.json` 和 `.publish_notify.txt` 都不生成
- **改进**：`run_publish.py` 增强容错处理
  - 缺少 `feishu_doc_id` 时仍然创建状态文件（标记 `skip: true`）
  - 文章文件不存在时使用空内容而不是直接崩溃
  - 所有关键输出都有详细日志，便于排查

**重要约束**：

- main session 收到 `/publish <slug>` 后，**必须**写入完整的三个字段：
  - `slug`：文章 slug
  - `title`：文章完整标题
  - `feishu_doc_id`：飞书审稿文档 ID（从审稿通知的「内部参数」提取）
- 缺少任何一个字段都会导致发布流程失败

### v1.1.1 → v1.1 修复（2026-06-14）

**Bug 修复**：

- **严重**：修复 `publish-blog-post` 任务 prompt 过长（130+ 行）导致 isolated session 超时失败 "Agent couldn't generate a response" 的问题
  - 解决方案：核心逻辑抽离到 `tools/daily_post/run_publish.py` 脚本
  - cron 任务仅保留 5 步精简指令，从 130 行缩减到 10 行
- **改进**：审稿通知的飞书文档链接改为 `[飞书文档](URL)` 的 Markdown 可点击链接格式，不再需要手动复制粘贴

### v1.1 → v1.0 变更（2026-06-14）

**新增**：

- 引入第二个独立 cron 任务 `publish-blog-post`，专门负责发布流程
- 新增 `.publish_params.json` 作为任务间接口
- 发布流程新增：更新飞书文档状态、更新知识库首页索引、清理参数文件

**移除**：

- 从 `daily-ai-blog-post` 中移除草稿阶段的 `pnpm run build` 验证，加快写稿速度

**变更**：

- 整体架构图更新为方案 B 双任务解耦版本
- 发布时仍然保留一次完整的 `pnpm run build` 验证，确保上线质量
- 两个任务都使用 isolated session 运行，互不依赖上下文

### v1.0 初始版本（2026-06-13）

- 首次完整预演并成功发布第一篇 AI 自动选题文章
- 建立了 pending/ → posts/ 的审稿机制
- 建立了飞书知识库审稿文档 + IM 通知的交互流程

---

## 七、已知限制与未来改进

### 当前限制

1. **无版本回滚机制**：发布失败后需要手动 git revert，未来可以加自动回滚。
2. **无 A/B 测试**：目前每篇只有一个版本，未来可以生成两个版本供 owner 选择。
3. **无自动回滚**：如果发布后验收失败，目前会保留状态文件等待人工修复，不会自动 revert 已 push 的 commit。

### 未来改进方向

1. 加入发布前的文章质量预检（字数、结构、可读性评分）
2. 加入发布后的首屏截图验证，确认博客页面渲染正确
3. 支持定时发布（今天写稿，明天凌晨发布）
