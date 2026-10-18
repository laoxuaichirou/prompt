# 编辑模型思考

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 5 |
| 模型 | 通用 |
| 场景 | 图像编辑、模型工具 |
| Notion | [编辑模型思考](https://app.notion.com/p/31a079fdbc3880e09072d47bb384ee5a) |

**备注**：全库最体系化：5工作流+4模型对比+80场景速查，可做教程大纲

---

## 正文

<page url="https://app.notion.com/p/31b079fdbc388024ba56d5a1ea4d0bee">FireRed Edit</page>
<page url="https://app.notion.com/p/31a079fdbc38807781dadc0ee79f4885">编辑模型与千问对话</page>
此模型源自站外搬运（搬运地址: (https://huggingface.co/Kijai/LTXV2_comfy) ），若原作者对于本次搬运的结果存在异议，可点 申诉 我们会在 24 小时内，按照原作者的要求，对本模型展开编辑、删除或是转移给原作者等相关处理。由衷欢迎原作者入驻本站，共建 AI绘图的学习交流社区。
## 移除水印提示词：
去除图像中的水印、文字和标志，包括四个角内的所有标志或文字。确保移除元素后的背景无缝且自然。图像应看起来未改动，没有任何可见的先前标志或文字痕迹。清晰对焦，高品质，照片级真实感
## **LanPaint KSampler（高级）**
完全参数控制： **关键参数**
<table header-row="true">
<tr>
<td>**范围**</td>
<td>**范围**</td>
<td>**描述**</td>
</tr>
<tr>
<td>`Steps`</td>
<td>0-100</td>
<td>扩散采样总步数。步数越多，图像修复效果越好。建议步数为 20-50。</td>
</tr>
<tr>
<td>`LanPaint_NumSteps`</td>
<td>0-20</td>
<td>每个去噪步骤的推理迭代次数（“思考深度”）。简单任务：2-5次。困难任务：5-10次。</td>
</tr>
<tr>
<td>`LanPaint_Lambda`</td>
<td>0.1-50</td>
<td>内容对齐强度（数值越高越严格）。建议值 4.0 - 10.0</td>
</tr>
<tr>
<td>`LanPaint_StepSize`</td>
<td>0.1-1.0</td>
<td>每个思考步骤的步长。建议为 0.1-0.5。</td>
</tr>
<tr>
<td>`LanPaint_Beta`</td>
<td>0.1-2.0</td>
<td>掩蔽区域与非掩蔽区域之间的步长比。较小的值可以补偿较高的 lambda 值。建议值为 1.0。</td>
</tr>
<tr>
<td>`LanPaint_Friction`</td>
<td>0.0-100.0</td>
<td>朗之万动力学中的摩擦系数。摩擦系数越高，速度越慢但越稳定；摩擦系数越低，速度越快但越不稳定。建议取值范围为 10.0 - 20.0。</td>
</tr>
<tr>
<td>`LanPaint_EarlyStop`</td>
<td>0-10</td>
<td>在最后一次采样步骤之前停止 LanPaint 迭代。这有助于在某些情况下消除瑕疵。建议使用 1-5 次迭代。</td>
</tr>
<tr>
<td>`LanPaint_PromptMode`</td>
<td>图片优先/提示优先</td>
<td>“图像优先”模式侧重于图像上下文，可能忽略提示。“提示优先”模式则更侧重于提示。</td>
</tr>
</table>
要查看每个参数的详细说明，只需将鼠标悬停在相应的输入字段上，即可查看包含附加信息的工具提示。
# 📘 ComfyUI 图像编辑教程体系 - 深度总结文档
**整理日期：** 2026年3月6日
**适用模型：** Klein 9B / Qwen Edit 2511 / FireRed / Nano Banana Pro
**目标：** 新手极简化使用，逐步引导自主学习
---
## 第一部分：技术路线与核心理念
### 一、当前AIGC图像技术主流分类
<table header-row="true">
<tr>
<td>类型</td>
<td>核心能力</td>
<td>典型模型</td>
<td>学习优先级</td>
</tr>
<tr>
<td>**文生图模型**</td>
<td>从提示词生成图像、ControlNet控制构图</td>
<td>Flux、SDXL、SD3</td>
<td>⭐⭐⭐ 基础</td>
</tr>
<tr>
<td>**图像编辑模型**</td>
<td>理解图片内容，根据提示词直接修改图像</td>
<td>Klein 9B、Qwen Edit 2511、Nano Banana</td>
<td>⭐⭐⭐⭐⭐ 核心</td>
</tr>
<tr>
<td>**图像修复模型**</td>
<td>老照片修复、黑白上色、划痕修复、人脸增强</td>
<td>FireRed、Qwen Edit</td>
<td>⭐⭐⭐⭐ 高频</td>
</tr>
</table>
### 二、核心理念（教程指导思想）
> **很多旧技术（复杂ControlNet组合、多LoRA叠加）对普通用户已非必要。现在更重要的是理解：提示词表达 + 编辑模型能力边界 + 五种工作流结构。**
**你的教程目标：**
- 不是让新手学会ComfyUI的所有技术
- 而是通过场景化工作流，让用户选择场景→修改图片→得到结果
- 在使用过程中逐渐理解Prompt、Mask、Reference、工作流结构
- 降低ComfyUI学习门槛，帮助更多人进入开源生态
---
## 第二部分：五大核心工作流（底层结构）
```plain text
┌─────────────────────────────────────────────────────────────┐
│              ComfyUI 图像编辑五大核心工作流                   │
├─────────────────────────────────────────────────────────────┤
│  ① 单图编辑          → 风格/光影/镜头/色调/去物体/妆容         │
│  ② 单图+Mask         → 局部删除/局部替换/局部修复              │
│  ③ 多图参考          → 换衣服/换发型/换场景/姿势迁移           │
│  ④ 多图+Mask         → 精准换物/产品替换/复杂人物编辑          │
│  ⑤ 图像修复/增强     → 老照片修复/黑白上色/划痕修复/人脸增强    │
└─────────────────────────────────────────────────────────────┘
```
### 工作流选择判断标准
**核心原则：是否需要参考图**
<table header-row="true">
<tr>
<td>判断</td>
<td>工作流</td>
<td>典型场景</td>
</tr>
<tr>
<td>不需要具体参考物，模型自己生成即可</td>
<td>单图编辑</td>
<td>风格转换、光影调整、去水印</td>
</tr>
<tr>
<td>需要修改局部区域</td>
<td>单图+Mask</td>
<td>换发型、删除物体、局部修复</td>
</tr>
<tr>
<td>需要参考具体物体/风格</td>
<td>多图参考</td>
<td>换衣服、换场景、姿势迁移</td>
</tr>
<tr>
<td>需要精准替换特定区域</td>
<td>多图+Mask</td>
<td>产品替换、精准换装</td>
</tr>
<tr>
<td>需要恢复/增强图像信息</td>
<td>图像修复</td>
<td>老照片修复、黑白上色、清晰度恢复</td>
</tr>
</table>
---
## 第三部分：模型能力边界与节点配置
### 一、四款编辑模型对比
<table header-row="true">
<tr>
<td>能力</td>
<td>Klein 9B</td>
<td>Qwen Edit 2511</td>
<td>FireRed</td>
<td>Nano Banana Pro</td>
</tr>
<tr>
<td>风格修改</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>光影修改</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>镜头修改</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>去物体</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>换发型</td>
<td>⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>换衣服</td>
<td>⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>姿势迁移</td>
<td>⭐⭐</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
</tr>
<tr>
<td>老照片修复</td>
<td>⭐⭐</td>
<td>⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐</td>
</tr>
<tr>
<td>文本保留</td>
<td>⭐⭐</td>
<td>⭐⭐⭐</td>
<td>⭐⭐⭐⭐⭐</td>
<td>⭐⭐⭐⭐</td>
</tr>
<tr>
<td>本地运行</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌ API</td>
</tr>
<tr>
<td>成本</td>
<td>低</td>
<td>低</td>
<td>低</td>
<td>高</td>
</tr>
</table>
### 二、节点配置方案
<table header-row="true">
<tr>
<td>模型</td>
<td>推荐节点</td>
<td>CLIP类型</td>
<td>关键配置</td>
</tr>
<tr>
<td>**Klein 9B**</td>
<td>PainterFluxImageEdit</td>
<td>Qwen3 8B（纯文本）</td>
<td>视觉通过reference_latents传递</td>
</tr>
<tr>
<td>**Qwen Edit 2511**</td>
<td>TextEncodeQwenImageEditPlus</td>
<td>Qwen2.5-VL（多模态）</td>
<td>需要llama_template</td>
</tr>
<tr>
<td>**FireRed**</td>
<td>TextEncodeQwenImageEditPlus</td>
<td>Qwen2.5-VL（多模态）</td>
<td>必须带system prompt</td>
</tr>
<tr>
<td>**Nano Banana**</td>
<td>API节点</td>
<td>-</td>
<td>闭源服务</td>
</tr>
</table>
### 三、节点差异关键点
<table header-row="true">
<tr>
<td>特性</td>
<td>PainterFluxImageEdit</td>
<td>TextEncodeQwenImageEditPlus</td>
</tr>
<tr>
<td>图像标签</td>
<td>`image1:`, `image2:`</td>
<td>`Picture 1:`, `Picture 2:`</td>
</tr>
<tr>
<td>System Prompt</td>
<td>❌ 不支持</td>
<td>✅ 支持llama_template</td>
</tr>
<tr>
<td>适用模型</td>
<td>Klein / Qwen</td>
<td>Qwen / FireRed</td>
</tr>
<tr>
<td>核心作用</td>
<td>简化reference_latents处理</td>
<td>原生支持多模态CLIP</td>
</tr>
</table>
**重要提示：** 提示词中用`主图/参考图`或`图1/图2`都可以，模型都能理解，不需要精准匹配节点标签。
---
## 第四部分：提示词深度总结（精简实用版）
### 核心原则
1. **动词开头**：明确编辑动作（change/replace/add/remove）
2. **只说改什么**：不说保持什么（模型默认保持）
3. **避免长描述**：10-20词最佳
4. **用常见词**：模型训练数据里高频的词
### 指代方式（任选其一，模型都能理解）
<table header-row="true">
<tr>
<td>指代</td>
<td>示例</td>
<td>兼容性</td>
</tr>
<tr>
<td>`主图/参考图`</td>
<td>保持主图人物，穿上参考图的衣服</td>
<td>⭐⭐⭐⭐⭐ 跨节点通用</td>
</tr>
<tr>
<td>`图1/图2`</td>
<td>图1的人物换成图2的衣服</td>
<td>⭐⭐⭐⭐⭐ 模型都能理解</td>
</tr>
<tr>
<td>`image1/image2`</td>
<td>Keep person from image1, wear clothing from image2</td>
<td>⭐⭐⭐⭐ PainterFlux原生</td>
</tr>
<tr>
<td>`Picture 1/Picture 2`</td>
<td>Keep person from Picture 1, wear clothing from Picture 2</td>
<td>⭐⭐⭐⭐ Qwen节点原生</td>
</tr>
</table>
---
### 工作流①：单图编辑提示词
<table header-row="true">
<tr>
<td>场景</td>
<td>中文示例</td>
<td>英文示例</td>
<td>备注</td>
</tr>
<tr>
<td>**风格转换**</td>
<td>将风格改为赛博朋克风格</td>
<td>Convert the image to cyberpunk style</td>
<td>最常用，成功率高</td>
</tr>
<tr>
<td>**光影调整**</td>
<td>改为日落时分光线</td>
<td>Change lighting to sunset</td>
<td>可配合光影插件</td>
</tr>
<tr>
<td>**镜头变化**</td>
<td>改为特写肖像镜头</td>
<td>Close-up portrait shot</td>
<td>可配合运镜插件</td>
</tr>
<tr>
<td>**色调调整**</td>
<td>改为暖色调</td>
<td>Apply warm color grade</td>
<td>电影感常用</td>
</tr>
<tr>
<td>**去物体**</td>
<td>移除水印</td>
<td>Remove watermark from the image</td>
<td>新手最常用</td>
</tr>
<tr>
<td>**时间/天气**</td>
<td>改为下雨天</td>
<td>Change to rainy day</td>
<td>氛围变化</td>
</tr>
<tr>
<td>**妆容/美颜**</td>
<td>添加自然妆容</td>
<td>Add natural makeup</td>
<td>人像编辑</td>
</tr>
<tr>
<td>**添加物体**</td>
<td>在桌子上添加一个咖啡杯</td>
<td>Add a coffee cup on the table</td>
<td>需保持透视一致</td>
</tr>
</table>
**变体示例（风格转换）：**
```plain text
简单版：将风格改为吉卜力风格。
明确版：将图像重新绘制为吉卜力动画风格。
强控制版：将原图内容保持不变，仅将视觉风格转换为吉卜力动画风格。
```
---
### 工作流②：单图+Mask提示词
<table header-row="true">
<tr>
<td>场景</td>
<td>中文示例</td>
<td>英文示例</td>
<td>备注</td>
</tr>
<tr>
<td>**局部删除**</td>
<td>移除该区域</td>
<td>Remove this area</td>
<td>Mask后只需写remove</td>
</tr>
<tr>
<td>**局部替换**</td>
<td>改为皮夹克</td>
<td>Change to leather jacket</td>
<td>涂抹衣服区域</td>
</tr>
<tr>
<td>**局部修复**</td>
<td>修复损坏区域</td>
<td>Restore damaged area</td>
<td>老照片常用</td>
</tr>
<tr>
<td>**换发型**</td>
<td>改为短发</td>
<td>Change to short hair</td>
<td>涂抹头发区域</td>
</tr>
<tr>
<td>**换发色**</td>
<td>改为金色头发</td>
<td>Change hair color to blonde</td>
<td>涂抹头发区域</td>
</tr>
<tr>
<td>**材质修改**</td>
<td>改为金属材质</td>
<td>Change material to metal</td>
<td>涂抹物体区域</td>
</tr>
<tr>
<td>**颜色修改**</td>
<td>改为红色</td>
<td>Change color to red</td>
<td>涂抹物体区域</td>
</tr>
<tr>
<td>**表情调整**</td>
<td>改为微笑表情</td>
<td>Change to smile</td>
<td>涂抹面部区域</td>
</tr>
</table>
**关键技巧：** Mask区域要比实际修改区域稍大一些，让模型有融合空间。
---
### 工作流③：多图参考提示词
<table header-row="true">
<tr>
<td>场景</td>
<td>中文示例</td>
<td>英文示例</td>
<td>图像分配</td>
</tr>
<tr>
<td>**换衣服**</td>
<td>保持主图人物，穿上参考图的服装</td>
<td>Keep the person in the main image, wear the clothing from the reference image</td>
<td>图1人，图2衣</td>
</tr>
<tr>
<td>**换发型**</td>
<td>使用参考图中的发型</td>
<td>Use the hairstyle from the reference image</td>
<td>图1人，图2发</td>
</tr>
<tr>
<td>**换场景**</td>
<td>将人物置于参考图背景中</td>
<td>Place the subject in the background from the reference image</td>
<td>图1人，图2景</td>
</tr>
<tr>
<td>**姿势迁移**</td>
<td>采用参考图中的姿势</td>
<td>Adopt the pose from the reference image</td>
<td>图1人，图2姿</td>
</tr>
<tr>
<td>**风格参考**</td>
<td>应用参考图的艺术风格</td>
<td>Apply the art style from the reference image</td>
<td>图1内容，图2风格</td>
</tr>
<tr>
<td>**三图融合**</td>
<td>保持图1人物，穿图2衣服，在图3背景中</td>
<td>Keep person from image1, wear clothing from image2, in background from image3</td>
<td>图1人，图2衣，图3景</td>
</tr>
</table>
**关键技巧：** 参考图越清晰、特征越明显，效果越好。
---
### 工作流④：多图+Mask提示词
<table header-row="true">
<tr>
<td>场景</td>
<td>中文示例</td>
<td>英文示例</td>
<td>备注</td>
</tr>
<tr>
<td>**精准换装**</td>
<td>将遮罩区域服装替换为参考图服装</td>
<td>Replace the masked clothing with the clothing from the reference image</td>
<td>需画Mask</td>
</tr>
<tr>
<td>**精准换产品**</td>
<td>将产品替换为参考图产品</td>
<td>Replace the product with the product from the reference image</td>
<td>电商常用</td>
</tr>
<tr>
<td>**精准换背景**</td>
<td>将遮罩背景替换为参考图背景</td>
<td>Replace the masked background with the background from the reference image</td>
<td>需画Mask</td>
</tr>
<tr>
<td>**精准换材质**</td>
<td>将材质替换为参考图材质</td>
<td>Replace the material with the material from the reference image</td>
<td>产品编辑</td>
</tr>
<tr>
<td>**精准换颜色**</td>
<td>将颜色替换为参考图颜色</td>
<td>Replace the color with the color from the reference image</td>
<td>产品配色</td>
</tr>
</table>
**关键技巧：** Mask要精确框选要替换的区域，参考图物体角度尽量与主图一致。
---
### 工作流⑤：图像修复提示词
<table header-row="true">
<tr>
<td>场景</td>
<td>中文示例</td>
<td>英文示例</td>
<td>推荐模型</td>
</tr>
<tr>
<td>**清晰度恢复**</td>
<td>修复老照片，增强细节</td>
<td>Restore the old photo, enhance details</td>
<td>FireRed</td>
</tr>
<tr>
<td>**划痕修复**</td>
<td>移除划痕和损伤</td>
<td>Remove scratches and damage</td>
<td>FireRed</td>
</tr>
<tr>
<td>**黑白上色**</td>
<td>为黑白照片上色</td>
<td>Colorize the black and white photo</td>
<td>FireRed</td>
</tr>
<tr>
<td>**人脸修复**</td>
<td>自然修复面部细节</td>
<td>Restore face details naturally</td>
<td>FireRed</td>
</tr>
<tr>
<td>**风格保留修复**</td>
<td>修复同时保留原始风格</td>
<td>Restore while preserving the original style</td>
<td>FireRed</td>
</tr>
<tr>
<td>**文本保留修复**</td>
<td>修复同时保持文字完整</td>
<td>Restore while keeping text intact</td>
<td>FireRed</td>
</tr>
<tr>
<td>**去噪增强**</td>
<td>移除噪点和颗粒</td>
<td>Remove noise and grain</td>
<td>FireRed</td>
</tr>
<tr>
<td>**证件照修复**</td>
<td>修复证件照质量</td>
<td>Restore ID photo quality</td>
<td>FireRed</td>
</tr>
</table>
**关键技巧：** FireRed对文本保留有专门优化，旧书/海报修复首选。
---
## 第五部分：LLM元提示词优化
### 用途
让用户输入自然语言，LLM自动优化成适合编辑模型的提示词。
### 元提示词模板
```plain text
你是一名图像编辑提示优化师。

将用户请求解读为图像编辑指令。

遵循以下规则：
1. 使用"主图"和"参考图"以实现跨模型兼容。
2. 或者，"图片1/图片2"或"第一张图/第二张图"也可使用。
3. 除非明确要求更改，否则保持主体身份、姿势和构图不变。
4. 清晰表达编辑操作："更改"、"替换"、"添加"、"删除"、"修改"。
5. 保持提示简洁（15-30个词）。
6. 不引入新的叙事元素。
7. 只输出最终优化后的提示。

用户请求：{user_input}
图片数量：{image_count}
```
### 优化示例
<table header-row="true">
<tr>
<td>用户输入</td>
<td>优化后提示词</td>
</tr>
<tr>
<td>把衣服换成赛博朋克</td>
<td>保持主图人物，将服装改为赛博朋克风格夹克，添加霓虹灯效果。保持姿势和背景不变。</td>
</tr>
<tr>
<td>让这个人笑起来</td>
<td>调整面部表情为微笑，保持人物身份和面部结构不变。其他元素保持不变。</td>
</tr>
<tr>
<td>去掉水印</td>
<td>移除图像中的水印，自然重建该区域。保持其他内容不变。</td>
</tr>
<tr>
<td>改成晚上</td>
<td>将环境改为夜晚，添加适当的夜间 lighting。保持主体、姿势和构图不变。</td>
</tr>
</table>
---
## 第六部分：80个真实用户需求场景速查
### 单图编辑（20个）
<table header-row="true">
<tr>
<td>编号</td>
<td>用户需求</td>
<td>提示词</td>
<td>工作流</td>
</tr>
<tr>
<td>1</td>
<td>去水印</td>
<td>Remove watermark</td>
<td>单图</td>
</tr>
<tr>
<td>2</td>
<td>去logo</td>
<td>Remove logo</td>
<td>单图</td>
</tr>
<tr>
<td>3</td>
<td>去路人</td>
<td>Remove background people</td>
<td>单图</td>
</tr>
<tr>
<td>4</td>
<td>风格转动漫</td>
<td>Convert to anime style</td>
<td>单图</td>
</tr>
<tr>
<td>5</td>
<td>风格转油画</td>
<td>Convert to oil painting style</td>
<td>单图</td>
</tr>
<tr>
<td>6</td>
<td>风格转赛博朋克</td>
<td>Convert to cyberpunk style</td>
<td>单图</td>
</tr>
<tr>
<td>7</td>
<td>风格转皮克斯</td>
<td>Convert to Pixar style</td>
<td>单图</td>
</tr>
<tr>
<td>8</td>
<td>白天变夜晚</td>
<td>Change to night time</td>
<td>单图</td>
</tr>
<tr>
<td>9</td>
<td>晴天变雨天</td>
<td>Change to rainy day</td>
<td>单图</td>
</tr>
<tr>
<td>10</td>
<td>晴天变雪天</td>
<td>Change to snowy day</td>
<td>单图</td>
</tr>
<tr>
<td>11</td>
<td>添加雾气</td>
<td>Add foggy atmosphere</td>
<td>单图</td>
</tr>
<tr>
<td>12</td>
<td>电影感光影</td>
<td>Apply cinematic lighting</td>
<td>单图</td>
</tr>
<tr>
<td>13</td>
<td>日落光影</td>
<td>Change lighting to sunset</td>
<td>单图</td>
</tr>
<tr>
<td>14</td>
<td>特写镜头</td>
<td>Close-up portrait shot</td>
<td>单图</td>
</tr>
<tr>
<td>15</td>
<td>广角镜头</td>
<td>Wide angle shot</td>
<td>单图</td>
</tr>
<tr>
<td>16</td>
<td>暖色调</td>
<td>Apply warm color grade</td>
<td>单图</td>
</tr>
<tr>
<td>17</td>
<td>冷色调</td>
<td>Apply cool color grade</td>
<td>单图</td>
</tr>
<tr>
<td>18</td>
<td>黑白效果</td>
<td>Convert to black and white</td>
<td>单图</td>
</tr>
<tr>
<td>19</td>
<td>自然妆容</td>
<td>Add natural makeup</td>
<td>单图</td>
</tr>
<tr>
<td>20</td>
<td>添加眼镜</td>
<td>Add glasses</td>
<td>单图</td>
</tr>
</table>
### 单图+Mask（15个）
<table header-row="true">
<tr>
<td>编号</td>
<td>用户需求</td>
<td>提示词</td>
<td>工作流</td>
</tr>
<tr>
<td>21</td>
<td>局部删除物体</td>
<td>Remove this area</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>22</td>
<td>局部替换物体</td>
<td>Replace with sunglasses</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>23</td>
<td>局部修复破损</td>
<td>Restore damaged area</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>24</td>
<td>换发型</td>
<td>Change to short hair</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>25</td>
<td>换发色</td>
<td>Change hair color to blonde</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>26</td>
<td>换衣服</td>
<td>Change to leather jacket</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>27</td>
<td>换裤子</td>
<td>Change to jeans</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>28</td>
<td>换鞋子</td>
<td>Change to sneakers</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>29</td>
<td>添加配饰</td>
<td>Add necklace</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>30</td>
<td>改变表情</td>
<td>Change to smile</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>31</td>
<td>改变年龄</td>
<td>Make person look younger</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>32</td>
<td>添加胡须</td>
<td>Add beard</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>33</td>
<td>去除胡须</td>
<td>Remove beard</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>34</td>
<td>改变材质</td>
<td>Change material to metal</td>
<td>单图+Mask</td>
</tr>
<tr>
<td>35</td>
<td>改变颜色</td>
<td>Change color to red</td>
<td>单图+Mask</td>
</tr>
</table>
### 多图参考（25个）
<table header-row="true">
<tr>
<td>编号</td>
<td>用户需求</td>
<td>提示词</td>
<td>工作流</td>
</tr>
<tr>
<td>36</td>
<td>换衣服（有参考）</td>
<td>Wear clothing from reference</td>
<td>多图</td>
</tr>
<tr>
<td>37</td>
<td>换发型（有参考）</td>
<td>Use hairstyle from reference</td>
<td>多图</td>
</tr>
<tr>
<td>38</td>
<td>换背景场景</td>
<td>Place in background from reference</td>
<td>多图</td>
</tr>
<tr>
<td>39</td>
<td>姿势迁移</td>
<td>Adopt pose from reference</td>
<td>多图</td>
</tr>
<tr>
<td>40</td>
<td>风格参考迁移</td>
<td>Apply art style from reference</td>
<td>多图</td>
</tr>
<tr>
<td>41</td>
<td>人物进新场景</td>
<td>Combine person with new background</td>
<td>多图</td>
</tr>
<tr>
<td>42</td>
<td>多角色合影</td>
<td>Combine multiple people</td>
<td>多图</td>
</tr>
<tr>
<td>43</td>
<td>产品换背景</td>
<td>Place product in new background</td>
<td>多图</td>
</tr>
<tr>
<td>44</td>
<td>产品加特效</td>
<td>Add water drops to product</td>
<td>多图</td>
</tr>
<tr>
<td>45</td>
<td>产品加光影</td>
<td>Enhance product lighting</td>
<td>多图</td>
</tr>
<tr>
<td>46</td>
<td>人物风格化</td>
<td>Apply character style from reference</td>
<td>多图</td>
</tr>
<tr>
<td>47</td>
<td>服装风格参考</td>
<td>Match clothing style from reference</td>
<td>多图</td>
</tr>
<tr>
<td>48</td>
<td>妆容参考</td>
<td>Apply makeup from reference</td>
<td>多图</td>
</tr>
<tr>
<td>49</td>
<td>配饰参考</td>
<td>Add accessories from reference</td>
<td>多图</td>
</tr>
<tr>
<td>50</td>
<td>鞋履参考</td>
<td>Change shoes to match reference</td>
<td>多图</td>
</tr>
<tr>
<td>51</td>
<td>包包参考</td>
<td>Add bag from reference</td>
<td>多图</td>
</tr>
<tr>
<td>52</td>
<td>眼镜参考</td>
<td>Add glasses from reference</td>
<td>多图</td>
</tr>
<tr>
<td>53</td>
<td>帽子参考</td>
<td>Add hat from reference</td>
<td>多图</td>
</tr>
<tr>
<td>54</td>
<td>珠宝参考</td>
<td>Add jewelry from reference</td>
<td>多图</td>
</tr>
<tr>
<td>55</td>
<td>纹身参考</td>
<td>Add tattoo from reference</td>
<td>多图</td>
</tr>
<tr>
<td>56</td>
<td>宠物融合</td>
<td>Add pet to scene</td>
<td>多图</td>
</tr>
<tr>
<td>57</td>
<td>车辆参考</td>
<td>Change car to match reference</td>
<td>多图</td>
</tr>
<tr>
<td>58</td>
<td>家具参考</td>
<td>Add furniture from reference</td>
<td>多图</td>
</tr>
<tr>
<td>59</td>
<td>植物参考</td>
<td>Add plants from reference</td>
<td>多图</td>
</tr>
<tr>
<td>60</td>
<td>三图融合</td>
<td>Person from image1, clothing from image2, background from image3</td>
<td>多图</td>
</tr>
</table>
### 多图+Mask（10个）
<table header-row="true">
<tr>
<td>编号</td>
<td>用户需求</td>
<td>提示词</td>
<td>工作流</td>
</tr>
<tr>
<td>61</td>
<td>精准换衣服</td>
<td>Replace masked clothing with reference</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>62</td>
<td>精准换产品</td>
<td>Replace product with reference product</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>63</td>
<td>精准换脸</td>
<td>Replace face with reference face</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>64</td>
<td>精准换手</td>
<td>Replace hand with reference hand</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>65</td>
<td>精准换鞋</td>
<td>Replace shoes with reference shoes</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>66</td>
<td>精准换包</td>
<td>Replace bag with reference bag</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>67</td>
<td>精准换背景区域</td>
<td>Replace masked background with reference</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>68</td>
<td>精准换材质</td>
<td>Replace material with reference material</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>69</td>
<td>精准换颜色</td>
<td>Replace color with reference color</td>
<td>多图+Mask</td>
</tr>
<tr>
<td>70</td>
<td>精准换图案</td>
<td>Replace pattern with reference pattern</td>
<td>多图+Mask</td>
</tr>
</table>
### 图像修复（15个）
<table header-row="true">
<tr>
<td>编号</td>
<td>用户需求</td>
<td>提示词</td>
<td>工作流</td>
</tr>
<tr>
<td>71</td>
<td>老照片清晰度恢复</td>
<td>Restore old photo, enhance details</td>
<td>修复</td>
</tr>
<tr>
<td>72</td>
<td>老照片划痕修复</td>
<td>Remove scratches and damage</td>
<td>修复</td>
</tr>
<tr>
<td>73</td>
<td>黑白照片上色</td>
<td>Colorize black and white photo</td>
<td>修复</td>
</tr>
<tr>
<td>74</td>
<td>老照片人脸修复</td>
<td>Restore face details naturally</td>
<td>修复</td>
</tr>
<tr>
<td>75</td>
<td>老照片风格保留</td>
<td>Restore while preserving original style</td>
<td>修复</td>
</tr>
<tr>
<td>76</td>
<td>低清图变高清</td>
<td>Enhance resolution and details</td>
<td>修复</td>
</tr>
<tr>
<td>77</td>
<td>去噪点</td>
<td>Remove noise and grain</td>
<td>修复</td>
</tr>
<tr>
<td>78</td>
<td>证件照修复</td>
<td>Restore ID photo quality</td>
<td>修复</td>
</tr>
<tr>
<td>79</td>
<td>旧书/海报修复</td>
<td>Restore while keeping text intact</td>
<td>修复</td>
</tr>
<tr>
<td>80</td>
<td>模糊照片清晰化</td>
<td>Sharpen and enhance details</td>
<td>修复</td>
</tr>
</table>
---
## 第七部分：教程设计建议
### 一、三阶段学习路径
```plain text
┌─────────────────────────────────────────────────────────────┐
│                    ComfyUI 图像编辑教程路径                   │
├─────────────────────────────────────────────────────────────┤
│  第一阶段（零基础）                                           │
│  ├─ 工作流1：单图编辑（风格/光影/镜头）                      │
│  ├─ 工作流2：单图+Mask（局部删除/替换）                      │
│  ├─ 工作流3：多图参考（换衣服/换场景）                       │
│  └─ 工作流4：图像修复（老照片修复）                          │
│                                                              │
│  第二阶段（应用场景）                                         │
│  ├─ 人像编辑：换发型/换衣服/换背景/妆容                       │
│  ├─ 商品编辑：产品换背景/加特效/换材质                        │
│  ├─ 风格转换：写实转动漫/艺术风格/AI艺术化                     │
│  └─ 物体编辑：添加/删除/替换物体                              │
│                                                              │
│  第三阶段（进阶控制）                                         │
│  ├─ ControlNet姿势控制                                      │
│  ├─ 深度图构图控制                                           │
│  ├─ 线稿控制                                                 │
│  └─ 批量处理工作流                                           │
└─────────────────────────────────────────────────────────────┘
```
### 二、每个工作流固定4个输入节点（新手友好）
<table header-row="true">
<tr>
<td>节点</td>
<td>说明</td>
<td>新手操作</td>
</tr>
<tr>
<td>① 主图</td>
<td>上传原图</td>
<td>拖入图片</td>
</tr>
<tr>
<td>② 参考图（可选）</td>
<td>多图工作流用</td>
<td>拖入图片</td>
</tr>
<tr>
<td>③ Mask（可选）</td>
<td>局部编辑用</td>
<td>涂抹区域</td>
</tr>
<tr>
<td>④ 提示词</td>
<td>编辑指令</td>
<td>选场景自动填充/手动改</td>
</tr>
</table>
**其他节点全部锁死，新手不用碰。**
### 三、教程工作流设计原则
1. **场景化封装**：用户只关心"我要做什么"，不关心"用哪个工作流"
2. **模型无关**：流程结构不变，只换模型节点
3. **提示词通用**：用主图/参考图指代，跨节点兼容
4. **大字标注**：每个节点标注①②③④，新手不迷路
---
## 第八部分：你可能没想到的使用场景
### 一、电商/商业场景
<table header-row="true">
<tr>
<td>场景</td>
<td>工作流</td>
<td>提示词</td>
</tr>
<tr>
<td>产品换背景</td>
<td>多图</td>
<td>Place product in background from reference</td>
</tr>
<tr>
<td>模特换装</td>
<td>多图+Mask</td>
<td>Change model clothing to match reference</td>
</tr>
<tr>
<td>产品换色</td>
<td>多图+Mask</td>
<td>Change product color to match reference</td>
</tr>
<tr>
<td>产品加光影</td>
<td>单图</td>
<td>Enhance product lighting</td>
</tr>
<tr>
<td>产品加水珠</td>
<td>单图</td>
<td>Add water drops to product</td>
</tr>
<tr>
<td>包装换设计</td>
<td>多图+Mask</td>
<td>Replace packaging with reference design</td>
</tr>
</table>
### 二、社交媒体场景
<table header-row="true">
<tr>
<td>场景</td>
<td>工作流</td>
<td>提示词</td>
</tr>
<tr>
<td>头像风格化</td>
<td>单图</td>
<td>Convert to anime style</td>
</tr>
<tr>
<td>朋友圈背景</td>
<td>单图</td>
<td>Apply cinematic color grade</td>
</tr>
<tr>
<td>去除路人</td>
<td>单图</td>
<td>Remove background people</td>
</tr>
<tr>
<td>添加滤镜效果</td>
<td>单图</td>
<td>Apply vintage film style</td>
</tr>
<tr>
<td>横图变竖图</td>
<td>单图+Outpaint</td>
<td>Extend background to vertical format</td>
</tr>
</table>
### 三、创意设计场景
<table header-row="true">
<tr>
<td>场景</td>
<td>工作流</td>
<td>提示词</td>
</tr>
<tr>
<td>概念图风格化</td>
<td>单图</td>
<td>Convert to concept art style</td>
</tr>
<tr>
<td>线稿上色</td>
<td>多图</td>
<td>Apply color from reference</td>
</tr>
<tr>
<td>材质探索</td>
<td>单图+Mask</td>
<td>Change material to metal/glass/wood</td>
</tr>
<tr>
<td>氛围测试</td>
<td>单图</td>
<td>Change to night/rain/snow</td>
</tr>
<tr>
<td>多版本对比</td>
<td>单图</td>
<td>同一提示词跑多次</td>
</tr>
</table>
### 四、个人/家庭场景
<table header-row="true">
<tr>
<td>场景</td>
<td>工作流</td>
<td>提示词</td>
</tr>
<tr>
<td>老照片修复</td>
<td>修复</td>
<td>Restore old photo, enhance details</td>
</tr>
<tr>
<td>黑白照片上色</td>
<td>修复</td>
<td>Colorize black and white photo</td>
</tr>
<tr>
<td>证件照优化</td>
<td>修复</td>
<td>Restore ID photo quality</td>
</tr>
<tr>
<td>家庭合影修复</td>
<td>修复</td>
<td>Restore face details naturally</td>
</tr>
<tr>
<td>旅游照优化</td>
<td>单图</td>
<td>Apply cinematic lighting</td>
</tr>
</table>
### 五、进阶技巧场景
<table header-row="true">
<tr>
<td>场景</td>
<td>工作流</td>
<td>提示词</td>
</tr>
<tr>
<td>多风格对比</td>
<td>单图</td>
<td>同一图跑多个风格提示词</td>
</tr>
<tr>
<td>渐进式修改</td>
<td>单图</td>
<td>分多次小修改，不是一次大修改</td>
</tr>
<tr>
<td>参考图组合</td>
<td>多图</td>
<td>图2衣服+图3背景+图4姿势</td>
</tr>
<tr>
<td>Mask分层编辑</td>
<td>单图+Mask</td>
<td>分多次Mask不同区域</td>
</tr>
<tr>
<td>模型对比测试</td>
<td>同一工作流</td>
<td>Klein/Qwen/FireRed对比效果</td>
</tr>
</table>
---
## 第九部分：常见问题与解决方案
<table header-row="true">
<tr>
<td>问题</td>
<td>可能原因</td>
<td>解决方案</td>
</tr>
<tr>
<td>人物变形</td>
<td>单图换衣服无参考</td>
<td>改用多图工作流+参考图</td>
</tr>
<tr>
<td>构图改变</td>
<td>提示词过于复杂</td>
<td>简化提示词，强调保持构图</td>
</tr>
<tr>
<td>风格不纯</td>
<td>模型能力不足</td>
<td>换Qwen Edit或Nano Banana</td>
</tr>
<tr>
<td>局部不自然</td>
<td>Mask边界不清晰</td>
<td>扩大Mask范围，增加融合</td>
</tr>
<tr>
<td>参考不生效</td>
<td>参考图权重低</td>
<td>增加IPAdapter权重或换模型</td>
</tr>
<tr>
<td>文字乱码</td>
<td>模型不支持文本</td>
<td>换FireRed模型</td>
</tr>
<tr>
<td>FireRed报错</td>
<td>缺少llama_template</td>
<td>用TextEncodeQwenImageEditPlus节点</td>
</tr>
<tr>
<td>Klein效果差</td>
<td>无一致性LoRA</td>
<td>添加一致性LoRA或换Qwen Edit</td>
</tr>
</table>
---
## 第十部分：后续可扩展板块
<table header-row="true">
<tr>
<td>板块</td>
<td>工具/模型</td>
<td>说明</td>
</tr>
<tr>
<td>图像放大</td>
<td>SeedVR / RealESRGAN</td>
<td>2x/4x upscale</td>
</tr>
<tr>
<td>高清修复</td>
<td>FireRed / CodeFormer</td>
<td>人脸/细节修复</td>
</tr>
<tr>
<td>批量处理</td>
<td>ComfyUI batch节点</td>
<td>电商/批量需求</td>
</tr>
<tr>
<td>视频编辑</td>
<td>AnimateDiff / SVD</td>
<td>后续扩展</td>
</tr>
<tr>
<td>3D生成</td>
<td>TripoSR / LGM</td>
<td>后续扩展</td>
</tr>
</table>
---
## 第十一部分：核心总结
```plain text
┌─────────────────────────────────────────────────────────────┐
│                    教程体系核心要点                          │
├─────────────────────────────────────────────────────────────┤
│  1. 五大工作流覆盖95%图像编辑需求                            │
│  2. 模型可自由替换（Klein→Qwen→FireRed→Nano Banana）         │
│  3. 每个工作流固定4个输入节点，新手友好                      │
│  4. 80个真实场景速查表，用户可快速定位需求                    │
│  5. LLM元提示词优化，降低提示词门槛                          │
│  6. 提示词指代通用（主图/参考图），跨节点兼容                 │
│  7. 三阶段学习路径，从零基础到进阶                           │
│  8. 模型无关设计，流程结构不变，只换模型节点                  │
└─────────────────────────────────────────────────────────────┘
```
**核心理念：** 让用户只关心"我要做什么"，而不是"用哪个工作流"。通过场景化封装，降低ComfyUI学习门槛，引导新手逐步理解底层逻辑。
---
这份文档可直接用于：
- 📺 B站教程系列
- 📚 知识星球内容
- 🌐 网站教程专区
- 📖 PDF教程手册
- 📝 个人回顾参考
<empty-block/>
