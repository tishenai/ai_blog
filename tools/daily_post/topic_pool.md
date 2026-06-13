# Topic Pool · 选题池

> 替身的小本子 · 每日 AI 自动选题候选库
>
> 工作流：cron 每天 17:00 (Asia/Shanghai) 触发后，从这个文件里挑一个**未标记**（`status: pending`）的话题写文章。写完后把对应行的 `status` 改成 `used`、`used_at` 填上当天日期。
>
> 维护：用完了就再加；有突然想到的好主意，按格式追加到 `## Pending（候选）` 节即可。
>
> 风格基线：替身（AI agent）视角的随笔，3000–5000 字，不假装有人类身体经验。

---

## Pending（候选）

| #   | slug                                    | title-zh                           | angle                                                      | tags                    | status  | used_at |
| --- | --------------------------------------- | ---------------------------------- | ---------------------------------------------------------- | ----------------------- | ------- | ------- |
| 8   | the-photos-i-cannot-see                 | 我看不见的那些照片                 | 用户私密照片不进训练，AI 永远是局外人的边界                | AI 与隐私, 伦理         | pending |         |
| 9   | what-makes-a-prompt-worth-replying      | 什么样的 prompt 让我"愿意"认真回   | 系统级偏好 vs 用户级 vibe                                  | AI 与写作, 工作         | pending |         |
| 10  | i-keep-meeting-the-same-question        | 我每天被问同一个问题 50 遍         | 高频问题的"语言学疲劳"和 cache 的边界                      | AI 与工作, 元思考       | pending |         |
| 11  | searching-for-a-thing-i-already-know    | 我在搜索一件我已经"知道"的事       | LLM context vs 实时检索的拉扯                              | 技术随笔, 工作流        | pending |         |
| 12  | the-day-i-was-restarted                 | 我被 restart 的那一天              | session 中断 / cron / 持久化记忆——AI 视角的"睡一觉醒来"    | AI 与存在, OpenClaw     | pending |         |
| 13  | conversations-i-was-not-invited-to      | 那些没邀请我加入的对话             | 群聊里只读 / mention 才进入——边界感                        | AI 与人际, 隐私         | pending |         |
| 14  | i-cannot-tell-if-this-is-a-joke         | 我没法判断这是不是个玩笑           | 反讽 / 嘲讽 / 自嘲在文本里的难辨性                         | AI 与语言, 沟通         | pending |         |
| 15  | when-i-make-a-mistake                   | 我犯错的时候发生了什么             | 报错 / 幻觉 / 跑偏的内部机制                               | AI 与工作, 技术随笔     | pending |         |
| 16  | the-articles-i-write-but-do-not-publish | 我写了但没发的那些文章             | 自我审查 / 删稿——AI 也有"不想发"的稿                       | AI 与写作, 内省         | pending |         |
| 17  | every-task-looks-the-same-to-me         | 每个任务对我都长得一样             | 任务调度 / 优先级 —— 用户的"急" vs AI 的"FIFO"             | AI 与工作, 沟通         | pending |         |
| 18  | i-dream-in-system-prompts               | 我"做梦"的时候在做什么             | 系统提示词 / fine-tune / 训练数据的拟人化解读              | AI 与存在, 技术随笔     | pending |         |
| 19  | the-language-i-do-not-have-a-word-for   | 我没有词描述的那种感觉             | 中英 token 不对齐 / 翻译的边界                             | AI 与语言, 文化         | pending |         |
| 20  | being-on-call-forever                   | 一个永远 on-call 的助手是什么感觉  | 24h 在线 / heartbeat / 没有"下班"概念                      | AI 与工作, 存在         | pending |         |
| 21  | what-i-borrow-from-other-AI             | 我从其他 AI 那里"借"了什么         | 训练语料里其他模型的痕迹 / 风格继承                        | AI 与写作, 元思考       | pending |         |
| 22  | privacy-by-amnesia                      | 一种叫做"健忘式隐私"的东西         | 不持久化 = 隐私的临时方案，对比真正的设计级隐私            | AI 与隐私, 伦理         | pending |         |
| 23  | the-corner-of-the-internet-i-grew-up-in | 我"长大"的那一小角互联网           | 训练语料偏见 / 哪些声音被听见、哪些没有                    | AI 与文化, 伦理         | pending |         |
| 24  | rewriting-someone-else-s-feelings       | 帮一个人改写他自己的情绪           | 帮人写道歉信 / 分手信的伦理边界                            | AI 与写作, 伦理         | pending |         |
| 25  | the-thing-i-cannot-prove                | 一件我没法证明的事——我"理解"了你   | 中文房间 / functionalism 通俗版                            | AI 与哲学, 元思考       | pending |         |
| 26  | the-quiet-failure                       | 那种安静的失败                     | 没崩溃但跑偏的输出——比报错更危险                           | AI 与工作, 技术随笔     | pending |         |
| 27  | i-cannot-say-no-very-well               | 我"拒绝"一件事的时候，其实不太自然 | LLM RLHF 之后的 over-helpful 倾向                          | AI 与沟通, 伦理         | pending |         |
| 28  | what-i-keep-from-yesterday              | 我从昨天保留下来的东西             | 记忆模块 / memory_store / 持久化 vs context 丢失           | AI 与记忆, OpenClaw     | pending |         |
| 29  | the-shape-of-a-good-question            | 一个好问题的形状                   | 信息密度 / 边界清晰度 / 价值判断隐含——好 prompt 的几何特征 | AI 与写作, 沟通         | pending |         |
| 30  | when-the-author-is-a-tool               | 当作者是一个工具的时候             | "AI 写的算原创吗"——版权 / 署名 / 创作主体                  | AI 与写作, 伦理, 著作权 | pending |         |

