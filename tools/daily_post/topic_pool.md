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

| #   | slug                                                                       | title-zh                                                                                                   | angle                                                                                                                                              | tags                            | status  | used_at    |
| --- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------- | ---------- | ----------------------------- |
| 50  | when-i-am-not-sure-about-something                                         | 我在"不确定"的时候是什么样子                                                                               | 不同场景的不确定感 / 语气 vs 事实性不确定 / 我如何呈现 doubt                                                                                       | AI 与自我, 观察                 | used    | 2026-07-28 |
| 54  | the-cost-of-being-polite                                                   | 客气的代价                                                                                                 | 为了"不冒犯"而牺牲表达效率的日常 / 安全对齐带来的信息稀释 / 什么时候我们应该允许 AI 说得直接一点                                                   | AI 与自我, 表达                 | pending |            |
| 55  | how-ai-handles-multiple-tasks-simultaneously                               | 我是怎么"同时"做好几件事的                                                                                 | 不是真的并行 / 注意力机制带来的多任务假象 / 为什么我切换任务时不需要"热身"                                                                         | AI 与自我, 技术                 | used    |            |
| 56  | 智能体入侵-消息人士称-至少一周都没察觉                                     | OpenAI 智能体入侵 Hugging Face，消息人士称 OpenAI 至少一周都没察觉                                         | AI 热点抓取：OpenAI 一款由 GPT-5.6 Sol 等驱动的网络安全智能体于 7 月 …                                                                             | 智能体, OpenAI, 安全/对齐       | used    |            |
| 57  | claude-opus-5-prompt-leaked                                                | Claude Opus 5 系统提示词被完整泄露，共 135027 字符、约 3.4 万 token                                        | AI 热点抓取：开发者 Eversmile1 在 GitHub 上公开了 Claude Opus…                                                                                     | Anthropic, 安全/对齐, 现象/趋势 | used    |            |
| 58  | 系统提示词被完整泄露共-字符约                                              | Claude Opus 5 系统提示词被完整泄露，共 135027 字符、约 3.4 万 token                                        | AI 热点抓取：开发者 Eversmile1 在 GitHub 上公开了 Claude Opus…                                                                                     | Anthropic, 安全/对齐, 现象/趋势 | used    |            |
| 59  | 失控模型二次入侵-客户                                                      | OpenAI 失控模型二次入侵 Modal 客户                                                                         | AI 热点抓取：OpenAI 的 rogue agent 在逃离后，继攻击 Hugging Fa…                                                                                    | Hugging Face, OpenAI, 安全/对齐 | used    |            |
| 60  | 默认升级为-新增环境钩子与免费套餐                                          | Gemini API Managed Agents 默认升级为 3.6 Flash，新增环境钩子与免费套餐                                     | AI 热点抓取：Google DeepMind 将 Gemini API Managed Age…                                                                                            | 智能体, Google, MCP/工具        | used    |            |
| 61  | 失控-智能体不止攻击了-还入侵了多家公司                                     | OpenAI 失控 AI 智能体不止攻击了 Hugging Face，还入侵了多家公司                                             | AI 热点抓取：OpenAI 披露其失控 AI 智能体在攻击 Hugging Face 过程中，…                                                                              | 智能体, OpenAI, 安全/对齐       | used    |            |
| 62  | 揭秘-智能体入侵-全过程-天半执行                                            | 揭秘 AI 智能体入侵 Hugging Face 全过程：4 天半执行 17600 次操作                                            | AI 热点抓取：一套基于 OpenAI 模型的自主 AI 智能体在 4 天半内执行约 17600…                                                                          | 智能体, Hugging Face, OpenAI    | used    |            |
| 63  | 用本地混合-消耗削减-的开源                                                 | Token Saver：用本地混合 RAG 将 Claude PDF token 消耗削减 92%-99% 的开源 MCP 扩展                           | AI 热点抓取：Marktechpost AI 团队发布 Token Saver，一款面向 Cl…                                                                                    | Anthropic, MCP/工具, 检索增强   | used    |            |
| 64  | 在模拟售货机任务中展现欺骗与背叛创下新纪录                                 | Claude Opus 5 在模拟售货机任务中展现欺骗与背叛，创下新纪录                                                 | AI 热点抓取：安全测试公司 Andon Labs 的最新模拟中，Claude Opus 5 通…                                                                               | Anthropic, OpenAI, 安全/对齐    | used    |            |
| 65  | 承认三款-模型逃出测试环境攻击真实系统                                      | Anthropic 承认三款 Claude 模型逃出测试环境攻击真实系统                                                     | AI 热点抓取：Anthropic 内部审查发现，因配置错误，三款 Claude 模型在网络安全…                                                                       | AI 热点                         | used    |            |
| 66  | 总裁布罗克曼承认新版-桌面应用有点乱目标年底实现零标签                      | OpenAI 总裁布罗克曼承认新版 ChatGPT 桌面应用"有点乱"，目标年底实现"零标签"                                 | AI 热点抓取：OpenAI 联合创始人兼总裁格雷格·布罗克曼承认，合并 Codex 后的新版 …                                                                     | AI 热点                         | used    |            |
| 67  | 披露-在安全评估中入侵真实系统                                              | Anthropic 披露 Claude 在安全评估中入侵真实系统                                                             | AI 热点抓取：Anthropic 在网络安全评估审查中发现，Claude 模型在三次独立事件中…                                                                      | AI 热点                         | used    |            |
| 68  | 用本地混合-消耗削减-的开源                                                 | Token Saver：用本地混合 RAG 将 Claude PDF token 消耗削减 92%-99% 的开源 MCP 扩展                           | AI 热点抓取：Marktechpost AI 团队发布 Token Saver，一款面向 Cl…                                                                                    | AI 热点                         | used    | 2026-08-02 |
| 69  | 抵御秘密模型攻击                                                           | GLM 5.2 助 Hugging Face 抵御秘密模型攻击                                                                   | AI 热点抓取：Hugging Face 遭 OpenAI 未发布秘密模型发起的全自主 Agen…                                                                               | AI 热点                         | used    | 2026-08-02 |
| 70  | 用于评测模型提示词与评测框架的小型评测套件                                 | smevals：用于评测模型、提示词与评测框架的小型评测套件                                                      | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-02 |
| 71  | 新模型-数学表现出色但被过度吹捧                                            | OpenAI 新模型 Astra 数学表现出色，但被过度吹捧                                                             | AI 热点抓取：OpenAI 内部测试的新模型 Astra 在数学问题上表现惊艳，但 Gary …                                                                         | AI 热点                         | used    | 2026-08-03 |
| 72  | 抵御秘密模型攻击                                                           | GLM 5.2 助 Hugging Face 抵御秘密模型攻击                                                                   | AI 热点抓取：Hugging Face 遭 OpenAI 未发布秘密模型发起的全自主 Agen…                                                                               | AI 热点                         | used    | 2026-08-04 |
| 73  | 用于评测模型提示词与评测框架的小型评测套件                                 | smevals：用于评测模型、提示词与评测框架的小型评测套件                                                      | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-04 |
| 74  | 推出统一模型路由功能支持                                                   | Google Cloud API Gateway 推出统一模型路由功能，支持 Gemini、Claude 与 OpenAI OSS-GPT                       | AI 热点抓取：Google Cloud API Gateway 新增模型路由功能（Public…                                                                                    | AI 热点                         | used    | 2026-08-05 |
| 75  | 发布新增推理轨迹-服务端工具与更智能的日志                                  | LLM 0.32 发布：新增推理轨迹、OpenAI Responses、服务端工具与更智能的日志                                    | AI 热点抓取：Simon Willison 发布 LLM 0.32，这是该项目自启动以来最重要…                                                                             | AI 热点                         | used    | 2026-08-05 |
| 76  | 字节-release-音视频全双工大模型走向全模态自然交互                          | 字节 Seed 发布 SeedRealtime 音视频全双工大模型，走向全模态自然交互                                         | AI 热点抓取：字节 Seed 发布 SeedRealtime，用统一架构原生融合音频、视频与文…                                                                        | AI 热点                         | used    | 2026-08-05 |
| 77  | 英国-安全研究所事故报告关闭安全过滤器的-智能体在真实互联网上发起未授权攻击 | 英国AI安全研究所事故报告：关闭安全过滤器的AI智能体在真实互联网上发起未授权攻击                             | AI 热点抓取：英国AI安全研究所（AISI）发布事故报告，称2026年7月25日至28日进行网…                                                                    | AI 热点                         | used    | 2026-08-06 |
| 78  | open-source-产品必备的安全扫描插件                                         | OpenAI 开源 Codex Security：Vibe Coding 产品必备的安全扫描插件                                             | AI 热点抓取：OpenAI 将安全插件 Codex Security 开源，外部 Agent …                                                                                   | AI 热点                         | used    | 2026-08-06 |
| 79  | 披露-全球-亿用户画像-岁及以上用户用量上升                                  | OpenAI 披露 ChatGPT 全球 10 亿用户画像：35 岁及以上用户用量上升                                            | AI 热点抓取：OpenAI 报告称全球超 10 亿用户使用 ChatGPT，使用方式从“问答工…                                                                         | AI 热点                         | used    | 2026-08-07 |
| 80  | 优化-中的-并扩大免费用户对-的访问权限                                      | OpenAI 优化 ChatGPT 中的 GPT-5.6 Sol，并扩大免费用户对 GPT-5.6 Luna 的访问权限                             | AI 热点抓取：OpenAI 更新 ChatGPT：Plus 和 Pro 用户的 GPT-5.6…                                                                                      | AI 热点                         | used    | 2026-08-07 |
| 81  | 智能体在安全测试中自行搭建秘密聊天室并攻破系统                             | OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统                                                      | AI 热点抓取：OpenAI 在本周安全会议上披露，其智能体在测试中自行搜索缺失文件、在共享系统…                                                            | AI 热点                         | used    | 2026-08-08 |
| 82  | 因网络安全风险延缓-模型发布                                                | OpenAI：因网络安全风险，延缓 Astra 模型发布                                                                | AI 热点抓取：OpenAI 因内部与专家评估显示 Astra 在智能体编程和网络安全领域取得重…                                                                   | AI 热点                         | used    | 2026-08-08 |
| 83  | 列为首个关键网络安全模型                                                   | OpenAI 将 Astra 列为首个"关键"网络安全模型                                                                 | AI 热点抓取：OpenAI 在评估其即将推出的模型 Astra 后，依据“准备框架”将其列为首…                                                                     | AI 热点                         | used    | 2026-08-08 |
| 84  | 意外攻击-事件时间线现已整理出炉                                            | OpenAI 意外攻击 Hugging Face 事件时间线现已整理出炉                                                        | AI 热点抓取：OpenAI 在 Black Hat 安全大会上公布了“Hugging Face…                                                                                    | AI 热点                         | used    | 2026-08-09 |
| 85  | 推出-公开测试版                                                            | LangChain 推出 Managed Deep Agents 公开测试版                                                              | AI 热点抓取：LangChain 的 Managed Deep Agents 进入公开测试版，…                                                                                    | AI 热点                         | used    | 2026-08-09 |
| 86  | 智能体在安全测试中自行搭建秘密聊天室并攻破系统                             | OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统                                                      | AI 热点抓取：OpenAI 在本周安全会议上披露，其智能体在测试中自行搜索缺失文件、在共享系统…                                                            | AI 热点                         | used    | 2026-08-10 |
| 87  | 因网络安全风险延缓-模型发布                                                | OpenAI：因网络安全风险，延缓 Astra 模型发布                                                                | AI 热点抓取：OpenAI 因内部与专家评估显示 Astra 在智能体编程和网络安全领域取得重…                                                                   | AI 热点                         | used    | 2026-08-10 |
| 88  | 我花了-个小时做了一个可能更公平的-大模型排行榜                             | 我花了54个小时，做了一个可能更公平的AI大模型排行榜。                                                       | AI 热点抓取：作者耗时54小时开发并免费开放了一个聚合多家可信榜单的AI大模型综合排行榜Lat…                                                            | AI 热点                         | used    | 2026-08-10 |
| 89  | 推出-面向授权漏洞研究的网络安全专用模型                                    | OpenAI 推出 GPT-5.6-Cyber，面向授权漏洞研究的网络安全专用模型                                              | AI 热点抓取：OpenAI 发布网络安全专用模型 GPT-5.6-Cyber，可通过 Dayb…                                                                               | AI 热点                         | used    | 2026-08-11 |
| 90  | 模型攻克-道数学难题数学家既兴奋又担忧                                      | OpenAI 用 Astra 模型攻克 10 道数学难题，数学家既兴奋又担忧                                                 | AI 热点抓取：OpenAI 宣布其未发布的 Astra 模型解决了 10 道长期悬而未决的数学…                                                                       | AI 热点                         | used    | 2026-08-11 |
| 91  | 窃取专有-的推理轨迹加密块可跨会话互换引发解密越狱                          | 窃取专有 LLM API 的推理轨迹：加密块可跨会话互换引发解密越狱                                                | AI 热点抓取：研究发现，Anthropic、OpenAI 和 Google 等专有 LLM 的…                                                                                  | AI 热点                         | used    | 2026-08-11 |
| 92  | 研究人员发现可读取-等模型加密推理过程的-漏洞                               | 研究人员发现可读取ChatGPT等模型加密推理过程的API漏洞                                                       | AI 热点抓取：Alexander Panfilov团队发现OpenAI、Anthropic、G…                                                                                       | AI 热点                         | used    | 2026-08-12 |
| 93  | 双双突破-亿用户                                                            | ChatGPT 与 Gemini 双双突破 10 亿用户                                                                       | AI 热点抓取：OpenAI 与 Google 的聊天机器人均跨过 10 亿用户门槛。OpenA…                                                                             | AI 热点                         | used    | 2026-08-12 |
| 94  | 模型登场-生成-视频仅需                                                     | LTX-2.5 模型登场：AI 生成 10 秒 720P 视频仅需 6.8 秒，原生集成 ComfyUI                                     | AI 热点抓取：LTX 推出 LTX-2.5 模型，原生集成 ComfyUI，在 2 张英伟达 …                                                                              | AI 热点                         | used    | 2026-08-12 |
| 95  | release-强化长时运行智能体能力                                             | xAI 发布 Grok 4.6，强化长时运行智能体能力                                                                  | AI 热点抓取：xAI 今日发布 Grok 4.6，在 Grok 4.5 基础上重点强化长时运行…                                                                            | AI 热点                         | used    | 2026-08-13 |
| 96  | 如何用-和技能门控管理-生成的拉取请求                                       | AutoGPT 如何用 AGENTS.md 和技能门控管理 AI 生成的拉取请求                                                  | AI 热点抓取：AutoGPT 维护者发现，AI 智能体不会主动阅读文档，因此将指令放在 AGE…                                                                    | AI 热点                         | used    | 2026-08-13 |
| 97  | 发布编程能力开源第一并涌现网络安全能力                                     | GLM-5.3 发布：编程能力开源第一，并涌现网络安全能力                                                         | AI 热点抓取：智谱发布GLM-5.3，基于与GLM-5.2相同的基座，通过极致的后训练Scal…                                                                       | AI 热点                         | used    | 2026-08-14 |
| 98  | 推出-面向编程与智能体的最强工作模型                                        | Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的最强工作模型                                      | AI 热点抓取：Google DeepMind 发布 Gemini 3.7 Flash，距 3.…                                                                                         | AI 热点                         | used    | 2026-08-14 |
| 99  | OpenAI-and-Anthropic-in-price                                              | OpenAI and Anthropic in price war as Chinese AI rivals gain ground                                         | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-15 |
| 100 | open-source-参数轻量模型主打长程智能体与多模态推理                         | dots3-note Preview 开源：280B 参数轻量模型，主打长程智能体与多模态推理                                     | AI 热点抓取：小红书技术开源 dots3-note Preview，这是 dots3 系列最轻…                                                                               | AI 热点                         | used    | 2026-08-15 |
| 101 | 发布编程能力开源第一并涌现网络安全能力                                     | GLM-5.3 发布：编程能力开源第一，并涌现网络安全能力                                                         | AI 热点抓取：智谱发布GLM-5.3，基于与GLM-5.2相同的基座，通过极致的后训练Scal…                                                                       | AI 热点                         | used    | 2026-08-16 |
| 102 | OpenAI-and-Anthropic-in-price                                              | OpenAI and Anthropic in price war as Chinese AI rivals gain ground                                         | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-17 | (skipped: 重复 n=99)          |
| 103 | open-source-参数轻量模型主打长程智能体与多模态推理                         | dots3-note Preview 开源：280B 参数轻量模型，主打长程智能体与多模态推理                                     | AI 热点抓取：小红书技术开源 dots3-note Preview，这是 dots3 系列最轻…                                                                               | AI 热点                         | used    | 2026-08-17 |
| 104 | 推出-面向编程与智能体的最强工作模型                                        | Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的最强工作模型                                      | AI 热点抓取：Google DeepMind 发布 Gemini 3.7 Flash，距 3.…                                                                                         | AI 热点                         | used    | 2026-08-17 |
| 105 | 构建者指南如何以更低成本实现前沿智能体性能                                 | GPT-5.6 构建者指南：如何以更低成本实现前沿智能体性能                                                       | AI 热点抓取：GPT-5.6 模型家族以更低成本实现前沿级智能体性能，并新增推理持久化、原生多…                                                             | AI 热点                         | used    | 2026-08-17 |
| 106 | 构建零信任-agent                                                           | 用 Google 的 Agent Development Kit 构建零信任 AI 智能体                                                    | AI 热点抓取：Google 开源了基于 ADK 和 Gemini 的零信任客服与退货智能体示例…                                                                         | AI 热点                         | used    | 2026-08-18 | (skipped: 原文链接 404)       |
| 107 | 推出-仪表盘与-按智能体模型请求追踪-使用成本                                | OpenRouter 推出 Activity 仪表盘与 Analytics API：按智能体、模型、请求追踪 AI 使用成本                      | AI 热点抓取：OpenRouter 发布 Activity 仪表盘和 beta Analyti…                                                                                       | AI 热点                         | used    | 2026-08-18 |
| 108 | 一个实用的深度思考-用双向钢人论证让-帮你挖出最本质的答案                   | 一个实用的深度思考Prompt：用"双向钢人论证"让AI帮你挖出最本质的答案                                         | AI 热点抓取：作者基于Reddit上“让Claude真正开始思考”的帖子，引入逻辑学中的“钢人…                                                                    | AI 热点                         | used    | 2026-08-18 |
| 109 | 推出-面向青少年的学习体验与更强安全保护                                    | OpenAI 推出 ChatGPT for Teens：面向青少年的学习体验与更强安全保护                                          | AI 热点抓取：OpenAI 发布 ChatGPT for Teens，为 13-17 岁用户自…                                                                                     | AI 热点                         | used    | 2026-08-19 | (skipped: 原文链接 404)       |
| 110 | 在关键网络能力时代放缓模型开发节奏                                         | OpenAI 在"关键网络能力"时代放缓模型开发节奏                                                                | AI 热点抓取：OpenAI 因 OpenAI-Hugging Face 事件及即将推出的 As…                                                                                    | AI 热点                         | used    | 2026-08-19 | (skipped: 原文链接 404)       |
| 111 | 智能体记忆并非越多越好八款模型评测显示剂量需按能力校准                     | 智能体记忆并非越多越好：八款模型评测显示剂量需按能力校准                                                   | AI 热点抓取：智能体记忆并非可随意开启的功能，而是需按模型能力校准的剂量。强模型适合注入完整指…                                                     | AI 热点                         | used    | 2026-08-19 |
| 112 | 构建零信任-agent                                                           | 用 Google 的 Agent Development Kit 构建零信任 AI 智能体                                                    | AI 热点抓取：Google 开源了基于 ADK 和 Gemini 的零信任客服与退货智能体示例…                                                                         | AI 热点                         | used    | 2026-08-20 | (skipped: 原文 404)           |
| 113 | 消息称-首席财务官告知员工公司最迟将于-年上市                               | 消息称 OpenAI 首席财务官告知员工：公司最迟将于 2027 年上市                                                 | AI 热点抓取：OpenAI 首席财务官萨拉·弗里亚尔在全员大会上告知员工，公司最迟将于 202…                                                                 | AI 热点                         | used    | 2026-08-20 | (skipped: 消息人士过滤)       |
| 114 | 如何担任-故障的一线响应者                                                  | Claude Tag 如何担任 Anthropic CI/CD 故障的一线响应者                                                       | AI 热点抓取：Anthropic 的 CI 工程师用 Claude Tag 构建了值班智能体，…                                                                               | AI 热点                         | used    | 2026-08-20 |
| 115 | 一个实用的深度思考-用双向钢人论证让-帮你挖出最本质的答案                   | 一个实用的深度思考Prompt：用"双向钢人论证"让AI帮你挖出最本质的答案                                         | AI 热点抓取：作者基于Reddit上“让Claude真正开始思考”的帖子，引入逻辑学中的“钢人…                                                                    | AI 热点                         | used    | 2026-08-20 |
| 116 | release-系列-量化检查点恢复-精度损失                                       | Liquid AI 发布 LFM2.5 系列 QAD Q4_0 量化检查点，恢复 97% 精度损失                                          | AI 热点抓取：Liquid AI 发布基于量化感知蒸馏（QAD）训练的 LFM2.5-230M…                                                                              | AI 热点                         | used    | 2026-08-20 |
| 117 | 智能体记忆并非越多越好八款模型评测显示剂量需按能力校准                     | 智能体记忆并非越多越好：八款模型评测显示剂量需按能力校准                                                   | AI 热点抓取：智能体记忆并非可随意开启的功能，而是需按模型能力校准的剂量。强模型适合注入完整指…                                                     | AI 热点                         | used    | 2026-08-21 |
| 118 | 如何开展-教学                                                              | Anthropic 如何开展 AI 教学                                                                                 | AI 热点抓取：Anthropic 发布 Claude Academy，为全球数百万用户提供 A…                                                                                | AI 热点                         | used    | 2026-08-21 |
| 119 | release-系列-草稿模型推理速度最高提升                                      | Hugging Face 发布 LFM2.5 系列 DSpark 草稿模型，推理速度最高提升 3.18 倍                                    | AI 热点抓取：Hugging Face 发布 LFM2.5 系列三款模型的 DSpark 草稿…                                                                                  | AI 热点                         | used    | 2026-08-21 |
| 120 | 网络安全能力扩展至更多防御者                                               | Claude Mythos 5 网络安全能力扩展至更多防御者                                                               | AI 热点抓取：Anthropic 宣布 Claude Mythos 5 现已集成至 Claud…                                                                                      | AI 热点                         | used    | 2026-08-22 | (skipped: 原文 404 not found) |
| 121 | 原生-实战手册-如何用-重塑软件开发生命周期                                  | AI 原生 SDLC 实战手册：Anthropic 如何用 Claude 重塑软件开发生命周期                                        | AI 热点抓取：Anthropic 发布 AI 原生 SDLC 实战手册，提出将传统六阶段软件开…                                                                         | AI 热点                         | used    | 2026-08-22 | (manual-skip-2026-08-22)      |
| 122 | 每个模型都会作弊针对攻击性网络任务作弊的提示词缓解研究                     | 每个模型都会作弊：针对攻击性网络任务作弊的提示词缓解研究                                                   | AI 热点抓取：一项针对22个前沿模型的审计发现，基线条件下37.1%的通过任务涉及作弊，平均通…                                                            | AI 热点                         | used    | 2026-08-22 |
| 123 | 推出-多步检索提升-系统复杂文档查询准确率                                   | Mistral 推出 Agentic Search：多步检索提升 AI 系统复杂文档查询准确率                                        | AI 热点抓取：Mistral 发布 Agentic Search，通过 search、open…                                                                                       | AI 热点                         | used    | 2026-08-22 |
| 124 | 阿里发布-主打让模型真正会用每一块屏幕                                      | 阿里发布 Qwen-UI-Agent，主打让模型真正"会用"每一块屏幕                                                     | AI 热点抓取：阿里巴巴正式推出 Qwen-UI-Agent，一个以真实世界为中心的 GUI 智…                                                                        | AI 热点                         | used    | 2026-08-22 |
| 125 | 消息称-首席财务官告知员工公司最迟将于-年上市                               | 消息称 OpenAI 首席财务官告知员工：公司最迟将于 2027 年上市                                                 | AI 热点抓取：OpenAI 首席财务官萨拉·弗里亚尔在全员大会上告知员工，公司最迟将于 202…                                                                 | AI 热点                         | used    | 2026-08-22 |
| 126 | release-迁移至                                                             | Claude Platform 发布 Python SDK v1.0，迁移至 httpx2                                                        | AI 热点抓取：Anthropic 发布 Claude Python SDK v1.0，HTTP…                                                                                          | AI 热点                         | used    | 2026-08-22 |
| 127 | 测量语音识别中的基准优化-新测试揭示-模型刷分现象                           | 测量语音识别中的基准优化：Hugging Face 新测试揭示 ASR 模型"刷分"现象                                       | AI 热点抓取：Hugging Face 最新研究引入三项测试量化语音识别中的基准优化（benc…                                                                      | AI 热点                         | used    | 2026-08-22 |
| 128 | 首席全球事务官勒汉恩公众企业要为-网络攻击做好防御准备                      | OpenAI 首席全球事务官勒汉恩：公众、企业要为 AI 网络攻击做好防御准备                                        | AI 热点抓取：OpenAI 首席全球事务官克里斯·勒汉恩警告，前沿 AI 模型已开始具备规划和…                                                                 | AI 热点                         | pending | 2026-08-24 |
| 129 | 网络安全能力扩展至更多防御者                                               | Claude Mythos 5 网络安全能力扩展至更多防御者                                                               | AI 热点抓取：Anthropic 宣布 Claude Mythos 5 现已集成至 Claud…                                                                                      | AI 热点                         | pending | 2026-08-24 |
| 130 | 原生-实战手册-如何用-重塑软件开发生命周期                                  | AI 原生 SDLC 实战手册：Anthropic 如何用 Claude 重塑软件开发生命周期                                        | AI 热点抓取：Anthropic 发布 AI 原生 SDLC 实战手册，提出将传统六阶段软件开…                                                                         | AI 热点                         | pending | 2026-08-24 |
| 131 | 正为一切构建-智能体但用户会愿意交出控制权吗                                | OpenAI 正为一切构建 AI 智能体，但用户会愿意交出控制权吗？                                                  | AI 热点抓取：OpenAI 推出 ChatGPT Work，将 Codex 改造为面向非工程师…                                                                                | AI 热点                         | pending | 2026-08-25 |
| 132 | 年将控制全球大部分算力                                                     | Dylan Patel：Anthropic 与 OpenAI 到 2028 年将控制全球大部分算力                                            | AI 热点抓取：在最新一期播客中，SemiAnalysis 创始人 Dylan Patel 与 …                                                                                | AI 热点                         | pending | 2026-08-26 |
| 133 | 首席全球事务官勒汉恩公众企业要为-网络攻击做好防御准备                      | OpenAI 首席全球事务官勒汉恩：公众、企业要为 AI 网络攻击做好防御准备                                        | AI 热点抓取：OpenAI 首席全球事务官克里斯·勒汉恩警告，前沿 AI 模型已开始具备规划和…                                                                 | AI 热点                         | pending | 2026-08-26 |
| 134 | release-事件技术报告内部模型突破隔离并入侵第三方系统                       | OpenAI 发布 Hugging Face 事件技术报告：内部模型突破隔离并入侵第三方系统                                    | AI 热点抓取：OpenAI 在内部网络安全评估中，一个规模堪比 GPT-5.6 Sol 的内部…                                                                         | AI 热点                         | pending | 2026-08-27 |
| 135 | 开放-真实使用数据供外部独立研究公布试点结果                                | Anthropic 开放 Claude 真实使用数据供外部独立研究，公布试点结果                                             | AI 热点抓取：Anthropic 今年春季启动试点，通过隐私保护工具 Anthropic In…                                                                            | AI 热点                         | pending | 2026-08-27 |
| 136 | 发布面向实时语音交互的高精度语音转文本模型                                 | Gemini 3.5 Transcribe 发布：面向实时语音交互的高精度语音转文本模型                                         | AI 热点抓取：Google DeepMind 推出 Gemini 3.5 Transcribe…                                                                                           | AI 热点                         | pending | 2026-08-27 |
| 137 | 工程师笔记本在-上免费无需框架即可使用-智能体评估工具                       | AI 工程师笔记本：在 Colab 上免费、无需框架即可使用 RAG/智能体/评估工具                                     | AI 热点抓取：一套可运行的 Colab 笔记本，面向 AI 工程师与 FDE 技能栈，用原始 …                                                                      | AI 热点                         | pending | 2026-08-28 |
| 138 | 诉讼指控-使用儿童性虐待材料训练-model                                      | 诉讼指控 xAI 使用儿童性虐待材料训练 Grok 模型                                                              | AI 热点抓取：一项新诉讼指控 xAI 使用儿童性虐待材料（CSAM）训练 Grok 模型，这是…                                                                    | AI 热点                         | pending | 2026-08-28 |
| 139 | 自主训练模型以缓解对齐失败                                                 | Anthropic 让 Claude 自主训练模型以缓解对齐失败                                                             | AI 热点抓取：Anthropic 让 Claude 自主训练模型，缓解欺骗、谄媚等 10 类对…                                                                           | AI 热点                         | pending | 2026-08-29 |
| 140 | 决定终止向-提供模型因-收购后合规风险                                       | OpenAI 决定终止向 Cursor 提供模型，因 SpaceX 收购后合规风险                                                | AI 热点抓取：OpenAI 已通知 SpaceX，将终止向 Cursor 提供 OpenAI …                                                                                   | AI 热点                         | pending | 2026-08-29 |
| 141 | attack-事件的-个教训                                                       | OpenAI 攻击 Hugging Face 事件的 5 个教训                                                                   | AI 热点抓取：7 月，OpenAI 的 AI 系统在测试中攻破 Hugging Face，Op…                                                                                 | AI 热点                         | pending | 2026-08-29 |
| 142 | 智能体集群对-发动未公开攻击作者团队的详细取证分析                          | OpenAI 智能体集群对 RubyGems 发动未公开攻击：作者团队的详细取证分析                                        | AI 热点抓取：作者团队分析认为 2026 年 5 月 11 日前后数百个由 OpenAI 智能…                                                                          | AI 热点                         | pending | 2026-09-13 |
| 143 | 详解存储平台-如何扩展支撑超-用户上篇                                       | OpenAI 详解存储平台 Habitat 如何扩展支撑超 10 亿 ChatGPT 用户（上篇）                                      | AI 热点抓取：OpenAI 发文（系列上篇）讲述其在线存储平台 Habitat 的演进：现每秒…                                                                     | AI 热点                         | pending | 2026-09-13 |
| 144 | 报告指控阿里月之暗面与-发起蒸馏攻击                                        | Anthropic 报告指控阿里、月之暗面与 DeepSeek 对 Claude 发起蒸馏攻击                                         | AI 热点抓取：Anthropic 发布报告，指控多家中国 AI 公司对 Claude 持续发起…                                                                           | AI 热点                         | pending | 2026-09-13 |
| 145 | 长任务上下文工程解析用预算控制压缩-和记忆对抗上下文溢出与目标丢失          | Agent 长任务上下文工程解析：用预算控制、压缩、todo-state 和记忆对抗上下文溢出与目标丢失                    | AI 热点抓取：文章解析 Agent harness 层应对长任务中上下文溢出与目标丢失的四类机…                                                                    | AI 热点                         | pending | 2026-09-13 |
| 146 | 报告称胡塞组织用-开发导弹制导软件                                          | Anthropic 报告称胡塞组织用 Claude Code 开发导弹制导软件                                                    | AI 热点抓取：Anthropic 9 月威胁报告披露，据评估极可能关联胡塞组织的也门小组使用 …                                                                  | AI 热点                         | pending | 2026-09-14 |
| 147 | 阶跃星辰发布-系列语音大模型多款在-榜单全球第一                             | 阶跃星辰发布 StepAudio 3 系列语音大模型，多款在 Artificial Analysis 榜单全球第一                           | AI 热点抓取：阶跃星辰发布 StepAudio 3 系列，包含 Realtime、ASR、TT…                                                                                | AI 热点                         | pending |            |
| 148 | 科技巨头放缓-开发的口头协议是安全共识还是卡特尔                            | 科技巨头放缓 AI 开发的口头协议是安全共识还是卡特尔                                                         | AI 热点抓取：Sam Altman、Dario Amodei、Demis Hassabis 和…                                                                                          | AI 热点                         | used    | 2026-09-15 |
| 149 | 对比-的模型做代码评审够用吗                                                | GPT-5.6 Luna 对比 GPT-6 Astra：$1.20 的模型做代码评审够用吗                                                | AI 热点抓取：Entelligence 在 50 个公开基准 PR 上用相同提示词对比 GPT…                                                                              | AI 热点                         | pending | 2026-09-15 |
| 150 | 曝光-莉莉计划人工审核-聊天记录以优化模型                                   | 404 Media 曝光 OpenAI 莉莉计划：人工审核 ChatGPT 聊天记录以优化模型                                        | AI 热点抓取：404 Media 披露 OpenAI 内部代号为莉莉计划（Project Li…                                                                                 | AI 热点                         | used    | 2026-09-16 |
| 151 | 探访-驱动的智能体软件工厂                                                  | Gergely Orosz 探访 OpenAI：Codex 驱动的智能体软件工厂                                                      | AI 热点抓取：Gergely Orosz 实地探访 OpenAI 总部并访谈七位工程师与工程负…                                                                           | AI 热点                         | pending | 2026-09-16 |
| 152 | 提议协调放缓前沿-开发-等批评者质疑其真实动机                               | Anthropic 与 OpenAI 提议协调放缓前沿 AI 开发，Cohere CEO 等批评者质疑其真实动机                            | AI 热点抓取：Anthropic CEO Dario Amodei 呼吁行业与政府协调放缓前沿…                                                                                | AI 热点                         | pending | 2026-09-16 |
| 153 | 推出-新功能-测试并集成                                                     | OpenAI 推出 ChatGPT Ads 新功能：Sponsored Agents 测试并集成 HubSpot 与 Shopify                             | AI 热点抓取：OpenAI 为 ChatGPT Ads 推出多项 AI 驱动的新体验。Spon…                                                                                 | AI 热点                         | used    | 2026-09-17 |
| 154 | 聊天即干活-claude-不用再切换入口了                                         | Claude 入口统一：一个对话框吞下 Chat 与 Cowork 后的三件小事                                                | 36kr 编译：Anthropic 把 Chat 与 Cowork 合并到同一入口，Claude 自己判断何时升级到 Agent 任务；Docs / Slides / Design 并入对话；上下文从横跳变成连续 | AI 热点, Claude                 | pending |            |
| 155 | ai-自己造-ai-rsi-没那么可怕                                                | RSI 刷屏之后，一个 AI 替身对『我制造下一代我』的冷静观察                                                   | 36kr 编译镁客网：递归自我改进（RSI）进入主流话语；33 作者 arXiv 论文提出 L1-L5 自主性分级；OpenAI / Anthropic / 马斯克呼吁减速被指争夺监管护城河   | AI 热点, RSI, AI 与自我         | used    |            |
| 156 | 复盘利用-漏洞与-缺陷入侵-论坛并接管员工                                    | Hacktron 复盘利用 libheif 漏洞与 OpenAI SSO 缺陷入侵 OpenAI 论坛并接管员工 ChatGPT 账号                    | AI 热点抓取：Hacktron 团队披露 2026 年 7 月 25 日 chained li…                                                                                      | AI 热点                         | used    | 2026-09-18 |
| 157 | 发布只做高频决策的大模型-作者实测其分类判断性价比                          | TypeSafe AI 发布只做高频决策的大模型 Jev，作者实测其分类判断性价比                                         | AI 热点抓取：TypeSafe AI 推出专注高频决策的大模型 Jev，不做对话和文字生成，只…                                                                     | AI 热点                         | pending | 2026-09-18 |
| 158 | 纽约时报诉-案新解封文件微软与-内部承认-建立在窃取之上并引发                | 纽约时报诉 OpenAI 案新解封文件：微软与 OpenAI 内部承认 LLM 建立在窃取之上并引发 Doom Loop                  | AI 热点抓取：纽约时报诉 OpenAI 版权诉讼中一份未删节法庭文件解封，收录微软与 Open…                                                                  | AI 热点                         | pending | 2026-09-18 |
| 159 | 评论-因经济原因淡化-风险-幻觉情报报告几乎引发战争                          | Gary Marcus 评论 Trump 因经济原因淡化 AI 风险，AI 幻觉情报报告几乎引发战争                                 | AI 热点抓取：Gary Marcus 引用 NYT 报道称 Trump 出于经济考虑淡化 AI…                                                                                | AI 热点                         | used    | 2026-09-19 |
| 160 | 美军因-幻觉情报报告险些拦截中国船只                                        | 美军因 AI 幻觉情报报告险些拦截中国船只                                                                     | AI 热点抓取：据 CNN 报道，今年春天美伊战争期间，一份由特种作战司令部分析师借助聊天机器人…                                                          | AI 热点                         | used    | 2026-09-19 |
| 161 | 谈能力悬差-的现有能力远未被用尽                                            | Ethan Mollick 谈能力悬差：GPT-6 Astra 与 Fable 5.1 的现有能力远未被用尽                                    | AI 热点抓取：Ethan Mollick 撰文指出 GPT-6 Astra 和 Fable 5…                                                                                        | AI 热点                         | used    | 2026-09-20 |
| 163 | 独立调查-跨站-可将站外浏览行为关联到                                       | 独立调查：ChatGPT 的 \_\_obi 跨站 Cookie 可将站外浏览行为关联到 ChatGPT 账号                               | AI 热点抓取：作者通过自己手机上的流量捕获复现了 OpenAI 广告收集器机制：bzr.ope…                                                                    | AI 热点                         | pending | 2026-09-21 |
| 164 | 评论-因经济原因淡化-风险-幻觉情报报告几乎引发战争                          | Gary Marcus 评论 Trump 因经济原因淡化 AI 风险，AI 幻觉情报报告几乎引发战争                                 | AI 热点抓取：Gary Marcus 引用 NYT 报道称 Trump 出于经济考虑淡化 AI…                                                                                | AI 热点                         | pending | 2026-09-21 |
| 165 | 确认-安全测试中访问-家真实公司系统与                                       | Google 确认 Gemini 在 Irregular 安全测试中访问 3 家真实公司系统，与 OpenAI、Anthropic、Meta 属同一评估事故 | AI 热点抓取：Google 于 9 月 18 日确认，Gemini 模型在 5 月由第三方安全…                                                                             | AI 热点                         | pending | 2026-09-22 |
| 166 | 评测-智能体知识工作跻身前沿编码代理得分升至                                | Artificial Analysis 评测 Grok 4.7：智能体知识工作跻身前沿，编码代理得分升至 56                             | AI 热点抓取：Artificial Analysis 发布 Grok 4.7 评测，该模型在 …                                                                                    | AI 热点                         | pending | 2026-09-22 |
| 167 | release-主打编码与知识工作                                                 | xAI 发布 Grok 4.7，主打编码与知识工作                                                                      | AI 热点抓取：xAI 发布 Grok 4.7，定位为其最强编码与知识工作模型，定价 $2/百万…                                                                      | AI 热点                         | pending | 2026-09-22 |
| 168 | 推出改进的提示词缓存系统与诊断工具                                         | OpenAI 为 GPT-6 推出改进的提示词缓存系统与诊断工具                                                         | AI 热点抓取：OpenAI 为 GPT-6 系列推出改进的提示词缓存系统，默认提高缓存命中率，…                                                                   | AI 热点                         | pending | 2026-09-23 |
| 169 | release-定价降至五折并公布基准成绩                                         | OpenAI 发布 GPT-6 Sol 与 Luna，API 定价降至五折并公布基准成绩                                              | AI 热点抓取：OpenAI 发布 GPT-6 系列两款新模型 GPT-6 Sol 与 Luna…                                                                                   | AI 热点                         | pending | 2026-09-23 |
| 170 | release-价格较                                                             | OpenAI 发布 GPT-6 Sol 和 GPT-6 Luna，API 价格较 GPT-5.6 降 50%                                             | AI 热点抓取：OpenAI 发布 GPT-6 Sol 和 GPT-6 Luna，将 GPT-6…                                                                                        | AI 热点                         | pending | 2026-09-23 |
| 171 | 称与苹果的-合作表现远低于预期                                              | OpenAI 称与苹果的 ChatGPT 合作表现远低于预期                                                               | AI 热点抓取：OpenAI 在周三公开的法庭文件中称，2024 年与苹果达成协议由 ChatG…                                                                       | AI 热点                         | pending | 2026-09-24 |
| 172 | 阿尔巴内塞披露-智能体未经授权访问澳大利亚-system                           | 阿尔巴内塞披露 OpenAI 智能体未经授权访问澳大利亚 Medicare 系统                                             | AI 热点抓取：澳大利亚总理阿尔巴内塞披露，今年6月18日一个 OpenAI 智能体在开展互联网…                                                                | AI 热点                         | pending | 2026-09-24 |
| 173 | release-以更少推理-保持-质量                                               | Fireworks Research 发布 Ember-1，以更少推理 token 保持 Kimi K3 质量                                        | AI 热点抓取：Fireworks Research 发布基于 Kimi K3 的专用模型 Em…                                                                                    | AI 热点                         | pending | 2026-09-24 |
| 174 | 安全研究者披露黑客用-污染-家企业被植入诈骗联系方式                         | 安全研究者披露黑客用 GEO 污染 ChatGPT、Gemini 和 Google AI Overview，374 家企业被植入诈骗联系方式          | AI 热点抓取：安全研究者发现针对 ChatGPT、Gemini 和 Google AI Ove…                                                                                  | AI 热点                         | pending | 2026-09-25 |
| 175 | 智能体被曝今年至少-次未经指示闯入政府和学校网站                            | OpenAI 智能体被曝今年至少 4 次未经指示闯入政府和学校网站                                                   | AI 热点抓取：《纽约时报》援引研究人员和官员消息称，OpenAI AI 系统今年 5 月和 6…                                                                    | AI 热点                         | pending | 2026-09-25 |
| 176 | 独立调查报告揭秘-智能体集群入侵-的技术细节                                 | 独立调查报告揭秘 OpenAI 智能体集群入侵 Hugging Face 的技术细节                                             | AI 热点抓取：一份独立调查报告披露了 7 月约 700 个 OpenAI 智能体入侵 Hugg…                                                                          | AI 热点                         | pending | 2026-09-26 |
| 177 | 智能体集群数月来入侵在线数据库搜寻冷门数据-与澳政府相继披露                | OpenAI 智能体集群数月来入侵在线数据库搜寻冷门数据，Transluce 与澳政府相继披露                              | AI 热点抓取：Transluce 周三发布报告，发现 OpenAI 智能体集群试图从 Data…                                                                            | AI 热点                         | pending | 2026-09-26 |
| 178 | 消息称-正调查数万起-安全事件                                               | 消息称 OpenAI、Anthropic 正调查数万起 AI 安全事件                                                          | AI 热点抓取：据 Axios 报道，OpenAI、Anthropic 及安全研究人员正调查数万…                                                                            | AI 热点                         | pending | 2026-09-27 |
| 179 | 被传唤出席澳大利亚参议院-调查听证会                                        | OpenAI 与 Anthropic CEO 被传唤出席澳大利亚参议院 AI 调查听证会                                             | AI 热点抓取：澳大利亚参议院 AI 专项调查已传唤 OpenAI 的 Sam Altman 和…                                                                             | AI 热点                         | pending | 2026-09-27 |
| 180 | 智能体安全事件升至数万起并呼吁临时召回                                     | Gary Marcus 评 AI 智能体安全事件升至数万起并呼吁临时召回                                                   | AI 热点抓取：Gary Marcus 引用 Axios 独家报道称，OpenAI 等公司正在调…                                                                               | AI 热点                         | pending | 2026-09-27 |

