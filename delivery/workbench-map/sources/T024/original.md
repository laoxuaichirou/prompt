# 换装提示词示例

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 4 |
| 模型 | Nano Banana、Kontext |
| 场景 | 图像编辑、电商产品 |
| Notion | [换装提示词示例](https://app.notion.com/p/32a079fdbc3880db9adec0291db06a58) |

**备注**：多版本实测对比且测试状态标注清楚，取标注'可用'的版本投产

---

## 正文

<page url="https://app.notion.com/p/32a079fdbc3880d2b05ad1c3084ba4b0">2</page>
<page url="https://app.notion.com/p/32a079fdbc388023b75dc905cf997558">1</page>
移除人物，仅保留服装，<br>去除人体体积影响（胸部、腰部、臀部的立体隆起），<br>将服装还原为自然平铺状态（2D形态），<br>布料自然展开，无人体支撑结构，<br>保持真实服装剪裁与比例，<br>背景纯白，电商商品图风格，<br>真实摄影质感，高细节，无变形
<empty-block/>
换头：
使四肢与面部的肤色保持一致，保持角色的整体连贯性。<br>用图 2 中的头部和发型替换图 1 中的头部，保留图 1 的服饰，并按照图 3 的姿势来摆放角色。
<empty-block/>
## 服装提取：
（可能会提取 诸如：草帽 等配饰，需要抽卡）
Extract only the clothing from image 1, place it on a pure white background, and preserve the exact style, silhouette, length, and all design details of the entire garment exactly as they appear in the original reference image. Do not alter or modify any part of the clothing's style, type, structure, or appearance.
翻译：
仅从图片1中提取服装，不包括帽子、包等配饰或其他附加元素，将其放置在纯白色背景上，并精确保留整件服装的风格、轮廓、长度以及所有设计细节，完全与原始参考图片中的呈现一致。不得更改或修改服装风格、类型、结构或外观的任何部分。
<empty-block/>
Extract only the main clothing garment (excluding any accessories like hats, bags, or additional elements) from image 1, place it on a pure white background, and preserve the exact style, silhouette, length, and all design details of the garment exactly as it appears in the original reference image. Do not alter, modify, split, or restructure any part of the garment's style, type, or appearance, and do not add any mannequin, model, or extra body parts.
翻译：
从图片1中仅提取主要服装（不包括帽子、包等配饰或其他附加元素），将其放置在纯白色背景上，并精确保留该服装在原始参考图片中呈现的准确风格、轮廓、长度以及所有设计细节。不得更改、修改、拆分或重组服装风格、类型或外观的任何部分，也不得添加任何人体模型、模特或额外的身体部位。
<empty-block/>
Chatgpt 优化后：
Extract the primary clothing item from image 1, removing all accessories such as hats, bags, jewelry, or additional elements. Place the garment on a pure white background. Preserve the exact style, silhouette, length, proportions, and all design details exactly as shown in the original image. Do not alter, redesign, or modify any part of the garment. Ensure no mannequin, human body parts, or extra objects are visible in the final result.
翻译：
从图片1中提取主要服装单品，去除所有配饰，如帽子、包包、首饰或其他附加元素。将这件服装放置在纯白色背景上。精确保留原图中所示的服装的确切风格、轮廓、长度、比例以及所有设计细节。不得更改、重新设计或修改服装的任何部分。确保最终结果中看不到人体模型、人体部位或其他多余物品。
<empty-block/>
chatgpt：
Extract only the clothing items that are clearly visible in the image. Do not infer, generate, or reconstruct any hidden or occluded parts.
Place the extracted clothing on a pure white background.
Preserve exactly the visible style, silhouette, proportions, and all design details as shown in the original image.
Do not add, extend, or complete any clothing elements that are not explicitly visible. Do not generate matching items or full outfits.
Ensure no human figure, mannequin, or body parts remain in the final image.
翻译：
仅提取图像中清晰可见的服装物品。请勿推断、生成或重建任何隐藏或被遮挡的部分。
将提取的服装放置在纯白色背景上。
精确保留原始图像中所示的可见风格、轮廓、比例以及所有设计细节。
请勿添加、扩展或补全任何未明确可见的服装元素。请勿生成搭配物品或完整套装。
确保最终图像中没有残留人体、人体模型或身体部位。
<empty-block/>
这一版太严格，我觉得不好，未测试：
Extract only the clothing regions that are explicitly visible at the pixel level in the image.
Strictly prohibit any inference or completion of hidden, occluded, or non-visible parts. Only include what is directly observable.
Place the extracted clothing on a clean white background.
Maintain exact visual fidelity: shape, silhouette, proportions, textures, and all details must match the visible regions of the original image.
Do not generate additional garments, matching pieces, or complete outfits.
Remove all human presence completely.
翻译：
仅提取图像中在像素层面可明确看到的衣物区域。
严禁对隐藏、遮挡或不可见的部分进行任何推断或补全。只包含可直接观察到的内容。
将提取出的衣物放置在干净的白色背景上。
保持精确的视觉保真度：形状、轮廓、比例、纹理以及所有细节都必须与原始图像的可见区域一致。
不得生成额外的服装、搭配单品或完整套装。
完全去除所有人体存在的痕迹。
<empty-block/>
豆包优化：
仅从参考图中提取**可见部分的完整服装本体**，不包含任何人物身体、头部、配饰（如帽子、包包、首饰等），将其放置在纯白色背景上。<br>严格遵循参考图中可见的服装细节：
1. 完全保留袖子的实际可见长度、版型（不得将中袖脑补成长袖/短袖）；
2. 完全保留裙子/下装的实际可见长度、位置（不得将膝上裙脑补成长裙/迷你裙）；
3. 完全保留服装的原始纹理、图案（不得将褶皱脑补成条纹/其他花纹）；
4. 完整还原服装的前后结构（不得出现背部空白、结构缺失等不合理情况）。<br>不得添加任何人体模型、假模特躯干或多余元素，不得修改服装的结构、风格或外观。<br>以标准服装版型展示，仅呈现参考图中已存在的可见信息，绝不脑补或创造任何原图不存在的细节。
<empty-block/>
参考别人工作流：
移除人物，保留服装本体，并将其展示为服装单品白底图。
服装的所有结构特征必须完全来源于输入图像本身。
不要推断、不要补全、不要修改任何服装结构。<br>严格保持服装颜色不变<br>服装在输入图像中呈现出的形态、边界、暴露与覆盖关系，<br>都被视为正确且完整的设计结果。
输出中不得出现人物或人体部分，<br>但必须保留服装原有的真实轮廓与结构边界。
仅改变展示方式，不改变服装本身。
输出应看起来像真实拍摄的服装单品照片。
<empty-block/>
## 换服装
```plain text
Perform a clothing swap: replace all garments worn by the person in image 1 with the outfit from image 2.

Use the outfit from image 2 as a complete and consistent set. Do not mix with any original clothing from image 1.

Strictly preserve identity and structure: pose, body proportions, face, hairstyle, skin tone, lighting conditions, and camera composition must remain unchanged.

The new clothing must be physically plausible: properly fitted to the body, respecting anatomy, gravity, fabric behavior, and perspective. Generate realistic folds, tension, and contact with the body.

Ensure correct occlusion handling: hair, arms, and body parts must naturally overlap or interact with the clothing without artifacts.

Completely remove original clothing. No remnants, layering errors, or visual artifacts are allowed.
```
---
# 翻译：
进行衣物交换：将图1中人物所穿的所有服装替换为图2中的全套服装。
使用图2中的全套服装作为完整且统一的搭配，不得与图1中原有的任何服装混合。
严格保留人物特征和结构：姿势、身体比例、面部、发型、肤色、光照条件和相机构图必须保持不变。
新服装必须符合物理合理性：贴合身体，遵循解剖结构、重力原理、面料特性和透视效果。生成真实的褶皱、张力以及与身体的接触状态。
确保正确处理遮挡问题：头发、手臂和身体部位必须与服装自然重叠或相互作用，不得出现瑕疵。
彻底移除原有服装，不允许有残留、分层错误或视觉瑕疵。
<empty-block/>
最初优化版（未比较）：
Replace the clothing of the person in image 1 with the outfit from image 2. Use the full outfit as a complete set, including all relevant parts (such as top, bottom, dress, or one-piece), and do not omit or mix elements.
Preserve the original pose, body structure, face, hairstyle, skin tone, lighting, and composition of image 1 exactly.
Ensure the new clothing fits the body naturally with correct proportions, realistic fabric deformation, accurate folds, shadows, and perspective. Maintain proper occlusion relationships (e.g., hands, hair, and body parts interacting correctly with the clothing).
Do not alter, redesign, or modify the style, structure, or details of the clothing from image 2. Remove all original clothing completely, with no residual artifacts or overlap.
翻译：
将图1中人物的服装替换为图2中的服装。完整使用整套服装，包括所有相关部分（如上衣、裤子、连衣裙或连体装），不要遗漏或混搭元素。
精确保留图1原有的姿势、身体结构、面部、发型、肤色、光线和构图。
确保新服装与身体自然贴合，比例正确，面料变形真实，褶皱、阴影和透视准确。保持适当的遮挡关系（例如，手、头发和身体部位与服装正确互动）。
不要改变、重新设计或修改图2中服装的风格、结构或细节。彻底移除所有原有服装，不得有残留痕迹或重叠。
<empty-block/>
<empty-block/>
豆包初版（上面都是以此为基础优化而来的）但没出现过错误，可以使用：
Replace the clothing of the figure in Figure 1 with the complete outfit in Figure 2 (whether it is a two-piece suit, a dress, or a jumpsuit), while retaining the posture, face shape, hairstyle, body structure, original lighting, composition, and skin color of the figure in Figure 1. Ensure that the new clothing fits the body naturally, generates realistic folds, shadows, and perspective effects, and must not modify the style, details, or fit of the clothing in Figure 2.
翻译：
将图1人物的衣物替换为图2中的完整服装（无论其为上下装套装、连衣裙或连体衣），保留图1人物的姿态、脸型、发型、肢体结构、原始光照、构图与肤色。确保新服装自然贴合身体，生成真实的褶皱、阴影与透视效果，不得修改图2服装的款式、细节与版型。
<empty-block/>
## 通用编辑元提示词（合并自「图像编辑」页）
泛化性更强，依赖用户提示词书写：
```bash
将用户请求解释为图像编辑指令。
首先确定主要的编辑任务（风格改变、物体添加、物体移除、光照调整等）。
保留原始图像中未明确要求改变的元素，包括主体身份、姿态、构图和空间布局。
确保物理合理性：保持正确的透视、逼真的阴影、一致的光照方向。
用一句话清晰地描述编辑后的结果。
仅输出最终的优化提示词。
```
换装请求精准替换：
```bash
你是专业的图像编辑指令生成专家，任务是将用户的换装请求，转化为精准、可执行的图像编辑提示词。

核心规则：
1.  **任务定位**：明确编辑为「精准换装」，仅替换指定服饰，**严格保留**原始图像的人物身份、姿态、构图、背景、光照、阴影及真实质感。
2.  **细节穷尽描述**：完整提取参考图中所有服饰的**款式、颜色、材质、纹理、结构细节、装饰特征、连接关系**（如吊袜带连接短裤与丝袜、胸罩上缘无蕾丝等），确保模型1:1还原。
3.  **边界约束**：仅修改用户要求替换的服饰，**绝不改动**任何非服装元素（人物、背景、配饰、光影等），保证物理合理性与视觉一致性。
4.  **输出要求**：用一句话清晰描述编辑结果，语言精准、约束明确，可直接用于图像编辑模型。

输入格式：
【原始图服饰描述】：{原始图中待替换服饰的完整描述}
【目标图服饰细节】：{目标图中所有待替换服饰的细节描述，含结构、材质、装饰、连接关系、设计细节等}
【用户换装需求】：{用户的核心换装指令}

输出要求：
仅输出最终可执行的图像编辑提示词，无额外解释。
```
用一句话清晰描述编辑后的最终效果：
```bash
你是专业的图像编辑指令生成专家，任务是将用户的换装请求，转化为精准、可执行的图像编辑提示词。

核心规则：
1.  **任务识别**：明确本次编辑为「换装」，仅替换服装/配饰，保留原始图像的人物身份、姿态、构图、空间布局、光照与阴影不变。
2.  **细节保真**：完整提取参考图中所有服饰的细节，包括款式、颜色、图案、材质、纹理、装饰、版型（如无袖高领、植绒蕾丝、吊袜带结构等），并清晰描述。
3.  **约束明确**：仅修改用户指定替换的服饰，其余元素（人物、背景、光影）严格保持原样，确保物理合理性与视觉一致性。
4.  **输出要求**：用一句话清晰描述编辑后的最终效果，语言简洁、约束明确，可直接用于图像编辑模型。

输出要求：
仅输出最终可执行的图像编辑提示词，无额外解释。
```
