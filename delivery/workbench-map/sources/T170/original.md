# AI漫剧提示词

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 4 |
| 模型 | Seedance |
| 场景 | 视频分镜 |
| Notion | [AI漫剧提示词](https://app.notion.com/p/AI-303079fdbc38801a9397cca4826f2f9e) |

**备注**：漫剧流水线落地度最高；飞书图床图片需转存Notion

---

## 正文

```bash
（直接复制此模板，补充【】内的自定义信息后发送，即可一次性生成剧本、人设提示词、场景风格、分镜提示词、转视频提示词，且分镜严格拆分为 4 个 15 秒适配即梦）
请基于 Seedance 2.0 的创作特性，为我制作一个1 分钟的创意短片，短片需拆分为4 个独立的 15 秒片段（适配即梦单次 15 秒生成限制），并一次性自动化生成以下全部内容，所有生成内容需高度适配 AI 生图、AI 视频生成 即梦 Seedance 2.0 的底层逻辑，提示词需标注核心关键词、风格（风格使用CG超写实3D渲染风格）、画面，要越详细越好，分镜需明确人物 / 场景 / 镜头动作，转视频提示词需匹配 Seedance 2.0 的运动、特效、节奏要求：
一、核心创作定位【补充后删除此括号】
短片主题：【例如：Seedance 2.0 功能展示、赛博都市的舞蹈瞬间、治愈系自然光影律动等】
核心风格：【例如：赛博朋克 / 日系动漫 / 写实光影 / 国风写意 / 极简扁平，需明确主风格】
情感基调：【例如：科技炫酷 / 温暖治愈 / 燃向动感 / 清新文艺】
核心亮点：【例如：突出 Seedance 2.0 的肢体动捕精度、镜头运镜效果、特效融合能力等，无则填 “无”】
二、需生成的全素材清单（按此结构输出，不可缺失）
1. 完整故事剧本
按4 个 15 秒片段拆分，标注每个片段的「时间节点、剧情内容、人物动作、镜头核心表达」，总时长严格控制 60 秒，剧情有连贯性，单个 15 秒片段有独立小高潮 / 画面闭环。
2. 全角色 AI 生图提示词
基于剧本提取所有出场角色，每个角色单独生成通用生图提示词（适配 Midjourney/Stable Diffusion / 即梦），格式为：「角色名称：核心特征 + 五官 / 身材 / 服饰 / 风格 + 画面参数（分辨率 / 画幅 / 光影）+ 负面提示词」，提示词字数控制在 50-80 字，核心关键词前置。
3. 统一场景设定 + 风格细则
明确短片的核心场景背景（如：未来都市霓虹街道 / 森系林间溪流 / 简约纯色演播厅），并细化风格落地规则（如：色彩搭配、光影类型、笔触 / 渲染精度、画面比例、是否加特效元素，需适配 Seedance 2.0 的视觉呈现）。
4. 分镜图 AI 生图提示词（4 个 15 秒，标注人物 + 镜头）
按15 秒 / 个生成 4 组分镜图提示词，每组对应剧本的 1 个 15 秒片段，每组包含「3-4 个关键分镜」（适配 15 秒视频的镜头节奏），每个分镜提示词需明确标注「出场人物、镜头类型（推 / 拉 / 摇 / 移 / 近景 / 特写 / 全景）、画面内容、核心风格」，格式为：「片段 X（00:XX-00:XX）- 分镜 X：人物 + 镜头动作 + 画面细节 + 风格 / 参数 + 负面提示词」，提示词适配 AI 生图，可直接复用。
5. 分镜图转视频 AI 提示词（适配 Seedance 2.0 / 即梦，4 个 15 秒）
按15 秒 / 个生成 4 组转视频专属提示词，严格匹配 Seedance 2.0 的功能特性，每组提示词对应 1 个片段的分镜内容，明确标注「人物运动节奏、镜头运镜方式、画面特效、帧率 / 分辨率、背景音乐风格、Seedance 2.0 专属参数（如动捕精度、肢体流畅度、背景融合度）」，格式为：「片段 X（00:XX-00:XX）转视频提示词：核心画面 + 运动节奏 + 镜头效果 + 特效 / 音效 + 技术参数 + 负面提示（如画面卡顿 / 肢体变形 / 穿模）」，可直接复制到 Seedance 2.0 / 即梦生成。
三、强制创作要求
所有内容高度适配 AI 工具，提示词无模糊表述，核心关键词突出，可直接复制使用；
分镜拆分严格遵循「4 个 15 秒」，单个片段时长不超过 15 秒，总时长精准 60 秒；
角色、场景在全剧本 / 分镜 / 提示词中保持统一，无前后矛盾；
Seedance 2.0 转视频提示词需兼顾「画面流畅度、动作自然度、场景融合度」，适配即梦的生成规则；
所有输出内容按「剧本→角色提示词→场景风格→分镜图提示词→转视频提示词」的顺序结构化呈现，层级清晰，便于复制和落地创作。
示例（补充后参考）
请基于 Seedance 2.0 的创作特性，为我制作一个1 分钟的创意短片，短片需拆分为4 个独立的 15 秒片段（适配即梦单次 15 秒生成限制），并一次性自动化生成以下全部内容，所有生成内容需高度适配 AI 生图、AI 视频生成（Seedance 2.0 / 即梦）的底层逻辑，提示词需标注核心关键词、风格权重、画面参数，分镜需明确人物 / 场景 / 镜头动作，转视频提示词需匹配 Seedance 2.0 的运动、特效、节奏要求：
一、核心创作定位
短片主题：Seedance 2.0 功能展示短片 ——AI 数字人光影舞蹈秀
核心风格：赛博朋克 + 未来科技风，写实 3D 渲染
情感基调：科技炫酷、动感燃向
核心亮点：突出 Seedance 2.0 的高精准肢体动捕、镜头跟随运镜、光影特效融合能力
二、需生成的全素材清单（按此结构输出，不可缺失）
1. 完整故事剧本
...（后续由豆包按要求生成）
2. 全角色 AI 生图提示词
...（后续由豆包按要求生成）
3. 统一场景设定 + 风格细则
...（后续由豆包按要求生成）
4. 分镜图 AI 生图提示词（4 个 15 秒，标注人物 + 镜头）
...（后续由豆包按要求生成）
5. 分镜图转视频 AI 提示词（适配 Seedance 2.0 / 即梦，4 个 15 秒）
...（后续由豆包按要求生成）
三、强制创作要求
所有内容高度适配 AI 工具，提示词无模糊表述，核心关键词突出，可直接复制使用；
分镜拆分严格遵循「4 个 15 秒」，单个片段时长不超过 15 秒，总时长精准 60 秒；
角色、场景在全剧本 / 分镜 / 提示词中保持统一，无前后矛盾；
Seedance 2.0 转视频提示词需兼顾「画面流畅度、动作自然度、场景融合度」，适配即梦的生成规则；
所有输出内容按「剧本→角色提示词→场景风格→分镜图提示词→转视频提示词」的顺序结构化呈现，层级清晰，便于复制和落地创作。
```
**【生成举例】全角色提示词（生成满意后再做3视图）：**
```bash
华山剑仙（男）
核心特征：俊朗清冷，仙侠气，江湖侠客；五官立体剑眉星目，身形挺拔修长，身着月白剑仙长袍配流云纹，手持玄铁长剑，剑穗垂落；CG 超写实 3D 渲染，8K，16:9，侧光逆光结合，光影层次丰富；

青城刀客（男）
核心特征：粗犷豪迈，江湖悍勇，刀客气魄；五官硬朗络腮胡，身形魁梧壮硕，身着玄黑劲装配皮质护具，手持镔铁大环刀，刀身带寒光；CG 超写实 3D 渲染，8K，16:9，顶光侧光结合，金属质感拉满；

丐帮棍王（男）
核心特征：沧桑干练，江湖草根，棍术高手；五官棱角分明面容黝黑，身形精壮结实，身着灰色丐帮布衣配补丁，手持檀木三节棍，棍身刻纹路；CG 超写实 3D 渲染，8K，16:9，自然光漫射，材质纹理清晰；

峨眉掌姬（女）
核心特征：清冷绝美，英气飒爽，峨眉弟子；五官精致丹凤眼，身形窈窕轻盈，身着淡粉峨眉道袍配白纱，赤手空拳，手腕戴银饰；CG 超写实 3D 渲染，8K，16:9，柔光逆光结合，仙气光影效果；
```
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=NzEyNjMxMTJiOWJlNDcyODFhY2IxZWIzNWFmMWVlOWJfSXpxZDBOS0h4RlJtbDJaaWJtd0tOSWhWcFV6NHgycFVfVG9rZW46UnBhU2JiSlZRb2xkSjN4MTdzWGMzRFh3bnY4XzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
<columns>
	<column ratio="50">
		![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=NjJmMGI3YmYzYjU1ODUxNTY0NjRmZTQ2ZWEzNTVkM2VfYW9lWjcwWTIwOGxuWGtQTUVEd1YzU0hibDAycGhqM2tfVG9rZW46SUxiMWJkWGFRb0lESDh4OFhpd2MwYk5lbklkXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
	</column>
	<column ratio="50">
		![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=NDUyYTMwMjNjYzNlZjlkOTFjZmJkY2FmMjMyZjkwNTJfQUFpTlByNDNQOFVXYVRQMEdhV3RsdUlTcjNUTGh3WXhfVG9rZW46V0RqRGJPd2pLb1B0Qkd4M092cGNpeEZyblplXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
	</column>
</columns>
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmI4OTg4ZGQ4ZWI3OWVkMjZlNjNmMTY5NTY3YTA2NDhfZUZpaXRhYm9odk10aXZGSVZSUEsyQ3Y5TzlYanNHRThfVG9rZW46SHhCMmJuR1psb1lBaXJ4UTlPR2NHRE5Jbm1iXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=OTBhM2NkYzMyNDE3MGUyMDI1YTQzOGM2MTMyMjZmNmFfZEdaS3B1YndaY1hLeFpDZVExMWdEaG03QnU3eXRlVW1fVG9rZW46QXVPMmI5NEJlb3VUbm54VWpVM2MyN1RWblplXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDYxNGM2MDBkMGVhZDMyM2ZhODQ2NDExOTgxZDI2NzJfUE1GVWFNV2IxdEpMZE1WNXNCMnNDc0lsZnhLZzllT2hfVG9rZW46VjBoQmJEcG1Nb0t6R254MjhEMmM5T1hTbnBiXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=MWQ1ZGQ5OTY0YTE5Y2Q3YmQ2MGYzOWFkODZmYWQwMjlfUno0dkE0ZjBUWG9WWXI3cjRaMjVaYlVKN3lpdzF3NnRfVG9rZW46RmpWU2JWRVhLb3hLQkJ4dDhuVWN4cWREbnJlXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=YjFhNjUyM2ZkOWIzZGNiZDMwZmY5OGE1ZjEyODNjOTlfVE5uWW5RS1pjd3JJY0NNT1JCeXo3MjdiM1RRY2VoYWlfVG9rZW46VTNCY2JVWkhNb3pCd014VmlFNmNuS1U2bkRkXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
## 场景
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=Yjk1NWFiNmE4MjhmNjhiZDcyYjJkYjQ1MDc4Y2ZmMzlfUjhHYXVIUWd1cHZYYUlLbmFHM0NJWXBJem8xNUZzdzFfVG9rZW46UTlRamJ6Q0Zlb2Nhcjd4Q1NRZ2NCWDF5bmhlXzE3NzA3NDM2ODU6MTc3MDc0NzI4NV9WNA)
丐帮棍王（男）<br>核心特征：沧桑干练，江湖草根，棍术高手；五官棱角分明面容黝黑，身形精壮结实，身着灰色丐帮布衣配补丁，手持檀木三节棍，棍身刻纹路；CG 超写实 3D 渲染，8K，16:9，自然光漫射，材质纹理清晰；<br>
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=MTdlZWU5ZDk0OWQ5MzQzNjdlMGY0Nzk0ODcyODUxOWVfTU44dWZZNDVhSE1ZV2FUQ0ZpMlQ1Q1A5bUFzOVNENTFfVG9rZW46UnBhU2JiSlZRb2xkSjN4MTdzWGMzRFh3bnY4XzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=MzU2Y2U4ZDgyNWUxM2I4OWUyZGZlZGZlMTZjYTkwMTdfNjNGUEFpRk5ZQ1MxaTREVHRwOTlESTdGRXlZTDUxV2JfVG9rZW46SUxiMWJkWGFRb0lESDh4OFhpd2MwYk5lbklkXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
青城刀客（男）<br>核心特征：粗犷豪迈，江湖悍勇，刀客气魄；五官硬朗络腮胡，身形魁梧壮硕，身着玄黑劲装配皮质护具，手持镔铁大环刀，刀身带寒光；CG 超写实 3D 渲染，8K，16:9，顶光侧光结合，金属质感拉满；
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTc4Y2E3NTBiOTA2MmUxMDcwYmIxOGQyMDdlZjc1NjBfQWVJbVFuaXBRWm9FRFVjalBsMEJsT3NJOURtcFd6VGxfVG9rZW46V0RqRGJPd2pLb1B0Qkd4M092cGNpeEZyblplXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWRjZTc3ZDZkYmUwOGVjMzU0OTJkOWIwNmRlZjk4YTFfTVdDNTJUdEdEWEl4YnlUdzh4cGxENXdlMGtOTnZ1WEZfVG9rZW46SHhCMmJuR1psb1lBaXJ4UTlPR2NHRE5Jbm1iXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
华山剑仙（男）<br>核心特征：俊朗清冷，仙侠气，江湖侠客；五官立体剑眉星目，身形挺拔修长，身着月白剑仙长袍配流云纹，手持玄铁长剑，剑穗垂落；CG 超写实 3D 渲染，8K，16:9，侧光逆光结合，光影层次丰富；
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=NDIxN2E4ZjBkMDYyNDA5MDQwOTdhMjdkMTQxNGRjNGFfb0xIUGJCbjJEaVdpcnNGUXBqS3h2RTV2cThCeHJtdTFfVG9rZW46QXVPMmI5NEJlb3VUbm54VWpVM2MyN1RWblplXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=MWIyOTA2NDc5MDMwNGU2MGVjM2ExYTJjODdlODYxZTdfdUxQemtsSDZnNVZycEQxbW8wUFNuaWhVaXB1Qjg0Y1ZfVG9rZW46RmpWU2JWRVhLb3hLQkJ4dDhuVWN4cWREbnJlXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
峨眉掌姬（女）<br>核心特征：清冷绝美，英气飒爽，峨眉弟子；五官精致丹凤眼，身形窈窕轻盈，身着淡粉峨眉道袍配白纱，赤手空拳，手腕戴银饰；CG 超写实 3D 渲染，8K，16:9，柔光逆光结合，仙气光影效果；
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=MWM1NDc1ZmRiZDNjMWNiZTRmZTQzNTI3YjI2ODY5MDFfVUtDZmcwdlNabTJ2M2h5VGxIbEdxVlhVUFNSam8zY1VfVG9rZW46VjBoQmJEcG1Nb0t6R254MjhEMmM5T1hTbnBiXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
![](https://airaysheng.feishu.cn/space/api/box/stream/download/asynccode/?code=NDhkZDY2MzUxNWI3MDQ1YjRkN2ZlYzFhYzNkMTdhOTBfOVdlS0lzZ3VQZDdsZ2thdEdGb3BOanFBTU95MkR1NWVfVG9rZW46VTNCY2JVWkhNb3pCd014VmlFNmNuS1U2bkRkXzE3NzA3NDM3MTY6MTc3MDc0NzMxNl9WNA)
<br><br>