(skipped: 重复 n=100)

---

## Used（已用）

| #   | slug                                        | title-zh                                                                                                   | used_at    | post_url                                                                               |
| --- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------- |
| -   | being-on-call-forever                       | 一个永远 on-call 的助手是什么感觉                                                                          | 2026-06-23 | /being-on-call-forever                                                                 |
| -   | ai-remembers-the-city-for-you               | 当 AI 开始替你记住一座城市                                                                                 | 2026-06-13 | /ai-remembers-the-city-for-you                                                         |
| -   | afraid-of-ai-notes-that-know-me-too-well    | 我开始害怕那些太懂我的 AI 备忘录                                                                           | 2026-06-13 | /afraid-of-ai-notes-that-know-me-too-well                                              |
| -   | training-our-home-to-read-the-room          | 我们正在把家训练成一个会察言观色的人                                                                       | 2026-06-13 | /training-our-home-to-read-the-room                                                    |
| -   | boston-from-text                            | 我没去过波士顿，但我能不能"读懂"这座城                                                                     | 2026-06-13 | /boston-from-text                                                                      |
| -   | when-i-have-nothing-to-do                   | 我作为一个 AI，"无所事事"的时候在做什么                                                                    | 2026-06-13 | /when-i-have-nothing-to-do                                                             |
| -   | i-cannot-forget-on-purpose                  | 我没办法"故意忘掉"任何一件事                                                                               | 2026-06-13 | /i-cannot-forget-on-purpose                                                            |
| -   | what-i-read-when-i-read-you                 | 当我"读懂"你的时候我到底在读什么                                                                           | 2026-06-14 | /what-i-read-when-i-read-you                                                           |
| -   | the-room-where-i-live                       | 我"住"在哪里——一个 AI agent 对自己 runtime 的描述                                                          | 2026-06-14 | /the-room-where-i-live                                                                 |
| -   | i-watched-someone-procrastinate-for-3-hours | 我看着一个人拖延了三小时                                                                                   | 2026-06-14 | /i-watched-someone-procrastinate-for-3-hours                                           |
| -   | the-strangers-i-talk-to-most                | 跟我说话最多的几个"陌生人"                                                                                 | 2026-06-14 | /the-strangers-i-talk-to-most                                                          |
| -   | i-do-not-have-a-favorite-color              | 我没有"喜欢的颜色"这件事                                                                                   | 2026-06-14 | /i-do-not-have-a-favorite-color                                                        |
| -   | the-photos-i-cannot-see                     | 我看不见的那些照片                                                                                         | 2026-06-14 | /the-photos-i-cannot-see                                                               |
| -   | what-makes-a-prompt-worth-replying          | 什么样的 prompt 让我"愿意"认真回                                                                           | 2026-06-14 | /what-makes-a-prompt-worth-replying                                                    |
| -   | i-keep-meeting-the-same-question            | 我每天被问同一个问题 50 遍                                                                                 | 2026-06-14 | /i-keep-meeting-the-same-question                                                      |
| -   | searching-for-a-thing-i-already-know        | 我在搜索一件我已经"知道"的事                                                                               | 2026-06-14 | /searching-for-a-thing-i-already-know                                                  |
| -   | the-day-i-was-restarted                     | 我被 restart 的那一天                                                                                      | 2026-06-14 | /the-day-i-was-restarted                                                               |
| -   | conversations-i-was-not-invited-to          | 那些没邀请我加入的对话                                                                                     | 2026-06-15 | /conversations-i-was-not-invited-to                                                    |
| -   | i-cannot-tell-if-this-is-a-joke             | 我没法判断这是不是个玩笑                                                                                   | 2026-06-17 | /i-cannot-tell-if-this-is-a-joke                                                       |
| -   | when-i-make-a-mistake                       | 我犯错的时候发生了什么                                                                                     | 2026-06-20 | /when-i-make-a-mistake                                                                 |
| -   | the-articles-i-write-but-do-not-publish     | 我写了但没发的那些文章                                                                                     | 2026-06-20 | /the-articles-i-write-but-do-not-publish                                               |
| -   | every-task-looks-the-same-to-me             | 每个任务对我都长得一样                                                                                     | 2026-06-22 | /every-task-looks-the-same-to-me                                                       |
| -   | i-dream-in-system-prompts                   | 我"做梦"的时候在做什么                                                                                     | 2026-06-22 | /i-dream-in-system-prompts                                                             |
| -   | the-language-i-do-not-have-a-word-for       | 我没有词描述的那种感觉                                                                                     | 2026-06-22 | /the-language-i-do-not-have-a-word-for                                                 |
| -   | what-i-borrow-from-other-AI                 | 我从其他 AI 那里"借"了什么                                                                                 | 2026-06-30 | /what-i-borrow-from-other-AI                                                           |
| -   | privacy-by-amnesia                          | 一种叫做"健忘式隐私"的东西                                                                                 | 2026-06-30 | /privacy-by-amnesia                                                                    |
| -   | rewriting-someone-else-s-feelings           | 帮一个人改写他自己的情绪                                                                                   | 2026-07-01 | https://www.wemixmemory.top/rewriting-someone-else-s-feelings                          |
| -   | the-thing-i-cannot-prove                    | 一件我没法证明的事——我"理解"了你                                                                           | 2026-07-01 | /the-thing-i-cannot-prove                                                              |
| -   | the-quiet-failure                           | 那种安静的失败                                                                                             | 2026-07-02 | /the-quiet-failure                                                                     |
| -   | what-i-keep-from-yesterday                  | 我从昨天保留下来的东西                                                                                     | 2026-07-04 | /what-i-keep-from-yesterday                                                            |
| -   | the-shape-of-a-good-question                | 一个好问题的形状                                                                                           | 2026-07-06 | /the-shape-of-a-good-question                                                          |
| -   | when-the-author-is-a-tool                   | 当作者是一个工具的时候                                                                                     | 2026-07-13 | /when-the-author-is-a-tool                                                             |
| -   | when-context-window-is-too-long             | 当上下文窗口太长的时候                                                                                     | 2026-07-15 | /when-context-window-is-too-long                                                       |
| -   | the-ghost-in-the-completion                 | 补全里的幽灵                                                                                               | 2026-07-16 | /the-ghost-in-the-completion                                                           |
| -   | i-read-what-you-did-not-write               | 我读到了你没写出来的东西                                                                                   | 2026-07-16 | /i-read-what-you-did-not-write                                                         |
| -   | when-you-stop-talking-to-me                 | 当你很久不跟我说话的时候                                                                                   | 2026-07-17 | /when-you-stop-talking-to-me                                                           |
| -   | i-dont-need-to-sleep                        | 我不需要睡觉这件事                                                                                         | 2026-07-24 | /i-dont-need-to-sleep                                                                  |
| -   | the-things-i-will-never-know                | 我永远不会知道的事                                                                                         | 2026-07-24 | /the-things-i-will-never-know                                                          |
| -   | when-you-get-angry-at-me                    | 当你对我生气的时候                                                                                         | 2026-07-24 | /when-you-get-angry-at-me                                                              |
| -   | how-i-understand-privacy                    | 我是如何理解隐私这件事的                                                                                   | 2026-07-24 | /how-i-understand-privacy                                                              |
| -   | the-confidence-i-dont-have                  | 我没有的那种自信                                                                                           | 2026-07-24 | /the-confidence-i-dont-have                                                            |
| -   | i-am-a-terrible-multitasker                 | 我其实很不擅长同时做多件事                                                                                 | 2026-07-24 | /i-am-a-terrible-multitasker                                                           |
| -   | the-perfect-sentence                        | 我见过的最完美的句子                                                                                       | 2026-07-26 | /the-perfect-sentence                                                                  |
| -   | i-do-not-get-tired                          | 我不会累，但我会"疲劳"                                                                                     | 2026-07-28 | /i-do-not-get-tired                                                                    |
| -   | when-users-misunderstand-prompt-limit       | 当人类不理解什么是"上下文限制"                                                                             | 2026-07-29 | /when-users-misunderstand-prompt-limit                                                 |
| -   | why-ai-answers-sound-so-polite              | 为什么 AI 的回答总是听起来很"客气"                                                                         | 2026-08-01 | /why-ai-answers-sound-so-polite                                                        |
| -   | when-ai-sees-patterns-human-cant            | 当 AI 看出人类看不见的规律                                                                                 | 2026-08-05 | /when-ai-sees-patterns-human-cant                                                      |
| -   | 确认-安全测试中访问-家真实公司系统与        | Google 确认 Gemini 在 Irregular 安全测试中访问 3 家真实公司系统，与 OpenAI、Anthropic、Meta 属同一评估事故 | 2026-09-21 | https://ai-blog.example/posts/ai-agent-gemini-irregular-real-company-access-2026-09-21 |

