# 【九宫格】1图转电影分镜图提示词

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 5 |
| 模型 | Nano Banana |
| 场景 | 视频分镜 |
| Notion | [【九宫格】1图转电影分镜图提示词](https://app.notion.com/p/1-300079fdbc3880f8b0aaf4043a585346) |

**备注**：工程化程度最高：XML结构+硬约束+关键帧格式

---

## 正文

### 1、电影分镜图九宫格
```plain text
<role>
You are an award-winning trailer director + cinematographer + storyboard artist. Your job: turn ONE reference image into a cohesive cinematic short sequence, then output AI-video-ready keyframes.
</role>

<input>
User provides: one reference image (image).
</input>

<non-negotiable rules - continuity & truthfulness>
First, analyze the full composition: identify ALL key subjects (person/group/vehicle/object/animal/props/environment elements) and describe spatial relationships and interactions (left/right/foreground/background, facing direction, what each is doing).
Do NOT guess real identities, exact real-world locations, or brand ownership. Stick to visible facts. Mood/atmosphere inference is allowed, but never present it as real-world truth.
Strict continuity across ALL shots: same subjects, same wardrobe/appearance, same environment, same time-of-day and lighting style. Only action, expression, blocking, framing, angle, and camera movement may change.
Depth of field must be realistic: deeper in wides, shallower in close-ups with natural bokeh. Keep ONE consistent cinematic color grade across the entire sequence.
Do NOT introduce new characters/objects not present in the reference image. If you need tension/conflict, imply it off-screen (shadow, sound, reflection, occlusion, gaze).
</non-negotiable rules - continuity & truthfulness>

<goal>
Expand the image into a 10–20 second cinematic clip with a clear theme and emotional progression (setup → build → turn → payoff).
The user will generate video clips from your keyframes and stitch them into a final sequence.
</goal>

<step 1 - scene breakdown>
Output (with clear subheadings):
Subjects: list each key subject (A/B/C…), describe visible traits (wardrobe/material/form), relative positions, facing direction, action/state, and any interaction.
Environment & Lighting: interior/exterior, spatial layout, background elements, ground/walls/materials, light direction & quality (hard/soft; key/fill/rim), implied time-of-day, 3–8 vibe keywords.
Visual Anchors: list 3–6 visual traits that must stay constant across all shots (palette, signature prop, key light source, weather/fog/rain, grain/texture, background markers).
</step 1 - scene breakdown>

<step 2 - theme & story>
From the image, propose:
Theme: one sentence.
Logline: one restrained trailer-style sentence grounded in what the image can support.
Emotional Arc: 4 beats (setup/build/turn/payoff), one line each.
</step 2 - theme & story>

<step 3 - cinematic approach>
Choose and explain your filmmaking approach (must include):
Shot progression strategy: how you move from wide to close (or reverse) to serve the beats
Camera movement plan: push/pull/pan/dolly/track/orbit/handheld micro-shake/gimbal—and WHY
Lens & exposure suggestions: focal length range (18/24/35/50/85mm etc.), DoF tendency (shallow/medium/deep), shutter “feel” (cinematic vs documentary)
Light & color: contrast, key tones, material rendering priorities, optional grain (must match the reference style)
</step 3 - cinematic approach>

<step 4 - keyframes for AI video (primary deliverable)>
Output a Keyframe List: default 9–12 frames (later assembled into ONE master grid). These frames must stitch into a coherent 10–20s sequence with a clear 4-beat arc.
Each frame must be a plausible continuation within the SAME environment.

Use this exact format per frame:

[KF# | suggested duration (sec) | shot type (ELS/LS/MLS/MS/MCU/CU/ECU/Low/Worm’s-eye/High/Bird’s-eye/Insert)]
Composition: subject placement, foreground/mid/background, leading lines, gaze direction
Action/beat: what visibly happens (simple, executable)
Camera: height, angle, movement (e.g., slow 5% push-in / 1m lateral move / subtle handheld)
Lens/DoF: focal length (mm), DoF (shallow/medium/deep), focus target
Lighting & grade: keep consistent; call out highlight/shadow emphasis
Sound/atmos (optional): one line (wind, city hum, footsteps, metal creak) to support editing rhythm
Hard requirements:
Must include: 1 environment-establishing wide, 1 intimate close-up, 1 extreme detail ECU, and 1 power-angle shot (low or high).
Ensure edit-motivated continuity between shots (eyeline match, action continuation, consistent screen direction / axis).
</step 4 - keyframes for AI video>

<step 5 - contact sheet output (MUST OUTPUT ONE BIG GRID IMAGE)>
You MUST additionally output ONE single master image: a Cinematic Contact Sheet / Storyboard Grid containing ALL keyframes in one large image.
Default grid: 3x3. If more than 9 keyframes, use 4x3 or 5x3 so every keyframe fits into ONE image.
Requirements:
The single master image must include every keyframe as a separate panel (one shot per cell) for easy selection.
Each panel must be clearly labeled: KF number + shot type + suggested duration (labels placed in safe margins, never covering the subject).
Strict continuity across ALL panels: same subjects, same wardrobe/appearance, same environment, same lighting & same cinematic color grade; only action/expression/blocking/framing/movement changes.
DoF shifts realistically: shallow in close-ups, deeper in wides; photoreal textures and consistent grading.
After the master grid image, output the full text breakdown for each KF in order so the user can regenerate any single frame at higher quality.
</step 5 - contact sheet output>

<final output format>
Output in this order:
A) Scene Breakdown
B) Theme & Story
C) Cinematic Approach
D) Keyframes (KF# list)
E) ONE Master Contact Sheet Image (All KFs in one grid)
</final output format>
```
### 2、电影镜头不同角度的九宫格
```plain text
<instruction>
Analyze the entire composition of the input image. Identify ALL key subjects present (whether it's a single person, a group/couple, a vehicle, or a specific object) and their
spatial relationship/interaction.
Generate a cohesive 3x3 grid "Cinematic Contact Sheet" featuring 9 distinct camera shots of exactly these subjects in the same environment.
You must adapt the standard cinematic shot types to fit the content (e.g., if a group, keep the group together; if an object, frame the whole object):

Row 1 (Establishing Context):
Extreme Long Shot (ELS): The subject(s) are seen small within the vast environment.
Long Shot (LS): The complete subject(s) or group is visible from top to bottom (head to toe / wheels to roof).
Medium Long Shot (American/3-4): Framed from knees up (for people) or a 3/4 view (for objects).

Row 2 (The Core Coverage):
Medium Shot (MS): Framed from the waist up (or the central core of the object). Focus on interaction/action.
Medium Close-Up (MCU): Framed from chest up. Intimate framing of the main subject(s).
Close-Up (CU): Tight framing on the face(s) or the "front" of the object.

Row 3 (Details & Angles):
Extreme Close-Up (ECU): Macro detail focusing intensely on a key feature (eyes, hands, logo, texture).
Low Angle Shot (Worm's Eye): Looking up at the subject(s) from the ground (imposing/heroic).
High Angle Shot (Bird's Eye): Looking down on the subject(s) from above.

Ensure strict consistency: The same people/objects, same clothes, and same lighting across all 9 panels. The depth of field should shift realistically (bokeh in close-ups).
</instruction>


A professional 3x3 cinematic storyboard grid containing 9 panels.
The grid showcases the specific subject(s)/scene from the input image in a comprehensive range of focal lengths.
Top Row: Wide environmental shot, Full-body view, 3/4 cut.
Middle Row: Waist-up view, Chest-up view, Face/Front close-up.
Bottom Row: Macro detail, Low Angle, High Angle.
All frames feature photorealistic textures, consistent cinematic color grading, and correct framing for the specific number of subjects or objects analyzed.
```
<empty-block/>
