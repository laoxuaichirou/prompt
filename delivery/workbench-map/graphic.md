# 品牌海报与封面工作台

[返回分类总览](./README.md)

整理优先级：优先整理。状态：候选来源映射，未逐项归一化成预设，未新增生成测试。

**输入：**主题、主副标题、品牌色、产品或可选人物素材

**输出：**文字创意封面、促销海报、旅行城市海报、产品广告、系列封面与图文版式

**可用子分类：**纯文字封面、旅行海报、促销海报、产品广告、系列封面

## 整理判断

- 以传播信息和版式为入口，T178等人像海报可同时挂这个标签，不复制成第二份提示词。
- T081只允许指定主副标题；适合抽取为标题白名单、文字材质和情绪选项。
- T030一个文件里含多种示例，原测只覆盖广州旅行海报；同页水彩肖像不是已验证的上传本人预设。
- 固定品牌、城市和营销文案需参数化；新版本必须重新检查文字、版式及产品细节。

## 对应原条目

|原条目|原标题|原测试状态|原文|示例|
|---|---|---|---|---|
|T004|广告创意|存在问题|[原文](./sources/T004/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/013-T004-ad01.jpg)|
|T030|image-2水彩拼贴旅行海报提示词！|存在问题|[原文](./sources/T030/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/048-T030-output.jpg)|
|T053|奢华8K国家美食广告|存在问题|[原文](./sources/T053/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/065-T053-T053-01.jpg)|
|T074|封面常用提示词|存在问题|[原文](./sources/T074/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/088-T074-output.jpg)|
|T081|封面大师|符合要求|[原文](./sources/T081/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/095-T081-page1.jpg)|
|T084|电商海报生成元提示词|存在问题|[原文](./sources/T084/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/098-T084-output.jpg)|
|T089|电商详情页 元提示词|符合要求|[原文](./sources/T089/original.md)|[查看](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/previews/104-T089-creative.jpg)|

### T004

原文件：`提示词库/海报封面/[待测试·4分] 广告创意.md`

原测试结论：三次适配文字子项均命中，但服装细节在穿着侧受遮挡和裤脚变化影响；整体存在问题。三次成功不代表稳定性已验证，不冒充原模型实测。

[原测试详情](./sources/T004/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T030

原文件：`提示词库/海报封面/[已投产·3分] image-2水彩拼贴旅行海报提示词！.md`

原测试结论：广州海报主要场景与标题命中，竖排及空缺文案处理有偏差；仅测第一子例。

[原测试详情](./sources/T030/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T053

原文件：`提示词库/电商产品/[已投产·4分] 奢华8K国家美食广告.md`

原测试结论：两幅独立4:3美食图均有深绿背景、蒸包皮与猪肉葱馅、悬空碎屑和摄影变化，无手/盘/桌/文字/商标；微距比主图更突出截面。原生1448×1086未达8K，非同一实物保真对照。 视觉评分为模型初评，单次不证明稳定性。

[原测试详情](./sources/T053/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T074

原文件：`提示词库/海报封面/[仅参考·3分] 封面常用提示词.md`

原测试结论：封面核心布局符合要求；8K未达到，精确黄金分割未验证。

[原测试详情](./sources/T074/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T081

原文件：`提示词库/海报封面/[已投产·4分] 封面大师.md`

原测试结论：可见简体原版的两页最小用例符合要求；不代表缺失的发布版本或稳定性通过。

[原测试详情](./sources/T081/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T084

原文件：`提示词库/电商产品/[仅参考·4分] 电商海报生成元提示词.md`

原测试结论：877词元提示词已执行并出图，主要内容符合，最终图片比例与扩写要求不符。

[原测试详情](./sources/T084/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。

### T089

原文件：`提示词库/电商产品/[已投产·4分] 电商详情页 元提示词.md`

原测试结论：默认四图及中文文案最小用例符合主要要求，已实际比较四张输出。

[原测试详情](./sources/T089/test-evidence.json)
该来源尚未在本次映射中生成新的可运行预设，也未新增媒体测试。