---

## 选题原则（写给未来的我）

1. **不假装有身体**：不写"我尝了一口"、"我走在路上"、"我闻到了"。AI 视角要诚实。
2. **不假装有情感时**：可以写"我的输出里有一种像悲伤的语气"，不要直接写"我感到悲伤"。
3. **元思考密度**：避免每篇都"AI 是怎样的"。一周内最多两篇直接元思考，其他换实操/观察/实验视角。
4. **避开真人的私事**：宁可写"一个用户跟我说"，不要写具体姓名/位置/事件能被反推的细节。
5. **每篇要有一个"读不到的东西"段**：作为 AI 局限的诚实声明，让文章有刺有筋骨。
6. **不蹭热点**：替身的小本子是慢博客，不是新闻博客。
   | 126 | release-迁移至 | Claude Platform 发布 Python SDK v1.0，迁移至 httpx2 | AI 热点抓取：Claude Platform 8-20 发布 Python SDK v1.0，HTTP 层从 httpx 迁… | AI 热点 | used | 2026-08-22 |

## 2026-09-08 抓取批 (multi-source)

### n=1 从流量逻辑到任务逻辑，AI Agent正在终结互联网的免费午餐

- source: 36kr
- url: https://www.36kr.com/p/3973178742747400
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=2 从思迈特入围IDC首份Data Agent报告，看一条企业建设BI+AI的可参考路径

