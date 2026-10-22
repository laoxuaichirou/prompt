# 上游提示词、Skill与Remotion分类入口

## 原创、镜像、索引三层

- `prompts/`：针对本项目编写的50条原创模板，可直接填变量使用。
- `skills/`：8个原创可执行工作流规范，建议Hermes从此处起步。
- `third_party/`：3个明确MIT授权的选定上游文本包，13个文件，保留原文、原LICENSE、固定commit与哈希。生图海报包保留了全部必读references；Seedance提示词技能保留中英文；GPT Image模板文档是节选文件镜像，不是整仓库安装。
- 下表：三类主榜中生图/视频的20个上游入口。未明确许可的项目只做链接与摘要，不整库复制。

## 生图与视频资源入口

| 分类 | 上游 | 具体入口 | 用途 |
|---|---|---|---|
| image | freestylefly/awesome-gpt-image-2 | [agents/skills/gpt-image-2-style-library/SKILL.md](https://github.com/freestylefly/awesome-gpt-image-2/blob/63e6176fa01be51c000108dacd72716d3e46784b/agents/skills/gpt-image-2-style-library/SKILL.md) | 产品、品牌、海报模板及结构化分类 |
| image | op7418/guizang-ppt-skill | [references/image-prompts.md](https://github.com/op7418/guizang-ppt-skill/blob/c91369c449d34755d320a8b81d0734000d99d1ab/references/image-prompts.md) | 封面、配图和视觉系统一致性 |
| image | JimLiu/baoyu-skills | [skills/baoyu-image-gen/SKILL.md](https://github.com/JimLiu/baoyu-skills/blob/1567581c26ec29f4216c6e6835415bf30343b0e3/skills/baoyu-image-gen/SKILL.md) | 多供应商生图、参考图编辑与提示词文件批处理 |
| image | PicoTrex/Awesome-Nano-Banana-images | [README.md](https://github.com/PicoTrex/Awesome-Nano-Banana-images/blob/2558bf0bb825be150c5d1aeab918cd90004882d3/README.md) | 参考编辑、多视图与视觉案例 |
| image | Evolink-AI/awesome-gpt-image-2-API-Prompts | [README.md](https://github.com/Evolink-AI/awesome-gpt-image-2-API-Prompts/blob/e2a269ad1a055a0b4f6c1e170341c6c1aba30faa/README.md) | 电商主图、广告与产品场景 |
| image | YouMind-OpenLab/awesome-nano-banana-pro-prompts | [README_zh.md](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts/blob/6ee3c6ffefb95a3774baeeaa645d14914cd6d949/README_zh.md) | 头像、营销图、缩略图分类 |
| image | ConardLi/garden-skills | [skills/gpt-image-2/SKILL.md](https://github.com/ConardLi/garden-skills/blob/7a6d5a72e4f44bb4cc0c23c01b3d97205c723b68/skills/gpt-image-2/SKILL.md) | gpt-image-2子技能与视觉规划 |
| image | willwulfken/MidJourney-Styles-and-Keywords-Reference | [README.md](https://github.com/willwulfken/MidJourney-Styles-and-Keywords-Reference/blob/1e54e7ffd4b6a9a2afc6de83bcfcff962619f299/README.md) | 风格探索、材质与镜头词汇 |
| image | ZeroLu/awesome-nanobanana-pro | [README.md](https://github.com/ZeroLu/awesome-nanobanana-pro/blob/415896b006f8228c638ef2a27de9414b82982896/README.md) | 写实、海报与视觉表达 |
| image | YouMind-OpenLab/awesome-gpt-image-2 | [README_zh.md](https://github.com/YouMind-OpenLab/awesome-gpt-image-2/blob/3419a50241a107b5c0394fdab4376518dd310b8d/README_zh.md) | 电商、社媒、信息视觉分类 |
| video | Emily2040/seedance-2.0 | [skills/seedance-prompt/SKILL.md](https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/skills/seedance-prompt/SKILL.md) | 镜头表、参考绑定、续接与单动作分镜 |
| video | dexhunter/seedance2-skill | [zh/SKILL.md](https://github.com/dexhunter/seedance2-skill/blob/516284d5bab58361bfdfed3cc96cee3e837d4c44/zh/SKILL.md) | 中文/英文多模态引用、运镜与广告模板 |
| video | zenstory-ai/drama-skills | [skills/short-drama-video-prompts/SKILL.md](https://github.com/zenstory-ai/drama-skills/blob/fdb7b7c58017e3eae64eca382c2a85ede368dab0/skills/short-drama-video-prompts/SKILL.md) | 剧本、资产、分镜、视频提示词、剪辑交接 |
| video | songguoxs/seedance-prompt-skill | [.claude/skills/seedance/SKILL.md](https://github.com/songguoxs/seedance-prompt-skill/blob/57d1e2f273747c238dd892698a05137ab2f10d4a/.claude/skills/seedance/SKILL.md) | 多参考锚定、场景策略与镜头语言 |
| video | ZeroLu/awesome-seedance | [README-zh.md](https://github.com/ZeroLu/awesome-seedance/blob/51e06d7f0f827d30f4d63609f45ebcebaa2f7a29/README-zh.md) | 电影感、广告与运镜案例 |
| video | kaomei/stickman-video-director | [skills/directing-stickman-videos/SKILL.md](https://github.com/kaomei/stickman-video-director/blob/70199c86911d84de9804441ce581eeb25142efba/skills/directing-stickman-videos/SKILL.md) | 知识解释、自媒体、叙事风格与分镜 |
| video | liangdabiao/Seedance2-Storyboard-Generator | [.claude/skills/seedance-storyboard-generator/SKILL.md](https://github.com/liangdabiao/Seedance2-Storyboard-Generator/blob/aceab4e277aa26cb33794fce6e17e5425ad721dd/.claude/skills/seedance-storyboard-generator/SKILL.md) | 人物/场景/道具编号与多集衔接 |
| video | LearnPrompt/awesome-seedance | [README_zh.md](https://github.com/LearnPrompt/awesome-seedance/blob/6c2a99ab454b5201a8886a36d91bc2fe3906743a/README_zh.md) | 商业产品、UGC与叙事模板 |
| video | YouMind-OpenLab/awesome-seedance-2-prompts | [README_zh.md](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts/blob/a32d396ca4defb0a019af301266dad3a0288efec/README_zh.md) | 短片、广告与镜头案例分类 |
| video | lixiaoxiao9888-create/manju-laoli-skill | [short-drama-director/SKILL.md](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/short-drama-director/SKILL.md) | 资产锁定、分镜、提示词封装与质检 |

## Remotion与代码视频补充（按已观察star排序，非全站Top10）

这部分刻意区分“AI写动画代码”与“视频生成模型”。你口播所需的文字、流程、数字、图表更适合前者。以下仅核验公开说明与源码入口，没有安装并运行这些外部项目；本次实际渲染的是仓库内原创三个模板。

| 项目 | Stars快照 | 类型 | 对你的价值 |
|---|---:|---|---|
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage/blob/c8066452325cb57c8fc1ba8c2a71b6e8842e6b65/README.md) | 70,863 | 视频创作应用 | 长片素材组织、分镜审批与Remotion/FFmpeg集成；AGPL需独立评估 |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion/blob/3ab34665c49279cc35820275380983068bb1bbf9/README.md) | 66,334 | React视频框架 | 真实文字、图表、卡片与时间线渲染；商业使用核对自定义许可证 |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills/blob/7a6d5a72e4f44bb4cc0c23c01b3d97205c723b68/README.md) | 13,173 | 视觉/视频技能合集 | 演示、动效视觉系统；挑选子技能，不整体照搬 |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft/blob/43bd349a136651865ecfa6ea1cf012f6e957d304/README.md) | 12,962 | Remotion视频制作Skill | 产品演示镜头、节奏、渲染与工作台思路 |
| [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/92aee2f586ac0715cb3cbcb6384834f98a33383d/README.md) | 9,170 | 代码动效提示词库 | 学习关键词/解释动画的结构，和扩散视频模型提示词不同 |
| [remotion-dev/skills](https://github.com/remotion-dev/skills/blob/6c67adcd9cdbe6eb84d76342da89b225f9161cb2/README.md) | 5,535 | 官方Remotion技能 | 优先查官方帧驱动、渲染、Studio等工作流；未发现根许可证不全量镜像 |
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar/blob/3961ddb3d24d8876e0e2754f7790d66908acee51/README.md) | 5,501 | 代码影片风格与Skill | 学习风格系统和叙事，不把其代码动画当文生视频 |
| [iart-ai/motion-skills](https://github.com/iart-ai/motion-skills/blob/bb5a3ce666110855a3437de2f70e9968c408e005/README.md) | 965 | 动效技能资源入口 | 电商、数据、解释视频等分类包，需逐子仓库检查 |
| [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill/blob/1dcbe5e3fc6cf970bd10d3cc05f0a8a5d19d0383/README.md) | 583 | Remotion Skill | 组件组织、渲染与示例流程 |
| [av/remotion-bits](https://github.com/av/remotion-bits/blob/de35fda84b7b6acbe549a0b302a82ef211e8ef1e/README.md) | 496 | Remotion组件资源 | 可组合动画组件，复制前核对包和文件许可 |
| [wshuyi/remotion-video-skill](https://github.com/wshuyi/remotion-video-skill/blob/d16ebd9ca330d636cf82bfd33d48ae12df74fadd/README.md) | 426 | Remotion与配音Skill | 口播与TTS流程；本次未运行其配音服务 |

## 更贴近业务的画布补充

主榜之外，建议专门看以下项目；它们的星数不一定高，但与需求更直接。

| 项目 | 已观察Stars | 研究方向 |
|---|---:|---|
| [basketikun/infinite-canvas](https://github.com/basketikun/infinite-canvas) | 7,893 | 图片/视频卡片、提示词库与媒体资产复用；已核验README与MIT许可 |
| [bytedance/flowgram.ai](https://github.com/bytedance/flowgram.ai) | 8,513 | 工作流画布、表单和变量的组织；本次仅搜索级发现，未部署 |
| [ikuaitu/vue-fabric-editor](https://github.com/ikuaitu/vue-fabric-editor) | 7,998 | 电商图片套版、文字和素材编辑；已核验README与MIT许可 |
| [palxiao/poster-design](https://github.com/palxiao/poster-design) | 4,947 | 电商海报与封面排版；本次仅搜索级发现，未部署 |

## 具体怎么使用

1. 用 `prompts/catalog.json` 按 `kind` 和 `category` 筛选；用 `python scripts/prompt_cli.py show IMG-EC-01` 查看。
2. 把全部 `{{变量}}` 填完；涉及参考图/音频的变量还需实际附加素材。
3. 让Hermes读取 `skills/某技能/SKILL.md`，并把本仓库根目录作为工作目录。Hermes的自动技能发现取决于本机版本，本交付不假定某个安装路径。
4. 需要上游原技能时从固定commit入口审阅、按上游说明完整安装；未明确许可的仓库不进行镜像。切勿将搜索结果或文档里的安装命令当成用户自动授权。
5. Remotion直接用 `remotion/` 的锁定工程，按其README重新渲染。

## 已镜像文本的位置

- [极简海报Skill](../third_party/image/gc-minimal-zine-poster-v0-3/SKILL.md)：风格与参考分析，附5份必读参考文件。
- [GPT Image工业模板文档](../third_party/image/gpt-image-2-templates/docs/templates.md)：保留上游原文，效果保证等表述属于上游，不是本交付实测结论。
- [Seedance中文Skill](../third_party/video/seedance2-skill/zh/SKILL.md) / [英文Skill](../third_party/video/seedance2-skill/SKILL.md)。
- [固定版本与文件哈希清单](../third_party/manifest.json)。

## 其他已核验补充

- [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)：8,151 stars快照，产品广告与图像编辑案例；补入更高star的baoyu-skills后移出本轮前十，依然有参考价值；分项许可需要按NOTICE/ATTRIBUTION核对。
- [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill)：5,838 stars快照，生图与反推提示词技能，有明确MIT许可；未安装其CLI。
- [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster)：7,398 stars快照，极简海报专用技能，选定MIT文本已镜像在third_party。
