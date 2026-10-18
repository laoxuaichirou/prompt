# 创意人像生成工作台：提示词预设草案 v0.1

面向“上传人物照片→选择风格/创意→得到同一人物的新图片”的预设集合。数据源为本轮提示词库测试记录。本次只整理、归一化和分类，没有新增生图。

## 规模与输入

- **84张去重预设卡**，来自88个原条目；其中74张为单张人物照、2张为单照＋可选辅助图，共76张可设计成单照入口。
- 其余8张：4张需产品、服装或宠物素材，4张需双人或多人照片。
- **20个辅助引擎**：身份编译、动作、换装、姿态迁移、修复、分镜等；不当作20种视觉风格。
- 14条工具拦截条目停用，7条原文/子页缺失条目保留缺失记录，不编造可运行预设。
- T001有40个场景选项，T025有22种调色选项；它们不是62条已测试通过的独立预设。

原测试工具为 `image_gen.imagegen`，后端模型未知；原文指定其他模型的，属于ChatGPT适配测试，不代表原模型实测。

## 关键证据区别

原测试记录中的“符合要求”仅针对当时的测试输入与用例。本JSON中的人物输入归一化、固定示例身份移除、参数化提示词均属于新版本，**全部标记为未生图回归**，不能直接当作已投产预设。

- **T145**原文没有明确引用上传人像，本轮也是文字生成虚构人物；“上传任意照片做本人＋手办”是新增适配，需要首次身份迁移测试。
- **T178**原测使用人物照＋合成球衣两图；单人物照、按球队文字合成球衣是新增路径，精确队服仍需球衣图。
- **T044**原文要求不同随机脸，与固定本人冲突；本版已明确改成同一人，必须重测。
- **T138/T154**、**T136/T137**、**T078/T112**、**T124/T126**分别合并为一张卡，保留每次原测试各自结论，不平均或覆盖。

[查看84张预设的原测试效果索引](./GALLERY.md) · [40场景与22种调色](./VARIANTS.md) · [20个辅助引擎](./ENGINES.md)

## 分类目录

|分类|卡数|内容|
|---|---:|---|
|[3D与动画电影](./categories/3d.md)|4|T091、T138、T150、T157|
|[漫画与绘画](./categories/illustration.md)|5|T077、T100、T101、T102、T139|
|[微缩与创意合成](./categories/creative.md)|12|T026、T031、T078、T088、T096、T117、T121、T129、T131、T145、T156、T158|
|[海报与平面设计](./categories/poster.md)|8|T027、T074、T075、T076、T079、T140、T153、T178|
|[场景写真与时装](./categories/scene.md)|21|T001、T013、T014、T032、T034、T035、T041、T042、T044、T045、T048、T107、T109、T123、T128、T130、T136、T141、T147、T151、T176|
|[表情与多格拼贴](./categories/expression.md)|10|T012、T019、T033、T098、T106、T113、T119、T127、T133、T159|
|[多角度与机位](./categories/views.md)|5|T110、T120、T146、T172、T173|
|[调色与光影](./categories/lighting.md)|2|T025、T093|
|[静态故事与时间想象](./categories/story.md)|9|T015、T036、T037、T040、T080、T094、T132、T143、T160|
|[多素材扩展](./categories/multi.md)|8|T005、T007、T087、T090、T115、T122、T124、T177|

## 建议首轮回归的20张卡

优先级针对工作台覆盖与需求，不是通过排名。建议用至少3个不同人物作为输入，检查“换人后仍像本人”、服装道具一致性及多图连续性。写实与Q版分别验收，Q版不能同时承诺头身夸张和真人比例完全不变。

|优先|预设|功能|原测|原测试示例|
|---|---|---|---|---|
|1|[T178 本人世界杯双重曝光海报](./categories/poster.md)|单张人物照＋可选辅助图|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/217-T178-output.jpg)|
|2|[T145 本人和Q版模型喝咖啡](./categories/creative.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/183-T145-output.jpg)|
|3|[T131 橱窗里的动画版自己](./categories/creative.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/169-T131-output.jpg)|
|4|[T138 风格化3D漫画本人](./categories/3d.md)|单张人物照|符合要求 / 符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/176-T138-output.jpg)|
|5|[T157 动画电影全身卡通](./categories/3d.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/191-T157-output.jpg)|
|6|[T091 收藏级Q版人偶](./categories/3d.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/120-T091-output.jpg)|
|7|[T102 怪诞梦幻超现实插画](./categories/illustration.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/144-T102-output.jpg)|
|8|[T139 墨影符文侧写](./categories/illustration.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/177-T139-output.jpg)|
|9|[T110 人物五视角参考](./categories/views.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/149-T110-back.jpg)|
|10|[T172 人物七视图资产板](./categories/views.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/212-T172-output.jpg)|
|11|[T120 人物九景别联系表](./categories/views.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/159-T120-output.jpg)|
|12|[T173 本人俯仰角对比](./categories/views.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/213-T173-high.jpg)|
|13|[T136 雪林旅行九格](./categories/scene.md)|单张人物照|符合要求 / 存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/174-T136-output.jpg)|
|14|[T093 冷暖动态光影写真](./categories/lighting.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/129-T093-cool-low.jpg)|
|15|[T098 本人九格大头贴](./categories/expression.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/140-T098-output.jpg)|
|16|[T106 一框六种时装风格](./categories/expression.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/146-T106-output.jpg)|
|17|[T121 本人涂装自己的手办](./categories/creative.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/160-T121-output.jpg)|
|18|[T076 工作室涂鸦大片](./categories/poster.md)|单张人物照|符合要求|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/090-T076-output.jpg)|
|19|[T078 掌心Q版小人](./categories/creative.md)|单张人物照＋可选辅助图|存在问题 / 存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/092-T078-output.jpg)|
|20|[T156 从拍立得中浮出](./categories/creative.md)|单张人物照|存在问题|[看图](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/190-T156-output.jpg)|

## 可导入文件

- [portrait-presets.json](./portrait-presets.json)：84张卡、身份策略、参考图槽、变量默认值、布局与输出数量、原测来源、待回归状态。
- [portrait-engines.json](./portrait-engines.json)：20个辅助引擎。
- [preset-index.csv](./preset-index.csv)：可用Excel筛选的目录。
- [unavailable.json](./unavailable.json)：停用与缺失来源。
- [scope-index.json](./scope-index.json)：全部219原条目的收录/不收录理由。
- [sources/](./sources/)：原文副本和完整原测证据，SHA256可核对。
- [集成说明](./INTEGRATION.md)：变量渲染、参考素材绑定、元提示词调用顺序。

## 建议的工作台入口

上传本人照片 → 选分类/预设 → 填该预设需要的变量 → 若需要再传球衣/商品/姿态或其他人物照片 → 执行 → 查看与原照片的对比。用户只需要看到影响结果的选项。原文固定名人、合成测试者年龄、绝对8K/RAW/100%身份保证不直接暴露成已实现能力。

本次交付为预设数据与提示词目录，尚未构建工作台应用。