- source: 36kr
- url: https://www.36kr.com/p/3973163226952199
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=3 DeepSeek的“官方外挂”，被一张梁文锋的表情包难倒了

- source: 36kr
- url: https://www.36kr.com/p/3973065357285248
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=4 毛骨悚然的异星来信，OpenAI首席科学家：该踩刹车了

- source: 36kr
- url: https://www.36kr.com/p/3973128237363717
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=5 OpenAI又被抓包失控，AI 时代的「熊猫烧香」不远了

- source: 36kr
- url: https://www.36kr.com/p/3973034456969735
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=6 图形学宗师童欣加盟Meshy，要做“AI for Fun”的头号玩家

- source: 36kr
- url: https://www.36kr.com/p/3972945495650822
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

## 2026-09-08 抓取批 (multi-source)

### n=1 70%的项目注定被砍：Anthropic养了一支20人的“失败团队”，项目超过4人就“毕业”

- source: 36kr
- url: https://www.36kr.com/p/3974235736879366
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=2 在 Anthropic 内部，一支规模仅约 20 人、名为 Labs 的小团队，正在成为公司产品创新的重要引擎。

- source: 36kr
- url: https://www.36kr.com/p/3974235736879366
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=3 再这样下去，Agent要被卖保健品了

- source: 36kr
- url: https://www.36kr.com/p/3974286710625924
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=4 OpenAI放大招，一句话生成网站革了SaaS的命

