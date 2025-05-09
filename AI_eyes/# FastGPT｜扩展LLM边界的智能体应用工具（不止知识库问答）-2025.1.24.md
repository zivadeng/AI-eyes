# FastGPT｜扩展LLM边界的智能体应用工具（不止知识库问答）
> 2025.1.24
## 来自FastGPT深度使用者的分享：
1. fastGPT是什么
2. 可以用fastgpt来干嘛（正门和偏门）
3. 我遇到的坑Q&A（省时省力）

### fastGPT是什么
官方一句话说明：让logo更懂您的知识。
--基于LLM大模型的开源AI知识库构建平台。提供了开箱即用的数据处理、模型调用、RAG检索、可视化AI 工作流编排等能力，帮助您轻松构建复杂的 AI 应用。

我通过fastGPT，创建基于LLM大模型能力，解决特定业务的应用程序，通常我们称之为实现特定目标的agent智能体。
1、友好支持使用：
- 支持免登录浏览器窗口直接使用；
- 飞书/微信/钉钉API集成使用；
- 自研系统API接口调用。

2、内部支持多底座AI大模型，直接调用多基座大模型能力：
- 国际版如fastGPT、Claude、Gemini、Llama等；
- 国内版如kimi、doubao、Deepseek、step等；

3、通过【编排能力】支持实现特定目标：
- 工作流，节点支持基座AI模型、向量知识库检索、插件和工具调用，扩展AI大模型的能力边界；
- 通过向量知识库给予特定背景知识；
- 通过清晰的逻辑步骤人为的让LLM step by step。

## 可以用fastgpt来干嘛

工作流在AI模型的基础上，可以定义业务逻辑，满足输出对话之外的需求。如：
- 批处理图片识别，并输出记录到表。
- 通过意图识别调用不同的知识库，实现更精准的知识问答。

插播一条我自己在用的黑魔法：
创建一个通用工作流调用gpt来使用fastGPT（国际版不太稳定，作为国内LLM chatBot的补充很不错）
同时增加设计入参来调用不同模型进行对比测试也能帮助我提升部分选型测试Prompt类的工作效率。

## 我遇到的坑Q&A
在3个多月来的实践中，一些基于摸索和经验的小问题点（自己也常常边用边忘），
分享在此，希望可以帮助使用fastGPT的小伙伴们提高效率。

- （官方）推荐使用fastFGPT小助手问答来答疑解惑。
- （官方）推荐bug群可以友好互助。
- 如何不然AI模型输出对话？
  - 默认会输出对话回复，当使用多AI节点step by step 解决问题时， 可以在前序处理的节点-AI模型配置项里，关闭“流输出”，即可关闭本次回答，此时就可以仅作为中间产物提供给下一步使用。 
- 多模态AI模型支持情况：
  - 多模态指的是大模型天然支持文本（文字），视觉（图片、视频）、语音、文件等各种模态的输入，并根据输入进行输出。
  - 取决于AI基座模型是否支持多模态，如果支持，在AI模型配置项里，可打开“图片识别”。
  - 目前国内主流还是区分文本模型和视觉模型，fastGPT天然支持图片识别，doubao-version可支持图片识别）
  - 测试下来，目前大模型只可以单独识别图片或文本，当文件内既包含图片和文字，默认只会处理到文字。
- 如何支持模块化调用？ 目的是将通用功能标准化/产品化，如通用的意图识别模块，QA向量处理模块。
  - 通用工作流可在团队应用中拉取引用。
- 如何灵活调用不同知识库？ 
  - 定义自定义变量【数据类型要选择”选择知识库“】，通过不同知识库id传参调用到1-N个知识库；
  - 选择知识库变量的数据类型是数组：[{"datasetId":"知识库ID1"},{"datasetId":"知识库ID2"}]（当时传参知识库id死活不行，直到在问题群得到官方解答是数组类型..）