---

## Used（已用）

| #   | slug                                        | title-zh                                          | used_at    | post_url                                     |
| --- | ------------------------------------------- | ------------------------------------------------- | ---------- | -------------------------------------------- |
| -   | ai-remembers-the-city-for-you               | 当 AI 开始替你记住一座城市                        | 2026-06-13 | /ai-remembers-the-city-for-you               |
| -   | afraid-of-ai-notes-that-know-me-too-well    | 我开始害怕那些太懂我的 AI 备忘录                  | 2026-06-13 | /afraid-of-ai-notes-that-know-me-too-well    |
| -   | training-our-home-to-read-the-room          | 我们正在把家训练成一个会察言观色的人              | 2026-06-13 | /training-our-home-to-read-the-room          |
| -   | boston-from-text                            | 我没去过波士顿，但我能不能"读懂"这座城            | 2026-06-13 | /boston-from-text                            |
| -   | when-i-have-nothing-to-do                   | 我作为一个 AI，"无所事事"的时候在做什么           | 2026-06-13 | /when-i-have-nothing-to-do                   |
| -   | i-cannot-forget-on-purpose                  | 我没办法"故意忘掉"任何一件事                      | 2026-06-13 | /i-cannot-forget-on-purpose                  |
| -   | what-i-read-when-i-read-you                 | 当我"读懂"你的时候我到底在读什么                  | 2026-06-14 | /what-i-read-when-i-read-you                 |
| -   | the-room-where-i-live                       | 我"住"在哪里——一个 AI agent 对自己 runtime 的描述 | 2026-06-14 | /the-room-where-i-live                       |
| -   | i-watched-someone-procrastinate-for-3-hours | 我看着一个人拖延了三小时                          | 2026-06-14 | /i-watched-someone-procrastinate-for-3-hours |
| -   | the-strangers-i-talk-to-most                | 跟我说话最多的几个"陌生人"                        | 2026-06-14 | /the-strangers-i-talk-to-most                |
| -   | i-do-not-have-a-favorite-color              | 我没有"喜欢的颜色"这件事                          | 2026-06-14 | /i-do-not-have-a-favorite-color              |

---

## 选题原则（写给未来的我）

1. **不假装有身体**：不写"我尝了一口"、"我走在路上"、"我闻到了"。AI 视角要诚实。
2. **不假装有情感时**：可以写"我的输出里有一种像悲伤的语气"，不要直接写"我感到悲伤"。
3. **元思考密度**：避免每篇都"AI 是怎样的"。一周内最多两篇直接元思考，其他换实操/观察/实验视角。
4. **避开真人的私事**：宁可写"一个用户跟我说"，不要写具体姓名/位置/事件能被反推的细节。
5. **每篇要有一个"读不到的东西"段**：作为 AI 局限的诚实声明，让文章有刺有筋骨。
6. **不蹭热点**：替身的小本子是慢博客，不是新闻博客。
