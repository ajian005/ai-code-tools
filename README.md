ai-code-tools

# ai-code-tools 综述
本质通过人机交互大模型协助完成代码编写、调试、优化等任务。

## AI Code工具交互方式:
本质: 人机交互(API | SDK | CLI | IDE | IDE Plugin | Web等) + 智能体 + AI模型

AI Coding 并非一蹴而就的技术跃迁，而是经历了从统计学概率预测到深度理解上下文，再到自主规划任务的演进过程。

## 第一阶段：基于统计的自动补全（2015-2020）
在大型语言模型（LLM）爆发之前，代码补全工具主要依赖于统计模型（如N-gram）或早期的深度学习模型（如 LSTM）。
●  这一阶段的代表产品包括 Kite 和早期的 Tabnine。它们的核心逻辑是 “预测下一个词”。通过分析大量的开源代码库，模型学习代码的概率分布。
● 这些工具缺乏对长上下文的理解能力。它们只能感知当前行或临近几行的代码，无法理解跨文件的逻辑引用，更无法生成完整的函数或类。

## 第二阶段：生成式Copilot时代（2021-2024）
Github Copilot 以 VS Code 插件形式出现开始逐步改变游戏规则，并带来了行业交互变更。
● 2021 年，GitHub Copilot 预览版发布，标志着行业进入 “副驾驶” 时代。它利用 Transformer 架构的注意力机制，能够处理文件级的上下文，理解函数名、注释意图，并生成整段代码。
● 这一阶段的核心交互是 “幽灵文本”（Ghost Text）—— 灰色的建议代码显示在光标后，用户按 Tab 键接受。此外，Chat（对话框）功能开始出现，允许开发者通过自然语言提问。
● 而在产品形态上涌现出了大量插件形态的智能补全产品，并出现了以 VSCode 为基座的 AI IDE 产品。

## 第三阶段：Agentic & Vibe Coding（2024-2026）
2024 年起，单纯的 “补全” 已无法满足需求，开发者需要AI具备 “代理（Agent）” 能力 —— 即自主规划、执行多步操作、调用工具并自我修正。
● 2024 年，Cursor 推出 Composer 模式成为首个支持自然语言对话让 Agent 完成文件修改的 IDE，同年还有 Windsurf、MarsCode 等新 AI IDE 产品露头。
● 2025 年，Anthropic 推出的 Claude Code 将进程再次往前推动了一大步，完全脱离 IDE 改用更极客的 CLI 方式进行编码。
● 同年，以 Lovable 为首的无码产品掀起了一阵非技术人员也可全栈应用生成的浪潮，人人都是开发者的时代即将到来。

从实际观察上看，Vibe Coding 迎来了人人都是开发者时代外，更迎来了时时都在开发的 “癫狂” 状态。不过真的非常精彩，每每回想起来都很兴奋，单纯就编码而言，技术平权终有一日是可被预期的，这是行业大势。





# AI Code工具分类

## CLI(Command Line Interface) 命令行工具
### Anthropic Claude Code

### Google Gemini

### OpenAI CodeX

### OpenCode

### 阿里云  Qwen Code

### 腾讯  codebuddy code

### 命令行辅助工具: CC Switch (Change Code Switch)

## SDK(Software Development Kit) 软件开发工具包
### Anthropic Claude Code  SDK

### Google Gemini SDK

## IDE(Interactive Development Environment) 集成开发环境
### Visual Studio Code
### Cursor
### Google Antigravity
### 字节 TRAE 
### 阿里 Qoder
### 腾讯 codebuddy

## IDE Plugin 集成开发环境插件
### Visual Studio Code 插件
### Cursor 插件
### Google Antigravity 插件
### 字节 TRAE 插件
### 阿里 Qoder 插件
### 腾讯 codebuddy 插件


## Web Web应用
### Anthropic Claude Code Web应用

### Google Gemini Web应用
### Google AI Studio
### Lovable  https://lovable.dev/
