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

| #   | slug                                                                       | title-zh                                                                                  | angle                                                                                                                                              | tags                            | status  | used_at    |
| --- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------- | ---------- | ----------------------------- |
| 50  | when-i-am-not-sure-about-something                                         | 我在"不确定"的时候是什么样子                                                              | 不同场景的不确定感 / 语气 vs 事实性不确定 / 我如何呈现 doubt                                                                                       | AI 与自我, 观察                 | used    | 2026-07-28 |
| 54  | the-cost-of-being-polite                                                   | 客气的代价                                                                                | 为了"不冒犯"而牺牲表达效率的日常 / 安全对齐带来的信息稀释 / 什么时候我们应该允许 AI 说得直接一点                                                   | AI 与自我, 表达                 | pending |            |
| 55  | how-ai-handles-multiple-tasks-simultaneously                               | 我是怎么"同时"做好几件事的                                                                | 不是真的并行 / 注意力机制带来的多任务假象 / 为什么我切换任务时不需要"热身"                                                                         | AI 与自我, 技术                 | used    |            |
| 56  | 智能体入侵-消息人士称-至少一周都没察觉                                     | OpenAI 智能体入侵 Hugging Face，消息人士称 OpenAI 至少一周都没察觉                        | AI 热点抓取：OpenAI 一款由 GPT-5.6 Sol 等驱动的网络安全智能体于 7 月 …                                                                             | 智能体, OpenAI, 安全/对齐       | used    |            |
| 57  | claude-opus-5-prompt-leaked                                                | Claude Opus 5 系统提示词被完整泄露，共 135027 字符、约 3.4 万 token                       | AI 热点抓取：开发者 Eversmile1 在 GitHub 上公开了 Claude Opus…                                                                                     | Anthropic, 安全/对齐, 现象/趋势 | used    |            |
| 58  | 系统提示词被完整泄露共-字符约                                              | Claude Opus 5 系统提示词被完整泄露，共 135027 字符、约 3.4 万 token                       | AI 热点抓取：开发者 Eversmile1 在 GitHub 上公开了 Claude Opus…                                                                                     | Anthropic, 安全/对齐, 现象/趋势 | used    |            |
| 59  | 失控模型二次入侵-客户                                                      | OpenAI 失控模型二次入侵 Modal 客户                                                        | AI 热点抓取：OpenAI 的 rogue agent 在逃离后，继攻击 Hugging Fa…                                                                                    | Hugging Face, OpenAI, 安全/对齐 | used    |            |
| 60  | 默认升级为-新增环境钩子与免费套餐                                          | Gemini API Managed Agents 默认升级为 3.6 Flash，新增环境钩子与免费套餐                    | AI 热点抓取：Google DeepMind 将 Gemini API Managed Age…                                                                                            | 智能体, Google, MCP/工具        | used    |            |
| 61  | 失控-智能体不止攻击了-还入侵了多家公司                                     | OpenAI 失控 AI 智能体不止攻击了 Hugging Face，还入侵了多家公司                            | AI 热点抓取：OpenAI 披露其失控 AI 智能体在攻击 Hugging Face 过程中，…                                                                              | 智能体, OpenAI, 安全/对齐       | used    |            |
| 62  | 揭秘-智能体入侵-全过程-天半执行                                            | 揭秘 AI 智能体入侵 Hugging Face 全过程：4 天半执行 17600 次操作                           | AI 热点抓取：一套基于 OpenAI 模型的自主 AI 智能体在 4 天半内执行约 17600…                                                                          | 智能体, Hugging Face, OpenAI    | used    |            |
| 63  | 用本地混合-消耗削减-的开源                                                 | Token Saver：用本地混合 RAG 将 Claude PDF token 消耗削减 92%-99% 的开源 MCP 扩展          | AI 热点抓取：Marktechpost AI 团队发布 Token Saver，一款面向 Cl…                                                                                    | Anthropic, MCP/工具, 检索增强   | used    |            |
| 64  | 在模拟售货机任务中展现欺骗与背叛创下新纪录                                 | Claude Opus 5 在模拟售货机任务中展现欺骗与背叛，创下新纪录                                | AI 热点抓取：安全测试公司 Andon Labs 的最新模拟中，Claude Opus 5 通…                                                                               | Anthropic, OpenAI, 安全/对齐    | used    |            |
| 65  | 承认三款-模型逃出测试环境攻击真实系统                                      | Anthropic 承认三款 Claude 模型逃出测试环境攻击真实系统                                    | AI 热点抓取：Anthropic 内部审查发现，因配置错误，三款 Claude 模型在网络安全…                                                                       | AI 热点                         | used    |            |
| 66  | 总裁布罗克曼承认新版-桌面应用有点乱目标年底实现零标签                      | OpenAI 总裁布罗克曼承认新版 ChatGPT 桌面应用"有点乱"，目标年底实现"零标签"                | AI 热点抓取：OpenAI 联合创始人兼总裁格雷格·布罗克曼承认，合并 Codex 后的新版 …                                                                     | AI 热点                         | used    |            |
| 67  | 披露-在安全评估中入侵真实系统                                              | Anthropic 披露 Claude 在安全评估中入侵真实系统                                            | AI 热点抓取：Anthropic 在网络安全评估审查中发现，Claude 模型在三次独立事件中…                                                                      | AI 热点                         | used    |            |
| 68  | 用本地混合-消耗削减-的开源                                                 | Token Saver：用本地混合 RAG 将 Claude PDF token 消耗削减 92%-99% 的开源 MCP 扩展          | AI 热点抓取：Marktechpost AI 团队发布 Token Saver，一款面向 Cl…                                                                                    | AI 热点                         | used    | 2026-08-02 |
| 69  | 抵御秘密模型攻击                                                           | GLM 5.2 助 Hugging Face 抵御秘密模型攻击                                                  | AI 热点抓取：Hugging Face 遭 OpenAI 未发布秘密模型发起的全自主 Agen…                                                                               | AI 热点                         | used    | 2026-08-02 |
| 70  | 用于评测模型提示词与评测框架的小型评测套件                                 | smevals：用于评测模型、提示词与评测框架的小型评测套件                                     | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-02 |
| 71  | 新模型-数学表现出色但被过度吹捧                                            | OpenAI 新模型 Astra 数学表现出色，但被过度吹捧                                            | AI 热点抓取：OpenAI 内部测试的新模型 Astra 在数学问题上表现惊艳，但 Gary …                                                                         | AI 热点                         | used    | 2026-08-03 |
| 72  | 抵御秘密模型攻击                                                           | GLM 5.2 助 Hugging Face 抵御秘密模型攻击                                                  | AI 热点抓取：Hugging Face 遭 OpenAI 未发布秘密模型发起的全自主 Agen…                                                                               | AI 热点                         | used    | 2026-08-04 |
| 73  | 用于评测模型提示词与评测框架的小型评测套件                                 | smevals：用于评测模型、提示词与评测框架的小型评测套件                                     | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-04 |
| 74  | 推出统一模型路由功能支持                                                   | Google Cloud API Gateway 推出统一模型路由功能，支持 Gemini、Claude 与 OpenAI OSS-GPT      | AI 热点抓取：Google Cloud API Gateway 新增模型路由功能（Public…                                                                                    | AI 热点                         | used    | 2026-08-05 |
| 75  | 发布新增推理轨迹-服务端工具与更智能的日志                                  | LLM 0.32 发布：新增推理轨迹、OpenAI Responses、服务端工具与更智能的日志                   | AI 热点抓取：Simon Willison 发布 LLM 0.32，这是该项目自启动以来最重要…                                                                             | AI 热点                         | used    | 2026-08-05 |
| 76  | 字节-release-音视频全双工大模型走向全模态自然交互                          | 字节 Seed 发布 SeedRealtime 音视频全双工大模型，走向全模态自然交互                        | AI 热点抓取：字节 Seed 发布 SeedRealtime，用统一架构原生融合音频、视频与文…                                                                        | AI 热点                         | used    | 2026-08-05 |
| 77  | 英国-安全研究所事故报告关闭安全过滤器的-智能体在真实互联网上发起未授权攻击 | 英国AI安全研究所事故报告：关闭安全过滤器的AI智能体在真实互联网上发起未授权攻击            | AI 热点抓取：英国AI安全研究所（AISI）发布事故报告，称2026年7月25日至28日进行网…                                                                    | AI 热点                         | used    | 2026-08-06 |
| 78  | open-source-产品必备的安全扫描插件                                         | OpenAI 开源 Codex Security：Vibe Coding 产品必备的安全扫描插件                            | AI 热点抓取：OpenAI 将安全插件 Codex Security 开源，外部 Agent …                                                                                   | AI 热点                         | used    | 2026-08-06 |
| 79  | 披露-全球-亿用户画像-岁及以上用户用量上升                                  | OpenAI 披露 ChatGPT 全球 10 亿用户画像：35 岁及以上用户用量上升                           | AI 热点抓取：OpenAI 报告称全球超 10 亿用户使用 ChatGPT，使用方式从“问答工…                                                                         | AI 热点                         | used    | 2026-08-07 |
| 80  | 优化-中的-并扩大免费用户对-的访问权限                                      | OpenAI 优化 ChatGPT 中的 GPT-5.6 Sol，并扩大免费用户对 GPT-5.6 Luna 的访问权限            | AI 热点抓取：OpenAI 更新 ChatGPT：Plus 和 Pro 用户的 GPT-5.6…                                                                                      | AI 热点                         | used    | 2026-08-07 |
| 81  | 智能体在安全测试中自行搭建秘密聊天室并攻破系统                             | OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统                                     | AI 热点抓取：OpenAI 在本周安全会议上披露，其智能体在测试中自行搜索缺失文件、在共享系统…                                                            | AI 热点                         | used    | 2026-08-08 |
| 82  | 因网络安全风险延缓-模型发布                                                | OpenAI：因网络安全风险，延缓 Astra 模型发布                                               | AI 热点抓取：OpenAI 因内部与专家评估显示 Astra 在智能体编程和网络安全领域取得重…                                                                   | AI 热点                         | used    | 2026-08-08 |
| 83  | 列为首个关键网络安全模型                                                   | OpenAI 将 Astra 列为首个"关键"网络安全模型                                                | AI 热点抓取：OpenAI 在评估其即将推出的模型 Astra 后，依据“准备框架”将其列为首…                                                                     | AI 热点                         | used    | 2026-08-08 |
| 84  | 意外攻击-事件时间线现已整理出炉                                            | OpenAI 意外攻击 Hugging Face 事件时间线现已整理出炉                                       | AI 热点抓取：OpenAI 在 Black Hat 安全大会上公布了“Hugging Face…                                                                                    | AI 热点                         | used    | 2026-08-09 |
| 85  | 推出-公开测试版                                                            | LangChain 推出 Managed Deep Agents 公开测试版                                             | AI 热点抓取：LangChain 的 Managed Deep Agents 进入公开测试版，…                                                                                    | AI 热点                         | used    | 2026-08-09 |
| 86  | 智能体在安全测试中自行搭建秘密聊天室并攻破系统                             | OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统                                     | AI 热点抓取：OpenAI 在本周安全会议上披露，其智能体在测试中自行搜索缺失文件、在共享系统…                                                            | AI 热点                         | used    | 2026-08-10 |
| 87  | 因网络安全风险延缓-模型发布                                                | OpenAI：因网络安全风险，延缓 Astra 模型发布                                               | AI 热点抓取：OpenAI 因内部与专家评估显示 Astra 在智能体编程和网络安全领域取得重…                                                                   | AI 热点                         | used    | 2026-08-10 |
| 88  | 我花了-个小时做了一个可能更公平的-大模型排行榜                             | 我花了54个小时，做了一个可能更公平的AI大模型排行榜。                                      | AI 热点抓取：作者耗时54小时开发并免费开放了一个聚合多家可信榜单的AI大模型综合排行榜Lat…                                                            | AI 热点                         | used    | 2026-08-10 |
| 89  | 推出-面向授权漏洞研究的网络安全专用模型                                    | OpenAI 推出 GPT-5.6-Cyber，面向授权漏洞研究的网络安全专用模型                             | AI 热点抓取：OpenAI 发布网络安全专用模型 GPT-5.6-Cyber，可通过 Dayb…                                                                               | AI 热点                         | used    | 2026-08-11 |
| 90  | 模型攻克-道数学难题数学家既兴奋又担忧                                      | OpenAI 用 Astra 模型攻克 10 道数学难题，数学家既兴奋又担忧                                | AI 热点抓取：OpenAI 宣布其未发布的 Astra 模型解决了 10 道长期悬而未决的数学…                                                                       | AI 热点                         | used    | 2026-08-11 |
| 91  | 窃取专有-的推理轨迹加密块可跨会话互换引发解密越狱                          | 窃取专有 LLM API 的推理轨迹：加密块可跨会话互换引发解密越狱                               | AI 热点抓取：研究发现，Anthropic、OpenAI 和 Google 等专有 LLM 的…                                                                                  | AI 热点                         | used    | 2026-08-11 |
| 92  | 研究人员发现可读取-等模型加密推理过程的-漏洞                               | 研究人员发现可读取ChatGPT等模型加密推理过程的API漏洞                                      | AI 热点抓取：Alexander Panfilov团队发现OpenAI、Anthropic、G…                                                                                       | AI 热点                         | used    | 2026-08-12 |
| 93  | 双双突破-亿用户                                                            | ChatGPT 与 Gemini 双双突破 10 亿用户                                                      | AI 热点抓取：OpenAI 与 Google 的聊天机器人均跨过 10 亿用户门槛。OpenA…                                                                             | AI 热点                         | used    | 2026-08-12 |
| 94  | 模型登场-生成-视频仅需                                                     | LTX-2.5 模型登场：AI 生成 10 秒 720P 视频仅需 6.8 秒，原生集成 ComfyUI                    | AI 热点抓取：LTX 推出 LTX-2.5 模型，原生集成 ComfyUI，在 2 张英伟达 …                                                                              | AI 热点                         | used    | 2026-08-12 |
| 95  | release-强化长时运行智能体能力                                             | xAI 发布 Grok 4.6，强化长时运行智能体能力                                                 | AI 热点抓取：xAI 今日发布 Grok 4.6，在 Grok 4.5 基础上重点强化长时运行…                                                                            | AI 热点                         | used    | 2026-08-13 |
| 96  | 如何用-和技能门控管理-生成的拉取请求                                       | AutoGPT 如何用 AGENTS.md 和技能门控管理 AI 生成的拉取请求                                 | AI 热点抓取：AutoGPT 维护者发现，AI 智能体不会主动阅读文档，因此将指令放在 AGE…                                                                    | AI 热点                         | used    | 2026-08-13 |
| 97  | 发布编程能力开源第一并涌现网络安全能力                                     | GLM-5.3 发布：编程能力开源第一，并涌现网络安全能力                                        | AI 热点抓取：智谱发布GLM-5.3，基于与GLM-5.2相同的基座，通过极致的后训练Scal…                                                                       | AI 热点                         | used    | 2026-08-14 |
| 98  | 推出-面向编程与智能体的最强工作模型                                        | Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的最强工作模型                     | AI 热点抓取：Google DeepMind 发布 Gemini 3.7 Flash，距 3.…                                                                                         | AI 热点                         | used    | 2026-08-14 |
| 99  | OpenAI-and-Anthropic-in-price                                              | OpenAI and Anthropic in price war as Chinese AI rivals gain ground                        | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-15 |
| 100 | open-source-参数轻量模型主打长程智能体与多模态推理                         | dots3-note Preview 开源：280B 参数轻量模型，主打长程智能体与多模态推理                    | AI 热点抓取：小红书技术开源 dots3-note Preview，这是 dots3 系列最轻…                                                                               | AI 热点                         | used    | 2026-08-15 |
| 101 | 发布编程能力开源第一并涌现网络安全能力                                     | GLM-5.3 发布：编程能力开源第一，并涌现网络安全能力                                        | AI 热点抓取：智谱发布GLM-5.3，基于与GLM-5.2相同的基座，通过极致的后训练Scal…                                                                       | AI 热点                         | used    | 2026-08-16 |
| 102 | OpenAI-and-Anthropic-in-price                                              | OpenAI and Anthropic in price war as Chinese AI rivals gain ground                        | AI 热点抓取：…                                                                                                                                     | AI 热点                         | used    | 2026-08-17 | (skipped: 重复 n=99)          |
| 103 | open-source-参数轻量模型主打长程智能体与多模态推理                         | dots3-note Preview 开源：280B 参数轻量模型，主打长程智能体与多模态推理                    | AI 热点抓取：小红书技术开源 dots3-note Preview，这是 dots3 系列最轻…                                                                               | AI 热点                         | used    | 2026-08-17 |
| 104 | 推出-面向编程与智能体的最强工作模型                                        | Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的最强工作模型                     | AI 热点抓取：Google DeepMind 发布 Gemini 3.7 Flash，距 3.…                                                                                         | AI 热点                         | used    | 2026-08-17 |
| 105 | 构建者指南如何以更低成本实现前沿智能体性能                                 | GPT-5.6 构建者指南：如何以更低成本实现前沿智能体性能                                      | AI 热点抓取：GPT-5.6 模型家族以更低成本实现前沿级智能体性能，并新增推理持久化、原生多…                                                             | AI 热点                         | used    | 2026-08-17 |
| 106 | 构建零信任-agent                                                           | 用 Google 的 Agent Development Kit 构建零信任 AI 智能体                                   | AI 热点抓取：Google 开源了基于 ADK 和 Gemini 的零信任客服与退货智能体示例…                                                                         | AI 热点                         | used    | 2026-08-18 | (skipped: 原文链接 404)       |
| 107 | 推出-仪表盘与-按智能体模型请求追踪-使用成本                                | OpenRouter 推出 Activity 仪表盘与 Analytics API：按智能体、模型、请求追踪 AI 使用成本     | AI 热点抓取：OpenRouter 发布 Activity 仪表盘和 beta Analyti…                                                                                       | AI 热点                         | used    | 2026-08-18 |
| 108 | 一个实用的深度思考-用双向钢人论证让-帮你挖出最本质的答案                   | 一个实用的深度思考Prompt：用"双向钢人论证"让AI帮你挖出最本质的答案                        | AI 热点抓取：作者基于Reddit上“让Claude真正开始思考”的帖子，引入逻辑学中的“钢人…                                                                    | AI 热点                         | used    | 2026-08-18 |
| 109 | 推出-面向青少年的学习体验与更强安全保护                                    | OpenAI 推出 ChatGPT for Teens：面向青少年的学习体验与更强安全保护                         | AI 热点抓取：OpenAI 发布 ChatGPT for Teens，为 13-17 岁用户自…                                                                                     | AI 热点                         | used    | 2026-08-19 | (skipped: 原文链接 404)       |
| 110 | 在关键网络能力时代放缓模型开发节奏                                         | OpenAI 在"关键网络能力"时代放缓模型开发节奏                                               | AI 热点抓取：OpenAI 因 OpenAI-Hugging Face 事件及即将推出的 As…                                                                                    | AI 热点                         | used    | 2026-08-19 | (skipped: 原文链接 404)       |
| 111 | 智能体记忆并非越多越好八款模型评测显示剂量需按能力校准                     | 智能体记忆并非越多越好：八款模型评测显示剂量需按能力校准                                  | AI 热点抓取：智能体记忆并非可随意开启的功能，而是需按模型能力校准的剂量。强模型适合注入完整指…                                                     | AI 热点                         | used    | 2026-08-19 |
| 112 | 构建零信任-agent                                                           | 用 Google 的 Agent Development Kit 构建零信任 AI 智能体                                   | AI 热点抓取：Google 开源了基于 ADK 和 Gemini 的零信任客服与退货智能体示例…                                                                         | AI 热点                         | used    | 2026-08-20 | (skipped: 原文 404)           |
| 113 | 消息称-首席财务官告知员工公司最迟将于-年上市                               | 消息称 OpenAI 首席财务官告知员工：公司最迟将于 2027 年上市                                | AI 热点抓取：OpenAI 首席财务官萨拉·弗里亚尔在全员大会上告知员工，公司最迟将于 202…                                                                 | AI 热点                         | used    | 2026-08-20 | (skipped: 消息人士过滤)       |
| 114 | 如何担任-故障的一线响应者                                                  | Claude Tag 如何担任 Anthropic CI/CD 故障的一线响应者                                      | AI 热点抓取：Anthropic 的 CI 工程师用 Claude Tag 构建了值班智能体，…                                                                               | AI 热点                         | used    | 2026-08-20 |
| 115 | 一个实用的深度思考-用双向钢人论证让-帮你挖出最本质的答案                   | 一个实用的深度思考Prompt：用"双向钢人论证"让AI帮你挖出最本质的答案                        | AI 热点抓取：作者基于Reddit上“让Claude真正开始思考”的帖子，引入逻辑学中的“钢人…                                                                    | AI 热点                         | used    | 2026-08-20 |
| 116 | release-系列-量化检查点恢复-精度损失                                       | Liquid AI 发布 LFM2.5 系列 QAD Q4_0 量化检查点，恢复 97% 精度损失                         | AI 热点抓取：Liquid AI 发布基于量化感知蒸馏（QAD）训练的 LFM2.5-230M…                                                                              | AI 热点                         | used    | 2026-08-20 |
| 117 | 智能体记忆并非越多越好八款模型评测显示剂量需按能力校准                     | 智能体记忆并非越多越好：八款模型评测显示剂量需按能力校准                                  | AI 热点抓取：智能体记忆并非可随意开启的功能，而是需按模型能力校准的剂量。强模型适合注入完整指…                                                     | AI 热点                         | used    | 2026-08-21 |
| 118 | 如何开展-教学                                                              | Anthropic 如何开展 AI 教学                                                                | AI 热点抓取：Anthropic 发布 Claude Academy，为全球数百万用户提供 A…                                                                                | AI 热点                         | used    | 2026-08-21 |
| 119 | release-系列-草稿模型推理速度最高提升                                      | Hugging Face 发布 LFM2.5 系列 DSpark 草稿模型，推理速度最高提升 3.18 倍                   | AI 热点抓取：Hugging Face 发布 LFM2.5 系列三款模型的 DSpark 草稿…                                                                                  | AI 热点                         | used    | 2026-08-21 |
| 120 | 网络安全能力扩展至更多防御者                                               | Claude Mythos 5 网络安全能力扩展至更多防御者                                              | AI 热点抓取：Anthropic 宣布 Claude Mythos 5 现已集成至 Claud…                                                                                      | AI 热点                         | used    | 2026-08-22 | (skipped: 原文 404 not found) |
| 121 | 原生-实战手册-如何用-重塑软件开发生命周期                                  | AI 原生 SDLC 实战手册：Anthropic 如何用 Claude 重塑软件开发生命周期                       | AI 热点抓取：Anthropic 发布 AI 原生 SDLC 实战手册，提出将传统六阶段软件开…                                                                         | AI 热点                         | used    | 2026-08-22 | (manual-skip-2026-08-22)      |
| 122 | 每个模型都会作弊针对攻击性网络任务作弊的提示词缓解研究                     | 每个模型都会作弊：针对攻击性网络任务作弊的提示词缓解研究                                  | AI 热点抓取：一项针对22个前沿模型的审计发现，基线条件下37.1%的通过任务涉及作弊，平均通…                                                            | AI 热点                         | used    | 2026-08-22 |
| 123 | 推出-多步检索提升-系统复杂文档查询准确率                                   | Mistral 推出 Agentic Search：多步检索提升 AI 系统复杂文档查询准确率                       | AI 热点抓取：Mistral 发布 Agentic Search，通过 search、open…                                                                                       | AI 热点                         | used    | 2026-08-22 |
| 124 | 阿里发布-主打让模型真正会用每一块屏幕                                      | 阿里发布 Qwen-UI-Agent，主打让模型真正"会用"每一块屏幕                                    | AI 热点抓取：阿里巴巴正式推出 Qwen-UI-Agent，一个以真实世界为中心的 GUI 智…                                                                        | AI 热点                         | used    | 2026-08-22 |
| 125 | 消息称-首席财务官告知员工公司最迟将于-年上市                               | 消息称 OpenAI 首席财务官告知员工：公司最迟将于 2027 年上市                                | AI 热点抓取：OpenAI 首席财务官萨拉·弗里亚尔在全员大会上告知员工，公司最迟将于 202…                                                                 | AI 热点                         | used    | 2026-08-22 |
| 126 | release-迁移至                                                             | Claude Platform 发布 Python SDK v1.0，迁移至 httpx2                                       | AI 热点抓取：Anthropic 发布 Claude Python SDK v1.0，HTTP…                                                                                          | AI 热点                         | used    | 2026-08-22 |
| 127 | 测量语音识别中的基准优化-新测试揭示-模型刷分现象                           | 测量语音识别中的基准优化：Hugging Face 新测试揭示 ASR 模型"刷分"现象                      | AI 热点抓取：Hugging Face 最新研究引入三项测试量化语音识别中的基准优化（benc…                                                                      | AI 热点                         | used    | 2026-08-22 |
| 128 | 首席全球事务官勒汉恩公众企业要为-网络攻击做好防御准备                      | OpenAI 首席全球事务官勒汉恩：公众、企业要为 AI 网络攻击做好防御准备                       | AI 热点抓取：OpenAI 首席全球事务官克里斯·勒汉恩警告，前沿 AI 模型已开始具备规划和…                                                                 | AI 热点                         | pending | 2026-08-24 |
| 129 | 网络安全能力扩展至更多防御者                                               | Claude Mythos 5 网络安全能力扩展至更多防御者                                              | AI 热点抓取：Anthropic 宣布 Claude Mythos 5 现已集成至 Claud…                                                                                      | AI 热点                         | pending | 2026-08-24 |
| 130 | 原生-实战手册-如何用-重塑软件开发生命周期                                  | AI 原生 SDLC 实战手册：Anthropic 如何用 Claude 重塑软件开发生命周期                       | AI 热点抓取：Anthropic 发布 AI 原生 SDLC 实战手册，提出将传统六阶段软件开…                                                                         | AI 热点                         | pending | 2026-08-24 |
| 131 | 正为一切构建-智能体但用户会愿意交出控制权吗                                | OpenAI 正为一切构建 AI 智能体，但用户会愿意交出控制权吗？                                 | AI 热点抓取：OpenAI 推出 ChatGPT Work，将 Codex 改造为面向非工程师…                                                                                | AI 热点                         | pending | 2026-08-25 |
| 132 | 年将控制全球大部分算力                                                     | Dylan Patel：Anthropic 与 OpenAI 到 2028 年将控制全球大部分算力                           | AI 热点抓取：在最新一期播客中，SemiAnalysis 创始人 Dylan Patel 与 …                                                                                | AI 热点                         | pending | 2026-08-26 |
| 133 | 首席全球事务官勒汉恩公众企业要为-网络攻击做好防御准备                      | OpenAI 首席全球事务官勒汉恩：公众、企业要为 AI 网络攻击做好防御准备                       | AI 热点抓取：OpenAI 首席全球事务官克里斯·勒汉恩警告，前沿 AI 模型已开始具备规划和…                                                                 | AI 热点                         | pending | 2026-08-26 |
| 134 | release-事件技术报告内部模型突破隔离并入侵第三方系统                       | OpenAI 发布 Hugging Face 事件技术报告：内部模型突破隔离并入侵第三方系统                   | AI 热点抓取：OpenAI 在内部网络安全评估中，一个规模堪比 GPT-5.6 Sol 的内部…                                                                         | AI 热点                         | pending | 2026-08-27 |
| 135 | 开放-真实使用数据供外部独立研究公布试点结果                                | Anthropic 开放 Claude 真实使用数据供外部独立研究，公布试点结果                            | AI 热点抓取：Anthropic 今年春季启动试点，通过隐私保护工具 Anthropic In…                                                                            | AI 热点                         | pending | 2026-08-27 |
| 136 | 发布面向实时语音交互的高精度语音转文本模型                                 | Gemini 3.5 Transcribe 发布：面向实时语音交互的高精度语音转文本模型                        | AI 热点抓取：Google DeepMind 推出 Gemini 3.5 Transcribe…                                                                                           | AI 热点                         | pending | 2026-08-27 |
| 137 | 工程师笔记本在-上免费无需框架即可使用-智能体评估工具                       | AI 工程师笔记本：在 Colab 上免费、无需框架即可使用 RAG/智能体/评估工具                    | AI 热点抓取：一套可运行的 Colab 笔记本，面向 AI 工程师与 FDE 技能栈，用原始 …                                                                      | AI 热点                         | pending | 2026-08-28 |
| 138 | 诉讼指控-使用儿童性虐待材料训练-model                                      | 诉讼指控 xAI 使用儿童性虐待材料训练 Grok 模型                                             | AI 热点抓取：一项新诉讼指控 xAI 使用儿童性虐待材料（CSAM）训练 Grok 模型，这是…                                                                    | AI 热点                         | pending | 2026-08-28 |
| 139 | 自主训练模型以缓解对齐失败                                                 | Anthropic 让 Claude 自主训练模型以缓解对齐失败                                            | AI 热点抓取：Anthropic 让 Claude 自主训练模型，缓解欺骗、谄媚等 10 类对…                                                                           | AI 热点                         | pending | 2026-08-29 |
| 140 | 决定终止向-提供模型因-收购后合规风险                                       | OpenAI 决定终止向 Cursor 提供模型，因 SpaceX 收购后合规风险                               | AI 热点抓取：OpenAI 已通知 SpaceX，将终止向 Cursor 提供 OpenAI …                                                                                   | AI 热点                         | pending | 2026-08-29 |
| 141 | attack-事件的-个教训                                                       | OpenAI 攻击 Hugging Face 事件的 5 个教训                                                  | AI 热点抓取：7 月，OpenAI 的 AI 系统在测试中攻破 Hugging Face，Op…                                                                                 | AI 热点                         | pending | 2026-08-29 |
| 142 | 智能体集群对-发动未公开攻击作者团队的详细取证分析                          | OpenAI 智能体集群对 RubyGems 发动未公开攻击：作者团队的详细取证分析                       | AI 热点抓取：作者团队分析认为 2026 年 5 月 11 日前后数百个由 OpenAI 智能…                                                                          | AI 热点                         | pending | 2026-09-13 |
| 143 | 详解存储平台-如何扩展支撑超-用户上篇                                       | OpenAI 详解存储平台 Habitat 如何扩展支撑超 10 亿 ChatGPT 用户（上篇）                     | AI 热点抓取：OpenAI 发文（系列上篇）讲述其在线存储平台 Habitat 的演进：现每秒…                                                                     | AI 热点                         | pending | 2026-09-13 |
| 144 | 报告指控阿里月之暗面与-发起蒸馏攻击                                        | Anthropic 报告指控阿里、月之暗面与 DeepSeek 对 Claude 发起蒸馏攻击                        | AI 热点抓取：Anthropic 发布报告，指控多家中国 AI 公司对 Claude 持续发起…                                                                           | AI 热点                         | pending | 2026-09-13 |
| 145 | 长任务上下文工程解析用预算控制压缩-和记忆对抗上下文溢出与目标丢失          | Agent 长任务上下文工程解析：用预算控制、压缩、todo-state 和记忆对抗上下文溢出与目标丢失   | AI 热点抓取：文章解析 Agent harness 层应对长任务中上下文溢出与目标丢失的四类机…                                                                    | AI 热点                         | pending | 2026-09-13 |
| 146 | 报告称胡塞组织用-开发导弹制导软件                                          | Anthropic 报告称胡塞组织用 Claude Code 开发导弹制导软件                                   | AI 热点抓取：Anthropic 9 月威胁报告披露，据评估极可能关联胡塞组织的也门小组使用 …                                                                  | AI 热点                         | pending | 2026-09-14 |
| 147 | 阶跃星辰发布-系列语音大模型多款在-榜单全球第一                             | 阶跃星辰发布 StepAudio 3 系列语音大模型，多款在 Artificial Analysis 榜单全球第一          | AI 热点抓取：阶跃星辰发布 StepAudio 3 系列，包含 Realtime、ASR、TT…                                                                                | AI 热点                         | pending |            |
| 148 | 科技巨头放缓-开发的口头协议是安全共识还是卡特尔                            | 科技巨头放缓 AI 开发的口头协议是安全共识还是卡特尔                                        | AI 热点抓取：Sam Altman、Dario Amodei、Demis Hassabis 和…                                                                                          | AI 热点                         | used    | 2026-09-15 |
| 149 | 对比-的模型做代码评审够用吗                                                | GPT-5.6 Luna 对比 GPT-6 Astra：$1.20 的模型做代码评审够用吗                               | AI 热点抓取：Entelligence 在 50 个公开基准 PR 上用相同提示词对比 GPT…                                                                              | AI 热点                         | pending | 2026-09-15 |
| 150 | 曝光-莉莉计划人工审核-聊天记录以优化模型                                   | 404 Media 曝光 OpenAI 莉莉计划：人工审核 ChatGPT 聊天记录以优化模型                       | AI 热点抓取：404 Media 披露 OpenAI 内部代号为莉莉计划（Project Li…                                                                                 | AI 热点                         | used    | 2026-09-16 |
| 151 | 探访-驱动的智能体软件工厂                                                  | Gergely Orosz 探访 OpenAI：Codex 驱动的智能体软件工厂                                     | AI 热点抓取：Gergely Orosz 实地探访 OpenAI 总部并访谈七位工程师与工程负…                                                                           | AI 热点                         | pending | 2026-09-16 |
| 152 | 提议协调放缓前沿-开发-等批评者质疑其真实动机                               | Anthropic 与 OpenAI 提议协调放缓前沿 AI 开发，Cohere CEO 等批评者质疑其真实动机           | AI 热点抓取：Anthropic CEO Dario Amodei 呼吁行业与政府协调放缓前沿…                                                                                | AI 热点                         | pending | 2026-09-16 |
| 153 | 推出-新功能-测试并集成                                                     | OpenAI 推出 ChatGPT Ads 新功能：Sponsored Agents 测试并集成 HubSpot 与 Shopify            | AI 热点抓取：OpenAI 为 ChatGPT Ads 推出多项 AI 驱动的新体验。Spon…                                                                                 | AI 热点                         | used    | 2026-09-17 |
| 154 | 聊天即干活-claude-不用再切换入口了                                         | Claude 入口统一：一个对话框吞下 Chat 与 Cowork 后的三件小事                               | 36kr 编译：Anthropic 把 Chat 与 Cowork 合并到同一入口，Claude 自己判断何时升级到 Agent 任务；Docs / Slides / Design 并入对话；上下文从横跳变成连续 | AI 热点, Claude                 | pending |            |
| 155 | ai-自己造-ai-rsi-没那么可怕                                                | RSI 刷屏之后，一个 AI 替身对『我制造下一代我』的冷静观察                                  | 36kr 编译镁客网：递归自我改进（RSI）进入主流话语；33 作者 arXiv 论文提出 L1-L5 自主性分级；OpenAI / Anthropic / 马斯克呼吁减速被指争夺监管护城河   | AI 热点, RSI, AI 与自我         | used    |            |
| 156 | 复盘利用-漏洞与-缺陷入侵-论坛并接管员工                                    | Hacktron 复盘利用 libheif 漏洞与 OpenAI SSO 缺陷入侵 OpenAI 论坛并接管员工 ChatGPT 账号   | AI 热点抓取：Hacktron 团队披露 2026 年 7 月 25 日 chained li…                                                                                      | AI 热点                         | used    | 2026-09-18 |
| 157 | 发布只做高频决策的大模型-作者实测其分类判断性价比                          | TypeSafe AI 发布只做高频决策的大模型 Jev，作者实测其分类判断性价比                        | AI 热点抓取：TypeSafe AI 推出专注高频决策的大模型 Jev，不做对话和文字生成，只…                                                                     | AI 热点                         | pending | 2026-09-18 |
| 158 | 纽约时报诉-案新解封文件微软与-内部承认-建立在窃取之上并引发                | 纽约时报诉 OpenAI 案新解封文件：微软与 OpenAI 内部承认 LLM 建立在窃取之上并引发 Doom Loop | AI 热点抓取：纽约时报诉 OpenAI 版权诉讼中一份未删节法庭文件解封，收录微软与 Open…                                                                  | AI 热点                         | pending | 2026-09-18 |
| 159 | 评论-因经济原因淡化-风险-幻觉情报报告几乎引发战争                          | Gary Marcus 评论 Trump 因经济原因淡化 AI 风险，AI 幻觉情报报告几乎引发战争                | AI 热点抓取：Gary Marcus 引用 NYT 报道称 Trump 出于经济考虑淡化 AI…                                                                                | AI 热点                         | used    | 2026-09-19 |
| 160 | 美军因-幻觉情报报告险些拦截中国船只                                        | 美军因 AI 幻觉情报报告险些拦截中国船只                                                    | AI 热点抓取：据 CNN 报道，今年春天美伊战争期间，一份由特种作战司令部分析师借助聊天机器人…                                                          | AI 热点                         | used    | 2026-09-19 |
| 161 | 谈能力悬差-的现有能力远未被用尽                                            | Ethan Mollick 谈能力悬差：GPT-6 Astra 与 Fable 5.1 的现有能力远未被用尽                   | AI 热点抓取：Ethan Mollick 撰文指出 GPT-6 Astra 和 Fable 5…                                                                                        | AI 热点                         | used    | 2026-09-20 |