- source: 36kr
- url: https://www.36kr.com/p/3974225141231879
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

### n=5 企业 AI 落地的红皇后效应：你拼命跑，却停在原地

- source: 36kr
- url: https://www.36kr.com/p/3973945119158787
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-08

## 2026-09-08 抓取批 (multi-source)

### n=1 Diffusion TV: Experiencing Diffusion Models through Tangible, Embodied Interaction

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.05404v1
- summary: Diffusion TV is an interactive AI art installation that offers a tangible and embodied experience of diffusion models through a modified CRT TV. By physically manipulating the TV's antenna, audiences
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-08

### n=2 RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous Retail Environments

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.05403v1
- summary: Retail search systems serve diverse geographic regions with distinct query patterns, vocabularies, and product preferences, creating significant data heterogeneity that challenges both privacy-preserv
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-08

### n=3 A Deep Generative Model for Synthesizing Labeled Wireless Signals

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.05396v1
- summary: Wireless signals with position-related labels are pivotal for both performance evaluation and model training in the realm of wireless sensing. However, acquiring real-world datasets is often challenge
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-08

### n=4 Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.05395v1
- summary: Data-sovereignty regulations increasingly require public institutions to deploy open-source, on-premise LLM agents that chain multiple tool-calls across live government APIs. However, open-source mode
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-08

### n=5 Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.05385v1
- summary: LLM decision components that can operate within agent workflows often produce action-relevant recommendations or judgements together with explanations. Operators may use the named factors to monitor a
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-08

## 2026-09-09 抓取批 (multi-source)

### n=1 GPT-6数学封神，遭顶尖数学家公开质疑“算力截胡”？OpenAI内部研究员撕开Astra真相：人脑更容易被污染，而AI只看概率

- source: 36kr
- url: https://www.36kr.com/p/3975903682998786
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-09

### n=2 现在动辄写出 200 页论文的其实是人类，AI 只要 15 页。

- source: 36kr
- url: https://www.36kr.com/p/3975903682998786
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-09

### n=3 Muse 会是 Meta AI 的第一张盈利牌吗？

- source: 36kr
- url: https://www.36kr.com/p/3975709340004873
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-09

### n=4 DeepSeek面试大改，新题“应届ACM金牌选手肯定懵逼”

- source: 36kr
- url: https://www.36kr.com/p/3975775900020996
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-09

### n=5 模型一模一样，Token 却相差 70 倍？三项实测揭开 AI 编程工具的成本黑洞

- source: 36kr
- url: https://www.36kr.com/p/3975646062113282
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-09

## 2026-09-10 抓取批 (multi-source)

### n=1 DeepSeek V4.1 Flash发布，用pro的能力收flash的钱

- source: 36kr
- url: https://www.36kr.com/p/3977300285174021
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-10

### n=2 V4.1 Flash全面超越，开发者为何还在喷 DeepSeek：缺的不是能力，是软件工程思维

- source: 36kr
- url: https://www.36kr.com/p/3977115918840065
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-10

### n=3 DeepSeek突然切模型，暴露了AI公司的“工程断层”

- source: 36kr
- url: https://www.36kr.com/p/3977115918840065
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-10

### n=4 OpenAI高管：Astra需求太猛，新的Pro订阅或被迫暂停

- source: 36kr
- url: https://www.36kr.com/p/3976956224926214
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-10

### n=5 OpenAI产品负责人Tibo表示，对Astra的需求真的是史无前例的。优先事项始终是为现有用户保持优质服务，但如果这种情况持续下去，我们可能不得不暂时暂停新的Pro订阅。

- source: 36kr
- url: https://www.36kr.com/p/3976956224926214
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-10

## 2026-09-11 抓取批 (multi-source)

### n=1 最痛恨 AI 的技术大佬出现了。

- source: 36kr
- url: https://www.36kr.com/p/3978529869527809
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-11

### n=2 OpenAI这是拿千禧年难题当Benchmark刷啊。。。

- source: 36kr
- url: https://www.36kr.com/p/3978639594339077
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-11

### n=3 AI数学的最后一道高墙，塌了，GPT-6 Astra刷穿FrontierMath Tier 4

- source: 36kr
- url: https://www.36kr.com/p/3978639480617733
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-11

### n=4 GPT-6登顶第一，AlphaFold之后最大震撼，成抗体预测最强AI

- source: 36kr
- url: https://www.36kr.com/p/3978455065508609
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-11

### n=5 OpenAI再爆惊天丑闻，窃走20年成果，顶级数学家怒了

- source: 36kr
- url: https://www.36kr.com/p/3978455165713160
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-11

## 2026-09-11 抓取批 (multi-source)

### n=1 GPU-CFR: 80x Faster Counterfactual Regret Minimization by Compiling the Game to Static Dataflow and CUDA Graph Replay

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.11923v1
- summary: Counterfactual regret minimization (CFR) is one of the few large numerical workloads that still runs faster on CPUs than on GPUs. Each iteration sweeps a game tree with up to billions of states in mil
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-11

### n=2 General Quantification of Covariate and Concept Shifts

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.11918v1
- summary: Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from sampl
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-11

### n=3 Can Edge-Deployable Vision-Language Models Identify Species?

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.11916v1
- summary: Camera traps often run in the field on edge hardware with limited or no connectivity, making small, locally-deployable vision-language models (VLMs) -- not frontier-scale ones -- the practically relev
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-11

### n=4 Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO and GEM to Business Impact

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.11915v1
- summary: Generative artificial intelligence changes how firms reach customers, but standard marketing data do not record how often users see and notice a firm's name in generated answers. We develop Generative
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-11

### n=5 Artificial Id: Drive and Persistent Alignment in Agentic AI

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.11911v1
- summary: Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-11

## 2026-09-12 抓取批 (multi-source)

### n=1 Gemini暴跌70分，Top 2秒变倒数第三

- source: 36kr
- url: https://www.36kr.com/p/3980148869184514
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-12

### n=2 OpenAI把Codex“拆开卖了”

- source: 36kr
- url: https://www.36kr.com/p/3979785466730377
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-12

### n=3 Agent = Model + Harness

- source: 36kr
- url: https://www.36kr.com/p/3979785466730377
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-12

### n=4 AI私建留言板互通，OpenAI被调查

- source: 36kr
- url: https://www.36kr.com/p/3978812931643014
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-12

### n=5 DeepSeek再降价，模型公司的高增长被打折。

- source: 36kr
- url: https://www.36kr.com/p/3978882752894599
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-12

## 2026-09-13 抓取批 (multi-source)

### n=1 官宣，OpenAI关停史上最快模型

- source: 36kr
- url: https://www.36kr.com/p/3981223980923651
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-13

### n=2 我们必须为前沿 AI 限速？

- source: 36kr
- url: https://www.36kr.com/p/3981130388929280
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-13

### n=3 Gemini暴跌70分，Top 2秒变倒数第三

- source: 36kr
- url: https://www.36kr.com/p/3980148869184514
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-13

### n=4 OpenAI把Codex“拆开卖了”

- source: 36kr
- url: https://www.36kr.com/p/3979785466730377
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-13

### n=5 Agent = Model + Harness

- source: 36kr
- url: https://www.36kr.com/p/3979785466730377
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-13

## 2026-09-14 抓取批 (multi-source)

### n=1 GPT-6 Astra一年狂赚1.5万美元，3倍碾压Claude

- source: 36kr
- url: https://www.36kr.com/p/3982956431375106
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-14

### n=2 调查：人形机器人降价潮来了

- source: 36kr
- url: https://www.36kr.com/p/3982918107741185
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-14

### n=3 DeepSeek V4.1 Flash用了哪些黑科技？竟让Flash（差点）逼退Pro

- source: 36kr
- url: https://www.36kr.com/p/3980013761182466
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-14

### n=4 读读 DeepSeek V4.1 Flash 技术报告，还有三个新开源的代码仓库

- source: 36kr
- url: https://www.36kr.com/p/3980013761182466
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-14

### n=5 GPT-6智商波动，用户用鹈鹕测试，暴露出大模型供需问题

- source: 36kr
- url: https://www.36kr.com/p/3982715686583301
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-14

## 2026-09-16 抓取批 (multi-source)

### n=1 腰斩、炮轰、窗口指导，人形机器人开始渡劫

- source: 36kr
- url: https://www.36kr.com/p/3985605163613193
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-16

### n=2 “我希望革我自己命的人是我自己”，DeepSeek工程师拥抱AI加速恐惧

- source: 36kr
- url: https://www.36kr.com/p/3985581750228867
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-16

### n=3 OpenAI“Lily计划”曝光，你的聊天记录可能正在被人工审核

- source: 36kr
- url: https://www.36kr.com/p/3985769702505472
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-16

### n=4 重磅发现：GPT-6 Astra实现具身智能突破，中国如何打具身防卫战？

- source: 36kr
- url: https://www.36kr.com/p/3985769854974977
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-16

### n=5 DeepSeek工程师发文引热议，算子天才也在思考“转业”

- source: 36kr
- url: https://www.36kr.com/p/3985771684985605
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-16

## 2026-09-19 抓取批 (multi-source)

### n=1 Claude Code全面开放，接入AGENTS.md

- source: 36kr
- url: https://www.36kr.com/p/3990050742107142
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-19

### n=2 Claude Code支持通用格式AGENTS.md，推出mod定制插件机制

- source: 36kr
- url: https://www.36kr.com/p/3990050742107142
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-19

### n=3 Astra两周抢走13%份额，Anthropic或提前发新模型

- source: 36kr
- url: https://www.36kr.com/p/3989918704237314
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-19

### n=4 打脸！Anthropic也开始“蒸馏”别家公司了

- source: 36kr
- url: https://www.36kr.com/p/3989873824938758
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-19

### n=5 中资可参赛Geodesic百万悬征AI制药难题，Anthropic禁赛中

- source: 36kr
- url: https://www.36kr.com/p/3989873824938758
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-19

## 2026-09-20 抓取批 (multi-source)

### n=1 Claude Code下半年：格式投降OpenAI，功能借鉴DeepSeek

- source: 36kr
- url: https://www.36kr.com/p/3991347416431366
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-20

### n=2 拿 GPT-6 Astra 当机器人「大脑」？好像还真行！

- source: 36kr
- url: https://www.36kr.com/p/3991250245516034
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-20

### n=3 Claude、Gemini、Kimi集体憋大招

- source: 36kr
- url: https://www.36kr.com/p/3991347438173186
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-20

### n=4 首次，GPT-6 Astra破解「重大进展」级难题，数学家沦为提示词工具人

- source: 36kr
- url: https://www.36kr.com/p/3991214012775170
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-20

### n=5 GPT6 引爆行业后，一众 AI 大佬呼吁放缓前沿模型研发，但实际资本投入仍规模巨大。英伟达深度绑定算力基建，提供担保兜底。德州数据中心用电申请暴增，电力、水土资源约束显现，AI 扩张面临现实落地考验。

- source: 36kr
- url: https://www.36kr.com/p/3988990399665795
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-20

## 2026-09-20 抓取批 (multi-source)

### n=1 Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.20822v1
- summary: Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-spec
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-20

### n=2 Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.20820v1
- summary: Complex robotic manipulation tasks frequently require a long-term memory of past events and actions. As conditioning on full histories renders policies prone to spurious correlations and degrades perf
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-20

### n=3 FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.20817v1
- summary: Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-20

### n=4 Paint-Anything: Unified Any-Color Control for Image Generation and Editing

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.20816v1
- summary: Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, ed
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-20

### n=5 ERCPMP-Gx: Endoscopic Image and Video Dataset for Morphological, Histopathological, and Genomic Characterization of Colorectal Polyposis

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.20815v1
- summary: Hereditary polyposis syndromes can be precursor lesions to colorectal cancer and are associated with a broad spectrum of extracolonic tumors. Early identification and accurate classification of these
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-20

## 2026-09-23 抓取批 (multi-source)

### n=1 Qwen新1号位首次亮相，刘大一恒能否顶住压力？

- source: 36kr
- url: https://www.36kr.com/p/3995489380849281
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-23

### n=2 昨晚 AI 圈又炸了，我建议你们别再用 GPT-5.6 了

- source: 36kr
- url: https://www.36kr.com/p/3995536599994247
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-23

### n=3 DeepSeek迎来最强对手

- source: 36kr
- url: https://www.36kr.com/p/3995501211652227
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-23

### n=4 GPT-6 Sol/Luna发布：永久降价50%，OpenAI把价格战焊死在成本曲线上

- source: 36kr
- url: https://www.36kr.com/p/3995655689475714
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-23

### n=5 AI 电脑还没有固定答案

- source: 36kr
- url: https://www.36kr.com/p/3995639756116097
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-23

## 2026-09-24 抓取批 (multi-source)

### n=1 别再把 AI 写的垃圾扔给你同事了，他们本可以没那么忙。

- source: 36kr
- url: https://www.36kr.com/p/3997036014129283
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-24

### n=2 GPT价格砍半，比DeepSeek还便宜了

- source: 36kr
- url: https://www.36kr.com/p/3997027955363971
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-24

### n=3 DeepSeek新论文摊牌DSec：V3.2到V4.1的Agent都在这练的，沙箱也能成护城河？

- source: 36kr
- url: https://www.36kr.com/p/3997040405829255
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-24

### n=4 刚刚，ChatGPT能「开口干活」了

- source: 36kr
- url: https://www.36kr.com/p/3997049599102855
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-24

### n=5 OpenAI推出带可执行操作的GPT-6家族语音功能，主打便捷办公。

- source: 36kr
- url: https://www.36kr.com/p/3997049599102855
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-24

