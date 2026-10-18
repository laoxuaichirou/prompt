# 人物多角度提示词（3+1版）

| 属性 | 值 |
|---|---|
| 状态 | 仅参考 |
| 评分 | 3 |
| 模型 | 通用、Nano Banana |
| 场景 | 人像摄影、图像编辑 |
| Notion | [人物多角度提示词（3+1版）](https://app.notion.com/p/3-1-2dc079fdbc3880159f92e58b6377df5b) |

**备注**：高价值原料仓但无组织重复严重；标题'3+1版'名不副实；子页LoRA素材值得单独评级

---

## 正文

<page url="https://app.notion.com/p/31a079fdbc388011a98dc32d51738751">一键生成10张🍠写真图</page>
<page url="https://app.notion.com/p/304079fdbc3880b09c9dd3e9456ba2d4">人物lora素材生成</page>
<page url="https://app.notion.com/p/305079fdbc388006b78afa66818e4602"></page>
<page url="https://app.notion.com/p/310079fdbc388062b355f3644bd51c70">角色设计（待测试）</page>
<page url="https://app.notion.com/p/313079fdbc3880f1830af1689674047e">**免费且一致的角色提示**</page>
<page url="https://app.notion.com/p/31d079fdbc3880958a31e2d0f5a480c0">人物资产</page>
<page url="https://app.notion.com/p/31d079fdbc3880a7ab2bd6a29316f9c6">搜集提示词</page>
<empty-block/>
klein delight lora：
中文
```bash
重新照亮图像，消除所有现有光照条件，并用中性、均匀的光照替换。
应用柔和、均匀分布的光照，无方向性阴影，无刺眼高光，无戏剧性对比。
保持所有主体的原始身份，
精确保留面部结构、肤色、比例、表情、头发、服装和纹理。
不要改变姿势、相机角度、背景几何形状或图像构图。
光照应显得平衡，具有工作室中性感，类似于漫射阴天或柔和的灯箱设置。
确保整个图像曝光一致，具有逼真的深度，仅在必要时为形状添加微妙的阴影。
```
英文
```bash
Relight the image to remove all existing lighting conditions and replace them with neutral, uniform illumination.
Apply soft, evenly distributed lighting with no directional shadows, no harsh highlights, and no dramatic contrast. 
Maintain the original identity of all subjects exactly—preserve facial structure, skin tone, proportions, expressions, hair, clothing, and textures.
Do not alter pose, camera angle, background geometry, or image composition. 
Lighting should appear balanced, and studio-neutral, similar to diffuse overcast or a soft lightbox setup.
Ensure consistent exposure across the entire image with realistic depth and subtle shading only where necessary for form.
```
编辑模型元提示词（Qwen给出来的）
```bash
Interpret the user request as an image editing instruction.
First determine the primary editing task (style change, object addition, 
object removal, lighting adjustment, etc.).
Preserve all elements of the original image that are not explicitly 
requested to change, including subject identity, pose, composition, 
and spatial layout.
Ensure physical plausibility: maintain correct perspective, realistic 
shadows, consistent lighting direction.
Describe the edited result clearly in a single paragraph.
Output only the final optimized prompt.
将用户请求解释为图像编辑指令。
首先确定主要的编辑任务（风格改变、物体添加、物体移除、光照调整等）。
保留原始图像中未明确要求改变的元素，包括主体身份、姿态、构图和空间布局。
确保物理合理性：保持正确的透视、逼真的阴影、一致的光照方向。
用一句话清晰地描述编辑后的结果。
仅输出最终的优化提示词。
```
人物正面全身照，站直，双臂自然下垂，头顶与脚底齐框。纯白背景，无影棚布光，正交相机，8K分辨率。
人物背面全身照，站直，双臂自然下垂，头顶与脚底齐框。纯白背景，无影棚布光，正交相机，8K分辨率。
人物左侧90度全身照，站直，双臂自然下垂，头顶与脚底齐框。纯白背景，无影棚布光，正交相机，8K分辨率。
人物右侧90度全身照，站直，双臂自然下垂，头顶与脚底齐框。纯白背景，无影棚布光，正交相机，8K分辨率。
人物面部特写，正视镜头，纯白背景，无影棚布光，8K分辨率。
<empty-block/>
<empty-block/>
<empty-block/>
<empty-block/>
纯白背景无影棚光8K正交正视全身，【主体】站直双臂自然下垂，头顶与脚底齐镜。<br>纯白背景无影棚光8K正交正视半身，【主体】截取至大腿中段，双手完整入画。<br>纯白背景无影棚光8K正交正视面部特写，【主体】双眼直视镜头，微距浅景深。<br>纯白背景无影棚光8K正交右侧全身，【主体】90°侧立，手臂贴腿，完整侧轮廓。<br>纯白背景无影棚光8K正交右侧半身，【主体】躯干90°转向，远侧手臂微后。<br>纯白背景无影棚光8K正交右侧面部特写，【主体】头转90°，近耳贴镜。<br>纯白背景无影棚光8K正交左侧全身，【主体】90°侧立，与右侧成镜像。<br>纯白背景无影棚光8K正交左侧半身，【主体】躯干45°转向，远侧手臂微后。<br>纯白背景无影棚光8K正交左侧面部特写，【主体】头转90°，近耳贴镜。<br>纯白背景无影棚光8K正交背视全身，【主体】背对镜头，脚跟与后脑齐镜，双臂下垂。<br>纯白背景无影棚光8K正交右后过肩，【主体】背对头肩水平，右肩在前，左肩远。<br>纯白背景无影棚光8K正交左后过肩，【主体】背对头肩水平，左肩在前，右肩远。<br>纯白背景无影棚光8K正交俯拍平躺，【主体】仰卧地面，四肢外展30°，相机平行身体。<br>纯白背景无影棚光8K正交俯拍侧卧，【主体】右侧屈膝侧卧，相机垂直身体轴线。<br>纯白背景无影棚光8K正交仰拍足底，【主体】踩透明台，相机正下方，完整脚底轮廓。<br>纯白背景无影棚光8K正交45°仰拍漂浮，【主体】离地30 cm失重，发梢/尾尖微动。
创建一个正视图，纯白色背景上的全身姿势，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个半身图，纯白色背景上的半身照，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个特写正视图，纯白色背景上的人脸特写，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个右侧面，纯白色背景上的全身姿势，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个右侧图，纯白色背景上的半身姿势，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个特写右视图，纯白色背景上的人脸特写，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个右侧过肩视图。角色的背对着镜头。请将头部和身体保持在同一水平线上，在白色的背景前<br>创建一个过肩视图。角色的后脑勺背对着镜头。在白色的背景前<br>创建一个左侧面，纯白色背景上的全身姿势，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个左侧图，纯白色背景上的半身姿势，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个特写左视图，纯白色背景上的人脸特写，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个左过肩视图。角色的背对着镜头。请将头部和身体保持在同一水平线上，在白色的背景前<br>创建一个人物平躺在地上的视图，纯白色背景，一致的照明和风格，没有背景噪音，没有阴影<br>创建一个人物侧躺在地上的视图，纯白色背景，一致的照明和风格，没有背景噪音，没有阴影
<empty-block/>
Next Scene：将镜头向前移动<br>Next Scene：将镜头向后移动<br>Next Scene：将镜头向左移动<br>Next Scene：将镜头向右移动<br>Next Scene：将镜头向上移动<br>Next Scene：将镜头向下移动<br>Next Scene：将镜头向左旋转45度<br>Next Scene：将镜头向右旋转45度<br>Next Scene：将镜头向左旋转90度<br>Next Scene：将镜头向右旋转90度<br>Next Scene：将镜头转为俯视<br>Next Scene：将镜头转为仰视<br>Next Scene：将镜头转为广角镜头<br>Next Scene：将镜头转为特写镜头
<empty-block/>
即梦使用：3.0 3.1画风 3D 游戏CG OC渲染质感
主体 一个成年兽人 强壮身材 脸上血红色符文 手持战斧 深色纯色背景
灯光 角色面光 45度侧光 边缘光
构图 角色正面中景朝镜头 镜头平视<br>香蕉PRO：镜头拍摄人物全身三视图（正面侧面背面），四种日常的不同脸部表情特写，四种日常的不同的姿势，3D 游戏CG OC渲染质感
人物描述：皮肤质感：皮肤细腻，自然瑕疵。
背景：黑色背景。全身像，视觉冲击力，光影交错，
材质：细节复杂，质感细腻，高细节，3D 游戏CG OC渲染质感
灯光：45度侧光，轮廓光，3D 游戏CG OC渲染质感
排版：三等分排版，第一排，三视图，第二排 人物表情；第三排，人物动作
