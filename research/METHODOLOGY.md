# 检索范围、排名规则与证据

## 这份Top10表示什么

三类榜单分别是**本次检索并人工判定相关、核验README及许可的候选项目中，按star降序取前十**。共保存65个成功检索页、405个去重搜索候选；另对4个已知仓库直接核验。不是全站穷尽排名；没有使用“搜索第一页就是该行业前十”的推断。检索遗漏、搜索词语义与公开网页限流都会影响候选覆盖。

采集工作发生在2026-10-23北京时间（UTC原始记录为2026-10-22晚间）。每条星数有自己的UTC时间戳；不同页面之间不构成同一秒快照。星数会变化，复查时不应要求与未来实时星数完全相等。

## 分类口径先于排序

| 类别 | 纳入 | 排除 |
|---|---|---|
| 画布 | 直接提供创意内容白板/设计/媒体节点工作流的成品，或直接实现节点编辑的框架 | 通用2D/3D渲染库、图表库、游戏引擎、仅数据库结构图、纯网站低代码构建、没有编辑器的技能文档 |
| 生图提示词/Skill | 主体是生图案例/关键词/提示词，或包含明确可定位的生图/配图技能 | 只有模型权重、推理UI、图像理解论文、纯前端代码设计技能、去水印工具 |
| 视频生成提示词/Skill | 主要服务于生成视频的导演、分镜、参考绑定与提示词库 | 仅视频推理应用/模型，纯录屏工具、仅知识提炼工具、只靠代码生成动效的合集 |

纯代码动效与Remotion资源单列在 [补充资源](04-upstream-resources.md)，不混作扩散类视频模型提示词。影片生成应用也作为补充竞品研究，避免用应用的star替代其内部某个技能的star。

## 实际检索方式

当前环境对 `api.github.com` 的直接CONNECT返回403，但 `github.com/search` 与 `raw.githubusercontent.com` 可用。因此使用GitHub公开网页的结构化仓库搜索数据，不请求用户新密钥，不尝试绕过限流。

查询使用 `type=repositories&s=stars&o=desc`。按多组关键词和star阈值扩展，再去重。原始每页JSON仅保留查询、URL、时间、结果数和仓库元数据；不保存登录信息、网页CSRF数据或密钥。

代表性关键词组：

- 画布：`canvas`、`infinite-canvas`、`AI canvas`、`canvas editor`、`node-based image`、`node editor`、`whiteboard`、`design editor`，以及ComfyUI、xyflow、penpot、drawio的名称查询。
- 生图：`image prompts`、`image prompt`、`image generation prompts`、`image generation skill`、`midjourney prompts`、`nano banana prompts`、`nano-banana`、`gpt image prompts`、`gpt4o images`、`stable diffusion prompts`。
- 视频：`video prompts`、`video generation prompts`、`video generation skill`、`seedance`、`seedance in:name`、`seedance skill`、`AI video skill`、`sora prompts`、`veo prompts`。
- 动效：`remotion in:name`、`remotion skill`，用来做补充资源索引。

全部成功请求见 [evidence/search](evidence/search/)。直接核验使用公开仓库页面的精确 `stargazerCount` 字段，单独存放在 [evidence/direct](evidence/direct/)；它们不计入65个搜索页。后期13个扩展检索页返回429，详见 [search-failures.json](evidence/search-failures.json)。失败请求没有被当成零结果，也没有宣称覆盖了这些请求本应返回的项目。部分扩展问题已被此前更宽查询覆盖，但不据此宣称完整。

## 人工筛选例子

| 项目/类型 | 处理与原因 |
|---|---|
| three.js / D3 / Chart.js / PixiJS / Fabric.js | star很高；通用渲染/图表库，作为底层技术参考，不进入“创作画布成品/节点编辑框架”主榜 |
| React Flow / xyflow | 直接是可自定义节点编辑器框架，符合主榜口径 |
| drawio-desktop 与 drawio web仓库 | 同一产品只算一次，选星数更高的桌面主仓库，注明不是媒体生产应用 |
| dream-num/univer | Office运行时/表格文档为主，本轮不列为创意媒体画布；需要办公协同时另评估 |
| onlook-dev/onlook | 网站界面代码可视化构建，不作为本次媒体内容画布主榜 |
| Leonxlnx/taste-skill | 当前README说明主技能是前端界面设计，用互联网图片；生图技能已迁到另库，不把它101k star计作生图技能star |
| guizang-ppt-skill / garden-skills | 有明确配图/生图工作流入口，纳入生图；标注合集/配图用途，不能说全库都是生图技能 |
| JimLiu/baoyu-skills | 找到完整独立生图技能，补入候选并按star进入生图榜；发布技能不自动执行 |
| openai/skills | 当前README标记deprecated，历史imagegen/sora入口在固定版本均404；不把旧版本技能当当前可用资源 |
| sickn33/antigravity-awesome-skills | 重定向后的fal-generate是通用集成规范，缺具体模板与执行例子，历史上游不可用；不作为本轮提示词库。详见candidate-decisions证据 |
| GoogleCloudPlatform/generative-ai | 通用教程/示例工程，非本轮提示词库或独立Agent Skill，作为后续官方接入资料 |
| OpenMontage / FireRed-OpenStoryline | 视频创作应用，补充研究；不冒充视频提示词库 |
| yihui-dev/awesome-opus5-5-videos / lemo-opuscar / video-shotcraft | 以AI写代码制作视频/动效为主，移到Remotion与代码视频补充表 |
| Recordly / cangjie-skill | 分别是录屏工具、从知识提炼技能；不是生成视频提示词 |
| stable-diffusion-videos / open-higgsfield | 生成应用或推理工具；不因描述出现prompt就当提示词/Skill库 |
| 文字命中但主题无关的政治、招聘或Node服务仓库 | 排除；搜索词命中不等于领域相关 |

## 如何核验

每个入榜仓库保存默认分支、完整commit SHA、README哈希、根目录文件清单、许可文件头和固定版本URL。详情在 [evidence/repos](evidence/repos/)。表格同时输出 [JSON](top30.json) 和 [UTF-8 BOM CSV](top30.csv)。固定版本入口另做在线读取校验，结果见 `evidence/entry-checks.json`。

复查star：找到表格条目的 `star_evidence`，核对 `items[].name` 与 `stars`。复查内容：访问固定commit README或具体SKILL入口，避免分支后续变化造成误判。仓库自称的模型能力、免费成本与性能没有因出现在README就当成已验证事实。

## 排名与推荐分开

榜单严格按星数，不按个人偏好重排。对于本项目，优先借鉴React Flow编辑底座、Toonflow影视流程、商品排版子编辑器与Remotion模板；另外研究infinite-canvas。星数较低的项目也可能更接近用户目标。

许可证只记录本次仓库文件事实，不代替对分项素材、商标、人像或供应商服务条款的核对。未明确许可的项目只收链接与摘要；复制入库的上游文本独立保留其原LICENSE与SHA256，见 `third_party/manifest.json`。
