# 创作桌工作台与Hermes验收

交付日期：2026-10-23（Asia/Shanghai）。这是在原有研究、50条提示词、8个Skill及A/B实测之上追加的可运行工作台。历史研究和实验结论沿用原始证据，本轮没有新增图像模型调用。

## 现在可以直接操作

| 页面 | 实际行为 |
|---|---|
| 画布流程 | 四种模板、卡片编辑、拖动/缩放、引用连接、撤销重做；动效模板直接播放真实MP4 |
| 素材库 | 上传PNG/JPEG/WebP/MP4、查看、下载、去重、加入画布；本机持久保存 |
| 提示词库 | 搜索/分类50条模板、填参、复制/下载完整提示词、加入画布；8个Skill可阅读并转为需求卡片 |
| A/B评审 | 五组原始生图与原始结论、A/B/都不采用/待评审、自定义两图比较、备注、黑/白/棋盘底、100%像素检查 |
| 口播动效 | 三种Remotion样片播放、修改文案、参数导出；连接本机服务后实际重渲染、下载与加入画布 |
| 工程迁移 | v2 JSON内嵌上传图片/MP4、画布、评审和文案草稿；空白浏览器可恢复，兼容旧版v1工程 |

Skill加入画布只是文本规范，未自动启动Agent。图片参考卡片之间的连接是制作引用，尚未提交给生成供应商。用户评审与原始实验评审分开保存；选择B不代表实验结论被改成“通过”。

## 启动

仅体验素材、提示词、A/B和现有MP4，只需Python3：

```bash
python scripts/studio_server.py
```

浏览器打开 **http://127.0.0.1:8765/prototype/index.html**。可加 `--port 8766`。不同协议/域名/端口使用不同的浏览器存储空间；换端口前先导出工程。

需要修改文案后重新输出MP4时，先安装Node22+、Chrome/Chromium、ffmpeg/ffprobe与中文字体，再在仓库运行：

```bash
cd remotion
npm ci --ignore-scripts
npm run typecheck
cd ..
python scripts/studio_server.py
```

浏览器有“本机Remotion服务已连接”即可渲染。本次使用系统 `/usr/bin/chromium`；其他位置可在启动服务器前设置 `REMOTION_BROWSER_EXECUTABLE`。Windows PowerShell用 `$env:REMOTION_BROWSER_EXECUTABLE='实际路径'`。本机服务使用Python标准库，不需要FastAPI/Flask，不使用模型密钥；依赖版本锁定于Remotion工程。

三个本机组件为KineticWords、ProcessSteps、DataComparison。只接受受限的标题/三项列表/数值等JSON参数；保留内置插画。每次运行一个任务，完成后用ffprobe检查1080×1920/30fps/H.264及6/8秒时长，再将MP4交回网页。生成文件暂存于被Git忽略的 `.cache/studio-renders/`。服务重启后旧任务URL失效；网页会把完成的MP4保存为本机素材，应导出工程或下载单个MP4备份。

静态服务器或file://不提供渲染API，页面会保留样片与参数下载，禁用重渲染。直接打开GitHub源码页面不会运行网页；请克隆/下载后启动上述本机地址。没有部署公网站点。

## 一条建议体验流程

1. 在“素材库”上传一张商品实拍，点“加入画布”。
2. 在“提示词库”找IMG-EC-02，填写product，加入画布；将需求卡连到素材/计划卡。实际模型生成时还需把原图真正附给服务。
3. 在“A/B评审”选择“我的素材”，把两张图片并排，切换目标背景并按100%检查。选择一版、写备注，加入画布。
4. 在“口播动效”填写短标题与三个关键词，点重新渲染。完成后播放、下载MP4或加入画布。
5. 右上角“导出工程”；用另一个空白浏览器导入，确认图片、视频、评审、草稿与画布引用都在。

本轮用虚构保温杯样例验收上传与迁移；不把它当真实商品保真测试。

## 存储与迁移约定

