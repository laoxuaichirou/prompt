# 任务四：独立商品与图片编辑测试素材

本包实际使用 **ChatGPT 自带生图/图片编辑**制作素材：5 次原图/参考图生成、3 次真实编辑，共 8 张独立摄影风格 PNG；另有根据最终原图制作的 2 张对应蒙版。**10 张独立 PNG 均实际纳入 ZIP，没有用拼图代替独立素材，没有空图片或缺失图片。**

所有人物均按约32岁虚构成年人生成，没有使用真实人物照片；商品和夹克使用本次新设虚构品牌 **NIVOXA-47**。未作品牌全球唯一性或商标注册声明。

三张编辑结果统一标为 **“GPT效果参考”**，不能写成 Qwen/Krea/H3 已测试通过。它们都是第一次实际结果，全部保留，未用代码修图、贴回背景或筛掉不理想图。

## 独立素材下载与索引

以下每个链接都是**一个真实独立PNG**；GitHub文件页可用 Download raw file 下载，解压本包后也可直接打开。

| ID | 场景与用途 | 独立文件 | 实际像素 |
| --- | --- | --- | --- |
| A01 | 商品换背景：商品原图 | [source-product.png](assets/product-background/source-product.png) | 1254×1254 |
| A02 | 商品换背景：空背景参考 | [reference-background.png](assets/product-background/reference-background.png) | 1254×1254 |
| A03 | 双图换装：虚构成年人人物原图 | [source-person.png](assets/two-image-tryon/source-person.png) | 1024×1536 |
| A04 | 双图换装：夹克参考 | [reference-jacket.png](assets/two-image-tryon/reference-jacket.png) | 1254×1254 |
| A05 | 蒙版局部修改：最终客厅原图 | [source-living-room.png](assets/masked-local-edit/source-living-room.png) | 1254×1254 |
| A06 | **GPT效果参考**：商品换背景 | [第一次结果](assets/product-background/gpt-effect-reference-attempt-01.png) | 1254×1254 |
| A07 | **GPT效果参考**：双图换装 | [第一次结果](assets/two-image-tryon/gpt-effect-reference-attempt-01.png) | 1024×1536 |
| A08 | **GPT效果参考**：局部改色；严格区外保留失败 | [第一次结果，保留不理想部分](assets/masked-local-edit/gpt-effect-reference-attempt-01.png) | 1254×1254 |
| A09 | A05对应二值蒙版：白色编辑、黑色保留 | [mask-edit-white.png](assets/masked-local-edit/mask-edit-white.png) | 1254×1254 |
| A10 | A05对应alpha蒙版：透明编辑、不透明保留 | [mask-edit-alpha.png](assets/masked-local-edit/mask-edit-alpha.png) | 1254×1254 |

[asset-index.json](asset-index.json) 包含各文件尺寸、模式、SHA256、来源、提示词、实际参考顺序和编辑调用绑定；[asset-index.csv](asset-index.csv) 可用表格软件查看。

## 三个场景怎么使用

| 场景 | 固定输入顺序 | 修改目标 | 保留要求 |
| --- | --- | --- | --- |
| 商品换背景 | 1=A01商品，2=A02空背景 | 把灰色棚拍环境替换成暖色咖啡馆台面 | 瓶身、薄荷盖、右侧提环、双行品牌字和产品材质 |
| 双图换装 | 1=A03人物，2=A04衣服 | 只把白T恤换成参考夹克 | 同一虚构成年人、脸/头发/手/姿势、牛仔裤、鞋及背景；三粒扣、乳白领、穿着者左胸口袋、双肘补丁 |
| 蒙版局部修改 | 1=A05原图，2=A09二值蒙版 | 只把中间陶土色抱枕改钴蓝 | 抱枕位置形状、接缝和褶皱；其余沙发、侧抱枕、墙画、灯、植物、地毯和茶几 |

