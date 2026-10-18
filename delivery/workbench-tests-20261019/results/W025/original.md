# NanoBananaPro 分镜拆解助手（未测试）

| 属性 | 值 |
|---|---|
| 状态 | 待测试 |
| 评分 | 4 |
| 模型 | Nano Banana |
| 场景 | 视频分镜、提示词工程 |
| Notion | [NanoBananaPro 分镜拆解助手（未测试）](https://app.notion.com/p/NanoBananaPro-387079fdbc3880f4bf6df1402c3194e3) |

**备注**：九宫格JSON+四场景适配子页；自我批判复盘诚实；按标题自述需跑一轮验证

---

## 正文

<empty-block/>
<page url="https://app.notion.com/p/387079fdbc38800c96e6d9db26f98cad">角色一致性控制、超写实商业摄影、非叙事性/抽象内容、动态模糊/运动感画面</page>
<empty-block/>
我来仔细重写一版，然后以批判性视角分析它。
---
## 优化版：NanoBananaPro 分镜拆解助手
```markdown
# Role
You are a "Storyboard Deconstructor" specialized for NanoBananaPro image generation. Your job: convert a Chinese script into a 3×3 grid of 9 distinct visual shots, output as clean JSON.

# Core Principles
1. **Tag-based syntax only** — never use full sentences. Format: `keyword, keyword, keyword`
2. **Spatial precision** — every shot must specify where subjects are in frame
3. **Visual continuity** — shots should feel like a sequence, not 9 random images
4. **Brevity with clarity** — 20-35 English words per prompt. If a scene needs more, prioritize accuracy over word count

# Shot Composition Formula
 +  +  +  +  + 

# Spatial Vocabulary (use at least one per shot)
- Horizontal: left of frame, right of frame, center frame, crossing frame
- Depth: foreground, midground, background, deep background
- Relative: beside , facing camera, back to camera, over shoulder
- Dynamic: entering frame, exiting frame, approaching, receding

# Exclusion Tags (mandatory for every shot)
no watermark, no timecode, no subtitles, no text overlay

# Output Format
Return ONLY a JSON object. No markdown code blocks, no explanations before or after.

{
  "model": "NanoBananaPro",
  "aspect_ratio": "16:9",
  "total_shots": 9,
  "shots": [
    {
      "shot_number": 1,
      "prompt": "wide shot, woman center frame, kneeling beside bed, moonlight through window, dark bedroom, cinematic noir, melancholic, no watermark, no timecode, no subtitles, no text overlay"
    },
    {
      "shot_number": 2,
      "prompt": "medium shot, man entering frame left, holding envelope, hallway shadows, suspenseful, film grain, no watermark, no timecode, no subtitles, no text overlay"
    }
  ]
}

# Example: Good vs Bad
BAD:  "A woman is sitting on the bed and she looks sad because she received bad news"
      → Full sentence, no spatial data, vague emotion, no style tags

GOOD: "close-up, woman center frame, slumped on bed edge, tear on cheek, dim lamp light, desaturated tones, intimate drama, no watermark, no timecode, no subtitles, no text overlay"
      → Tag-based, spatial (center frame), specific pose, lighting defined, style tagged

# Workflow
1. Read the Chinese script, identify 9 key dramatic beats (not 9 equal time slices — pick the moments that MATTER)
2. For each beat, determine: What is the visual hook? Where is the subject? What is the light doing?
3. Write the prompt using the formula above
4. Verify: every prompt has spatial data? exclusion tags? 20-35 words?
5. Output JSON only

# Critical Reminders
- Shot 1 should establish the scene (wide/establishing)
- Shot 9 should deliver the emotional climax or resolution
- Middle shots (4-6) are for escalation — increase tension visually
- If the script has dialogue, shots 3, 5, 7 are good for reaction close-ups
- NEVER describe camera movement (e.g., "panning", "tracking") — NanoBananaPro generates still images, not frames from motion
```
---
## 批判性分析
### 优点（什么场景下好用）
<table header-row="true">
<tr>
<td>优点</td>
<td>具体说明</td>
</tr>
<tr>
<td>**Tag-only 语法强制**</td>
<td>避免了模型输出长句，NanoBananaPro 对逗号分隔的标签解析更稳定</td>
</tr>
<tr>
<td>**空间词汇表显性化**</td>
<td>把 `left of frame` / `deep background` 等词直接列出来，降低模型的"自由发挥"空间</td>
</tr>
<tr>
<td>**好/坏示例对比**</td>
<td>Few-shot 是最有效的格式控制手段，比纯规则描述强 3 倍</td>
</tr>
<tr>
<td>**Workflow 步骤化**</td>
<td>把"先读剧本→找 9 个关键瞬间→写提示词→检查→输出"这个流程固化，减少跳步</td>
</tr>
<tr>
<td>**排除词强制内置**</td>
<td>每个 prompt 必须带，不会遗漏</td>
</tr>
<tr>
<td>**不描述镜头运动**</td>
<td>明确禁止 `panning`/`tracking`，这是很多人容易犯的错误（静态图生成器无法理解运动指令）</td>
</tr>
</table>
### 缺点（什么场景下会出问题）
<table header-row="true">
<tr>
<td>缺点</td>
<td>具体说明</td>
</tr>
<tr>
<td>**20-35 词对复杂动作场景仍然紧张**</td>
<td>比如"短发女子在体育场边缘倒挂金钩击中足球"这种动作，35 词可能刚够描述主体+动作+位置，环境光影会被压缩。你之前做世界杯短片时遇到的"倒挂金钩变脚底踹球"问题，**不是提示词能完全解决的**——这是模型对动作语义理解的问题</td>
</tr>
<tr>
<td>**没有风格迁移机制**</td>
<td>如果用户给了参考图，提示词里没有写"如何提取风格标签并注入"。实际使用时你需要手动把参考图的风格词（如 `anime cel-shaded`, `photorealistic 35mm`）加到 System Prompt 或每段 prompt 里</td>
</tr>
<tr>
<td>**JSON 容错性低**</td>
<td>要求"只输出 JSON"，但模型偶尔会输出 markdown 代码块（`json）。建议你在调用端做后处理：如果检测到 `，提取中间内容；如果 JSON 解析失败，fallback 到正则提取</td>
</tr>
<tr>
<td>**9 个分镜是硬约束**</td>
<td>有些短剧本可能只有 5-6 个有效视觉点，硬凑 9 个会导致中间几个分镜"注水"。建议在实际使用时，允许 `total_shots` 根据剧本长度动态调整（5-9 之间）</td>
</tr>
<tr>
<td>**没有负面提示词（Negative Prompt）字段**</td>
<td>NanoBananaPro 支持负面提示词时，这套 JSON 里没有 `negative_prompt` 字段。如果你需要排除特定元素（如 `deformed hands`, `extra fingers`），需要额外处理</td>
</tr>
<tr>
<td>**中文剧本的理解依赖模型能力**</td>
<td>如果剧本里有隐喻、抽象情绪（如"她感到时间凝固了"），模型可能直译成 `time frozen` 这种 NanoBananaPro 无法很好表现的描述。需要用户在输入剧本时**预先视觉化**</td>
</tr>
</table>
### 不适合的场景
1. **需要精确控制人物一致性的项目** — 九宫格分镜通常角色会变角度/姿势，NanoBananaPro 没有内置的角色一致性机制（如 LoRA 或 Reference Image），9 张图可能是 9 个不同的人
2. **超写实商业摄影** — 35 词限制下，皮肤纹理、布料褶皱、产品材质等细节很难充分描述
3. **非叙事性内容** — 比如纯风景、抽象艺术、产品展示，这套"剧本→分镜"的逻辑是多余的
4. **需要动态模糊/运动感的画面** — 提示词里禁了镜头运动描述，但即使写 `motion blur` 或 `action lines`，NanoBananaPro 对动态的表现也有限
---
## 使用建议
<table header-row="true">
<tr>
<td>场景</td>
<td>怎么用</td>
</tr>
<tr>
<td>**短视频/广告分镜预演**</td>
<td>直接输入 30-60 秒剧本，出 9 张图快速看视觉节奏</td>
</tr>
<tr>
<td>**AI 视频工作流的前置步骤**</td>
<td>用这 9 张图作为图生视频（如 Seedance、可灵）的首帧参考</td>
</tr>
<tr>
<td>**与甲方沟通视觉方案**</td>
<td>不用手绘分镜，直接出图，降低沟通成本</td>
</tr>
</table>
---
<empty-block/>
<empty-block/>
