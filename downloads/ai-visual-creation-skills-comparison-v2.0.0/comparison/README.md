# 对照关系与怎么开始

先确认目的：比较的是规则文件生成的提示词，还是最终图像，还是视频。三种结果分开记录。

| 编号 | A：原始或忠实整理 | B：此前改编 | 可比较的内容 |
|---|---|---|---|
| P1 | tutorial-film-production | creative-workflow-planner | 同一故事的资产/镜头计划；如生成，额外固定执行流程 |
| P2 | tutorial-canvas-foundation | image-storyboard-director | 同一参考、同一四格要求下的静态结果；四格是共用用户任务，不是原课程默认要求 |
| P3 | seedance-director（原文件） | video-prompt-director | 同一视频请求的文本；接入同一视频模型后才比较动态效果 |
| P4 | ctx-6-dev（RAR原文件） | context-driven-dev | 相同代码基线、需求与验证环境下的实现与交互成本 |

`visual-consistency-reviewer` 无一一对应的原始 Skill，可作为独立返修方法测试，但不能只在B组使用它后声称这是初次生成质量的公平A/B。可另外测量“完整流程”效果，并计入额外生成与人工成本。

三份原稿载体是案例基线：

- ash-swordswoman-source：十秒八拍原稿。
- crimson-blade-source：十五秒六镜原稿。
- visual-ad-source：巧克力与赛博朋克原稿。

原视频稿改成宫格属于“跨媒介改编实验”，不是严格原版视频效果对照。若要测原稿与改稿，必须事先约定两组相同的静态转换规则、格数、参考、保留的事件，保存适配文本。

## 当前状态

所有P1—P4结果均为未执行。历史三张图只支持部分改编方法可用于静态预演，不填写到任一P组成绩中。

建议按 [测试流程](test-protocol.md) 先做P2，再做P1；没有视频模型时P3仅测文本，视频栏保持未测。测试题见 [统一任务](test-cases.md)，差异见 [改编清单](differences.md)。
