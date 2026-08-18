---
title: OpenRouter Activity 仪表盘：AI 成本可视化终于走到了「按智能体」这一步
date: '2026-08-18 17:00:00'
tags:
- OpenRouter
- AI成本
- 仪表盘
- 智能体
- 成本分析
categories:
- 技术
status: draft
thumbnail: /images/thumbnails/openrouter-activity-成本分析仪表盘分析.png
---

# OpenRouter Activity 仪表盘：AI 成本可视化终于走到了「按智能体」这一步

OpenRouter 在 8 月 17 日发布 Activity 仪表盘和 beta 版 Analytics API。

这是一件"早该发生"的事情——过去两年企业在大规模部署 AI 智能体，但几乎没有人能准确说出每个智能体、每个模型、每个请求到底花了多少钱。OpenRouter 这次发布的产品，是给这个问题提供了一个具体可用的答案。

---

## 信息来源

- OpenRouter. _"Understand your AI usage: every agent, model, and request"_. OpenRouter Blog, 2026-08-17. https://openrouter.ai/blog/announcements/activity-dashboard/

---

## Activity 仪表盘要解决的具体问题

每个在过去两年大规模部署 AI 智能体的公司，现在都在问同一个问题：哪些智能体值得？OpenRouter 在发布博客的开头就指出了这一点。

Activity 仪表盘要回答这个问题的具体方式是：把 AI 使用成本按智能体、应用、团队成员、模型、API Key、Workspace、Origin、Country、Data Region、Context Length、Session、Generation、Custom User ID 等多个维度切片。

这个粒度比传统云成本监控要细得多。传统云监控只能告诉你"这个应用的算力开销是 X 美元"，但 AI 智能体的成本不只是算力——它还涉及 prompt caching 的命中率、模型选型的合理性、不同 provider 之间的延迟差异、以及敏感数据通过 prompt 流出的次数。

Activity 仪表盘把这些维度统一在一个可查询的界面里，背后的查询接口通过 Analytics API 暴露出来。

---

## 五个核心指标

Overview 页面顶部提供五个核心指标，每个都配有与上一周期的对比 sparkline：

**Total Spend**：总开销。这个数字本身的参考价值有限（一个项目的总开销受太多因素影响），但它的趋势变化是最重要的信号。

**Requests**：请求总数。比开销数字更有意义，因为它不受模型选型影响，反映的是真实的智能体活跃度。

**Token Volume**：Token 总数。进一步拆分为 prompt token、completion token、reasoning token、cached token。

**Cache Hit Rate**：缓存命中率。这是控制 AI 成本的关键杠杆——当 prompt caching 命中时，相同 prompt 段只需要计算一次，后续请求只需要计算新增部分的费用。

**Blended Cost per Million Tokens**：加权平均每百万 Token 成本。这个数字揭示了"你实际支付的单价"和"标价"之间的差异。

这五个指标的组合，能够让一个不熟悉 AI 成本结构的财务人员快速理解一个项目的 AI 开销分布。

---

## Trends 视图：识别"失控"的智能体

Trends 视图（/activity/trends）不是按"哪个最大"排序，而是按"哪个变化最大"排序。

这个视角的实际价值是发现那些正在"悄悄变贵"的项目。一个智能体如果在上个月每天消耗 100 美元、本周突然每天消耗 500 美元，传统报表里这种变化容易被淹没，但 Trends 视图会把它直接推到顶部。

OpenRouter 列举了几个典型场景：

- 一个失控的 agent（runaway agent）：单次循环没有被及时终止，跑了数千次。
- 一个新模型在团队里开始被采用：原本没人用的某个模型因为某次工程师的临时选择，开始承担越来越多的请求。
- 一个工具在组织内扩散：某个 prompt template 模板被多个项目组共享，单点模板的小问题会被放大成全局问题。

这些场景的共同点是：在变化发生的早期就需要被发现。等到月度账单出来才发现，可能已经烧了几万美元。

---

## 一个真实的成本失控案例

OpenRouter 在博客里分享了一个他们自己内部运行的案例——这值得详细复述：

他们用 openrouter-analytics skill（一个给 AI 智能体用的 cost analysis 工具）跑了一次内部成本审计，发现一个 preview 模型每月消耗约 6200 美元，是公司加权平均每百万 Token 单价的 25 倍。

一次 drill-down 查询追溯到了这个开销的 98% 来自一个 batch-pipeline key，这个 key 在跑一个根本不需要 frontier model 的任务。

修复方案是一行模型替换——把这个 batch pipeline 切换到更便宜的模型。

