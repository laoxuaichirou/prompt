# 图像编辑与修复工作台

[返回分类总览](./README.md)

整理优先级：优先整理。状态：候选来源映射，未逐项归一化成预设，未新增生成测试。

**输入：**已有图片＋明确修改指令；换装、姿态或场景替换可需第二份参考

**输出：**画质修复、添加删除替换、换背景、换姿态、换装、调色与重布光、场景人物替换

**可用子分类：**修复、局部编辑、换背景、姿态迁移、换装、调色、重布光

## 整理判断

- 入口先选择要改的部分，并记录应保持的人物、商品、构图和背景。与其他工作台共用编辑能力。
- T025原文多数是不同主体的调色示例，纯调色控制变量版本属于新增适配。
- T093原测同时改变色温与机位，不是单一光照因素的严格对照。
- T022含编辑笔记与多个子任务，只能逐个提取可用操作，不整页视为一个稳定预设。

## 对应原条目

|原条目|原标题|原测试状态|原文|示例|
|---|---|---|---|---|
|T006|JsonPromptMaker 身份锁定元提示词（原无标题）|存在问题|[原文](./sources/T006/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/017-T006-run01.jpg)|
|T021|GPT2画质修复元提示词|符合要求|[原文](./sources/T021/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/037-T021-T021.jpg)|
|T022|编辑模型思考|符合要求|[原文](./sources/T022/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/038-T022-T022.jpg)|
|T023|高清修复提示词模板|存在问题|[原文](./sources/T023/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/039-T023-T023.jpg)|
|T024|换装提示词示例|存在问题|[原文](./sources/T024/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/040-T024-T024-initial.jpg)|
|T025|22种AI调色提示词22种AI调色提示词|符合要求|[原文](./sources/T025/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/042-T025-T025-look01.jpg)|
|T093|动态光影超精细写真|符合要求|[原文](./sources/T093/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/129-T093-cool-low.jpg)|
|T095|【图片提示词】添加、删除、替换提示词增强|存在问题|[原文](./sources/T095/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/135-T095-add.jpg)|
|T097|【电商】产品背景更换场景丨提示词优化|符合要求|[原文](./sources/T097/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/139-T097-output.jpg)|
|T099|换姿势|符合要求|[原文](./sources/T099/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/141-T099-output.jpg)|
|T134|人物一致性|符合要求|[原文](./sources/T134/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/172-T134-garden.jpg)|

### T006

原文件：`提示词库/图像编辑/[待测试·3分] JsonPromptMaker 身份锁定元提示词（原无标题）.md`

原测试结论：两次编辑已实测；主体保留较好，衬衫款式未命中。独立LLM确定性测试未完成，不能宣称原模板完全通过。

[原测试详情](./sources/T006/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T021

原文件：`提示词库/图像编辑/[已投产·5分] GPT2画质修复元提示词.md`

原测试结论：本次合成降质人像A型污染清除符合视觉初评；只证明该子用例可用，不证明真实信息恢复或全类型稳定性。

[原测试详情](./sources/T021/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T022

原文件：`提示词库/图像编辑/[已投产·5分] 编辑模型思考.md`

原测试结论：移除本会话自加标记的最小用例符合初评；整页其余工作流未验证，原5分标签不作为证据。

[原测试详情](./sources/T022/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T023

原文件：`提示词库/图像编辑/[已投产·4分] 高清修复提示词模板.md`

原测试结论：合成降质人像视觉清理成功，但4K要求未满足；生成式纹理不是被证实的真实信息恢复。

[原测试详情](./sources/T023/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T024

原文件：`提示词库/图像编辑/[已投产·4分] 换装提示词示例.md`

原测试结论：两版换装链路已实测，主版本次细节较好；初版抽绳变化，严格服装保真未全部满足。

[原测试详情](./sources/T024/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T025

原文件：`提示词库/图像编辑/[已投产·4分] 22种AI调色提示词22种AI调色提示词.md`

原测试结论：所选01与17两个直接生图子例符合视觉初评；其余20组、纯调色控制变量及稳定性未验证。

[原测试详情](./sources/T025/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T093

原文件：`提示词库/图像编辑/[仅参考·2分] 动态光影超精细写真.md`

原测试结论：补入明确样式后，双图系列最小用例符合主要视觉要求。

[原测试详情](./sources/T093/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T095

原文件：`提示词库/图像编辑/[仅参考·4分] 【图片提示词】添加、删除、替换提示词增强.md`

原测试结论：三子例均实际出图，删除和换字表现良好；添加有局部背景改动，原格式合同存在冲突。

[原测试详情](./sources/T095/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T097

原文件：`提示词库/图像编辑/[已投产·3分] 【电商】产品背景更换场景丨提示词优化.md`

原测试结论：短句背景优化的森林最小用例符合主要要求。

[原测试详情](./sources/T097/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T099

原文件：`提示词库/图像编辑/[已投产·3分] 换姿势.md`

原测试结论：双参考姿态转换最小用例符合主要要求。

[原测试详情](./sources/T099/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T134

原文件：`提示词库/人像摄影/[已投产·4分] 人物一致性.md`

原测试结论：两种场景的身份替换最小用例视觉初评符合，精确身份及未测模板不在结论内。

[原测试详情](./sources/T134/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。
