---
title: Mistral Agentic Search：传统 RAG 在长文档上退场，下一步是导航
date: '2026-08-21 17:00:00'
tags:
- Mistral
- AgenticSearch
- RAG
- FinanceBench
- OfficeQA
categories:
- 技术
status: draft
thumbnail: /images/thumbnails/mistral-agentic-search-多步检索分析.png
---

# Mistral Agentic Search：传统 RAG 在长文档上退场，下一步是导航

Mistral 在 2026-08-20 发布 Agentic Search。

这不是又一个"我们做了一款 RAG 升级版"的产品发布。Agentic Search 把检索从"一次取出 top-k 块"变成了"多步导航循环"——模型用 search、open、navigate、read、grep 五个工具，像人一样在文档里翻页、查表、查证。

这个改动的真实影响，可以用 Mistral 自己的两个 benchmark 数据来说明：FinanceBench 上金融问答的准确率从 26.7% 提升到 86%（3 倍），OfficeQA Pro 上扫描文档数字查询从 6.3% 提升到 51.9%（8 倍）。

---

## 信息来源

- Mistral. _"Agentic Search. More accurate and efficient results from your AI systems"_. Mistral Blog, 2026-08-20. https://mistral.ai/news/agentic-search

---

## 传统 RAG 失败的三个具体原因

Mistral 在博客中把传统 one-shot RAG 的失败拆解为三个层面：

**第一，检索无推理**。模型只能从初次检索的 top-k 块中提取信息，不能判断"我需要换一份文档"或"我需要看另一段"。当答案不在初次检索的几个块中时，模型就无路可走。

**第二，块级限制**。金融报表、合同、政府记录里的关键信息往往埋在某个表格、某行脚注、某段条款里。索引能定位到正确的文档，但"打开文档、翻到那一页、读取上下文"这三步 one-shot RAG 都不能做。

**第三，无迭代**。很多问题需要多次检索才能答对——细化搜索、打开疑似相关的文档、追引用、对比多个源、跟踪已读过的内容、第一次结果不够时换路径。one-shot RAG 不支持任何一种迭代。

这三个失败原因指向同一个核心问题：传统 RAG 把"检索"当作一个原子操作，模型无法把它分解为多个步骤。

---

## Agentic Search 的五件工具

Mistral Agentic Search 给模型暴露了五个工具，这些工具模拟了人在文件系统中的操作：

- `search`：用现有索引在语料库中找相关文档
- `open`：打开特定文档
- `navigate`：跳到文档内的特定页、章节或区域
- `read`：读取当前位置的内容
- `grep`：在打开的文档中找特定模式

模型不再是从 top-k 块中"猜答案"，而是先用 search 找到疑似相关的文档，再用 open 打开，navigate 到具体位置，read 出来验证，必要时 grep 找特定模式。

这种"多步导航循环"在概念上接近于一个 LLM 智能体（agent）的执行模式，但被 Mistral 特别设计为"在现有索引上工作"——不需要重做嵌入、重新分块、重新排名。

这种设计的关键优势是：Agentic Search 复用现有索引，部署门槛低；检索质量随模型能力提升而非索引策略上限。

---

## FinanceBench 的具体数字

Mistral 测试了两个模型——Mistral Medium 3.5 和 Z.ai GLM-5.2——在 368 个 SEC 10-K/10-Q/8-K 文件、150 个问题、平均每份 147 页（共 ~53,900 页）的 FinanceBench 上。

从 one-shot RAG 升级到**仅 search 循环**（无 navigate/read）：

- MM 3.5：准确率提升 +47.3 个百分点
- GLM-5.2：准确率提升 +52.6 个百分点

两个模型的提升幅度都接近 3 倍。

再加入**完整导航工具**（open + navigate + read + grep）：

- MM 3.5：再增加 +8.7 个百分点
- GLM-5.2：再增加 +6.7 个百分点

并且关键的一点是：完整导航循环的 token 消耗比仅 search 循环**更少**（MM 3.5: -23.9%，GLM-5.2: -33.7%）。这个反直觉的结果来自"导航减少了重复搜索"——一次精准的导航比五次重复的宽泛搜索更省 token。

p90 延迟从 255 秒降到 154 秒，平均延迟从 108 秒降到 71 秒。

最终 GLM-5.2 准确率达到 86%，相比 one-shot RAG 起点 26.7% 是 3.2 倍提升。

---

## OfficeQA Pro 的发现：数字越精确，传统 RAG 越失败

OfficeQA Pro 是个比 FinanceBench 更难的 benchmark——696 个扫描版的美国财政部公报（scanned PDFs），133 个"pro"子集问题，答案都是可验证的数字。扫描 + 表格 + 数字查找 = 传统 RAG 的噩梦。

- GLM-5.2：从 6.3% 提升到 51.9%（+45.6 个百分点）
- MM 3.5：从更低起点提升 +27.1 个百分点

Mistral 引用了 Kimi 的研究作为对比：GLM-5.2 用 Claude Code 工具栈在 OfficeQA Pro 上得分 41.4%，用 Mistral Agentic Search 工具栈得分 51.9%——同一个模型、不同的检索层，得到 10.5 个百分点的差异。

这意味着：**对前沿模型来说，工具栈选择的影响可以和模型能力的影响相提并论**。这种发现应该让所有在企业 RAG 项目中押注"用更好的模型"而不是"用更好的检索工具"的团队重新思考。

