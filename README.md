# 数模国赛：Prompt 协作流程、Skills 与 LaTeX 模板

将一个真实数学建模项目中的协作方式整理为开箱可用的工作流：**明确目标与边界，用证明、代码和实验推进，最后交付与证据一致的论文和支撑材料。**

这里提供我的 Prompt 方法、一个可安装的 Codex 技能，以及参考已有论文格式实现的中文 LaTeX 模板。适合从初始 idea 开始建模，也适合继续已有项目、处理 review、优化算法和完成论文交付。

[协作流程](docs/prompt-workflow.md) · [提示词示例](docs/prompt-examples.md) · [技能入口](skills/cumcm-modeling/SKILL.md) · [论文模板](templates/latex-paper/README.md) · [PDF预览](templates/latex-paper/preview/main.pdf)

## 从哪里开始

| 你的目标 | 建议入口 |
|---|---|
| 学习这套对话与推进方法 | 阅读 [Prompt 协作流程](docs/prompt-workflow.md) |
| 在 Codex 中开始建模 | 安装 `cumcm-modeling`，提供题目、附件和本轮目标 |
| 给已有项目做理论或算法审查 | 选择 [对应提示词](docs/prompt-examples.md)，说明当前版本和操作边界 |
| 直接使用论文排版 | 复制 [LaTeX 模板目录](templates/latex-paper)，编译后替换教学内容 |
| 将新经验反馈到项目 | 阅读下方的维护与贡献说明 |

Prompt 方法和论文模板可以独立使用；完整流程不要求题目有模拟器。

## 我的 Prompt 方式

常用结构是：

> **技能名 + 材料位置 + 本轮目标 + 操作边界 + 所需交付**

首次把任务说明白，随后用短提示调整方向。例如追问“理论是否自洽”“本地模型和官方一致吗”，将优化目标改为“优先鲁棒性”，或明确“暂不改论文”“先不要正式启动”。助手根据证据推进，状态写进工作文档，而不是只留在聊天中。

```mermaid
flowchart LR
    A[题目与初始思路] --> B[模型与理论审查]
    B --> C[实现与验证]
    C --> D[Review与鲁棒优化]
    D --> E[冻结采用版本]
    E --> F[论文与代码支撑]
    D --> B
```

这条流程可以按项目需要回退或跳转。正式测试是有真实接口且明确授权时才执行的分支。

首次提示可以直接写：

```text
使用 $cumcm-modeling。
题目和附件在当前目录，初始思路在 idea.md。
先审查问题1和问题2的假设、目标与理论缺口，给出证明、反例或修正模型。
实现必要代码并做本地验证，暂不修改论文正文，不启动正式测试。
维护工作文档、理论推导和论文大纲，按我的现有身份提交本地 Git。
```

已有上下文后可以简短地继续：

```text
继续优化，优先鲁棒性。
在同一固定案例上比较平均效果、P95、最大退化和失败，保留全部统计分母。
本轮预算两小时，仍不改论文、不启动正式测试。
```

换新会话时补充项目路径，让助手先读 `AGENTS.md`、工作文档和 Git 状态。单独一句“继续”不能提供新项目缺失的历史。

## 快速开始

### 1. 获取仓库

```bash
git clone https://github.com/sakur7a/cumcm-modeling-skills.git
cd cumcm-modeling-skills
```

### 2. 安装技能

在有 `skill-installer` 的 Codex 环境中发送：

```text
使用 $skill-installer，从 sakur7a/cumcm-modeling-skills
安装 skills/cumcm-modeling 下的技能。
若已存在同名技能，先比较差异，保留我的本地修改。
```

也可以手动将完整 `skills/cumcm-modeling` 文件夹复制到环境配置的个人技能目录。作者当前环境使用 `~/.codex/skills/`；保留 `SKILL.md`、`agents/`、`references/` 与 `assets/` 的结构。若客户端未识别，刷新或重启后检查技能列表。

