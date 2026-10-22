# 创作桌：AI画布研究、提示词与视频素材工具箱

为电商商品素材、影视分镜、5–10分钟AI长片和自媒体口播素材准备的研究与规划交付。包含三类项目榜单、分类提示词/Skill、可交互画布原型，以及实际生成的图片和Remotion样片。

**先看 [交付文档与Hermes验收](docs/交付文档-Hermes验收.md)** · [下载中文交付PDF](artifacts/交付文档-创作画布研究与规划.pdf) · [下载仓库ZIP](https://github.com/laoxuaichirou/prompt/archive/refs/heads/main.zip)

这是研究、规划与可运行样例。画布原型尚未接入真实付费生成接口；5/10分钟文件是镜头计划，三个MP4是6/8/6秒口播动效素材。

## 从这里开始

| 你要做什么 | 入口 |
|---|---|
| 理解课程 | [PDF课程整理](docs/01-PDF课程整理.md) |
| 看产品方案 | [画布工具产品规划](docs/02-画布工具产品规划.md) |
| 选画布技术/竞品 | [画布项目Top10](research/01-canvas-top10.md) |
| 找生图提示词/Skill | [生图Top10](research/02-image-top10.md) |
| 找视频提示词/Skill | [视频Top10](research/03-video-top10.md) |
| 找Remotion/上游资源 | [分类资源入口](research/04-upstream-resources.md) |
| 直接用模板 | [50条原创提示词](prompts/README.md) / [机器可读JSON](prompts/catalog.json) |
| 交给Hermes执行 | [8个原创技能](skills/README.md) |
| 阅读上游原文 | [选定MIT文本镜像](third_party/README.md) |
| 体验画布交互 | 本机打开 [prototype/index.html](prototype/index.html) |
| 复用口播动效 | [Remotion工程与重现步骤](remotion/README.md) |
| 检查实测结果 | [生图与动效测试记录](docs/03-生图与动效测试记录.md) |

## 画布交互原型

![创作桌原型](artifacts/canvas-prototype.png)

选择模板，直接编辑卡片；支持拖动、引用连接、缩放、撤销重做、本机自动保存、工程JSON导入导出。四种入口对应电商、影视、长片和口播。浏览器禁用本机存储时会提示导出备份。

原型没有构建依赖；生成按钮为明确标注的“检查执行计划”，不调用AI服务。图片卡片使用下面本次真实生图结果。

## 本次实际生成图片

<table><tr><td><img src="artifacts/IMG-EC-01.png" width="240" alt="电商白底主图"></td><td><img src="artifacts/IMG-FILM-03.png" width="360" alt="气象站影视关键帧"></td><td><img src="artifacts/IMG-FILM-08.png" width="180" alt="口播插画"></td></tr><tr><td>电商主图 · IMG-EC-01</td><td>影视关键帧 · IMG-FILM-03</td><td>口播插画 · IMG-FILM-08</td></tr></table>

三条均为原创提示词单次测试，完整调用文本、尺寸、哈希和观察局限见 [image-test-results.json](artifacts/image-test-results.json)。没有真实商品参考，不能据此认定实拍保真或跨镜头一致性。其他模板未逐条生成测试。

## Remotion真实样片

| 模板 | 文件 | 参数 |
|---|---|---|
| 关键词逐项进入 | [remotion-kinetic.mp4](artifacts/remotion-kinetic.mp4) | 6秒，180帧 |
| 三步流程卡片 | [remotion-steps.mp4](artifacts/remotion-steps.mp4) | 8秒，240帧 |
| 数据对照图 | [remotion-comparison.mp4](artifacts/remotion-comparison.mp4) | 6秒，180帧 |

均为1080×1920、30fps、H.264、静音；源文件、props和package-lock已保存。数据对照是明确标注的虚构示例。普通MP4不透明；配音和完整口播合成尚未制作。

## 排名和推荐

三类各10项，按**已检索并核验的相关候选**star降序排列，采集日期2026-10-23北京时间。保存65个成功检索页、405个去重搜索候选和30个固定文件入口校验。扩展搜索有429限流，不能证明全站穷尽；详见 [方法与排除规则](research/METHODOLOGY.md)。[CSV](research/top30.csv) / [JSON](research/top30.json)可供Hermes读取。

按你的用途，推荐优先研究React Flow编辑底座、Toonflow影视流程、商品图片排版子编辑器与Remotion；无限画布上的模型参数默认折叠。长片分章节、分镜头生产，角色/商品/场景先定稿，试产一镜后才批量。

## 本机验收

```bash
# 在仓库根目录，Python3 + ffprobe；无需模型密钥
python scripts/verify_delivery.py
node scripts/test_model.cjs

# 可选：Python Playwright + 已安装Chrome/Chromium
python scripts/test_canvas.py

# 提示词查询
python scripts/prompt_cli.py list --kind image --category ecommerce
python scripts/prompt_cli.py show IMG-EC-01
```

浏览器默认使用系统Chromium，可用 `CANVAS_BROWSER_EXECUTABLE` 指定其他路径。Remotion重新渲染请看工程README。`SHA256SUMS`用于本次交付文件校验，不要求异平台重编码结果字节完全相同。

## 范围与许可

原创代码/技能为MIT，原创提示词与研究笔记为CC BY 4.0；第三方镜像保留原许可，其他上游只提供来源与分类。详情见 [LICENSE](LICENSE)。原始课程PDF未公开分发。模型服务、Remotion/tldraw等依赖保留各自条款。

本次没有实现后台队列、多人协作、真实供应商API、TTS或5–10分钟整片。后续实施范围、成本公式与验收门槛在产品规划和交付文档中逐项列明。
