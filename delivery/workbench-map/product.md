# 商品视觉工作台

[返回分类总览](./README.md)

整理优先级：优先整理。状态：候选来源映射，未逐项归一化成预设，未新增生成测试。

**输入：**商品照片＋目标场景/用途；少数原模板仅需商品文字描述

**输出：**换背景与场景陈列、手持商品广告、白底工业图鉴、商品多角度与细节、珠宝、美食等专项视觉、电商主图与详情页图

**可用子分类：**背景替换、产品棚拍、多视图图鉴、手持展示、珠宝广告、美食广告、详情页组图

## 整理判断

- 这是最接近创意人像工作台的第二个入口：把固定对象由人物换成商品，核心验收改为外形、颜色、标签与结构保真。
- T052和T082原测没有商品参考图，T053是文生美食；不能直接宣称它们已支持上传任意实物保真。
- T085原测使用瓶子与手掌两份参考；T086需要版式参考和商品图。
- T092标题中的96组不能视为96个已通过预设；原测仅覆盖第一组八角度，存在几何漂移。
- T083【AI商业】原文缺失，本方向只登记其缺失情况，不列为候选预设。

## 对应原条目

|原条目|原标题|原测试状态|原文|示例|
|---|---|---|---|---|
|T016|【商品】9宫格奢华悬浮运动鞋|存在问题|[原文](./sources/T016/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/029-T016-output.jpg)|
|T018|极简白底高端产品工业图鉴|存在问题|[原文](./sources/T018/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/031-T018-output.jpg)|
|T052|多视角亚麻椅材质分解图|存在问题|[原文](./sources/T052/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/064-T052-T052.jpg)|
|T053|奢华8K国家美食广告|存在问题|[原文](./sources/T053/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/065-T053-T053-01.jpg)|
|T054|戒指|存在问题|[原文](./sources/T054/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/067-T054-T054-01.jpg)|
|T082|kontext大家电场景图（示例）|符合要求|[原文](./sources/T082/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/097-T082-output.jpg)|
|T085|kontext电商手持商品|符合要求|[原文](./sources/T085/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/099-T085-output.jpg)|
|T086|无标题|符合要求|[原文](./sources/T086/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/100-T086-output.jpg)|
|T089|电商详情页 元提示词|符合要求|[原文](./sources/T089/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/104-T089-creative.jpg)|
|T092|96组角度提示词|存在问题|[原文](./sources/T092/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/121-T092-01.jpg)|
|T097|【电商】产品背景更换场景丨提示词优化|符合要求|[原文](./sources/T097/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/139-T097-output.jpg)|

### T016

原文件：`提示词库/电商产品/[已投产·5分] 【商品】9宫格奢华悬浮运动鞋.md`

原测试结论：九概念和3:4布局本次有效；产品细节严格一致性仍有问题，真实品牌与字标未验证。

[原测试详情](./sources/T016/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T018

原文件：`提示词库/电商产品/[已投产·5分] 极简白底高端产品工业图鉴.md`

原测试结论：版式有用，但视觉真实性约束不足，存在不可证实的新视图与结构用语；不能按真实工业资料直接验收。

[原测试详情](./sources/T018/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T052

原文件：`提示词库/电商产品/[已投产·4分] 多视角亚麻椅材质分解图.md`

原测试结论：三视图与材质分栏、亚麻/橡木/黑钢样本及文字可读，3:2成立；Frame标注线端点却落在座垫布面，未准确指向黑钢框架。多视图几何大体类似，不能当实物测量或真实材料鉴定。 视觉评分为模型初评，单次不证明稳定性。

[原测试详情](./sources/T052/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T053

原文件：`提示词库/电商产品/[已投产·4分] 奢华8K国家美食广告.md`

原测试结论：两幅独立4:3美食图均有深绿背景、蒸包皮与猪肉葱馅、悬空碎屑和摄影变化，无手/盘/桌/文字/商标；微距比主图更突出截面。原生1448×1086未达8K，非同一实物保真对照。 视觉评分为模型初评，单次不证明稳定性。

[原测试详情](./sources/T053/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T054

原文件：`提示词库/电商产品/[已投产·4分] 戒指.md`

原测试结论：双手交叠佩戴与绿绒八角盒两版均生成，包镶椭圆绿石和黄金融面戒圈大体延续；双手版无法可靠确认戒指位于要求的第四指，需人工复核。圆顶绿石未见原词要求的明显棱镜火彩，4K也未达到；中间单手子例未执行。 视觉评分为模型初评，单次不证明稳定性。

[原测试详情](./sources/T054/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T082

原文件：`提示词库/电商产品/[仅参考·2分] kontext大家电场景图（示例）.md`

原测试结论：可见客厅文生图示例符合主要视觉要求，仅ChatGPT适配单次初评。

[原测试详情](./sources/T082/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T085

原文件：`提示词库/电商产品/[已投产·3分] kontext电商手持商品.md`

原测试结论：合成成年手握持无品牌瓶子最小用例符合主要要求。

[原测试详情](./sources/T085/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T086

原文件：`提示词库/电商产品/[已投产·3分] 无标题.md`

原测试结论：指定自制参考的图鉴布局复现符合主要要求，结论仅限该最小用例。

[原测试详情](./sources/T086/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T089

原文件：`提示词库/电商产品/[已投产·4分] 电商详情页 元提示词.md`

原测试结论：默认四图及中文文案最小用例符合主要要求，已实际比较四张输出。

[原测试详情](./sources/T089/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T092

原文件：`提示词库/电商产品/[已投产·5分] 96组角度提示词.md`

原测试结论：第一组八角度已实际对比；纯侧面不严格、产品几何有漂移，8K未达到。

[原测试详情](./sources/T092/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T097

原文件：`提示词库/图像编辑/[已投产·3分] 【电商】产品背景更换场景丨提示词优化.md`

原测试结论：短句背景优化的森林最小用例符合主要要求。

[原测试详情](./sources/T097/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。
