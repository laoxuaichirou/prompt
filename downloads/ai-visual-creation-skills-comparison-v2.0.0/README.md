# 下载原版与改编版对照包 v2.0.0

[直接下载 ZIP（约14 MB）](https://raw.githubusercontent.com/laoxuaichirou/prompt/skill-pack-2026-10-31/downloads/ai-visual-creation-skills-comparison-v2.0.0/ai-visual-creation-skills-comparison-v2.0.0.zip) · [在线测试指南](comparison/README.md) · [两版差异](comparison/differences.md)

本次按用户要求补齐原始资料与忠实封装，用于用户自行验证。A含2个原始Skill和5个忠实封装；B保留上版5个改编Skill。8份原始附件和3张历史生成图片均在ZIP中。

历史图片实验发生在B版文件编写之前，不能算作加载B版的端到端测试；当前没有A/B效果结论，没有视频测试。下载后请先阅读测试指南，分别加载A、B验证，避免同时启用两组规则。

SHA-256：`4513fb0a663ce11d5e0a4815678d8d8cc9409f610d22f1c6c8be28cd649f7107`

---

# AI 创作 Skill 原版与改编版对照包

版本：2.0.0 · 日期：2026-10-31（北京时间）

本包用于用户自行验证，而不是宣称改编版已经优于原版。

## 两条路线

| 目录 | 内容 | 测试状态 |
|---|---|---|
| `A-source-faithful/skills/` | 2个原始 Skill 原文＋5个按课程/案例忠实封装的 Skill | 未执行本包端到端测试 |
| `B-adapted/skills/` | 上版的5个改编 Skill，文件保持不变 | 相关图片方法做过一次实验；新 Skill 本身未完整复测 |
| `sources/original/` | 用户提供的8份原始附件，保留文件内容 | 来源资料，不自动加载执行 |
| `evidence/prior-image-method-trial/` | 已有角色参考、四格初稿、修订图和观察 | 历史方法实验，非 A/B 结果 |
| `comparison/` | 配对关系、差异、统一测试题、空白结果表 | 等待用户测试 |

“忠实封装”表示从课程或提示词整理出使用步骤，不是原作者发布的 Skill。只有 `seedance-director` 与从 RAR 解出的 `ctx-6-dev` 是原 Skill 文件内容原样保留。

## 安装

1. 解压本包，先看 `comparison/README.md`。
2. 每次只加载一条路线里的一个目标 Skill：将单个文件夹整体复制到宿主支持的技能目录，或直接附上其中的 `SKILL.md`。
3. 不要将整个包放进自动扫描的技能目录，不要同时加载 A、B、原始附件与其他广泛触发的 Skill，否则可能混合规则。
4. 精确原版的模型名称、特殊输出块、确认门控等保持原文；宿主不支持时先记录不兼容，不能悄悄改成 B 的规则再称作原版测试。

原课件和原 Skill 的平台功能、技术表述不因此得到确认。技术勘误单独放在 `comparison/technical-notes.md`，不修改原文件。

## 先验证什么

当前没有视频模型：优先进行 `P1`、`P2` 两组图片或规划对照。视频导演 `P3` 只能先比较提示词文本，视频效果必须标记未测。

参考 `comparison/test-protocol.md`，同一任务、同一参考、同一模型与相同设置分别运行 A、B。控制统一的生成次数，不只挑最好的一张。测试完成后填写结果表，保留输入、提示词、原始输出与返修版本。

可以先用已有角色图快速试用，但它是在此前改编流程下生成的；正式基准建议另用一张与A/B无关的参考图，并明确其来源。任务与参考在两条路线中必须一致。

## 重要区别

- 历史顺序：研究材料→编写图片调用→生成/返修→整理 B 版 Skill。
- 当前顺序：保存原始文件→制作 A 版忠实封装→冻结 B 版→提供对照方案→交由用户验证。
- 本次未新生成视频，也未重新运行 A/B 图像对照；没有添加虚构成功率、分数或胜负结论。
- 三张历史图不能证明完整八拍连招、无闪烁、声音、视频时序或五个 Skill 的稳定表现。

## 完整性与记录

- `sources/manifest.json`：8份原始附件的 SHA-256。
- `comparison/skill-manifest.json`：每个 Skill 类型、来源、对照关系和文件哈希。
- `SHA256SUMS`：所有打包文件的校验值。
- `scripts/record_run.py`：无需额外依赖的本地记录工具，保存实际输入/输出文件的哈希，不调用模型、不判定通过。

示例：`python scripts/record_run.py --pair P2 --arm A --trial 1 --mode image --input prompt.txt --output result.png --out my-results/P2-A-1.json`

来源材料仅为本次用户验证提供，未附加未经确认的开源许可。本包不是课程、模型或 Skill 原作者的官方发行版。
