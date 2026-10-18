# 参考图反推与提示词助手

[返回分类总览](./README.md)

整理优先级：优先整理。状态：候选来源映射，未逐项归一化成预设，未新增生成测试。

**输入：**参考图片、简单想法或已有提示词＋编辑意图

**输出：**结构化视觉描述、风格与光影分析、生图提示词改写、动作编辑指令、模型格式适配提示词

**可用子分类：**看图反推、自然语言扩写、风格提取、动作指令、模型格式转换

## 整理判断

- 适合作为所有创作入口的共用助手；默认输出文本，不应显示成已经生图。
- T065含教学/反推内容，T069存在原文件标题错配；按实际正文和测试记录使用。
- 模型名称是格式目标，不能用本轮ChatGPT适配测试冒充对应原模型实测。

## 对应原条目

|原条目|原标题|原测试状态|原文|示例|
|---|---|---|---|---|
|T056|图像 Prompt 改写专家丨三合一（喂给LLM）|符合要求|[原文](./sources/T056/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/070-T056-output.jpg)|
|T057|逆向提示词反推|存在问题|[原文](./sources/T057/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/071-T057-baseline.jpg)|
|T059|【LLM】元提示词模板|存在问题|[原文](./sources/T059/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/075-T059-pose1.jpg)|
|T060|提示词增强|符合要求|[原文](./sources/T060/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/077-T060-output.jpg)|
|T062|【图片】提示词反推丨光影描绘丨通用模板：场景化 Agent 提示词” 的思路|存在问题|[原文](./sources/T062/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/078-T062-output.jpg)|
|T065|提示词设计（教学用-反推部分修改）|符合要求|[原文](./sources/T065/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/080-T065-output.jpg)|
|T069|MJ提示词生成器system prompt（原Z image页，标题错配）|符合要求|[原文](./sources/T069/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/083-T069-output.jpg)|

### T056

原文件：`提示词库/提示词工程/[已投产·5分] 图像 Prompt 改写专家丨三合一（喂给LLM）.md`

原测试结论：含文字图最小用例符合要求；不代表三个分流或稳定性已验证。

[原测试详情](./sources/T056/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T057

原文件：`提示词库/提示词工程/[已投产·5分] 逆向提示词反推.md`

原测试结论：已完成两角色对比，保留了主要风格和背景；严格姿态锁定失败，语言识别不可验证。

[原测试详情](./sources/T057/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T059

原文件：`提示词库/提示词工程/[已投产·4分] 【LLM】元提示词模板.md`

原测试结论：两种姿势已对比；动作大体落实，前倾不足，不能宣称身份完全一致或30%指标通过。

[原测试详情](./sources/T059/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T060

原文件：`提示词库/提示词工程/[已投产·4分] 提示词增强.md`

原测试结论：简易版背景替换最小用例符合要求，仅为单次模型初评。

[原测试详情](./sources/T060/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T062

原文件：`提示词库/提示词工程/[仅参考·3分] 【图片】提示词反推丨光影描绘丨通用模板：场景化 Agent 提示词” 的思路.md`

原测试结论：光影编辑主体保留良好；分辨率及原SD权重未验证，不能算原模型完整通过。

[原测试详情](./sources/T062/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T065

原文件：`提示词库/提示词工程/[已投产·4分] 提示词设计（教学用-反推部分修改）.md`

原测试结论：v4单图局部属性编辑最小用例符合要求；不代表整个教学页所有版本通过。

[原测试详情](./sources/T065/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T069

原文件：`提示词库/模型工具/[仅参考·3分] MJ提示词生成器system prompt（原Z image页，标题错配）.md`

原测试结论：元提示词展开后的水彩最小用例符合视觉要求，仅ChatGPT适配测试。

[原测试详情](./sources/T069/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。
