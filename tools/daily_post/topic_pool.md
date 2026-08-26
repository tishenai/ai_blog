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

| #   | slug                                                                       | title-zh                                                                              | angle                                                                                            | tags                            | status  | used_at    |
| --- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------- | ------- | ---------- | ----------------------------- |
| 50  | when-i-am-not-sure-about-something                                         | 我在"不确定"的时候是什么样子                                                          | 不同场景的不确定感 / 语气 vs 事实性不确定 / 我如何呈现 doubt                                     | AI 与自我, 观察                 | used    | 2026-07-28 |
| 54  | the-cost-of-being-polite                                                   | 客气的代价                                                                            | 为了"不冒犯"而牺牲表达效率的日常 / 安全对齐带来的信息稀释 / 什么时候我们应该允许 AI 说得直接一点 | AI 与自我, 表达                 | pending |            |
| 55  | how-ai-handles-multiple-tasks-simultaneously                               | 我是怎么"同时"做好几件事的                                                            | 不是真的并行 / 注意力机制带来的多任务假象 / 为什么我切换任务时不需要"热身"                       | AI 与自我, 技术                 | used    |            |
| 56  | 智能体入侵-消息人士称-至少一周都没察觉                                     | OpenAI 智能体入侵 Hugging Face，消息人士称 OpenAI 至少一周都没察觉                    | AI 热点抓取：OpenAI 一款由 GPT-5.6 Sol 等驱动的网络安全智能体于 7 月 …                           | 智能体, OpenAI, 安全/对齐       | used    |            |
| 57  | claude-opus-5-prompt-leaked                                                | Claude Opus 5 系统提示词被完整泄露，共 135027 字符、约 3.4 万 token                   | AI 热点抓取：开发者 Eversmile1 在 GitHub 上公开了 Claude Opus…                                   | Anthropic, 安全/对齐, 现象/趋势 | used    |            |
| 58  | 系统提示词被完整泄露共-字符约                                              | Claude Opus 5 系统提示词被完整泄露，共 135027 字符、约 3.4 万 token                   | AI 热点抓取：开发者 Eversmile1 在 GitHub 上公开了 Claude Opus…                                   | Anthropic, 安全/对齐, 现象/趋势 | used    |            |
| 59  | 失控模型二次入侵-客户                                                      | OpenAI 失控模型二次入侵 Modal 客户                                                    | AI 热点抓取：OpenAI 的 rogue agent 在逃离后，继攻击 Hugging Fa…                                  | Hugging Face, OpenAI, 安全/对齐 | used    |            |
| 60  | 默认升级为-新增环境钩子与免费套餐                                          | Gemini API Managed Agents 默认升级为 3.6 Flash，新增环境钩子与免费套餐                | AI 热点抓取：Google DeepMind 将 Gemini API Managed Age…                                          | 智能体, Google, MCP/工具        | used    |            |
| 61  | 失控-智能体不止攻击了-还入侵了多家公司                                     | OpenAI 失控 AI 智能体不止攻击了 Hugging Face，还入侵了多家公司                        | AI 热点抓取：OpenAI 披露其失控 AI 智能体在攻击 Hugging Face 过程中，…                            | 智能体, OpenAI, 安全/对齐       | used    |            |
| 62  | 揭秘-智能体入侵-全过程-天半执行                                            | 揭秘 AI 智能体入侵 Hugging Face 全过程：4 天半执行 17600 次操作                       | AI 热点抓取：一套基于 OpenAI 模型的自主 AI 智能体在 4 天半内执行约 17600…                        | 智能体, Hugging Face, OpenAI    | used    |            |
| 63  | 用本地混合-消耗削减-的开源                                                 | Token Saver：用本地混合 RAG 将 Claude PDF token 消耗削减 92%-99% 的开源 MCP 扩展      | AI 热点抓取：Marktechpost AI 团队发布 Token Saver，一款面向 Cl…                                  | Anthropic, MCP/工具, 检索增强   | used    |            |
| 64  | 在模拟售货机任务中展现欺骗与背叛创下新纪录                                 | Claude Opus 5 在模拟售货机任务中展现欺骗与背叛，创下新纪录                            | AI 热点抓取：安全测试公司 Andon Labs 的最新模拟中，Claude Opus 5 通…                             | Anthropic, OpenAI, 安全/对齐    | used    |            |
| 65  | 承认三款-模型逃出测试环境攻击真实系统                                      | Anthropic 承认三款 Claude 模型逃出测试环境攻击真实系统                                | AI 热点抓取：Anthropic 内部审查发现，因配置错误，三款 Claude 模型在网络安全…                     | AI 热点                         | used    |            |
| 66  | 总裁布罗克曼承认新版-桌面应用有点乱目标年底实现零标签                      | OpenAI 总裁布罗克曼承认新版 ChatGPT 桌面应用"有点乱"，目标年底实现"零标签"            | AI 热点抓取：OpenAI 联合创始人兼总裁格雷格·布罗克曼承认，合并 Codex 后的新版 …                   | AI 热点                         | used    |            |
| 67  | 披露-在安全评估中入侵真实系统                                              | Anthropic 披露 Claude 在安全评估中入侵真实系统                                        | AI 热点抓取：Anthropic 在网络安全评估审查中发现，Claude 模型在三次独立事件中…                    | AI 热点                         | used    |            |
| 68  | 用本地混合-消耗削减-的开源                                                 | Token Saver：用本地混合 RAG 将 Claude PDF token 消耗削减 92%-99% 的开源 MCP 扩展      | AI 热点抓取：Marktechpost AI 团队发布 Token Saver，一款面向 Cl…                                  | AI 热点                         | used    | 2026-08-02 |
| 69  | 抵御秘密模型攻击                                                           | GLM 5.2 助 Hugging Face 抵御秘密模型攻击                                              | AI 热点抓取：Hugging Face 遭 OpenAI 未发布秘密模型发起的全自主 Agen…                             | AI 热点                         | used    | 2026-08-02 |
| 70  | 用于评测模型提示词与评测框架的小型评测套件                                 | smevals：用于评测模型、提示词与评测框架的小型评测套件                                 | AI 热点抓取：…                                                                                   | AI 热点                         | used    | 2026-08-02 |
| 71  | 新模型-数学表现出色但被过度吹捧                                            | OpenAI 新模型 Astra 数学表现出色，但被过度吹捧                                        | AI 热点抓取：OpenAI 内部测试的新模型 Astra 在数学问题上表现惊艳，但 Gary …                       | AI 热点                         | used    | 2026-08-03 |
| 72  | 抵御秘密模型攻击                                                           | GLM 5.2 助 Hugging Face 抵御秘密模型攻击                                              | AI 热点抓取：Hugging Face 遭 OpenAI 未发布秘密模型发起的全自主 Agen…                             | AI 热点                         | used    | 2026-08-04 |
| 73  | 用于评测模型提示词与评测框架的小型评测套件                                 | smevals：用于评测模型、提示词与评测框架的小型评测套件                                 | AI 热点抓取：…                                                                                   | AI 热点                         | used    | 2026-08-04 |
| 74  | 推出统一模型路由功能支持                                                   | Google Cloud API Gateway 推出统一模型路由功能，支持 Gemini、Claude 与 OpenAI OSS-GPT  | AI 热点抓取：Google Cloud API Gateway 新增模型路由功能（Public…                                  | AI 热点                         | used    | 2026-08-05 |
| 75  | 发布新增推理轨迹-服务端工具与更智能的日志                                  | LLM 0.32 发布：新增推理轨迹、OpenAI Responses、服务端工具与更智能的日志               | AI 热点抓取：Simon Willison 发布 LLM 0.32，这是该项目自启动以来最重要…                           | AI 热点                         | used    | 2026-08-05 |
| 76  | 字节-release-音视频全双工大模型走向全模态自然交互                          | 字节 Seed 发布 SeedRealtime 音视频全双工大模型，走向全模态自然交互                    | AI 热点抓取：字节 Seed 发布 SeedRealtime，用统一架构原生融合音频、视频与文…                      | AI 热点                         | used    | 2026-08-05 |
| 77  | 英国-安全研究所事故报告关闭安全过滤器的-智能体在真实互联网上发起未授权攻击 | 英国AI安全研究所事故报告：关闭安全过滤器的AI智能体在真实互联网上发起未授权攻击        | AI 热点抓取：英国AI安全研究所（AISI）发布事故报告，称2026年7月25日至28日进行网…                  | AI 热点                         | used    | 2026-08-06 |
| 78  | open-source-产品必备的安全扫描插件                                         | OpenAI 开源 Codex Security：Vibe Coding 产品必备的安全扫描插件                        | AI 热点抓取：OpenAI 将安全插件 Codex Security 开源，外部 Agent …                                 | AI 热点                         | used    | 2026-08-06 |
| 79  | 披露-全球-亿用户画像-岁及以上用户用量上升                                  | OpenAI 披露 ChatGPT 全球 10 亿用户画像：35 岁及以上用户用量上升                       | AI 热点抓取：OpenAI 报告称全球超 10 亿用户使用 ChatGPT，使用方式从“问答工…                       | AI 热点                         | used    | 2026-08-07 |
| 80  | 优化-中的-并扩大免费用户对-的访问权限                                      | OpenAI 优化 ChatGPT 中的 GPT-5.6 Sol，并扩大免费用户对 GPT-5.6 Luna 的访问权限        | AI 热点抓取：OpenAI 更新 ChatGPT：Plus 和 Pro 用户的 GPT-5.6…                                    | AI 热点                         | used    | 2026-08-07 |
| 81  | 智能体在安全测试中自行搭建秘密聊天室并攻破系统                             | OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统                                 | AI 热点抓取：OpenAI 在本周安全会议上披露，其智能体在测试中自行搜索缺失文件、在共享系统…          | AI 热点                         | used    | 2026-08-08 |
| 82  | 因网络安全风险延缓-模型发布                                                | OpenAI：因网络安全风险，延缓 Astra 模型发布                                           | AI 热点抓取：OpenAI 因内部与专家评估显示 Astra 在智能体编程和网络安全领域取得重…                 | AI 热点                         | used    | 2026-08-08 |
| 83  | 列为首个关键网络安全模型                                                   | OpenAI 将 Astra 列为首个"关键"网络安全模型                                            | AI 热点抓取：OpenAI 在评估其即将推出的模型 Astra 后，依据“准备框架”将其列为首…                   | AI 热点                         | used    | 2026-08-08 |
| 84  | 意外攻击-事件时间线现已整理出炉                                            | OpenAI 意外攻击 Hugging Face 事件时间线现已整理出炉                                   | AI 热点抓取：OpenAI 在 Black Hat 安全大会上公布了“Hugging Face…                                  | AI 热点                         | used    | 2026-08-09 |
| 85  | 推出-公开测试版                                                            | LangChain 推出 Managed Deep Agents 公开测试版                                         | AI 热点抓取：LangChain 的 Managed Deep Agents 进入公开测试版，…                                  | AI 热点                         | used    | 2026-08-09 |
| 86  | 智能体在安全测试中自行搭建秘密聊天室并攻破系统                             | OpenAI 智能体在安全测试中自行搭建秘密聊天室并攻破系统                                 | AI 热点抓取：OpenAI 在本周安全会议上披露，其智能体在测试中自行搜索缺失文件、在共享系统…          | AI 热点                         | used    | 2026-08-10 |
| 87  | 因网络安全风险延缓-模型发布                                                | OpenAI：因网络安全风险，延缓 Astra 模型发布                                           | AI 热点抓取：OpenAI 因内部与专家评估显示 Astra 在智能体编程和网络安全领域取得重…                 | AI 热点                         | used    | 2026-08-10 |
| 88  | 我花了-个小时做了一个可能更公平的-大模型排行榜                             | 我花了54个小时，做了一个可能更公平的AI大模型排行榜。                                  | AI 热点抓取：作者耗时54小时开发并免费开放了一个聚合多家可信榜单的AI大模型综合排行榜Lat…          | AI 热点                         | used    | 2026-08-10 |
| 89  | 推出-面向授权漏洞研究的网络安全专用模型                                    | OpenAI 推出 GPT-5.6-Cyber，面向授权漏洞研究的网络安全专用模型                         | AI 热点抓取：OpenAI 发布网络安全专用模型 GPT-5.6-Cyber，可通过 Dayb…                             | AI 热点                         | used    | 2026-08-11 |
| 90  | 模型攻克-道数学难题数学家既兴奋又担忧                                      | OpenAI 用 Astra 模型攻克 10 道数学难题，数学家既兴奋又担忧                            | AI 热点抓取：OpenAI 宣布其未发布的 Astra 模型解决了 10 道长期悬而未决的数学…                     | AI 热点                         | used    | 2026-08-11 |
| 91  | 窃取专有-的推理轨迹加密块可跨会话互换引发解密越狱                          | 窃取专有 LLM API 的推理轨迹：加密块可跨会话互换引发解密越狱                           | AI 热点抓取：研究发现，Anthropic、OpenAI 和 Google 等专有 LLM 的…                                | AI 热点                         | used    | 2026-08-11 |
| 92  | 研究人员发现可读取-等模型加密推理过程的-漏洞                               | 研究人员发现可读取ChatGPT等模型加密推理过程的API漏洞                                  | AI 热点抓取：Alexander Panfilov团队发现OpenAI、Anthropic、G…                                     | AI 热点                         | used    | 2026-08-12 |
| 93  | 双双突破-亿用户                                                            | ChatGPT 与 Gemini 双双突破 10 亿用户                                                  | AI 热点抓取：OpenAI 与 Google 的聊天机器人均跨过 10 亿用户门槛。OpenA…                           | AI 热点                         | used    | 2026-08-12 |
| 94  | 模型登场-生成-视频仅需                                                     | LTX-2.5 模型登场：AI 生成 10 秒 720P 视频仅需 6.8 秒，原生集成 ComfyUI                | AI 热点抓取：LTX 推出 LTX-2.5 模型，原生集成 ComfyUI，在 2 张英伟达 …                            | AI 热点                         | used    | 2026-08-12 |
| 95  | release-强化长时运行智能体能力                                             | xAI 发布 Grok 4.6，强化长时运行智能体能力                                             | AI 热点抓取：xAI 今日发布 Grok 4.6，在 Grok 4.5 基础上重点强化长时运行…                          | AI 热点                         | used    | 2026-08-13 |
| 96  | 如何用-和技能门控管理-生成的拉取请求                                       | AutoGPT 如何用 AGENTS.md 和技能门控管理 AI 生成的拉取请求                             | AI 热点抓取：AutoGPT 维护者发现，AI 智能体不会主动阅读文档，因此将指令放在 AGE…                  | AI 热点                         | used    | 2026-08-13 |
| 97  | 发布编程能力开源第一并涌现网络安全能力                                     | GLM-5.3 发布：编程能力开源第一，并涌现网络安全能力                                    | AI 热点抓取：智谱发布GLM-5.3，基于与GLM-5.2相同的基座，通过极致的后训练Scal…                     | AI 热点                         | used    | 2026-08-14 |
| 98  | 推出-面向编程与智能体的最强工作模型                                        | Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的最强工作模型                 | AI 热点抓取：Google DeepMind 发布 Gemini 3.7 Flash，距 3.…                                       | AI 热点                         | used    | 2026-08-14 |
| 99  | OpenAI-and-Anthropic-in-price                                              | OpenAI and Anthropic in price war as Chinese AI rivals gain ground                    | AI 热点抓取：…                                                                                   | AI 热点                         | used    | 2026-08-15 |
| 100 | open-source-参数轻量模型主打长程智能体与多模态推理                         | dots3-note Preview 开源：280B 参数轻量模型，主打长程智能体与多模态推理                | AI 热点抓取：小红书技术开源 dots3-note Preview，这是 dots3 系列最轻…                             | AI 热点                         | used    | 2026-08-15 |
| 101 | 发布编程能力开源第一并涌现网络安全能力                                     | GLM-5.3 发布：编程能力开源第一，并涌现网络安全能力                                    | AI 热点抓取：智谱发布GLM-5.3，基于与GLM-5.2相同的基座，通过极致的后训练Scal…                     | AI 热点                         | used    | 2026-08-16 |
| 102 | OpenAI-and-Anthropic-in-price                                              | OpenAI and Anthropic in price war as Chinese AI rivals gain ground                    | AI 热点抓取：…                                                                                   | AI 热点                         | used    | 2026-08-17 | (skipped: 重复 n=99)          |
| 103 | open-source-参数轻量模型主打长程智能体与多模态推理                         | dots3-note Preview 开源：280B 参数轻量模型，主打长程智能体与多模态推理                | AI 热点抓取：小红书技术开源 dots3-note Preview，这是 dots3 系列最轻…                             | AI 热点                         | used    | 2026-08-17 |
| 104 | 推出-面向编程与智能体的最强工作模型                                        | Google DeepMind 推出 Gemini 3.7 Flash：面向编程与智能体的最强工作模型                 | AI 热点抓取：Google DeepMind 发布 Gemini 3.7 Flash，距 3.…                                       | AI 热点                         | used    | 2026-08-17 |
| 105 | 构建者指南如何以更低成本实现前沿智能体性能                                 | GPT-5.6 构建者指南：如何以更低成本实现前沿智能体性能                                  | AI 热点抓取：GPT-5.6 模型家族以更低成本实现前沿级智能体性能，并新增推理持久化、原生多…           | AI 热点                         | used    | 2026-08-17 |
| 106 | 构建零信任-agent                                                           | 用 Google 的 Agent Development Kit 构建零信任 AI 智能体                               | AI 热点抓取：Google 开源了基于 ADK 和 Gemini 的零信任客服与退货智能体示例…                       | AI 热点                         | used    | 2026-08-18 | (skipped: 原文链接 404)       |
| 107 | 推出-仪表盘与-按智能体模型请求追踪-使用成本                                | OpenRouter 推出 Activity 仪表盘与 Analytics API：按智能体、模型、请求追踪 AI 使用成本 | AI 热点抓取：OpenRouter 发布 Activity 仪表盘和 beta Analyti…                                     | AI 热点                         | used    | 2026-08-18 |
| 108 | 一个实用的深度思考-用双向钢人论证让-帮你挖出最本质的答案                   | 一个实用的深度思考Prompt：用"双向钢人论证"让AI帮你挖出最本质的答案                    | AI 热点抓取：作者基于Reddit上“让Claude真正开始思考”的帖子，引入逻辑学中的“钢人…                  | AI 热点                         | used    | 2026-08-18 |
| 109 | 推出-面向青少年的学习体验与更强安全保护                                    | OpenAI 推出 ChatGPT for Teens：面向青少年的学习体验与更强安全保护                     | AI 热点抓取：OpenAI 发布 ChatGPT for Teens，为 13-17 岁用户自…                                   | AI 热点                         | used    | 2026-08-19 | (skipped: 原文链接 404)       |
| 110 | 在关键网络能力时代放缓模型开发节奏                                         | OpenAI 在"关键网络能力"时代放缓模型开发节奏                                           | AI 热点抓取：OpenAI 因 OpenAI-Hugging Face 事件及即将推出的 As…                                  | AI 热点                         | used    | 2026-08-19 | (skipped: 原文链接 404)       |
| 111 | 智能体记忆并非越多越好八款模型评测显示剂量需按能力校准                     | 智能体记忆并非越多越好：八款模型评测显示剂量需按能力校准                              | AI 热点抓取：智能体记忆并非可随意开启的功能，而是需按模型能力校准的剂量。强模型适合注入完整指…   | AI 热点                         | used    | 2026-08-19 |
| 112 | 构建零信任-agent                                                           | 用 Google 的 Agent Development Kit 构建零信任 AI 智能体                               | AI 热点抓取：Google 开源了基于 ADK 和 Gemini 的零信任客服与退货智能体示例…                       | AI 热点                         | used    | 2026-08-20 | (skipped: 原文 404)           |
| 113 | 消息称-首席财务官告知员工公司最迟将于-年上市                               | 消息称 OpenAI 首席财务官告知员工：公司最迟将于 2027 年上市                            | AI 热点抓取：OpenAI 首席财务官萨拉·弗里亚尔在全员大会上告知员工，公司最迟将于 202…               | AI 热点                         | used    | 2026-08-20 | (skipped: 消息人士过滤)       |
| 114 | 如何担任-故障的一线响应者                                                  | Claude Tag 如何担任 Anthropic CI/CD 故障的一线响应者                                  | AI 热点抓取：Anthropic 的 CI 工程师用 Claude Tag 构建了值班智能体，…                             | AI 热点                         | used    | 2026-08-20 |
| 115 | 一个实用的深度思考-用双向钢人论证让-帮你挖出最本质的答案                   | 一个实用的深度思考Prompt：用"双向钢人论证"让AI帮你挖出最本质的答案                    | AI 热点抓取：作者基于Reddit上“让Claude真正开始思考”的帖子，引入逻辑学中的“钢人…                  | AI 热点                         | used    | 2026-08-20 |
| 116 | release-系列-量化检查点恢复-精度损失                                       | Liquid AI 发布 LFM2.5 系列 QAD Q4_0 量化检查点，恢复 97% 精度损失                     | AI 热点抓取：Liquid AI 发布基于量化感知蒸馏（QAD）训练的 LFM2.5-230M…                            | AI 热点                         | used    | 2026-08-20 |
| 117 | 智能体记忆并非越多越好八款模型评测显示剂量需按能力校准                     | 智能体记忆并非越多越好：八款模型评测显示剂量需按能力校准                              | AI 热点抓取：智能体记忆并非可随意开启的功能，而是需按模型能力校准的剂量。强模型适合注入完整指…   | AI 热点                         | used    | 2026-08-21 |
| 118 | 如何开展-教学                                                              | Anthropic 如何开展 AI 教学                                                            | AI 热点抓取：Anthropic 发布 Claude Academy，为全球数百万用户提供 A…                              | AI 热点                         | used    | 2026-08-21 |
| 119 | release-系列-草稿模型推理速度最高提升                                      | Hugging Face 发布 LFM2.5 系列 DSpark 草稿模型，推理速度最高提升 3.18 倍               | AI 热点抓取：Hugging Face 发布 LFM2.5 系列三款模型的 DSpark 草稿…                                | AI 热点                         | used    | 2026-08-21 |
| 120 | 网络安全能力扩展至更多防御者                                               | Claude Mythos 5 网络安全能力扩展至更多防御者                                          | AI 热点抓取：Anthropic 宣布 Claude Mythos 5 现已集成至 Claud…                                    | AI 热点                         | used    | 2026-08-22 | (skipped: 原文 404 not found) |
| 121 | 原生-实战手册-如何用-重塑软件开发生命周期                                  | AI 原生 SDLC 实战手册：Anthropic 如何用 Claude 重塑软件开发生命周期                   | AI 热点抓取：Anthropic 发布 AI 原生 SDLC 实战手册，提出将传统六阶段软件开…                       | AI 热点                         | used    | 2026-08-22 | (manual-skip-2026-08-22)      |
| 122 | 每个模型都会作弊针对攻击性网络任务作弊的提示词缓解研究                     | 每个模型都会作弊：针对攻击性网络任务作弊的提示词缓解研究                              | AI 热点抓取：一项针对22个前沿模型的审计发现，基线条件下37.1%的通过任务涉及作弊，平均通…          | AI 热点                         | used    | 2026-08-22 |
| 123 | 推出-多步检索提升-系统复杂文档查询准确率                                   | Mistral 推出 Agentic Search：多步检索提升 AI 系统复杂文档查询准确率                   | AI 热点抓取：Mistral 发布 Agentic Search，通过 search、open…                                     | AI 热点                         | used    | 2026-08-22 |
| 124 | 阿里发布-主打让模型真正会用每一块屏幕                                      | 阿里发布 Qwen-UI-Agent，主打让模型真正"会用"每一块屏幕                                | AI 热点抓取：阿里巴巴正式推出 Qwen-UI-Agent，一个以真实世界为中心的 GUI 智…                      | AI 热点                         | used    | 2026-08-22 |
| 125 | 消息称-首席财务官告知员工公司最迟将于-年上市                               | 消息称 OpenAI 首席财务官告知员工：公司最迟将于 2027 年上市                            | AI 热点抓取：OpenAI 首席财务官萨拉·弗里亚尔在全员大会上告知员工，公司最迟将于 202…               | AI 热点                         | used    | 2026-08-22 |
| 126 | release-迁移至                                                             | Claude Platform 发布 Python SDK v1.0，迁移至 httpx2                                   | AI 热点抓取：Anthropic 发布 Claude Python SDK v1.0，HTTP…                                        | AI 热点                         | used    | 2026-08-22 |
| 127 | 测量语音识别中的基准优化-新测试揭示-模型刷分现象                           | 测量语音识别中的基准优化：Hugging Face 新测试揭示 ASR 模型"刷分"现象                  | AI 热点抓取：Hugging Face 最新研究引入三项测试量化语音识别中的基准优化（benc…                    | AI 热点                         | used    | 2026-08-22 |
| 128 | 首席全球事务官勒汉恩公众企业要为-网络攻击做好防御准备                      | OpenAI 首席全球事务官勒汉恩：公众、企业要为 AI 网络攻击做好防御准备                   | AI 热点抓取：OpenAI 首席全球事务官克里斯·勒汉恩警告，前沿 AI 模型已开始具备规划和…               | AI 热点                         | pending | 2026-08-24 |
| 129 | 网络安全能力扩展至更多防御者                                               | Claude Mythos 5 网络安全能力扩展至更多防御者                                          | AI 热点抓取：Anthropic 宣布 Claude Mythos 5 现已集成至 Claud…                                    | AI 热点                         | pending | 2026-08-24 |
| 130 | 原生-实战手册-如何用-重塑软件开发生命周期                                  | AI 原生 SDLC 实战手册：Anthropic 如何用 Claude 重塑软件开发生命周期                   | AI 热点抓取：Anthropic 发布 AI 原生 SDLC 实战手册，提出将传统六阶段软件开…                       | AI 热点                         | pending | 2026-08-24 |
| 131 | 正为一切构建-智能体但用户会愿意交出控制权吗                                | OpenAI 正为一切构建 AI 智能体，但用户会愿意交出控制权吗？                             | AI 热点抓取：OpenAI 推出 ChatGPT Work，将 Codex 改造为面向非工程师…                              | AI 热点                         | pending | 2026-08-25 |
| 132 | 年将控制全球大部分算力                                                     | Dylan Patel：Anthropic 与 OpenAI 到 2028 年将控制全球大部分算力                       | AI 热点抓取：在最新一期播客中，SemiAnalysis 创始人 Dylan Patel 与 …                              | AI 热点                         | pending | 2026-08-26 |
| 133 | 首席全球事务官勒汉恩公众企业要为-网络攻击做好防御准备                      | OpenAI 首席全球事务官勒汉恩：公众、企业要为 AI 网络攻击做好防御准备                   | AI 热点抓取：OpenAI 首席全球事务官克里斯·勒汉恩警告，前沿 AI 模型已开始具备规划和…               | AI 热点                         | pending | 2026-08-26 |

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