原图/参考图生成的实际英文提示词在 `prompts/01…05`；真实编辑提示词在 `prompts/06…08`。中文复用说明见 [prompts/复用说明.md](prompts/复用说明.md)。提示词不是唯一可复现条件：工具没有暴露模型版本、seed、steps，不能承诺重跑得到相同像素。

## 蒙版与最终原图的对应关系

蒙版是在查看**实际A05最终原图后**制作，绑定其SHA256，并不是提前画一个矩形碰位置。实际原图为1254×1254；选中中间抱枕的像素包围框为 **[466,409,787,673)**，左上原点，右/下边界不包含，白区 **63,073像素，约4.011%画幅**。中心[620,500]为编辑区，左右抱枕和沙发座面测试点均为保留区。

- A09为L模式，仅0/255；**255编辑、0保留**，无羽化。
- A10为RGBA，RGB恒白；**alpha=0编辑、alpha=255保留**，与A09逐像素反相。
- A10是给后续需要透明蒙版约定的工具使用的独立技术素材，本次GPT调用没有使用它，也不能据此声称任一目标API已兼容。

完整坐标、原图哈希、方法在 [results/mask-metadata.json](results/mask-metadata.json)，生成代码为 [tools/make_mask.py](tools/make_mask.py)。代码仅分析原图像素并生成空白画布上的技术蒙版，不修改照片；8张照片均是工具输出原文件的字节一致副本。

**本次GPT编辑工具没有独立mask参数。** A09作为第二张参考图随文字指令传入，不等于执行了原生硬蒙版inpainting。本次局部编辑虽改对了颜色，但没有严格冻结蒙版外像素。

## 已观察的结果与不理想项

完整逐项记录在 [REVIEW.md](REVIEW.md)，机器可读差异在 [results/masked-edit-diff.json](results/masked-edit-diff.json)。

- 商品：目视可见咖啡馆背景、台面与接触阴影，主体与品牌可辨；并非对原商品像素进行无损剪贴，轮廓/光照/细节存在重绘，未认证几何、色彩和商标字形完全一致。
- 换装：目视可见同一人物构图、三粒扣、乳白领、胸袋和双侧补丁；不宣称人脸身份算法、服装尺寸或物理试穿精度通过。
- 局部编辑：中间抱枕确已变蓝，但沙发等区外纹理也改变。**严格“区外像素不变”检查失败**：区外约98.899%像素有至少一个通道变化，其中约10.038%像素的最大通道差超过16/255。数值仅是直接像素差，不是视觉质量得分；没有后期贴回原背景掩盖它。

没有“仅展示成功图”的筛选：所有8次工具输出和3次编辑首轮结果都在本包；未发生额外生成重试。明确不理想的A08作为边界测试素材保留，不伪造额外失败图。

## 文件检查与复现

直接使用PNG不需要代码依赖。可选检查需要 Python3 + Pillow，本次为Python3.12.14、Pillow12.3.0。

```bash
python3 tools/verify_manifest.py
python3 tools/check_assets.py
```

第一个核对原包文件清单和SHA256；第二个读取真实PNG、核对原图/蒙版尺寸、位置、通道和参考绑定，并重算差异。文件及蒙版检查通过与编辑质量通过是两件事：`results/checks.json`会明确保留严格局部保留 `FAIL`，不会打印Qwen/Krea/H3通过。

仅重建技术蒙版：`python3 tools/make_mask.py`。更换原图后必须重新检查ROI及轮廓，不能把旧蒙版缩放后声称仍精确对应。重跑会更新部分结果文件；应先核对原包哈希，再运行。可选 `python3 tools/package.py` 重新建立MANIFEST及ZIP。

真实运行日志在 `results/run-log.json`、`results/mask-build.stdout.log`、`results/asset-check.stdout.log`，工具调用记录在 `results/tool-calls.json`。源图原始输出路径只用于本次会话内部溯源，下载请用本包相对文件或GitHub，不是让你访问某个本机路径。

本包是独立任务四素材交付，没有覆盖任务一/三，也没有修改或接入现有画布。未执行和不能由这些结果证明的事项见 [UNVERIFIED.md](UNVERIFIED.md)。
