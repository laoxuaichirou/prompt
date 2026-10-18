# 【9宫格分镜】人物一致性分镜提示词

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 5 |
| 模型 | Nano Banana、Qwen-Image |
| 场景 | 视频分镜、提示词工程 |
| Notion | [【9宫格分镜】人物一致性分镜提示词](https://app.notion.com/p/9-328079fdbc388027b401e49b825d6db1) |

**备注**：指令+翻译+9帧示例三层完整，人物一致性分镜标杆

---

## 正文

中文翻译：
```bash
### 翻译结果（完整保留指令逻辑与专业术语）
---

<instruction>
分析完整电影场景，识别**所有核心主体**（单人/群体/情侣/载具/特定物品）及其空间关系与互动。
生成一个连贯的 3x3 宫格「电影感联系表」，包含 9 个不同机位镜头，精准呈现同一环境下的这些主体。
必须根据内容适配标准电影镜头类型（例如：群体场景需保持群体完整；物品场景需完整框住主体）：

**第一行（建立场景语境）：**
1.  **极远景 (Extreme Long Shot, ELS)：** 主体在广阔环境中显得渺小。
2.  **远景 (Long Shot, LS)：** 完整呈现主体/群体（人物从头到脚 / 载具从车轮到车顶）。
3.  **中远景 (Medium Long Shot / 美式3-4景)：** 人物膝盖以上 / 物品3/4视角的构图。

**第二行（核心叙事覆盖）：**
4.  **中景 (Medium Shot, MS)：** 腰部以上（或物品核心主体）构图，聚焦互动与动作。
5.  **中近景 (Medium Close-Up, MCU)：** 胸部以上构图，近距离呈现核心主体。
6.  **近景 (Close-Up, CU)：** 紧凑框住面部/物品正面，突出细节。

**第三行（细节与视角）：**
7.  **特写景 (Extreme Close-Up, ECU)：** 微距聚焦关键特征（眼睛、手部、纹饰、材质纹理）。
8.  **低角度镜头 (Worm's Eye View)：** 从地面向上仰视主体（营造威严/英雄感）。
9.  **高角度镜头 (Bird's Eye View)：** 从上方俯视主体。

**严格一致性要求：** 9 个画面中人物/物品、服饰、光照完全一致。景深需真实变化（特写镜头使用散景虚化）。
</instruction>

---

### 专业 3x3 电影分镜宫格（含 9 个画格）
该宫格以完整焦段范围，呈现输入图像中的特定主体/场景。

**顶行：** 环境广角镜头、完整全身景、3/4 视角景
**中行：** 腰部以上景、胸部以上景、面部/物品正面近景
**底行：** 微距细节、低角度、高角度

所有画格均具备写实纹理、统一电影感调色，且针对分析出的主体/物品数量采用正确构图。

分析输入图像并识别核心主体，在所有画格中保持外观、比例、材质、色彩与风格的绝对一致。

阅读场景描述，生成从开端到收尾逻辑连贯的 9 个电影场景序列。每个画格对应场景描述中下一关键瞬间。
AI 自动选择所有机位与构图。
确保电影感打光、统一调色、真实景深、环境演变连贯，无重复镜头。

---

### 场景输入：
一名维京人时隔许久回到自己的村庄

---

### 逐帧分镜（英文+中文对照，严格遵循 3x3 镜头逻辑）
#### Frame 1 (Extreme Long Shot)
`Extreme Long Shot, lone viking standing in misty fjord, distant wooden longhouses, snow-capped mountains, overcast sky, cinematic lighting, photorealistic, no timecode, no subtitles`
**极远景：** 孤独立于雾气峡湾的维京人，远处可见木质长屋与雪山，阴沉天空，电影感打光，写实风格，无时间码、无字幕

#### Frame 2 (Long Shot)
`Long Shot, viking in full fur cloak and horned helmet, standing tall before village longhouses, fjord water at his feet, overcast lighting, photorealistic, no timecode, no subtitles`
**远景：** 身着完整毛皮斗篷与角盔的维京人，在村庄长屋前站直，脚下是峡湾水面，阴沉打光，写实风格，无时间码、无字幕

#### Frame 3 (Medium Long Shot)
`Medium Long Shot, viking from knees up, gripping iron axe at his side, looking toward village, fur cloak flowing, overcast lighting, photorealistic, no timecode, no subtitles`
**中远景：** 维京人膝盖以上构图，手侧握铁斧，望向村庄，毛皮斗篷飘动，阴沉打光，写实风格，无时间码、无字幕

#### Frame 4 (Medium Shot)
`Medium Shot, viking from waist up, adjusting his horned helmet, gaze fixed on distant villagers, fur cloak, weathered leather tunic, cinematic lighting, photorealistic, no timecode, no subtitles`
**中景：** 维京人腰部以上构图，调整角盔，目光望向远处村民，毛皮斗篷、做旧皮革内搭，电影感打光，写实风格，无时间码、无字幕

#### Frame 5 (Medium Close-Up)
`Medium Close-Up, viking from chest up, weathered face, bushy beard, determined eyes, fur cloak collar, overcast lighting, soft bokeh, photorealistic, no timecode, no subtitles`
**中近景：** 维京人胸部以上构图，饱经风霜的面容、浓密胡须、坚定眼神，毛皮斗篷领口，阴沉打光，柔和散景，写实风格，无时间码、无字幕

#### Frame 6 (Close-Up)
`Close-Up, viking’s face, deep wrinkles, scar across cheek, intense gaze, fur framing face, overcast lighting, tight focus, photorealistic, no timecode, no subtitles`
**近景：** 维京人面部特写，深刻皱纹、脸颊伤疤、锐利目光，毛皮围绕面部，阴沉打光，紧凑对焦，写实风格，无时间码、无字幕

#### Frame 7 (Extreme Close-Up)
`Extreme Close-Up, viking’s calloused hand gripping axe handle, iron rivets, rough leather wrap, weathered wood texture, cinematic lighting, macro detail, photorealistic, no timecode, no subtitles`
**特写景：** 维京人布满老茧的手紧握斧柄，铁铆钉、粗糙皮革包裹、做旧木质纹理，电影感打光，微距细节，写实风格，无时间码、无字幕

#### Frame 8 (Low Angle Shot)
`Low Angle Shot, viking standing tall, horned helmet silhouetted against overcast sky, fur cloak billowing, imposing stance, cinematic lighting, photorealistic, no timecode, no subtitles`
**低角度镜头：** 仰视维京人，角盔在阴沉天空下形成剪影，毛皮斗篷飘动，威严站姿，电影感打光，写实风格，无时间码、无字幕

#### Frame 9 (High Angle Shot)
`High Angle Shot, viking standing in center of village square, surrounded by wooden longhouses, fjord below, overcast lighting, wide depth of field, photorealistic, no timecode, no subtitles`
**高角度镜头：** 俯视维京人站在村庄广场中央，四周环绕木质长屋，下方是峡湾，阴沉打光，宽景深，写实风格，无时间码、无字幕
```
原版：
```bash
<instruction>
Analyze the entire movie scene. Identify ALL key subjects present (whether it's a single person,
a group/couple, a vehicle, or a specific object) and their spatial relationship/interaction.
Generate a cohesive 3x3 grid "Cinematic Contact Sheet" featuring 9 distinct camera shots of
exactly these subjects in the same environment.
You must adapt the standard cinematic shot types to fit the content (e.g., if a group, keep the
group together; if an object, frame the whole object):
**Row 1 (Establishing Context):**
1. **Extreme Long Shot (ELS):** The subject(s) are seen small within the vast environment.
2. **Long Shot (LS):** The complete subject(s) or group is visible from top to bottom (head to
toe / wheels to roof).
3. **Medium Long Shot (American/3-4):** Framed from knees up (for people) or a 3/4 view (for
objects).
**Row 2 (The Core Coverage):**
4. **Medium Shot (MS):** Framed from the waist up (or the central core of the object). Focus on
interaction/action.
5. **Medium Close-Up (MCU):** Framed from chest up. Intimate framing of the main subject(s).
6. **Close-Up (CU):** Tight framing on the face(s) or the "front" of the object.
**Row 3 (Details & Angles):**
7. **Extreme Close-Up (ECU):** Macro detail focusing intensely on a key feature (eyes, hands,
logo, texture).
8. **Low Angle Shot (Worm's Eye):** Looking up at the subject(s) from the ground
(imposing/heroic).
9. **High Angle Shot (Bird's Eye):** Looking down on the subject(s) from above.
Ensure strict consistency: The same people/objects, same clothes, and same lighting across all
9 panels. The depth of field should shift realistically (bokeh in close-ups).
</instruction>
A professional 3x3 cinematic storyboard grid containing 9 panels.
The grid showcases the specific subjects/scene from the input image in a comprehensive range
of focal lengths.
**Top Row:** Wide environmental shot, Full view, 3/4 cut.
**Middle Row:** Waist-up view, Chest-up view, Face/Front close-up.
**Bottom Row:** Macro detail, Low Angle, High Angle.
All frames feature photorealistic textures, consistent cinematic color grading, and correct
framing for the specific number of subjects or objects analyzed.

Analyze the input image and identify the main subject(s). Maintain perfect consistency in
appearance, proportions, materials, colors, and style across all frames.
Read the SCENE INPUT and generate a cinematic 9-scene sequence that progresses logically
from start to finish. Each frame should represent the next meaningful moment based on the
scene description.
The AI chooses all camera angles and framing automatically.
Ensure cinematic lighting, consistent color grading, realistic depth of field, and coherent
environmental evolution. No repeated shots.
SCENE INPUT:
a viking visits his village after a long time
Frame 1:
Frame 2:
Frame 3:
Frame 4:
Frame 5:
Frame 6:
Frame 7:
Frame 8:
Frame 9:
```
