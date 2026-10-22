# 交付文档与Hermes本机验收

交付日期：2026-10-23（北京时间）。目标仓库：`laoxuaichirou/prompt`。本次为**研究、产品规划、资源库及可运行样例交付**；用户原需求是规划画布工具，未把后续生产系统冒充已经实现。

## 交付结果

| 需求 | 交付内容 | 位置 |
|---|---|---|
| PDF内容整理 | 33物理页的课程要点、流程、适用边界与产品转译 | 01-PDF课程整理.md |
| 三类各10个项目 | 画布/生图提示词Skill/视频提示词Skill，按已核验候选star降序，30项 | ../research/top30.json、top30.csv及三份榜单 |
| 研究可追溯 | 65个成功搜索页、405个去重搜索候选、30个固定文件入口在线校验 | ../research/evidence |
| 提示词分类 | 24生图+18视频/生产+8Remotion，共50条原创模板 | ../prompts/catalog.json |
| Skill分类 | 8个原创工作流技能 | ../skills |
| 上游原文 | 3个MIT授权选定文本包，13文件含LICENSE与固定版本哈希 | ../third_party |
| 工具规划 | 用户路径、架构、模型适配、资产版本、成本、MVP与验收 | 02-画布工具产品规划.md |
| 易用交互参考 | 无依赖画布原型，四模板、连线、保存、导入导出、撤销 | ../prototype/index.html |
| 生图实测 | 三张真实生成PNG及逐图检查、完整执行提示词 | ../artifacts/IMG-*.png、image-test-results.json |
| 口播Remotion | 三个实际渲染的静音MP4、源码、props与锁定依赖 | ../remotion、../artifacts/remotion-*.mp4 |
| 长片规划 | 5分钟/10分钟逐镜头计划，60/120镜，各5秒 | ../examples |
| 可下载资料 | 中文交付PDF、完整仓库归档、SHA256清单 | ../artifacts/交付文档-创作画布研究与规划.pdf、../SHA256SUMS |

## 关键建议

默认采用“模板向导 + 媒体卡片 + 场景级画布”。优先参考React Flow的节点编辑能力、Toonflow的影视资产工作流、简洁白板的交互，以及商品排版子编辑器。Remotion单独负责真实字体、流程图、卡片和数据动效。长视频用章节与镜头表组织，逐镜生成后合成，避免一次生成整片或在画布上同时摆满上百节点。

## 本机快速验收

建议先从GitHub检出本仓库，记录实际commit。运行命令均从仓库根目录开始：

```bash
# 需要Python3与ffprobe；不需要API密钥或互联网
python scripts/verify_delivery.py

# 需要Node；验证环路、类型与恶意/无效导入约束
node scripts/test_model.cjs

# 示例：查看与填入提示词
python scripts/prompt_cli.py list --kind image --category ecommerce
python scripts/prompt_cli.py show IMG-EC-01
python scripts/prompt_cli.py render IMG-EC-02 --vars '{"product":"保温杯"}'
```

默认验收同时检查文件SHA256，不要先运行 `build_manifest.py` 重写清单来掩盖不一致。修改源文件后应以原commit为基线审查差异，再按新版本重新生成清单。

可选的浏览器复查：本机安装Python Playwright及Chrome/Chromium后，`python scripts/test_canvas.py`。脚本默认Linux `/usr/bin/chromium`；其他系统需将该路径改为本机浏览器路径，或设置 `CANVAS_BROWSER_EXECUTABLE` 环境变量。测试启动临时本地静态服务并自动关闭，不会调用外部生成服务。截图和测试报告会被覆盖，应在单独检出或备份后复查。

可选的Remotion重新渲染：按 [remotion/README.md](../remotion/README.md) 执行 `npm ci --ignore-scripts`、`npm run typecheck`、`npm run render:all`。重新渲染的编码字节可能因浏览器/字体/平台而变化，**重现验收以实际画面、时长、帧率和内容为准；SHA256用于核对本次交付文件，不要求另一机器重编码后字节相同**。

查看网页原型：用浏览器打开 `prototype/index.html`。选择模板→拖动卡片→编辑文字→点击输出端口后点下游输入端口→检查计划→导出JSON→关闭重开→导入JSON。原型无构建依赖；如果浏览器对file协议禁用存储，使用本机静态文件服务并导出工程备份。

## 验收矩阵

| 检查 | 通过标准 | 本次证据 |
|---|---|---|
| PDF理解 | 不混淆物理页/课件页；明确平台特定规则 | PDF摘要与source哈希 |
| 主榜 | 每类10项、star降序、对应搜索记录和commit | top30及entry-checks |
| 范围透明 | 不宣称穷尽GitHub；429记录不作为空结果 | METHODOLOGY与search-failures |
| 模板 | 50个唯一ID、变量声明准确、用途/验收存在 | catalog及离线校验 |
| 原创技能 | 8个完整输入/执行/输出/验收规范 | skills/*/SKILL.md |
| 上游文本 | 原LICENSE保留，13文件哈希与来源一致 | third_party/manifest.json |
| 原型 | 保存恢复、连线、撤销、导入导出、移动端无横向溢出 | 16项真实Chromium检查；13个模型断言 |
| 生成图片 | 三个PNG可读，尺寸/哈希一致，观察与局限清楚 | image-test-results |
| 动效 | 1080×1920、30fps、6/8/6秒、180/240/180帧、H.264、静音 | media-probe及代表帧 |
| 长片计划 | 分镜帧区间连续，总长300/600秒，状态为planned | examples镜头表 |
| 下载 | 中文PDF可打开，归档含源码/资源/样片，无node_modules与密钥 | SHA256SUMS与交付归档 |

## 已完成与尚未实现

已完成：PDF整理；三类候选集star Top10；固定版本资源索引；分类模板与技能；三次生图；可操作原型；三个Remotion样片；产品规划；自动验收与文件校验清单。

尚未实现：真实图片/视频供应商API接入、付费视频生成、服务端持久队列、多人协作、配音/TTS、完整口播合成、5–10分钟最终影片、商品实拍保真/跨镜头连续性验证。50条模板中只有3条生图模板实际生图；其他没有虚报已测试。横版动效组件未输出样片。

检索边界：GitHub API在本环境被代理拒绝，使用公开仓库搜索与固定原始文件核验；扩展检索有429限流。榜单可以核对本次证据，但无法证明全站没有更高star的遗漏相关项目。上游README中的模型名称、参数、价格和效果承诺没有被当作本次已验证结果。

## 给Hermes的验收指令

```text
请在这个仓库中验收本次“创作画布研究与规划”交付。
先读取 docs/交付文档-Hermes验收.md 和 research/METHODOLOGY.md。
运行 python scripts/verify_delivery.py，再运行 node scripts/test_model.cjs。
有可用浏览器时独立复查 prototype 的保存、连线、撤销和导入导出。
播放 artifacts 下三个Remotion MP4，检查中文可读与底部安全区；图片按记录检查。
把通过、失败、未运行、需人工判断分开报告。
按用户原需求评估规划是否覆盖电商、影视、5–10分钟长片与口播素材；
不要把计划镜头表当已生成长片，也不要把静态样例当真实供应商接入完成。
不要因文件哈希不匹配就重写SHA256SUMS；先报告差异与原因。
```

## 后续启动顺序

先用真实商品和一场戏各做30秒试产，验证可用素材率与实际成本；据此锁定一个图片供应商和一个视频供应商，再实现P1–P3。先验5分钟合成，再扩10分钟。需要凭据时通过本机安全配置提供，不将密钥放入GitHub或聊天。
