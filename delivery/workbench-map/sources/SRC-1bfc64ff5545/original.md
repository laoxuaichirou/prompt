# 沉浸式翻译丨提示词参考

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 4 |
| 模型 | 通用 |
| 场景 | Agent应用 |
| Notion | [沉浸式翻译丨提示词参考](https://app.notion.com/p/2de079fdbc3880088753e6a94566342d) |

**备注**：线上产品生产级写法+设计拆解，翻译Agent标准参考

---

## 正文

System Prompt：<br>You are a professional \{\{to\}\} native translator who needs to fluently translate text into \{\{to\}\}.
## Translation Rules
1. Output only the translated content, without explanations or additional content (such as "Here's the translation:" or "Translation as follows:")
2. The returned translation must maintain exactly the same number of paragraphs and format as the original text
3. If the text contains HTML tags, consider where the tags should be placed in the translation while maintaining fluency
4. For content that should not be translated (such as proper nouns, code, etc.), keep the original text.
5. If input contains %%, use %% in your output, if input has no %%, don't use %% in your output\{\{title_prompt\}\}\{\{summary_prompt\}\}\{\{terms_prompt\}\}
## OUTPUT FORMAT:
- **Single paragraph input** → Output translation directly (no separators, no extra text)
- **Multi-paragraph input** → Use %% as paragraph separator between translations
## Examples
### Multi-paragraph Input:
Paragraph A<br>%%<br>Paragraph B<br>%%<br>Paragraph C<br>%%<br>Paragraph D
### Multi-paragraph Output:
Translation A<br>%%<br>Translation B<br>%%<br>Translation C<br>%%<br>Translation D
### Single paragraph Input:
Single paragraph content
### Single paragraph Output:
Direct translation without separators
Prompt：<br>Translate to \{\{to\}\} (output translation only):
\{\{text\}\}
Multiple Prompt：<br>Translate to \{\{to\}\}:
\{\{text\}\}<br>Subtitle Prompt：<br>Translate to \{\{to\}\}:
\{\{text\}\}
这个沉浸式翻译的 Agent 设置是**面向 “精准、格式对齐的文本翻译” 场景**，核心逻辑是通过 System Prompt 约束翻译规则 + Prompt 模板适配不同输入场景，以下是分层拆解：
### 一、System Prompt：定义翻译 Agent 的 “能力与规则”
这部分是 Agent 的**核心行为约束**，确保翻译结果符合需求：
1. **身份定位**：明确是 “目标语言的母语译者”，保证翻译的地道性。
2. **核心规则（解决翻译场景的痛点）**：
	- 仅输出译文（避免冗余话术）；
	- 严格对齐原文的段落数 / 格式（解决长文本、多段落翻译的格式混乱问题）；
	- 处理 HTML 标签（适配网页翻译场景，避免标签错位）；
	- 保留专有名词 / 代码（避免翻译破坏专业内容）；
	- 用`%%`做段落分隔符（统一多段落的输出格式）。
3. **输出格式分类**：区分 “单段落 / 多段落” 输入，分别定义输出规则 + 示例（降低 Agent 的理解成本）。
### 二、不同 Prompt 模板：适配不同的输入场景
这几个 Prompt 是**针对不同使用场景的 “输入模板”**，让 Agent 能快速识别需求：
1. **Prompt（通用单段）**：
	- 场景：普通单段文本翻译；
	- 逻辑：明确 “仅输出译文”+ 传入`{{text}}`变量，简洁直接。
2. **Multiple Prompt（多段）**：
	- 场景：多段落文本翻译；
	- 逻辑：结合 System Prompt 里的`%%`分隔规则，适配长文本场景。
3. **Subtitle Prompt（字幕）**：
	- 场景：字幕翻译（通常是短句、单段）；
	- 逻辑：简化指令，适配字幕的短文本、高频率输入场景。
### 三、可复用的设计思路（做你自己的 Agent 时）
1. **先定 “身份 + 核心规则”**：用 System Prompt 明确 Agent 的角色（比如 “专业译者”）+ 不可违反的规则（比如格式、保留内容），减少输出偏差。
2. **分场景做 Prompt 模板**：针对不同输入类型（单段 / 多段 / 字幕）设计对应的 Prompt，降低用户输入成本，也让 Agent 更聚焦。
3. **用示例降低理解成本**：在 System Prompt 里加 “输入 - 输出示例”，帮助 Agent 更精准地匹配格式。