- 上传内容只保存在当前浏览器，服务器不接收上传的商品文件；本机渲染只提交文字参数。网页没有生图密钥输入框。
- 上传图片每张≤8MiB，MP4≤20MiB，最多50份，所有素材原始字节合计≤32MiB；JSON因base64增大，上限46MiB。SVG、HTML和任意外部图片URL不接受。
- 素材、个人评审、提示词/动效文案草稿保存在IndexedDB；图结构在localStorage；导出工程包含两部分。浏览器隐私模式、禁用存储、配额不足会提示导出，不能替代长期备份。
- 上传按实际字节SHA256去重；工程导入时核验内嵌内容的字节、文件头与哈希。格式/哈希失败时保留现有画布。存储失败时仍保留内存并提示立即导出。
- 内置图片和样片依赖仓库相对路径；迁移须保留完整仓库。上传文件内嵌于工程JSON，不依赖原始文件路径。
- 导入合并原素材以保护撤销历史；如果合并后超出限额，会在修改状态前拒绝导入。个人评审/文案草稿用导入版本恢复；撤销/重做只作用于画布图结构。
- 当前是一个工作区及一个活动画布，四种模板共享素材库；没有多用户权限或后台项目库。

## 本轮实际验证

可核查证据：[浏览器测试记录](../artifacts/studio/workspace-test-report.json)、[自定义动效MP4](../artifacts/studio/custom-kinetic.mp4)、[渲染参数与ffprobe](../artifacts/studio/custom-kinetic-evidence.json)、[工作台截图](../artifacts/studio/motion-custom.png)。

实际完成：浏览器修改标题“一件商品一套素材”、三个关键词“先定稿/再复用/少搬运”、补充文案“本机实际渲染验收” → 本机API → Remotion → ffprobe → 下载MP4 → 保存素材库 → 加入画布 → 工程导出 → 新浏览器导入。

测试包含：素材去重、SVG拒绝、文件名转义、缺变量拦截、提示词/Skill入画布、自定义对比、原始alpha评审保留、真实MP4播放/定位、原生像素检查、草稿持久化、完整工作区迁移、篡改字节拒绝、v1兼容、五页面390px移动布局、静态模式降级、跨源请求拒绝、任意参数拒绝、第二个并行渲染拒绝。

本轮没有重新渲染全部三类自定义动效；自定义在线流程实际跑通KineticWords。其余两个组件的原始MP4仍为之前实际交付的样片。

## 给Hermes的验收指令

在GitHub最新main上验收；不要使用追加A/B之前的旧提交。先确认 `git status --short`，保留用户未提交修改。不要重新生成SHA256SUMS来掩盖差异，不调用付费生图/视频API，不推送修改。

基础验收：

```bash
python scripts/verify_delivery.py
python scripts/verify_ab_tests.py
python scripts/verify_studio.py
node scripts/test_model.cjs
node scripts/test_studio_model.cjs
```

上述检查会写入各自验证报告，但不应修改源码、媒体原件或校验基线。浏览器与重渲染复验会更新测试截图/记录，请在临时副本或单独检出中运行：

```bash
# Python安装 requirements-tools.txt 中的可选验收依赖
python scripts/test_canvas.py
python scripts/test_studio.py --render
```

若本机缺Remotion依赖，先按上文安装；只验静态前端可运行 `python scripts/test_studio.py`，其结果应标明渲染未重跑。不要以当前机器不能重渲染为由，删除仓库里已执行的渲染证据。

人工验收：上传真实商品实拍；与另一张图比较并写备注；编辑动效文案重渲染；打开下载的MP4核对实际文字；导出到空白浏览器恢复；按目标平台检查视频字幕安全区。最后报告“通过/失败/未测/待人工复核”，区分证据完整性和视觉质量。

## 后续开发边界

在线图片/AI视频模型、API凭据管理、供应商作业轮询、计费、TTS、完整5–10分钟长片和多人协作尚未接入。本机Remotion是代码动效渲染，不等于AI视频模型生成。数据对照组件持续标注“示例数据·非实测”，不得据此宣称效率提升。商用Remotion应独立检查其当前许可。