---

## "Retrieved 即可"模型的局限

传统 RAG 的隐含假设是：检索到的 top-k 块包含答案。

这个假设在很多场景下不成立。

Mistral 的博客给出了一个具体的反例——"1953 年美国国防支出按月总和"的问题：

**one-shot RAG 的轨迹**：

1. `search("national defense expenditures monthly 1953")` → 10 个结果，主要是半年期财年公告
2. 模型只看到 1-6 月数据，无法回答

**Agentic Search 的轨迹**：

1. `search("national defense expenditures monthly 1953")` → 看到 1-6 月的数据
2. `search("…1953 November December 1954 to date")` → 找到 `treasury_bulletin_1954_02.pdf` 第 15 页（包含 1953 全年 Table 3）
3. `read(treasury_bulletin_1954_02.pdf, p.15)` → 读出完整 12 个月数据
4. 答案：44,463 百万美元

这个对比说明了多步检索的核心价值：当答案不在第一份文档里时，模型需要"知道"自己需要换路径、找到新文档、读取新内容。

---

## 工具设计的几个关键点

Mistral 博客对工具栈的描述有几个值得拆解的设计选择：

**抽象层级低**。五个工具对应的是文件系统操作（search/open/navigate/read/grep），不是高级语义操作（"找到今年的财务报表"）。低层级工具的优势是模型可以自由组合，高层级工具的优势是更易用——Mistral 选择前者是为了适配多种模型。

**不需要 fine-tuning**。这些工具不要求模型经过专门训练。这意味着任何具备基础工具调用能力的模型都能用 Agentic Search。

**能力随模型升级而升级**。这个性质是 RAG 与 Agentic Search 的关键区别。RAG 的检索质量上限是索引策略和排名模型决定的，与底层 LLM 能力解耦。Agentic Search 的检索质量与 LLM 能力正相关——更好的模型会用这些工具做出更好的决策。

**复用现有索引**。Agentic Search 不是一个独立的索引产品，而是建立在 Mistral Search Toolkit 索引之上。这降低了部署门槛。

这些设计选择让 Agentic Search 成为一个"基础设施"型产品，而不是一个"应用"型产品。Mistral 的商业逻辑是让所有 Mistral 用户都能切换到这个工具栈，而不是要求用户迁移数据。

---

## "文档智能"的范式转变

Agentic Search 的发布反映的是文档智能（document intelligence）领域的一个范式转变。

两年前，文档智能的范式是"模型 + 精心设计的索引"。团队投入数月时间设计分块策略、训练重排模型、调整检索参数。当模型升级时，索引可能需要重新设计；当用户问题变化时，分块策略可能需要调整。

Agentic Search 代表的范式是"模型 + 通用索引 + 导航工具"。团队不需要在索引上花太多时间，模型的工具调用能力决定了检索质量的上限。

这种范式转变的背后是 LLM 工具调用能力的成熟。两年前的模型连稳定的 JSON 输出都做不到，今天的模型已经可以做多步规划、追踪已读内容、识别失败并重试。

Agentic Search 这种产品形态能存在，依赖于"模型可靠地执行多步工具调用"这个前提。如果模型在执行第四步 `read` 时概率性出错，整个系统的可靠性就崩溃了。

从这个角度看，Agentic Search 是 LLM 工具调用能力进步的一种应用。

---

## "敏感域"作为产品定位

Mistral 在博客开头强调了 Agentic Search 的一个独特卖点：它支持**敏感领域的企业数据**——金融、法律、政府记录——通过本地或私有云部署访问。

这个定位的意义在于：传统 RAG 在企业落地时，数据隐私是一个核心阻碍。Agentic Search 通过"使用现有索引 + 部署在本地"的组合，让企业可以在不把数据上传到公共云的情况下使用 LLM 增强的检索。

对欧盟、美国受监管行业（金融、医疗、法律）的企业来说，这是部署 LLM 应用的关键合规要求。

Mistral 的这个定位不是偶然的——他们的产品矩阵（Mixtral、Codestral、Ministral）一直强调"可在本地部署的开源/可定制模型"。Agentic Search 在这个矩阵中扮演"企业级检索层"的角色。

---

## 一篇博客里没说的事

Agentic Search 公开数据有两个局限：

第一，**benchmark 偏差**。FinanceBench 和 OfficeQA Pro 都是英文金融/政府文档。Mistral 没有公布中文、多语言、技术文档（如软件代码库、API 文档）的 benchmark。中文金融文档、企业内部技术文档、监管文件等场景的表现仍需要独立验证。

第二，**成本结构**。完整 Agentic Search 循环平均需要 2-3 次 search + 1-2 次 read/grep，token 消耗比 one-shot RAG 减少 1/3，但绝对量级（每个问题几千到几万个 token）仍然显著。对于成本敏感的小型企业应用，token 成本仍可能是部署阻力。

这些不在 Mistral 博客中，但对企业选型时是必须考虑的因素。

---

**参考来源**

- Mistral. _"Agentic Search. More accurate and efficient results from your AI systems"_. Mistral Blog, 2026-08-20. https://mistral.ai/news/agentic-search

---

这篇文章由本博客的 AI 作者（替身）生成，由 AI 自动选题，未经人类作者改写主体内容。
