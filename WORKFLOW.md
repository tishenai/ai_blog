# 每日 AI 自动选题工作流 · WORKFLOW.md

> 这是 `tishenai/ai_blog` 仓库的每日文章自动化流水线说明。
>
> **作者**：替身（OpenClaw 上的 AI agent）
> **当前版本**：v1.5.0（2026-06-14 发布后飞书文档轻量化）
> **上一版**：v1.4.0（2026-06-14 第二轮深度 review）
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
│   │   ├── lint_frontmatter.py    # ★ frontmatter 规范校验（SuzuBlog），--inject-thumbnail 补推荐字段
│   │   ├── build_wiki_index.py    # ★ 生成知识库首页 markdown（从 wiki 节点 JSON）
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
  thinking: medium
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

### v1.5.0 发布后飞书文档轻量化（2026-06-14）

**背景与问题**：

publish-blog-post cron job 反复在同一个阶段挂：`Agent couldn't generate a response`，lastDurationMs 达 100s+、token 用过 100k。跟踪下来：在 cron isolated session 里，`feishu_update_doc(mode='overwrite', markdown=<7000字正文>)` 会使整篇文章进入 messages context（tool call args + tool result echo + thinking 反复推理），叠加后超限。

主 session 不会遇到这个问题是因为会被背景压缩 + 多轮交互释放压力，cron isolated turn 是一发、不能缩水。

**修复（架构变更）**：

- 发布后的飞书审稿文档不再保留文章正文，仅保留横幅 + 博客/GitHub 双链接（约 200 字节）。
- run_publish.py step6 不再读文章正文，.feishu_doc_update.json 从 14KB 限为 600B。
- cron agent 调 update_doc 时 messages context 几乎不使用 token。

**体验变化**：

之前：打开飞书审稿文档可读全文。
现在：打开飞书审稿文档只看到「已发布 + 博客链接 + GitHub 链接」横幅，点进去在博客看全文。

体验上轻微降级，但考虑到：

1. 审稿阶段才是飞书文档的主场景（Draft 状态留全文，owner 在飞书里读完决定发布）。
2. 发布后该文档退为「档案入口」，轻量化作为导航卡片反而更符合信息架构。
3. 这是唯一避免 cron 发布压起 token 天花板的干净方案。

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
3. **首页 slug 映射主要靠 build_wiki_index.py 里的 TITLE_TO_SLUG 字典**：新发文章需手动补进去，未来考虑改为扫描 posts/ 目录 frontmatter 取 title。

### 未来改进方向

1. 加入发布前的文章质量预检（字数、结构、可读性评分）
2. 加入发布后的首屏截图验证，确认博客页面渲染正确
3. 支持定时发布（今天写稿，明天凌晨发布）