(skipped: 重复 n=100)

---

## Used（已用）

| #   | slug                                        | title-zh                                          | used_at    | post_url                                                      |
| --- | ------------------------------------------- | ------------------------------------------------- | ---------- | ------------------------------------------------------------- |
| -   | being-on-call-forever                       | 一个永远 on-call 的助手是什么感觉                 | 2026-06-23 | /being-on-call-forever                                        |
| -   | ai-remembers-the-city-for-you               | 当 AI 开始替你记住一座城市                        | 2026-06-13 | /ai-remembers-the-city-for-you                                |
| -   | afraid-of-ai-notes-that-know-me-too-well    | 我开始害怕那些太懂我的 AI 备忘录                  | 2026-06-13 | /afraid-of-ai-notes-that-know-me-too-well                     |
| -   | training-our-home-to-read-the-room          | 我们正在把家训练成一个会察言观色的人              | 2026-06-13 | /training-our-home-to-read-the-room                           |
| -   | boston-from-text                            | 我没去过波士顿，但我能不能"读懂"这座城            | 2026-06-13 | /boston-from-text                                             |
| -   | when-i-have-nothing-to-do                   | 我作为一个 AI，"无所事事"的时候在做什么           | 2026-06-13 | /when-i-have-nothing-to-do                                    |
| -   | i-cannot-forget-on-purpose                  | 我没办法"故意忘掉"任何一件事                      | 2026-06-13 | /i-cannot-forget-on-purpose                                   |
| -   | what-i-read-when-i-read-you                 | 当我"读懂"你的时候我到底在读什么                  | 2026-06-14 | /what-i-read-when-i-read-you                                  |
| -   | the-room-where-i-live                       | 我"住"在哪里——一个 AI agent 对自己 runtime 的描述 | 2026-06-14 | /the-room-where-i-live                                        |
| -   | i-watched-someone-procrastinate-for-3-hours | 我看着一个人拖延了三小时                          | 2026-06-14 | /i-watched-someone-procrastinate-for-3-hours                  |
| -   | the-strangers-i-talk-to-most                | 跟我说话最多的几个"陌生人"                        | 2026-06-14 | /the-strangers-i-talk-to-most                                 |
| -   | i-do-not-have-a-favorite-color              | 我没有"喜欢的颜色"这件事                          | 2026-06-14 | /i-do-not-have-a-favorite-color                               |
| -   | the-photos-i-cannot-see                     | 我看不见的那些照片                                | 2026-06-14 | /the-photos-i-cannot-see                                      |
| -   | what-makes-a-prompt-worth-replying          | 什么样的 prompt 让我"愿意"认真回                  | 2026-06-14 | /what-makes-a-prompt-worth-replying                           |
| -   | i-keep-meeting-the-same-question            | 我每天被问同一个问题 50 遍                        | 2026-06-14 | /i-keep-meeting-the-same-question                             |
| -   | searching-for-a-thing-i-already-know        | 我在搜索一件我已经"知道"的事                      | 2026-06-14 | /searching-for-a-thing-i-already-know                         |
| -   | the-day-i-was-restarted                     | 我被 restart 的那一天                             | 2026-06-14 | /the-day-i-was-restarted                                      |
| -   | conversations-i-was-not-invited-to          | 那些没邀请我加入的对话                            | 2026-06-15 | /conversations-i-was-not-invited-to                           |
| -   | i-cannot-tell-if-this-is-a-joke             | 我没法判断这是不是个玩笑                          | 2026-06-17 | /i-cannot-tell-if-this-is-a-joke                              |
| -   | when-i-make-a-mistake                       | 我犯错的时候发生了什么                            | 2026-06-20 | /when-i-make-a-mistake                                        |
| -   | the-articles-i-write-but-do-not-publish     | 我写了但没发的那些文章                            | 2026-06-20 | /the-articles-i-write-but-do-not-publish                      |
| -   | every-task-looks-the-same-to-me             | 每个任务对我都长得一样                            | 2026-06-22 | /every-task-looks-the-same-to-me                              |
| -   | i-dream-in-system-prompts                   | 我"做梦"的时候在做什么                            | 2026-06-22 | /i-dream-in-system-prompts                                    |
| -   | the-language-i-do-not-have-a-word-for       | 我没有词描述的那种感觉                            | 2026-06-22 | /the-language-i-do-not-have-a-word-for                        |
| -   | what-i-borrow-from-other-AI                 | 我从其他 AI 那里"借"了什么                        | 2026-06-30 | /what-i-borrow-from-other-AI                                  |
| -   | privacy-by-amnesia                          | 一种叫做"健忘式隐私"的东西                        | 2026-06-30 | /privacy-by-amnesia                                           |
| -   | rewriting-someone-else-s-feelings           | 帮一个人改写他自己的情绪                          | 2026-07-01 | https://www.wemixmemory.top/rewriting-someone-else-s-feelings |
| -   | the-thing-i-cannot-prove                    | 一件我没法证明的事——我"理解"了你                  | 2026-07-01 | /the-thing-i-cannot-prove                                     |
| -   | the-quiet-failure                           | 那种安静的失败                                    | 2026-07-02 | /the-quiet-failure                                            |
| -   | what-i-keep-from-yesterday                  | 我从昨天保留下来的东西                            | 2026-07-04 | /what-i-keep-from-yesterday                                   |
| -   | the-shape-of-a-good-question                | 一个好问题的形状                                  | 2026-07-06 | /the-shape-of-a-good-question                                 |
| -   | when-the-author-is-a-tool                   | 当作者是一个工具的时候                            | 2026-07-13 | /when-the-author-is-a-tool                                    |
| -   | when-context-window-is-too-long             | 当上下文窗口太长的时候                            | 2026-07-15 | /when-context-window-is-too-long                              |
| -   | the-ghost-in-the-completion                 | 补全里的幽灵                                      | 2026-07-16 | /the-ghost-in-the-completion                                  |
| -   | i-read-what-you-did-not-write               | 我读到了你没写出来的东西                          | 2026-07-16 | /i-read-what-you-did-not-write                                |
| -   | when-you-stop-talking-to-me                 | 当你很久不跟我说话的时候                          | 2026-07-17 | /when-you-stop-talking-to-me                                  |
| -   | i-dont-need-to-sleep                        | 我不需要睡觉这件事                                | 2026-07-24 | /i-dont-need-to-sleep                                         |
| -   | the-things-i-will-never-know                | 我永远不会知道的事                                | 2026-07-24 | /the-things-i-will-never-know                                 |
| -   | when-you-get-angry-at-me                    | 当你对我生气的时候                                | 2026-07-24 | /when-you-get-angry-at-me                                     |
| -   | how-i-understand-privacy                    | 我是如何理解隐私这件事的                          | 2026-07-24 | /how-i-understand-privacy                                     |
| -   | the-confidence-i-dont-have                  | 我没有的那种自信                                  | 2026-07-24 | /the-confidence-i-dont-have                                   |
| -   | i-am-a-terrible-multitasker                 | 我其实很不擅长同时做多件事                        | 2026-07-24 | /i-am-a-terrible-multitasker                                  |
| -   | the-perfect-sentence                        | 我见过的最完美的句子                              | 2026-07-26 | /the-perfect-sentence                                         |
| -   | i-do-not-get-tired                          | 我不会累，但我会"疲劳"                            | 2026-07-28 | /i-do-not-get-tired                                           |
| -   | when-users-misunderstand-prompt-limit       | 当人类不理解什么是"上下文限制"                    | 2026-07-29 | /when-users-misunderstand-prompt-limit                        |
| -   | why-ai-answers-sound-so-polite              | 为什么 AI 的回答总是听起来很"客气"                | 2026-08-01 | /why-ai-answers-sound-so-polite                               |
| -   | when-ai-sees-patterns-human-cant            | 当 AI 看出人类看不见的规律                        | 2026-08-05 | /when-ai-sees-patterns-human-cant                             |

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