然后在**实际参赛项目目录**中使用 `$cumcm-modeling` 并给出任务。只安装技能目录即可；整个仓库不是单个技能。客户端的加载位置与调用入口以当前环境及 [OpenAI 技能文档](https://learn.chatgpt.com/docs/build-skills)为准。

### 3. 编译论文模板

需要 Python 3.9+ 和含 XeLaTeX、CTeX/Fandol、TeX Gyre 及常用宏包的 TeX 发行版。无需 Python 第三方包或外部图片。

```bash
cd templates/latex-paper
python build.py
```

输出：

- `build/main.pdf`：论文教学示例。
- `build/ai-usage.pdf`：独立 AI 工具使用说明填写模板。

用于参赛项目时，复制整个 `latex-paper` 目录为项目的论文目录，先改 `config.tex`，再填各章节。已有论文时先比较结构，避免覆盖原稿。

模板中的模型、数据、图框和引用提示都是教学内容，必须替换后才能用于实际论文。关闭 `draft` 提示不会自动清除这些内容。

## 论文模板的格式与内容

模板参照作者项目 `paper_3` 的排版设置自行实现，不依赖该项目，也未复制旧论文正文或未注明再分发许可的竞赛类文件。

- A4、四边 25 mm，正文 12.05 pt，行距倍率 1.35。
- 摘要与关键词独占首页，无目录、无身份封面。
- 一级中文数字居中标题，下级编号 `1.1`、`1.1.1`；页码底部居中。
- 重述、分析、假设、符号、各问模型、检验与评价分文件维护。
- AI 声明位于参考文献前；证明、统计明细与源码支撑放在附录。
- 三四问可配置关闭；优先原论文系统字体，缺失时回退到 TeX 字体。

字体回退可能改变字形和分页。该格式是项目实践参考，提交要求应按当届官方规则核对。

模板通过解析教学问题展示“理论—程序—表格”的对应关系，附录用 `\lstinputlisting` 引入实际示例源码。详细配置见 [模板说明](templates/latex-paper/README.md)。

预览：[论文 PDF](templates/latex-paper/preview/main.pdf) · [AI 使用说明 PDF](templates/latex-paper/preview/ai-usage.pdf)

## 技能负责什么

| 模块 | 重点 |
|---|---|
| [理论审查](skills/cumcm-modeling/references/theory-review.md) | 假设、证明、反例、最优性目标、适用边界和权威来源 |
| [算法与验证](skills/cumcm-modeling/references/algorithm-validation.md) | 可复现基线、固定开发集、独立确认、压力测试和完整统计 |
| [官方测试](skills/cumcm-modeling/references/official-testing.md) | 区分演练与正式、预检、未知动作处理、退出与导出闭环 |
| [论文与交付](skills/cumcm-modeling/references/paper-delivery.md) | 最小同步、真实结果、源码附录、独立支撑材料和 AI 披露 |
| [工作账本模板](skills/cumcm-modeling/assets/work-ledger-template.md) | 持续保存当前状态、模型与证据映射及下一步 |

这些规则尤其关注：不把高精度复算当严格证明，不把平均提升当逐例占优，不把本地合成当官方验证，不只筛选成功案例，也不把计划写成已完成结果。

## 已验证范围

在作者的 Windows / XeLaTeX 环境中，模板四问版与关闭三四问后的两问版均通过双遍编译；复制到含空格的隔离目录后也能构建。默认示例为 7 页，AI 说明为 1 页，渲染页面已检查，未发现缺字、溢出或未解析引用。

技能结构、相对链接与安装副本一致性已检查。结构验证不等于模型行为评测。其他系统与 Overleaf 尚未逐一实测，宏包、字体和客户端差异需在使用环境中确认。

## 维护与贡献

本仓库是维护主来源，个人技能目录是安装副本。`git pull` 更新仓库后仍需比较并同步安装文件；不要静默覆盖本地修改。论文模板也需单独同步，修改技能不会自动更新项目论文。

欢迎通过 [Issues](https://github.com/sakur7a/cumcm-modeling-skills/issues) 提供使用反馈，或提交 PR。建议包含：技能版本、环境、最小复现提示、预期与实际行为、已脱敏的证据。通用方法放技能或文档，题目专用参数与真实成绩留在各自项目。

可以这样要求助手维护：

```text
把这次实践中的通用经验补充到 cumcm-modeling-skills。
检查适用条件和规则冲突，更新相关说明，同步本机安装副本，提交并推送。
不要修改参赛项目的论文或测试程序。
```

日常 Git 使用用户现有身份，无需匿名。代码支撑材料按具体要求处理，不额外强制匿名；密钥和私有配置不进入公开仓库。有限次数正式测试必须明确授权，示例提示本身不是执行许可。

## 许可与适用边界

仓库自编技能、文档、脚本与模板采用 [MIT License](LICENSE)，可使用、修改和再分发。TeX 发行版及其组件遵守各自许可证。

本项目提供协作方法和写作起点，不提供特定题目的完整解答，不自动获取旧聊天或比赛数据，不保证理论全局最优或比赛成绩。模型、格式、页数与 AI 政策按实际题目和当届要求确认。仓库不包含原参赛论文、身份配置或官方原日志。