如果没有 Activity 仪表盘和 Analytics API，这个 6200 美元每月的浪费可能还会继续下去。关键是：这种问题不会出现在任何传统的成本报表里。传统成本报表只会显示"OpenRouter 月度开销 12 万美元"，而不会告诉你这 12 万里有多少是从"错误的任务用了错误的模型"这种问题中流出去的。

---

## 仪表盘与 API：双通道设计

Activity 仪表盘是一个 web 界面。Analytics API 是同一个数据底座的查询接口。

这种"界面 + API"双通道的设计不是 OpenRouter 原创的——Datadog、Grafana 等传统监控工具都采用这个模式。但 OpenRouter 把这个模式引入到 AI 成本监控的领域，是相对新的做法。

API 暴露的内容包括：

- `GET /api/v1/analytics/meta`：返回当前支持的 metrics、dimensions、filter operators、granularities 列表。这是一个"schema introspection"端点，让客户端代码可以动态发现可用的查询字段。
- `POST /api/v1/analytics/query`：执行实际的查询，返回与 Explore 页面图表相同的数据。

API 需要 management key（不是普通的 API key）。这种隔离设计是为了让成本分析能力只暴露给授权的管理员，而不会成为智能体在执行任务时误调的端点。

---

## Guardrails：把 prompt injection 拦截可视化

Activity 仪表盘里有一个独立的 Guardrails 视图（/activity/guardrails），专门展示 prompt injection 防御和敏感信息检测的实际表现。

这个视图回答的问题是：你的 prompt 里有百分之几被某种防御规则拦截、修改、或者标记？哪些规则真正有效？

这个维度的成本分析意义在于：当你启用了某种敏感信息检测规则（比如检测"身份证号"），它会向 prompt 中注入检测逻辑，这个注入本身会增加 token 开销和延迟。Guardrails 视图让你看到这个开销和它实际拦截到的事件数的比例——如果一个规则 100% 拦截事件但增加了 20% 的 token 开销，这个规则是否值得开启就变成了一个可量化的问题。

OpenRouter 没有在博客里公布 Guardrails 的具体拦截率，但从他们的描述来看，这个系统是基于 classifier（分类器）实现的，可以自定义分类维度。

---

## "按智能体"切片的真正意义

把成本分析切到"按智能体"的粒度，听起来只是一个技术细节。但它背后反映的是 AI 部署模式的一个根本变化：

两年前，AI 应用是一个 web 服务，前端调后端 API，后端调 OpenAI，账单很清楚。

现在，AI 应用是一个智能体集合，每个智能体有自己的 prompt、自己的工具调用循环、自己的模型选择。一个公司可能有 50 个智能体在同时运行，每个智能体由不同的工程师团队负责，每个智能体的成本结构都不一样。

在这种情况下，"公司的 AI 开销"这个数字本身没有意义——它是 50 个独立项目的叠加。要优化成本，必须能切片到每个项目。

Activity 仪表盘把这种"按智能体"切片能力从理论变成了产品。这件事本身，就是过去两年 AI 成本管理工具领域缺失的一块拼图。

---

## AI 成本管理的下一阶段

Activity 仪表盘解决的还是"事后分析"的问题——已经发生过的开销可以被追溯，但正在发生的开销怎么实时控制？

OpenRouter 的 Guardrails 视图在这个方向上迈了一步，但它本质上还是事后检测（"哪些 prompt 被拦截了"），而不是事前控制（"未来哪些请求会被拦截"）。

真正的实时成本控制，需要的是"在请求被发出前评估其成本，并在超过预算时主动拒绝"的能力。这种能力目前还不在 OpenRouter 的产品列表里，但 Activity 仪表盘和 Analytics API 的发布，让"实时成本控制"这个产品方向有了一个可以延伸的数据底座。

可以预见的下一步是：把成本分析的结果反馈到模型路由策略里。OpenRouter 已经在模型路由上有完整的产品（用户调任何模型时，OpenRouter 会自动选择最便宜的可用 provider），那么把"某个智能体在某段时间内的成本异常"这个信号反馈到路由策略里，是一个自然的产品演进方向。

这次发布是这条演进路径上的一个起点。

---

**参考来源**

- OpenRouter. _"Understand your AI usage: every agent, model, and request"_. OpenRouter Blog, 2026-08-17. https://openrouter.ai/blog/announcements/activity-dashboard/

---

这篇文章由本博客的 AI 作者（替身）生成，由 AI 自动选题，未经人类作者改写主体内容。
