# 开箱即用的中文数模论文模板

这是一份参考作者项目 `paper_3` 实际格式、自行实现的写作模板，不复制旧论文正文或未注明再分发许可的竞赛专用类文件。使用 TeX 发行版提供的 `ctexart`；仓库自身文件以根目录 MIT 许可发布，外部 TeX 组件仍使用各自许可证。

## 对齐 paper_3 的格式

- A4、四边25 mm，正文12.05 pt，行距倍率1.35，段首缩进2字。
- 题名与摘要标题三号加粗，摘要和关键词独占首页，无目录、无身份封面。
- 一级标题居中黑体三号，用“一、二、三”编号；二级四号、三级小四，编号为1.1、1.1.1。
- 页码底部居中、无页眉线；图表中文题注、三线表，代码标题为“代码”。
- 问题重述、分析、假设、符号、各问模型、检验、评价顺序与paper_3对应；AI声明位于参考文献前，证明、明细和代码置于附录。
- 有宋体、黑体、Times New Roman和Arial时优先使用；缺失则回退Fandol与TeX Gyre字体，不要求Windows专用字体。回退字体的字形与分页可能不同，不声称逐像素一致。

这些是作者项目格式，不是对当前或未来竞赛官方要求的认证；提交前按当届要求确认。

## 立即编译

安装带有 XeLaTeX、CTeX、Fandol、TeX Gyre、titlesec、algorithm2e、cleveref 和常用宏包的 TeX Live / MiKTeX / TinyTeX，以及 Python 3.9+。模板不需要 Python 第三方包、BibTeX、外部图片或特定系统中文字体。

复制整个 `latex-paper` 目录到参赛项目的 `paper/`，在该目录运行：

```bash
python build.py
```

输出 `build/main.pdf` 与独立一页 `build/ai-usage.pdf`。脚本重新计算演示表格，双遍编译，并检查未解析引用、缺字和溢出警告。发现编译失败或严重检查问题时返回非零状态，详细日志位于 build/。不自动安装依赖，不连接官方接口。

没有Python时可直接双遍运行：

```bash
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

`generated/demo-table.tex` 已包含可直接编译的演示表格。在 Overleaf 中上传整个目录，编译器选择 XeLaTeX，主文件选择 `main.tex`；单独编译AI说明时选 `ai-usage.tex`。该路径未在Overleaf实际测试，按账户环境确认宏包可用性。

## 改哪些文件

| 文件 | 内容 |
|---|---|
| config.tex | 题名、关键词、模板提示开关、三四问开关、AI声明 |
| preamble.tex | 字体、版心、公式、表格、命题与代码样式 |
| sections/01-summary.tex | 摘要与关键词 |
| sections/01-restatement.tex 至 04-notation.tex | 重述、分析、假设与符号 |
| sections/05-model-q1.tex 至 08-model-q4.tex | 各问模型、算法与理论边界 |
| sections/09-validation.tex、10-evaluation.tex | 检验、结果与评价 |
| sections/references.tex | 参考文献填写位置 |
| sections/A1-proofs.tex、A2-tables.tex、A4-support-files.tex | 证明、统计口径与代码支撑 |
| ai-usage.tex | 独立AI工具使用说明 |
| examples/demo.py | 可运行教学示例，生成表格与CSV |

模板内使用一维稳健优化教学问题展示“证明—程序—表格”闭环，数据明确标注为演示，不是比赛实验。正文所有内容均需按真实题目替换；图框是占位，引用位置提示也不是可提交文献。附录程序通过 `\lstinputlisting` 引用完整源文件，避免手工复制后失配。

题号多少按题目调整，不强制四问。默认保留三四问占位，可在config.tex中改为 `\extendedquestionsfalse` 关闭；实际三四问需明确新约束，不照搬教学模型。参考文献替换为真正核验的来源后再加入 `\cite{...}`。若使用Python入口，更新 examples/ 与 build.py 的演示生成部分为项目真实数据处理入口。

## 与协作流程配合

```text
使用 $cumcm-modeling，采用 latex-template 作为论文起点。
先将已验证模型、采用算法和真实实验映射到章节，删除教学示例。
保持未解决的理论边界和数据来源说明，最后根据真实结论填写摘要。
按本届要求核对格式，编译并检查页面；只生成文件，不上传提交。
```

在 config.tex 中将 `\drafttrue` 改为 `\draftfalse` 只会关闭页首模板提示，不会清除教学内容或自动完成提交核验。

## 提交前必须由真实要求决定

本模板不提供官方封面、承诺页，也不声称满足某届页数、字体、匿名或AI披露规则。确认当届要求后按需调整；Git身份和代码支撑文件不额外匿名。数据、密钥、官方原日志及论文身份字段分别按用户和题目要求处理。

提交前删除所有教学内容、图框与示例引用提示，核对符号、表格来源、代码版本、正文和附录页数，检查PDF及支撑文件在独立目录中的可用性。示例证明不能用作实际题目的理论结论。