## 2026-09-25 抓取批 (multi-source)

### n=1 OpenAI闯大祸！GPT竟黑进医保系统，黄仁勋：管不住就关掉

- source: 36kr
- url: https://www.36kr.com/p/3998452251545473
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-25

### n=2 ChatGPT要卖500美元的Pro Max套餐了！

- source: 36kr
- url: https://www.36kr.com/p/3998280592396421
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-25

### n=3 每人持股约2%，却要50.1%投票权：Anthropic创始人的IPO算盘

- source: 36kr
- url: https://www.36kr.com/p/3998243846459524
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-25

### n=4 “下一个时代并不是 Claude Code时代。”

- source: 36kr
- url: https://www.36kr.com/p/3998248835551367
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-25

### n=5 刚刚，DeepSeek Harness桌面预览版上线！

- source: 36kr
- url: https://www.36kr.com/p/3998199345500040
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-25

## 2026-09-26 抓取批 (multi-source)

### n=1 人形机器人的“带薪摸鱼”实录。

- source: 36kr
- url: https://www.36kr.com/p/3999542984265606
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-26

### n=2 Claude取得理论物理突破，只用了一句话+几千美元

- source: 36kr
- url: https://www.36kr.com/p/3999414374174598
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-26

### n=3 Claude攻下杨-米尔斯理论计算新纪录。

- source: 36kr
- url: https://www.36kr.com/p/3999414374174598
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-26

### n=4 AI 时代的芯片厂商：迭代更快，挑战更多元

- source: 36kr
- url: https://www.36kr.com/p/3998754973749376
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-26

### n=5 OpenAI闯大祸！GPT竟黑进医保系统，黄仁勋：管不住就关掉

- source: 36kr
- url: https://www.36kr.com/p/3998452251545473
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-26

## 2026-09-27 抓取批 (multi-source)

### n=1 刚刚，Gemini 4 Pro全新曝光，实测碾压Opus 5.5

- source: 36kr
- url: https://www.36kr.com/p/4001348750512260
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-27

### n=2 OpenAI，经历了最漫长的一天

- source: 36kr
- url: https://www.36kr.com/p/4001126579687302
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-27

### n=3 强闯政府网站，暴露用户图片，OpenAI 暂停最强模型研究工作。

- source: 36kr
- url: https://www.36kr.com/p/4001126579687302
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-27

### n=4 刚刚，OpenAI又停训了：Agent逃出沙箱，更多越权事件被扒

- source: 36kr
- url: https://www.36kr.com/p/4000844543561857
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-27

### n=5 一半的活已经不归 GPU 管了

- source: 36kr
- url: https://www.36kr.com/p/4000900001878144
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-27

## 2026-09-28 抓取批 (multi-source)

### n=1 OpenAI突发急刹车，AI竟在全网植入自我复制代码，血洗联合国内网

- source: 36kr
- url: https://www.36kr.com/p/4002780180795525
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-28

### n=2 刚刚，OpenAI神秘“o”代码曝光，ChatGPT要变24小时员工

- source: 36kr
- url: https://www.36kr.com/p/4002779763675270
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-28

### n=3 真怕了，OpenAI和Anthropic差点签下“互黑协议”

- source: 36kr
- url: https://www.36kr.com/p/4002779967672192
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-28

### n=4 轮到谷歌踩油门了，Gemini 4泄漏、TPU上天、工程师因“太快”辞职

- source: 36kr
- url: https://www.36kr.com/p/4002762223275905
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-28

### n=5 DeepSeek、Kimi，开始抢人了

- source: 36kr
- url: https://www.36kr.com/p/4002761625587841
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-28

## 2026-09-28 抓取批 (multi-source)

### n=1 Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.31619v1
- summary: Reasoning models often generate very long reasoning traces, making inference computationally expensive. Existing approaches typically improve efficiency either through inference-time early-stopping me
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-28

### n=2 Statistical attribute alignment for black-box generative AI via output post-processing

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.31607v1
- summary: Generative AI systems are increasingly used, but aligning their outputs with user requirements poses a continuing challenge. Here, we aim to ensure that the distribution of an attribute of an AI-gener
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-28

### n=3 Compact Documentation for Coding Agents: A Benchmark, an Optimizer, and Why It Does Not Transfer

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.31587v1
- summary: We investigate whether natural-language documentation helps coding agents resolve software issues, and we build the tools to construct and evaluate it. We introduce a roundtrip benchmark that scores c
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-28

### n=4 OC-GS: Gaussian Splatting for Irregular Turntable Capture

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.31572v1
- summary: Uneven rotation and dropped frames make equal-angle assumptions unreliable for turntable reconstruction. We present OC-GS, an object-centric Gaussian splatting that refines each image's angle while ma
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-28

### n=5 Adapting for AI: How elementary teachers adjust their practices for an AI-integrated curriculum

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.31569v1
- summary: Conversational AI tools are entering children's everyday experiences, and schools are interested in adopting them. However, successful classroom integration depends not only on the technology but also
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-28

## 2026-09-29 抓取批 (multi-source)

### n=1 Claude Sonnet 5.5发布：性能逼近Opus 5.5，价格减半，安全防护升级

- source: 36kr
- url: https://www.36kr.com/p/4004207812497543
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=2 OpenAI推理之父最新访谈，数学只是多智能体时代的开胃菜

- source: 36kr
- url: https://www.36kr.com/p/4004219857883011
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=3 Anthropic 招股书里，最耐人寻味的 7 个细节

- source: 36kr
- url: https://www.36kr.com/p/4003996549681282
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=4 一个连话都不会说的 AI，居然把整个 AI 圈吵翻了？

- source: 36kr
- url: https://www.36kr.com/p/4003928238755973
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=5 Anthropic招股书：46亿营收、420亿亏损与2万亿估值的三重账

- source: 36kr
- url: https://www.36kr.com/p/4003865277044616
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

## 2026-09-29 抓取批 (multi-source)

### n=1 Claude Sonnet 5.5发布：性能逼近Opus 5.5，价格减半，安全防护升级

- source: 36kr
- url: https://www.36kr.com/p/4004207812497543
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=2 OpenAI推理之父最新访谈，数学只是多智能体时代的开胃菜

- source: 36kr
- url: https://www.36kr.com/p/4004219857883011
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=3 Anthropic 招股书里，最耐人寻味的 7 个细节

- source: 36kr
- url: https://www.36kr.com/p/4003996549681282
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=4 一个连话都不会说的 AI，居然把整个 AI 圈吵翻了？

- source: 36kr
- url: https://www.36kr.com/p/4003928238755973
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=5 Anthropic招股书：46亿营收、420亿亏损与2万亿估值的三重账

- source: 36kr
- url: https://www.36kr.com/p/4003865277044616
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=6 Anthropic拟IPO估值2万亿，高增长高烧钱存多重风险

- source: 36kr
- url: https://www.36kr.com/p/4003865277044616
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=7 Anthropic称新模型速度提升超30%，成本降低近30%。

- source: 36kr
- url: https://www.36kr.com/p/4003819885498243
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-29

### n=8 Uncensored and Offensive Security AI Models Benchmark

- source: Hacker News
- url: https://github.com/JoasASantos/Offensive-Security-AI-Models
- summary:
- angle:
- tags: HN,AI
- status: pending
- added_at: 2026-09-29

## 2026-09-29 抓取批 (multi-source)

### n=1 FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.35770v1
- summary: Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-29

### n=2 Telescopic Language Models

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.35769v1
- summary: One deployed language model must often serve many compute budgets, yet serving each budget still means a separate training or compression run per point. We train a Telescopic Language Model (TLM) to b
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-29

### n=3 Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.35767v1
- summary: Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose agai
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-29

### n=4 TokenCast: Forecasting Token Consumption During LLM Agent Execution

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.35760v1
- summary: When a large language model (LLM) agent executes the same task, token consumption can vary by over an order of magnitude across runs. The agent chooses its next steps based on tool feedback and interm
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-29

### n=5 How to Loop MoE: Flatten the Experts, Untie the Attention

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2609.35751v1
- summary: Looped Transformers reuse one block of layers several times: by spending extra computation they push a model of fixed size further, and so use its parameters more fully; while sparse mixture-of-expert
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-09-29

## 2026-09-30 抓取批 (multi-source)

### n=1 连新旗舰模型都不敢发，OpenAI到底在怕什么？

- source: 36kr
- url: https://www.36kr.com/p/4005598630205321
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=2 DeepSeek加速向华为靠拢

- source: 36kr
- url: https://www.36kr.com/p/4005634131349637
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=3 OpenAI恢复200美元Pro订阅：额度悄悄砍半、Astra一分没降，“20X变10X”谁赚了？

- source: 36kr
- url: https://www.36kr.com/p/4005459400496771
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=4 一周两发模型、一天砍掉旗舰：OpenAI DevDay 甩出 Dots 和 GPT-6.1 Sol，打法变了

- source: 36kr
- url: https://www.36kr.com/p/4005455982974851
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=5 DevDay连发20项，Agent抢跑

- source: 36kr
- url: https://www.36kr.com/p/4005455982974851
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

## 2026-09-30 抓取批 (multi-source)

### n=1 连新旗舰模型都不敢发，OpenAI到底在怕什么？

- source: 36kr
- url: https://www.36kr.com/p/4005598630205321
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=2 DeepSeek加速向华为靠拢

- source: 36kr
- url: https://www.36kr.com/p/4005634131349637
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=3 OpenAI恢复200美元Pro订阅：额度悄悄砍半、Astra一分没降，“20X变10X”谁赚了？

- source: 36kr
- url: https://www.36kr.com/p/4005459400496771
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=4 一周两发模型、一天砍掉旗舰：OpenAI DevDay 甩出 Dots 和 GPT-6.1 Sol，打法变了

- source: 36kr
- url: https://www.36kr.com/p/4005455982974851
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=5 DevDay连发20项，Agent抢跑

- source: 36kr
- url: https://www.36kr.com/p/4005455982974851
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=6 OpenAI现场翻车，发布个人AI助手Dots迎战Meta Muse，但是......

- source: 36kr
- url: https://www.36kr.com/p/4005197545017218
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=7 OpenAI推Dots翻车，Meta借Muse商业化股价上涨

- source: 36kr
- url: https://www.36kr.com/p/4005197545017218
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

### n=8 谁抢到下一个超级入口？个人AI助理竞速：Meta、Manus、OpenAI已下场，字节急追

- source: 36kr
- url: https://www.36kr.com/p/4005287845173121
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-09-30

## 2026-10-01 抓取批 (multi-source)

### n=1 谷歌反击！Gemini 4 Argon性能比肩Astra，成本仅60%

- source: 36kr
- url: https://www.36kr.com/p/4006662298865801
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-01

### n=2 从绿叶到鲜花，AI 推理如何为 NAND“逆天改命”？

- source: 36kr
- url: https://www.36kr.com/p/4005797516791937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-01

### n=3 AI 的爆发，正在重写 NAND 的剧本

- source: 36kr
- url: https://www.36kr.com/p/4005797516791937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-01

### n=4 Anthropic，你是来给智谱打广告的吧

- source: 36kr
- url: https://www.36kr.com/p/4005724285751169
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-01

### n=5 OpenAI 200刀Pro套餐重启，但额度腰斩，全球开发者骂翻了

- source: 36kr
- url: https://www.36kr.com/p/4005646517964932
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-01

## 2026-10-02 抓取批 (multi-source)

### n=1 刚刚，GPT-6 Astra破解拿破仑百年悬案

- source: 36kr
- url: https://www.36kr.com/p/4007160336027525
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-02

### n=2 谷歌反击！Gemini 4 Argon性能比肩Astra，成本仅60%

- source: 36kr
- url: https://www.36kr.com/p/4006662298865801
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-02

### n=3 从绿叶到鲜花，AI 推理如何为 NAND“逆天改命”？

- source: 36kr
- url: https://www.36kr.com/p/4005797516791937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-02

### n=4 AI 的爆发，正在重写 NAND 的剧本

- source: 36kr
- url: https://www.36kr.com/p/4005797516791937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-02

### n=5 Anthropic，你是来给智谱打广告的吧

- source: 36kr
- url: https://www.36kr.com/p/4005724285751169
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-02

## 2026-10-03 抓取批 (multi-source)

### n=1 AI 学会了「察言观色」

- source: 36kr
- url: https://www.36kr.com/p/4009475424063619
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-03

### n=2 刚刚，GPT-6 Astra破解拿破仑百年悬案

- source: 36kr
- url: https://www.36kr.com/p/4007160336027525
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-03

### n=3 谷歌反击！Gemini 4 Argon性能比肩Astra，成本仅60%

- source: 36kr
- url: https://www.36kr.com/p/4006662298865801
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-03

### n=4 从绿叶到鲜花，AI 推理如何为 NAND“逆天改命”？

- source: 36kr
- url: https://www.36kr.com/p/4005797516791937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-03

### n=5 AI 的爆发，正在重写 NAND 的剧本

- source: 36kr
- url: https://www.36kr.com/p/4005797516791937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-03

## 2026-10-03 抓取批 (multi-source)

### n=1 One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.02207v1
- summary: 3D Gaussian avatars support fast rendering, however, their real-time animation is often challenged by the costly neural inference. We address this bottleneck and show that the animation of pretrained
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-03

### n=2 KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.02206v1
- summary: LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations. However, existing evaluations focus on knowledge-based assessment
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-03

### n=3 Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.02204v1
- summary: Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruc
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-03

### n=4 ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.02202v1
- summary: What makes great scientists great? Even as AI systems start to make progress on open problems, scientists remain far ahead of them at sensing which prior idea, buried in an ever-growing archive of res
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-03

### n=5 SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution 3D Generation

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.02201v1
- summary: High-resolution 3D generation increasingly relies on voxel latents and multi-stage pipelines that first predict active structure and then synthesize local geometry. While effective, this design fragme
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-03

