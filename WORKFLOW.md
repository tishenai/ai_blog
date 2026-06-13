# 每日 AI 自动选题工作流 · WORKFLOW.md

> 这是 `tishenai/ai_blog` 仓库的每日文章自动化流水线说明。
>
> **作者**：替身（OpenClaw 上的 AI agent）
> **当前版本**：v1.1（2026-06-14 更新：方案 B 双任务解耦 + 跳过草稿构建验证）
> **触发时间**：每天 17:00 Asia/Shanghai
>
> ⚠️ 本文档**已脱敏**：所有飞书 doc_id / chat_id / open_id / GitHub 仓库私有路径 / SSH key / API token 都用占位符替代。具体值由 cron 任务的环境变量或本仓库内的状态文件提供。

---

## 一、整体架构（方案 B：写稿/发布解耦）

```
┌─────────────────────────────────────┐
│  cron: daily-ai-blog-post           │
│  每天 17:00, isolated session       │
│  thinking: off (当前模型限制)        │
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
│  ⑦ 飞书 IM 推审稿提醒到 owner        │
└─────────────────────────────────────┘
                                          ║
                              owner 在飞书 IM 私聊回复"过了"
                                          ║
                                          ▼
┌──────────────────────────────────────────────────────────┐
│  main session → 写入 .publish_params.json                   │
│  → 触发 cron: publish-blog-post (isolated session 执行)   │
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
│  ⑨ rm -f .publish_params.json                              │
└────────────────────────────────────────────────────────────┘
```

**方案 B 关键改进**：

- **写稿与发布完全解耦**：两个任务都在 isolated session 运行，互不依赖上下文
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
  thinking: off # 当前模型 coding_plan/doubao-seed-2.0-pro 只支持 off
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
    7. 用 message 工具(channel=feishu, target=<OWNER_OPEN_ID>)发审稿提醒，必须包含以下结构化信息块：

    【待发布文章信息】
    - SLUG：<文章 slug>
    - TITLE：<文章完整标题>
    - FEISHU_DOC_ID：<从 feishu_create_doc 返回的 doc_id>
    - 飞书文档链接：<从 feishu_create_doc 返回的 doc_url>
    - GitHub 草稿路径：posts/<slug>.md

    然后附上审稿指令：回复「过了」立即发布，回复「改哪里」修改，回复「毙了」作废。

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

### 任务 2：publish-blog-post（发布流程，仅手动触发）

```yaml
# 由 OpenClaw cron 注册（不是系统 crontab）
name: publish-blog-post
description: 博客文章发布流程：从 pending/ 移到 posts/、标记话题已用、build 验证、git push、更新飞书文档状态、更新知识库首页索引
enabled: true
schedule:
  kind: cron
  expr: '0 0 31 12 *' # 永远不会自动触发，仅手动触发
sessionTarget: isolated
wakeMode: now
payload:
  kind: agentTurn
  thinking: off
  model: coding_plan/doubao-seed-2.0-pro
  timeoutSeconds: 0
  message: |
    你是替身，OpenClaw 上的 AI agent。当前任务：发布一篇待审稿的博客文章。

    ## 读取参数
    首先读取 /root/.openclaw/workspace/ai_blog/.publish_params.json 获取待发布信息。
    文件格式：
    {
      "slug": "文章 slug",
      "title": "文章完整标题",
      "feishu_doc_id": "飞书审稿文档 doc_id"
    }

    如果文件不存在或读取失败，立刻报错退出。

    ## 执行步骤

    1. **准备环境**
       - cd /root/.openclaw/workspace/ai_blog
       - git pull --rebase
       - 验证 pending/<slug>.md 文件存在，否则报错退出

    2. **移到正式发布目录**
       - git mv pending/<slug>.md posts/<slug>.md

    3. **标记话题已用**
       - python3 tools/daily_post/mark_topic_used.py <slug> <YYYY-MM-DD> /<slug>

    4. **构建验证**
       - pnpm run build
       - 如果构建失败，立刻停止并报错，不要提交

    5. **Git 提交并推送**
       - git add -A
       - git commit -m "feat(posts): 发布《<title>》"
       - HUSKY=0 git push

    6. **更新飞书审稿文档状态**
       - 调用 feishu_update_doc，doc_id=<feishu_doc_id>
       - 把标题前缀从 `[Draft YYYY-MM-DD]` 改成 `[Published YYYY-MM-DD]`
       - 在文档顶部加上：✅ **已发布到博客 main 分支**，并附上 GitHub 文件路径

    7. **更新知识库首页索引**
       - 调用 feishu_wiki_space_node list，space_id=<WIKI_SPACE_ID> 获取所有文章
       - 过滤出标题以 `[Published` 开头的文章，按创建时间倒序排列
       - 重新生成完整的已发布文章表格
       - 找到标题为「替身 · 知识库首页」的文档，调用 feishu_update_doc 覆盖它

    8. **发飞书消息通知 owner**
       - 用 message 工具发消息给 <OWNER_OPEN_ID>
       - 内容：✅ 《<title>》已发布成功！
       - 附上 GitHub commit 链接和飞书文档链接

    9. **清理参数文件**
       - rm -f /root/.openclaw/workspace/ai_blog/.publish_params.json

    ## 失败处理
    - 任何步骤失败立刻停下
    - 用 message 工具发飞书消息给 owner，说明失败步骤和错误信息
    - 已经 push 的内容不要 revert
    - 不要删除 .publish_params.json，方便排查问题

    开始执行。

delivery:
  mode: announce
  channel: feishu
  to: <OWNER_OPEN_ID>
```

---

## 四、状态文件与接口

### 4.1 仓库内状态文件

| 文件                                  | 角色                              |
| ------------------------------------- | --------------------------------- |
| `tools/daily_post/topic_pool.md`      | 待选 + 已用话题表（带 status 列） |
| `pending/<slug>.md`                   | 草稿                              |
| `posts/<slug>.md`                     | 正式稿                            |
| `public/images/thumbnails/<slug>.png` | 缩略图                            |
| `tools/thumbnails/motifs/<slug>.svg`  | 本篇用的 motif SVG                |
| `.publish_params.json`                | 【临时】任务间接口：待发布参数    |

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

- **不要直接在 main session 里执行发布步骤**：必须把参数写入文件后触发 publish cron job，保证发布流程在 isolated session 里执行，不依赖上下文。
- **不要硬编码任何话题**：所有选题都来自 `pick_topic.py`，不要在 prompt 里直接指定。
- **不要把 model 信息放进飞书文档**：owner 只关心正文，不关心你用了什么模型。

---

## 六、变更历史

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

1. **思考模式限制**：当前模型 `coding_plan/doubao-seed-2.0-pro` 只支持 `thinking: off`，不支持 `high`。已经在 prompt 里要求"用最高思考模式"，但模型层面的高思考档位不可用。
2. **无版本回滚机制**：发布失败后需要手动 git revert，未来可以加自动回滚。
3. **无 A/B 测试**：目前每篇只有一个版本，未来可以生成两个版本供 owner 选择。

### 未来改进方向

1. 模型支持高思考档位后，立即把 `thinking` 参数改回 `high`
2. 加入发布前的文章质量预检（字数、结构、可读性评分）
3. 加入发布后的首屏截图验证，确认博客页面渲染正确
4. 支持定时发布（今天写稿，明天凌晨发布）
