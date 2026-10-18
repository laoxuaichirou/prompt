# 预设数据使用说明

[返回目录](./README.md)

这是一份可供工作台接入的预设数据草案，尚未实现图片上传、模型调用或生成界面。所有归一化提示词的 `normalized_prompt_test_status` 都是“未执行生图回归”。原测示例是合成人物测试结果，用于理解效果，不代表换成任意用户照片也已验证。

## 选择预设和绑定素材

从 `portrait-presets.json` 的 `presets` 读取卡片。分类、标题、缩略图和输入类型可直接用于目录。缩略图链接指向同一 GitHub 分支中已上传的原测试浏览副本。

|字段|使用方式|
|---|---|
|`id` / `source_ids`|`id` 是去重后的卡片ID；`source_ids` 保留原条目及重复版本编号|
|`input_mode: single`|一张人物照片入口；不表示该改写已验证身份保持|
|`input_mode: optional`|人物照必需；T078可加掌心构图图，T178可加球衣图|
|`input_mode: extra`|按 `reference_slots` 提供服装、产品或宠物图；T124也可用人宠合影|
|`input_mode: multi`|提供足够人物的单照或合影，按 `min_subjects` 绑定各自身份|
|`variables`|页面展示影响结果的选项；未修改时取 `default`，渲染模板中的 `{{变量名}}`|
|`layout`|记录目标画幅、拼格数量与独立输出数量；不是实际模型参数保证|
|`sources`|原文件名、SHA256、原文、原测输入和结论追溯|

图片必须作为实际图像附件传给所用工具；只在提示词中填写文件名或URL，不能代替上传图片。单人预设默认参考图1为身份，辅助素材为图2。多人按人物A/B/C分别描述，避免混脸。

辅助引擎有自己的图像顺序，必须按其正文绑定。例如T011为“身份、服装、场景”三图；T134为“源场景图1、目标人物图2”。不要对这些引擎强套“图1永远是目标本人”。

## 直接提示词与元提示词

1. `kind: image_prompt`：填入 `variables` 后，把 `image_prompt_template` 和参考素材交给图像工具。
2. `kind: meta_prompt`：先把 `meta_prompt_template` 与参考素材交给文本/视觉模型，得到包含 `layout`、`shots` 的规划JSON；逐项检查其中的 `image_prompt`，再交给图像工具。规划文本不能计为已生成图片。
3. `layout.type: separate`：逐张生成 `expected_images` 张。直接提示词中的 `per_output_instructions` 分别限定每张内容；单次调用明确“本次只生成这一视角/版本，不拼图”。共享同一人物参考、穿搭和场景约束。
4. `grid`、`strip`、`grid_overlay`：在一张图片中实现模板要求的格数或叠加构图，`expected_images` 为1。不能把不同卡片的输出合并成总拼图验收。

T001的 `count` 应与所选场景数、请求的独立输出数同步。其他卡片的输出数量按 `layout`，不要把“九个分镜”误解为总是要调用九次。

## 场景和调色选项

- **T001**：`variants` 保留40个原场景的标题及 `source_text`。用户选择标题后，将对应完整场景段落加入规划输入，以保留原文穿搭、环境及姿势细节；不只发送一个标题。场景段落中的未见外观可由模型合成，但身份仍来自上传照片。
- **T025**：`variants` 保留22种调色。选中一种后，将其 `title` 填入 `color_look`，将其 `color_description` 填入 `color_description`。不要把 `original_example` 的另一个人物或场景作为本次主体。默认调色描述是归一化后的简写，可用原文提取段替换。
- [查看40个场景与22种调色](./VARIANTS.md)。它们是选项，尚未逐项验证。

## 两个具体输入示例

T178：上传 `person_photo`；设置 `team="阿根廷蓝白"`、`jersey_number="10"`、`title="MY WORLD CUP"`，替换模板变量后生图。若要求精确复现某款球衣，再传 `aux_reference`。球队名称或配色描述本身不能保证官方队服细节准确。

T145：上传 `person_photo`；用默认发型策略渲染模板。生成目标是同画面里的写实本人和Q版小模型。原测试没有上传身份参考，因此这个“本人入口”需首次回归；原测“符合要求”仍只适用于原虚构人物用例。

以上是调用输入说明，没有在本次执行新的生图。

## 验收与状态

`source_test_statuses` 只描述原条目原用例。新版本的 `release_status: draft_identity_regression_required` 必须保留，不能因原条目成功而改成通过。

回归时保存输入照片、变量、最终提示词、工具/可见模型、全部输出和视觉检查。至少检查本人可辨识性、风格特征、手部与物件、文字、格数、跨图连续性；多角度或多版本必须查看完整组。背面和年龄变化是合成推演，不是对不可见真实信息的还原。

`unavailable.json` 的14条拦截与7条缺失来源不进入可运行卡片菜单。完整219条来源的收录关系见 `scope-index.json`。本轮没有为阻塞条目改写绕过版本。

原图和合成参考素材不重复装入本预设包；需要复查原测输入时，使用[原图分包](https://github.com/laoxuaichirou/prompt/blob/image-test-delivery-2026-10-18/delivery/image-parts/README.md)和[完整原测试记录](https://github.com/laoxuaichirou/prompt/raw/refs/heads/image-test-delivery-2026-10-18/delivery/prompt-test-records.zip)。`sources/*/test-evidence.json` 的相对图片路径以原测试记录包根目录为基准。