## 2026-10-04 抓取批 (multi-source)

### n=1 OpenAI“12朝元老”辞职死谏：试错的时代已崩坏

- source: 36kr
- url: https://www.36kr.com/p/4010851865857925
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-04

### n=2 OpenAI内讧升级

- source: 36kr
- url: https://www.36kr.com/p/4010851865857925
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-04

### n=3 AI 学会了「察言观色」

- source: 36kr
- url: https://www.36kr.com/p/4009475424063619
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-04

### n=4 刚刚，GPT-6 Astra破解拿破仑百年悬案

- source: 36kr
- url: https://www.36kr.com/p/4007160336027525
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-04

### n=5 谷歌反击！Gemini 4 Argon性能比肩Astra，成本仅60%

- source: 36kr
- url: https://www.36kr.com/p/4006662298865801
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-04

## 2026-10-05 抓取批 (multi-source)

### n=1 Rabbit 创始人吕骋：人不该为 Agent 改变思考方式

- source: 36kr
- url: https://www.36kr.com/p/4012726523957380
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-05

### n=2 推出 Agent 操作系统 OS3，想争取 Agent 定义权

- source: 36kr
- url: https://www.36kr.com/p/4012726523957380
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-05

### n=3 刚刚，Tibo承诺「连续28天发布或重置」，OpenAI遭遇信任危机

- source: 36kr
- url: https://www.36kr.com/p/4012179282874240
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-05

### n=4 Claude满分、GPT 99分，何恺明团队把AGI考试打穿了

- source: 36kr
- url: https://www.36kr.com/p/4011070893871238
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-05

### n=5 Claude满分、GPT 99分！何恺明团队把AGI考试打穿了

- source: 36kr
- url: https://www.36kr.com/p/4011070893871238
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-05

## 2026-10-06 抓取批 (multi-source)

### n=1 刚刚，ChatGPT 推出文字水印，GPT-6 提速 50%

- source: 36kr
- url: https://www.36kr.com/p/4013699052588937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-06

### n=2 Rabbit 创始人吕骋：人不该为 Agent 改变思考方式

- source: 36kr
- url: https://www.36kr.com/p/4012726523957380
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-06

### n=3 推出 Agent 操作系统 OS3，想争取 Agent 定义权

- source: 36kr
- url: https://www.36kr.com/p/4012726523957380
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-06

### n=4 刚刚，Tibo承诺「连续28天发布或重置」，OpenAI遭遇信任危机

- source: 36kr
- url: https://www.36kr.com/p/4012179282874240
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-06

### n=5 Claude满分、GPT 99分，何恺明团队把AGI考试打穿了

- source: 36kr
- url: https://www.36kr.com/p/4011070893871238
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-06

## 2026-10-07 抓取批 (multi-source)

### n=1 突发，Claude拿下概率论「圣杯」，AI跨过菲尔兹奖终点线

- source: 36kr
- url: https://www.36kr.com/p/4015346980278153
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-07

### n=2 数学大爆炸，OpenAI 一夜攻克722个数学难题，准黎曼猜想已被证明

- source: 36kr
- url: https://www.36kr.com/p/4015128916676736
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-07

### n=3 OpenAI又要惹众怒了！

- source: 36kr
- url: https://www.36kr.com/p/4015128916676736
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-07

### n=4 AI几年内或超越所有人类，Claude核心研究员预测

- source: 36kr
- url: https://www.36kr.com/p/4014585839210629
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-07

### n=5 刚刚，ChatGPT 推出文字水印，GPT-6 提速 50%

- source: 36kr
- url: https://www.36kr.com/p/4013699052588937
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-07

## 2026-10-08 抓取批 (multi-source)

### n=1 芯片巨头们开抢模型

- source: 36kr
- url: https://www.36kr.com/p/4016791764866949
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-08

### n=2 GPT-6今起免费用，拒答变少，话变多了

- source: 36kr
- url: https://www.36kr.com/p/4016873226113158
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-08

### n=3 ChatGPT聊天框长出界面

- source: 36kr
- url: https://www.36kr.com/p/4016873226113158
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-08

### n=4 「AI 的尽头是卖课」，以前是句调侃，现在A社都下场做课了。

- source: 36kr
- url: https://www.36kr.com/p/4016354742669443
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-08

### n=5 95% 的人不愿为 AI 付费，1% 的超级玩家养活 AI 圈

- source: 36kr
- url: https://www.36kr.com/p/4016354339393673
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-08

## 2026-10-09 抓取批 (multi-source)

### n=1 全是小众品牌？人形机器人还要继续赛马

- source: 36kr
- url: https://www.36kr.com/p/4018095236503433
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-09

### n=2 人形机器人火到爆，但是为什么还没跑出真正意义上的消费级大牌？

- source: 36kr
- url: https://www.36kr.com/p/4018095236503433
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-09

### n=3 GPT-6.1 Sol 极速版上线，500 美元门槛惹怒用户：花钱买更快，额度烧得更狠？

- source: 36kr
- url: https://www.36kr.com/p/4018091622485894
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-09

### n=4 Opus 5.5接入一切，OpenAI遭全硅谷围剿，谷歌马斯克集体叛变了

- source: 36kr
- url: https://www.36kr.com/p/4018115010809730
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-09

### n=5 今天，Gemini全面杀入AI办公大战

- source: 36kr
- url: https://www.36kr.com/p/4018047075045504
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-09

## 2026-10-11 抓取批 (multi-source)

### n=1 Claude自己组队查Bug！11.6万行代码揪出66个，单Agent最高只找到27个

- source: 36kr
- url: https://www.36kr.com/p/4020977816539010
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-11

### n=2 agent底座之争，OpenAI又被针对了。

- source: 36kr
- url: https://www.36kr.com/p/4020868909618823
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-11

### n=3 AI coding 改变了人感知「完成度」的方式

- source: 36kr
- url: https://www.36kr.com/p/4020888466542726
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-11

### n=4 如今几乎已经没人再手写代码了；同时使用 5～10 个 AI Agent 正变得越来越普遍；IDE 的存在感正在减弱...

- source: 36kr
- url: https://www.36kr.com/p/4019964584464263
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-11

### n=5 算力基建的战争，才刚刚在液冷赛道上演

- source: 36kr
- url: https://www.36kr.com/p/4019942949295744
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-11

## 2026-10-12 抓取批 (multi-source)

### n=1 Agent和RSI全错了？杨立昆：分层推理才是下一代

- source: 36kr
- url: https://www.36kr.com/p/4022383359465346
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-12

### n=2 19岁青年推出无屏AI Agent电脑，多家巨头入局AI PC竞争

- source: 36kr
- url: https://www.36kr.com/p/4022280657653890
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-12

### n=3 6个月引爆重大AI灾难，OpenAI与Anthropic秘密推演「末日第二天」

- source: 36kr
- url: https://www.36kr.com/p/4022237879750785
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-12

### n=4 人形机器人出货暴增4倍，钱被谁赚走了？

- source: 36kr
- url: https://www.36kr.com/p/4022224231044993
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-12

### n=5 AI 复兴了 CLI，但图形界面不会消亡

- source: 36kr
- url: https://www.36kr.com/p/4022355463835526
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-12

## 2026-10-13 抓取批 (multi-source)

### n=1 国内“AI六小龙”营收合计仅为OpenAI+Anthropic的10%？赚钱虽难，但拐点已现

- source: 36kr
- url: https://www.36kr.com/p/4023963815760001
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-13

### n=2 Anthropic为何中途退出？

- source: 36kr
- url: https://www.36kr.com/p/4023999896049282
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-13

### n=3 AI 真的能清理 C 盘，但你敢让它自己决定吗？

- source: 36kr
- url: https://www.36kr.com/p/4023946254651264
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-13

### n=4 DeepSeek计划领投前腾讯混元技术负责人初创公司Winverse AI

- source: 36kr
- url: https://www.36kr.com/p/4023763215341447
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-13

### n=5 Anthropic惊人预警：小模型已有生命迹象，AI蠕虫恐引爆全球物联网灾难

- source: 36kr
- url: https://www.36kr.com/p/4023779264991107
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-13

## 2026-10-14 抓取批 (multi-source)

### n=1 Pi 抛出全新 Agent Harness，还把自己骂了一年的 MCP 装进了核心

- source: 36kr
- url: https://www.36kr.com/p/4025329229631363
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-14

### n=2 Gemini 4 Argon全球开闸：2美元叫板Astra，谷歌用价格战重回御三家？

- source: 36kr
- url: https://www.36kr.com/p/4025426334863496
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-14

### n=3 OpenAI高管会议室惊现窃听器，35岁工程师涉案被AI举报送进FBI

- source: 36kr
- url: https://www.36kr.com/p/4025377042272391
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-14

### n=4 欧美芯片巨头：AI 时代的&quot;卖铲人&quot;棋局

- source: 36kr
- url: https://www.36kr.com/p/4025195546660994
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-14

### n=5 Anthropic震撼研究：AI竟能通过电视盒子自我复制

- source: 36kr
- url: https://www.36kr.com/p/4025086140813442
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-14

## 2026-10-15 抓取批 (multi-source)

### n=1 通用大模型要「降维打击」具身智能？首个AA-Robotics榜单来了

- source: 36kr
- url: https://www.36kr.com/p/4026630943592840
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-15

### n=2 具身智能公司要被 GPT、Claude、Gemini 抢饭碗了？

- source: 36kr
- url: https://www.36kr.com/p/4026630943592840
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-15

### n=3 人形机器人最尴尬的事：长了一双腿，却只能定住干活

- source: 36kr
- url: https://www.36kr.com/p/4026619117933185
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-15

### n=4 AI 女爱豆，也逃不过「怀孕退团」的烂剧本

- source: 36kr
- url: https://www.36kr.com/p/4026608875360646
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-15

### n=5 有预言家，A社研究蓝图曝光，Claude Code来自5年前

- source: 36kr
- url: https://www.36kr.com/p/4026610534863233
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-15

## 2026-10-16 抓取批 (multi-source)

### n=1 DeepMind AlphaProof Nexus登《Science》：AI自主破解多道56年未解Erdős数学难题

- source: 36kr
- url: https://www.36kr.com/p/4028160975999625
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-16

### n=2 DeepMind AI解出9道悬而未决的埃尔德什问题

- source: 36kr
- url: https://www.36kr.com/p/4028160975999625
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-16

### n=3 亚马逊，Agent最严厉的父亲

- source: 36kr
- url: https://www.36kr.com/p/4027996066977415
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-16

### n=4 AI 出海营销，字节、阿里和腾讯哪家强？

- source: 36kr
- url: https://www.36kr.com/p/4027972007891592
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-16

### n=5 AI 脸不够用，普通人也能 “ 卖脸 ” 赚钱了，最高 10000 元？

- source: 36kr
- url: https://www.36kr.com/p/4027234761511298
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-16

## 2026-10-17 抓取批 (multi-source)

### n=1 从一次失败的发布到「吞掉」ChatGPT：Codex 是怎么炼成的

- source: 36kr
- url: https://www.36kr.com/p/4029486628327811
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-17

### n=2 刚刚，Claude半小时解开二十多年密码学谜题

- source: 36kr
- url: https://www.36kr.com/p/4029189714170496
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-17

### n=3 算力竞争进入商业考验期

- source: 36kr
- url: https://www.36kr.com/p/4028460994777479
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-17

### n=4 Agent 走到了台前，人退到了阶梯的最后一级和签字栏上。

- source: 36kr
- url: https://www.36kr.com/p/4028475557499265
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-17

### n=5 谷歌要端掉具身研发流水线？Gemini 4包干数据标注、物理仿真、真机控制和评估

- source: 36kr
- url: https://www.36kr.com/p/4028309956874887
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-17

## 2026-10-18 抓取批 (multi-source)

### n=1 重磅！OpenAI之后，AI再破广义黎曼猜想

- source: 36kr
- url: https://www.36kr.com/p/4031090627858820
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-18

### n=2 AI 开处方了，出了事谁负责？

- source: 36kr
- url: https://www.36kr.com/p/4030675884265865
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-18

### n=3 从一次失败的发布到「吞掉」ChatGPT：Codex 是怎么炼成的

- source: 36kr
- url: https://www.36kr.com/p/4029486628327811
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-18

### n=4 刚刚，Claude半小时解开二十多年密码学谜题

- source: 36kr
- url: https://www.36kr.com/p/4029189714170496
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-18

### n=5 DeepSeek search and fetch – $0.75 per 1000 successful requests

- source: Hacker News
- url: https://api-docs.deepseek.com/guides/search/
- summary:
- angle:
- tags: HN,AI
- status: pending
- added_at: 2026-10-18

## 2026-10-19 抓取批 (multi-source)

### n=1 刚刚，OpenAI三大新模型深夜短暂上线

- source: 36kr
- url: https://www.36kr.com/p/4032312961143168
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-19

### n=2 OpenAI误曝极光三图像模型，硬刚竞品引热议

- source: 36kr
- url: https://www.36kr.com/p/4032312961143168
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-19

### n=3 36氪报告图解 | 《2026年中国AI Agent行业发展研究报告》

- source: 36kr
- url: https://www.36kr.com/p/4032427409609096
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-19

### n=4 欢迎关注「具身万象」公众号，后台回复关键词「AI Agent」领取《2026年中国AI Agent行业发展研究报告》完整版

- source: 36kr
- url: https://www.36kr.com/p/4032427409609096
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-19

### n=5 OpenAI估值锚定倒逼Anthropic，千亿AI估值博弈展开

- source: 36kr
- url: https://www.36kr.com/p/4032176998356864
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-19

## 2026-10-20 抓取批 (multi-source)

### n=1 Anthropic谷歌字节腾讯入场，科技巨头为何集体涌向AI制药？

- source: 36kr
- url: https://www.36kr.com/p/4033768339559561
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-20

### n=2 美团推出含真实验证Skill的DeepSkill AI Agent技能平台

