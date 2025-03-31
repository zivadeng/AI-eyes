## 背景
Agent智能体是LLM大模型商业落地的最佳方案，
它扩展了生成式 AI 模型的出厂能力。
2024 年 Google 团队关于 AI Agent（智能体）的技术白皮书，
全面介绍了 AI Agent 相关知识，整理输出如下：

## 定义
人类借助工具处理复杂任务，
生成式AI模型也可通过使用工具获取实时信息、
给出行动建议，
**具备推理、逻辑和访问外部信息能力的生成式AI模型就是 Agent**，
它扩展了生成式 AI 模型的出厂能力。

## Agent的定义与架构

###概念：
Agent是一种应用程序，能观察世界、使用工具实现目标，具有自主性，可处理模糊指令。

### 架构与组件：
**由模型、工具、编排层构成**。
- 模型是核心决策语言模型；
- 工具帮助 Agent 与外部互动，扩展行动范围；
- 编排层负责信息接收、推理、决策和行动的循环过程。

### 与模型的区别：
Agent能通过工具扩展知识、有状态且自带工具和逻辑层，
而模型知识局限于训练数据、无状态、无原生工具和逻辑层 。

### 认知架构与推理框架
类比厨师做菜：厨师根据顾客需求和食材做菜，过程包含信息收集、推理和行动，并根据反馈调整，这与 Agent的工作方式类似。

### 推理框架：
ReAct为语言模型提供思考策略；
Chain-of-Thought 通过中间步骤实现推理；
Tree-of-Thoughts 适合探索性任务。
以 ReAct 为例，Agent 接收用户查询后，按提示生成思考、行动、行动输入、观察，循环直至给出最终答案。

### 工具类型
Extensions：是连接 API 与 Agent 的组件，通过提供示例和参数，让 Agent 调用外部 API，如 Google 的 Code Interpreter extension 可从自然语言生成和运行 Python 代码。
Functions：模型设置函数并决定使用时机和参数，在客户端执行，可使模型结构化输出信息，方便其他系统解析。
Data Storage：通过向量数据库为Agent提供动态更新信息，用于检索增强生成（RAG），提升模型返回的相关性和实效性。

### 提升模型性能的学习方式
In-context learning：推理时为模型提供提示词、工具和示例，让其 “即时学习”，如 ReAct 框架。
Retrieval-based in-context learning：从外部存储检索信息填充模型提示词，如 RAG 架构。
Fine-tuning based learning：用特定示例训练模型，使模型具备使用工具的先验知识。

### 创建 Agent 的实践
基于 LangChain：使用 LangChain 和 LangGraph 开源库，结合 SerpAPI 和 Google Places API 等工具，可快速构建 Agent 原型。
Google Vertex AI Agent：介绍了其在Google产品中的应用架构，各组件协同工作以实现复杂功能。

### 总结
Agent 借助工具扩展语言模型能力，完成复杂任务，核心是编排层，不同推理技术和工具类型为其提供支持。未来 Agent 将更强大，“Agent chaining” 是发展方向，开发中需持续迭代。


中文版：
AI Agent（智能体）技术白皮书（Google，2024）

英文原版链接：
https://drive.google.com/file/d/1oEjiRCTbd54aSdB_eEe3UShxLBWK9xkt/view?pli=1

​