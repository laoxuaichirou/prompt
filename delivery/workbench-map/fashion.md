# 服装与虚拟试衣工作台

[返回分类总览](./README.md)

整理优先级：优先整理。状态：候选来源映射，未逐项归一化成预设，未新增生成测试。

**输入：**服装平铺/实物图；试衣时再提供人物照；可加场景和广告文案

**输出：**换装试穿图、同服装多动作模特组图、去人留衣与幽灵模特图、悬浮服装、服装广告与系列展示页视觉

**可用子分类：**人物试衣、服装静物、幽灵模特、模特组图、服装广告

## 整理判断

- 与人像工作台共享人物身份模块，但主保留对象是服装：领型、口袋、抽绳、剪裁、色块等。
- T024为换装；T051是先分析再生成去人留衣提示词；T055原文只有一句悬浮概念，不能当作完整通用方案。
- T017是落地页视觉图，原文固定示例人物与服饰；任意服装输入及可交互页面都没有据此验证。
- T007为25分镜商业广告，需完整检查每格；单张成图不等于服装一致性流程通过。

## 对应原条目

|原条目|原标题|原测试状态|原文|示例|
|---|---|---|---|---|
|T004|广告创意|存在问题|[原文](./sources/T004/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/013-T004-ad01.jpg)|
|T007|商业广告25分镜|存在问题|[原文](./sources/T007/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/019-T007-grid25.jpg)|
|T011|AI时尚丨JSON人物场景动作丨LLM提示词优化|存在问题|[原文](./sources/T011/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/021-T011-pose01.jpg)|
|T017|【服装展示】冬季时尚系列落地页设计，雪景|符合要求|[原文](./sources/T017/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/030-T017-output.jpg)|
|T019|电商模特组图生成-根据需要修改|存在问题|[原文](./sources/T019/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/032-T019-output.jpg)|
|T020|【元提示词】商业摄影|存在问题|[原文](./sources/T020/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/033-T020-pose01.jpg)|
|T024|换装提示词示例|存在问题|[原文](./sources/T024/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/040-T024-T024-initial.jpg)|
|T051|【元提示词】服装立体化lora：3Dghostmannequin|符合要求|[原文](./sources/T051/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/063-T051-T051.jpg)|
|T055|衣服悬浮在空中|符合要求|[原文](./sources/T055/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/069-T055-T055.jpg)|

### T004

原文件：`提示词库/海报封面/[待测试·4分] 广告创意.md`

原测试结论：三次适配文字子项均命中，但服装细节在穿着侧受遮挡和裤脚变化影响；整体存在问题。三次成功不代表稳定性已验证，不冒充原模型实测。

[原测试详情](./sources/T004/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T007

原文件：`提示词库/视频分镜/[待测试·3分] 商业广告25分镜.md`

原测试结论：25格数量与大致三幕命中，边框、无遮挡和8K要求未满足；仅静态适配测试，不是视频生成通过。

[原测试详情](./sources/T007/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T011

原文件：`提示词库/人像摄影/[已投产·5分] AI时尚丨JSON人物场景动作丨LLM提示词优化.md`

原测试结论：三图融合4图已实测，场景与服装大体有效；动态姿势指令失效，景别多样性较有限。

[原测试详情](./sources/T011/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T017

原文件：`提示词库/电商产品/[已投产·5分] 【服装展示】冬季时尚系列落地页设计，雪景.md`

原测试结论：本次静态落地页核心布局、人物服装及指定文案符合模型初评；仅一次适配，不代表中文长期稳定性或真实网页可用。

[原测试详情](./sources/T017/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T019

原文件：`提示词库/电商产品/[已投产·5分] 电商模特组图生成-根据需要修改.md`

原测试结论：九景别最小用例已实测，大部分层级有效，MLS偏近；单张宫格不证明跨调用一致性。

[原测试详情](./sources/T019/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T020

原文件：`提示词库/电商产品/[已投产·4分] 【元提示词】商业摄影.md`

原测试结论：四方案到四图链路完成，动作多样但机位/景别未全部命中，不能完整通过。

[原测试详情](./sources/T020/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T024

原文件：`提示词库/图像编辑/[已投产·4分] 换装提示词示例.md`

原测试结论：两版换装链路已实测，主版本次细节较好；初版抽绳变化，严格服装保真未全部满足。

[原测试详情](./sources/T024/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T051

原文件：`提示词库/电商产品/[已投产·4分] 【元提示词】服装立体化lora：3Dghostmannequin.md`

原测试结论：元输出按固定3Dghostmannequin开头与英文画质词结尾；实图仅保留蓝色V领短袖上衣，胸1下摆2贴袋、白色空白织标与侧开衩均在，无人体/模特/裤鞋/听诊器，立体中空质感基本符合本用例。未运行原ComfyUI/LoRA。 视觉评分为模型初评，单次不证明稳定性。

[原测试详情](./sources/T051/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T055

原文件：`提示词库/电商产品/[仅参考·2分] 衣服悬浮在空中.md`

原测试结论：空心人形由蓝色刷手服上衣和长裤形成，服装悬空有投影，无实际人体或模特，鞋和听诊器已移除；三上衣口袋与裤腿贴袋基本保留。原始单句很简略，本用例增加了明确的服装/形状输入，不代表裸句独立稳定性通过。 视觉评分为模型初评，单次不证明稳定性。

[原测试详情](./sources/T055/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。