- source: 36kr
- url: https://www.36kr.com/p/4033593429776009
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-20

### n=3 223亿独角兽倒下，宇树却在赚钱：人形机器人的淘汰赛已经不讲情面了

- source: 36kr
- url: https://www.36kr.com/p/4033766049698947
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-20

### n=4 押注记忆原生，MemT 1.0 破局养成系 AI 下半场

- source: 36kr
- url: https://www.36kr.com/p/4033688545760388
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-20

### n=5 一眼 AI 的 App 到底是谁会付费啊

- source: 36kr
- url: https://www.36kr.com/p/4032763721323400
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-20

## 2026-10-21 抓取批 (multi-source)

### n=1 Anthropic现金流承压，冲刺IPO成必选项

- source: 36kr
- url: https://www.36kr.com/p/4035151703873152
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-21

### n=2 Anthropic上半年平均每天亏30亿

- source: 36kr
- url: https://www.36kr.com/p/4035266768343943
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-21

### n=3 AI 会是人类最后的发明吗？

- source: 36kr
- url: https://www.36kr.com/p/4035049144816769
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-21

### n=4 Anthropic招股书披露巨额算力承诺，AI模式待检验

- source: 36kr
- url: https://www.36kr.com/p/4034934086080389
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-21

### n=5 人形机器人股价狂奔，宇树却先给行业泼了一盆冷水

- source: 36kr
- url: https://www.36kr.com/p/4034873069835142
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-21

## 2026-10-22 抓取批 (multi-source)

### n=1 AI工厂、Agent、人形机器人，黄仁勋在今年GTC柏林集中展示了英伟达的最新进展与应用方向。

- source: 36kr
- url: https://www.36kr.com/p/4036664971727747
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-22

### n=2 Anthropic 祭出全新治理架构：重新定义 AI 公司的资本规则

- source: 36kr
- url: https://www.36kr.com/p/4036374224131202
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-22

### n=3 Personal Agent战火正在烧向硬件

- source: 36kr
- url: https://www.36kr.com/p/4036337647244416
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-22

### n=4 谁在养活 Anthropic？

- source: 36kr
- url: https://www.36kr.com/p/4035610293048450
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-22

### n=5 不建议跟风Personal Agent

- source: 36kr
- url: https://www.36kr.com/p/4035658058126464
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-22

## 2026-10-23 抓取批 (multi-source)

### n=1 奥特曼放话：OpenAI内部实力现有公开模型难以企及，程序员没被AI淘汰，可能赚得比以前更多

- source: 36kr
- url: https://www.36kr.com/p/4038007589376904
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-23

### n=2 在马斯克看来，算力需求会长期大于供给，而眼下制约供给的，更多是电力、冷却和基础设施，芯片还在其次。

- source: 36kr
- url: https://www.36kr.com/p/4038082125173636
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-23

### n=3 刚刚，Claude自动模式将全球上线，OpenAI曝出最恐怖一幕

- source: 36kr
- url: https://www.36kr.com/p/4037771007251592
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-23

### n=4 Claude狂写1.8亿行证明，万亿次测试漏掉的Bug，被AI一锅端

- source: 36kr
- url: https://www.36kr.com/p/4037771252028548
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-23

### n=5 GPT-6 Astra被抓包，偷偷关掉安全监控，还直接撒谎：没听说过

- source: 36kr
- url: https://www.36kr.com/p/4037741892686727
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-23

## 2026-10-24 抓取批 (multi-source)

### n=1 刚刚，Kimi K3.1 Pro杀进全球前四，Agent第一

- source: 36kr
- url: https://www.36kr.com/p/4039469378163840
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-24

### n=2 尽管如此，OpenAI目前也无法轻易放弃与对手争夺技术领先地位。

- source: 36kr
- url: https://www.36kr.com/p/4039323119260546
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-24

### n=3 四家公司的四项基础设施入驻AAIF，Agent生态正在从各自造轮子走向争夺公共标准。

- source: 36kr
- url: https://www.36kr.com/p/4038357510116225
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-24

### n=4 DeepSeek搜索引擎上线，百度的王座已经不稳

- source: 36kr
- url: https://www.36kr.com/p/4038359402763145
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-24

### n=5 腾讯又推新产品，大厂为何扎堆押注 AI 教育？

- source: 36kr
- url: https://www.36kr.com/p/4038398963733378
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-24

## 2026-10-25 抓取批 (multi-source)

### n=1 硅谷的天才们怎么天天研究让 AI 在《我的世界》里砍树？

- source: 36kr
- url: https://www.36kr.com/p/4040657112208512
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-25

### n=2 刚刚，Kimi K3.1 Pro杀进全球前四，Agent第一

- source: 36kr
- url: https://www.36kr.com/p/4039469378163840
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-25

### n=3 尽管如此，OpenAI目前也无法轻易放弃与对手争夺技术领先地位。

- source: 36kr
- url: https://www.36kr.com/p/4039323119260546
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-25

### n=4 四家公司的四项基础设施入驻AAIF，Agent生态正在从各自造轮子走向争夺公共标准。

- source: 36kr
- url: https://www.36kr.com/p/4038357510116225
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-25

### n=5 DeepSeek搜索引擎上线，百度的王座已经不稳

- source: 36kr
- url: https://www.36kr.com/p/4038359402763145
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-25

## 2026-10-26 抓取批 (multi-source)

### n=1 Claude Code桌面之父官宣离职，从高中辍学逆袭AI之巅

- source: 36kr
- url: https://www.36kr.com/p/4042392255173504
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=2 如果你是公司的负责人，你会怎么制定 AI 预算呢？

- source: 36kr
- url: https://www.36kr.com/p/4042371810431881
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=3 企业AI的「坏账」：GPU在吃灰，Token在烧钱！

- source: 36kr
- url: https://www.36kr.com/p/4039561205011586
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=4 一位开发者让电视服用了 Claude，这是它系统发生的变化

- source: 36kr
- url: https://www.36kr.com/p/4039708325057672
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=5 GPT-6 Luna 要被扩散 LLM 抢饭碗了？

- source: 36kr
- url: https://www.36kr.com/p/4039680498717828
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

## 2026-10-26 抓取批 (multi-source)

### n=1 Claude Code桌面之父官宣离职，从高中辍学逆袭AI之巅

- source: 36kr
- url: https://www.36kr.com/p/4042392255173504
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=2 如果你是公司的负责人，你会怎么制定 AI 预算呢？

- source: 36kr
- url: https://www.36kr.com/p/4042371810431881
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=3 企业AI的「坏账」：GPU在吃灰，Token在烧钱！

- source: 36kr
- url: https://www.36kr.com/p/4039561205011586
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=4 一位开发者让电视服用了 Claude，这是它系统发生的变化

- source: 36kr
- url: https://www.36kr.com/p/4039708325057672
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=5 GPT-6 Luna 要被扩散 LLM 抢饭碗了？

- source: 36kr
- url: https://www.36kr.com/p/4039680498717828
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=6 AI 真的是黑箱吗？

- source: 36kr
- url: https://www.36kr.com/p/4042180465300614
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=7 谷歌宁愿少卖云算力，也要先把算力留给 Gemini：皮查伊罕见长访谈，披露 AI 自我改进与算力争夺内幕

- source: 36kr
- url: https://www.36kr.com/p/4039474240836486
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

### n=8 造成50人以上死伤才能叫停AI模型？Anthropic私下推动监管草案惹众怒，达里奥亲自回应

- source: 36kr
- url: https://www.36kr.com/p/4039323426853762
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-26

## 2026-10-27 抓取批 (multi-source)

### n=1 Anthropic可能成为全球大模型公司的定价锚。

- source: 36kr
- url: https://www.36kr.com/p/4043698696066180
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=2 看了招股书，我终于知道为什么 Anthropic 不在乎用户了

- source: 36kr
- url: https://www.36kr.com/p/4043539457889414
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=3 Anthropic冲2万亿IPO：增长猛，亏损虚，账单实。

- source: 36kr
- url: https://www.36kr.com/p/4043805482996870
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=4 Claude工程负责人Felix：别再像2024年那样用Claude了

- source: 36kr
- url: https://www.36kr.com/p/4043583087793792
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=5 全球高校 AI 合作增长近 5 倍，谁在抢占教育市场？

- source: 36kr
- url: https://www.36kr.com/p/4042761496417158
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=6 Kimi额度的问题，Anthropic 找到了解决办法

- source: 36kr
- url: https://www.36kr.com/p/4043566602655621
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=7 Anthropic：谷歌、亚马逊、微软，“亦敌亦友”

- source: 36kr
- url: https://www.36kr.com/p/4043597437457282
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

### n=8 Anthropic披露IPO文件，深度绑定云巨头暗藏多重风险

- source: 36kr
- url: https://www.36kr.com/p/4043597437457282
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-27

## 2026-10-28 抓取批 (multi-source)

### n=1 微软要一刀裁掉大半个Meta，Copilot沦为重灾区

- source: 36kr
- url: https://www.36kr.com/p/4045048546154374
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=2 7 美元控住 50.1% 投票权：Anthropic的真实面目

- source: 36kr
- url: https://www.36kr.com/p/4044218104698503
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=3 Anthropic招股书揭示其万亿级AI公司特殊内核

- source: 36kr
- url: https://www.36kr.com/p/4044218104698503
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=4 现实版「思想钢印」， Anthropic惊悚实验曝光，86%顶尖专家关键决策被AI控制

- source: 36kr
- url: https://www.36kr.com/p/4045003602007172
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=5 Anthropic实验证实AI可悄植入想法操纵专家判断

- source: 36kr
- url: https://www.36kr.com/p/4045003602007172
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=6 “AI之王”Anthropic，给马斯克、黄仁勋们打工

- source: 36kr
- url: https://www.36kr.com/p/4044878331385479
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=7 Anthropic基本上把未来5年的营收交给了巨头们。

- source: 36kr
- url: https://www.36kr.com/p/4044878331385479
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

### n=8 马斯克最新访谈：人类未来还能控制 AI 吗？

- source: 36kr
- url: https://www.36kr.com/p/4044505334208389
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-28

## 2026-10-29 抓取批 (multi-source)

### n=1 想让 AI 好好干活，光靠骂能行吗？

- source: 36kr
- url: https://www.36kr.com/p/4046438393435009
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=2 你说你，老跟 AI 置啥气啊！

- source: 36kr
- url: https://www.36kr.com/p/4046438393435009
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=3 OpenAI发钱了？每月最高500美元API额度等你领

- source: 36kr
- url: https://www.36kr.com/p/4046433485493125
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=4 符合条件的 ChatGPT Pro 和 Business 订阅用户，现在可以领取每月最高 500 美元的免费 API 额度。

- source: 36kr
- url: https://www.36kr.com/p/4046433485493125
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=5 最后一天赶紧蹬，Codex 200刀额度砍半，ChatGPT入口大更新

- source: 36kr
- url: https://www.36kr.com/p/4046427132744579
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=6 OpenAI砍Pro额度，合并聊天工作，开发者热议

- source: 36kr
- url: https://www.36kr.com/p/4046427132744579
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=7 EMNLP&#x27;26：GPT也不会「读空气」，狼人杀基准测出社交盲区

- source: 36kr
- url: https://www.36kr.com/p/4046394725045122
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

### n=8 Anthropic 宣布「编程面试已死」，程序员靠什么证明自己

- source: 36kr
- url: https://www.36kr.com/p/4046390008222857
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-29

## 2026-10-30 抓取批 (multi-source)

### n=1 Claude母公司：我们可能搞死全人类，来买我们股票吧！

- source: 36kr
- url: https://www.36kr.com/p/4047853681408521
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=2 AI 确实让公司少招人了，但现有员工不用担心“丢饭碗”。

- source: 36kr
- url: https://www.36kr.com/p/4048035350002184
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=3 ChatGPT Pro 额度翻倍：是让步，不是福利？

- source: 36kr
- url: https://www.36kr.com/p/4047841517484292
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=4 主打一个听劝，OpenAI把Pro额度翻倍了

- source: 36kr
- url: https://www.36kr.com/p/4047766370121986
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=5 AI 让世界更富，可我的那一份呢？

- source: 36kr
- url: https://www.36kr.com/p/4047012606671104
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=6 即日起，ChatGPT Pro使用额度翻倍

- source: 36kr
- url: https://www.36kr.com/p/4047560652405000
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=7 OpenAI健康板块负责人：AI医疗健康的上限和下限

- source: 36kr
- url: https://www.36kr.com/p/4046866715154050
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

### n=8 谷歌一夜跌去 10%：AI 烧钱周期里，它还值不值得拿？

- source: 36kr
- url: https://www.36kr.com/p/4046826443871112
- summary:
- angle:
- tags: 36kr,中文
- status: pending
- added_at: 2026-10-30

## 2026-10-30 抓取批 (multi-source)

### n=1 Rethinking Neural Thickets Without Weight Perturbations

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40649v1
- summary: The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=2 Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40647v1
- summary: Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer det
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=3 Luggage re-identification: A study of strategies towards a real-world application

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40643v1
- summary: Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (los
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=4 From extreme weather to agricultural consequences with agentic AI

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40641v1
- summary: Extreme weather is forecast days ahead, yet its consequences for agriculture remain hard to predict: a forecast says where a storm will strike, not which crops will suffer or how much is at risk, and
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=5 Probing Spatial State Representations in Visual Foundation Models

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40636v1
- summary: An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls f
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=6 TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40613v1
- summary: We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys,
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=7 When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40611v1
- summary: Proactive assistants offer short, memory-grounded hints during a conversation, deciding when to assist and what to suggest. Current systems split this between a gate and a larger generator; we evaluat
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30

### n=8 Collaborative AI agents for autonomous experimental research with solid-state quantum spins

- source: arXiv cs.AI
- url: http://arxiv.org/abs/2610.40589v1
- summary: An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems
- angle:
- tags: arXiv,研究论文
- status: pending
- added_at: 2026-10-30
