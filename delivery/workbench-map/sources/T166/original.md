# AI脚本分镜

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 3 |
| 模型 | 通用 |
| 场景 | 视频分镜 |
| Notion | [AI脚本分镜](https://app.notion.com/p/AI-305079fdbc388039a59eef4cbf6dac80) |

**备注**：同模板三副本中最完整（含真实输入案例），保留此份

---

## 正文

```bash
【输入方式】：参考图 + 文本描述  
【延展目标】：基于上一张图的画面风格、人物外形、光影氛围、镜头语言，生成下一张分镜图，使得剧情延续

保持人物外观一致  
色调光影与参考图统一  
背景元素延续，不突变  
构图具备电影感（景别 / 光影 / 空间层次）

镜头类型（特写 / 中景 / 远景 / 俯拍 / 跟拍 / 环绕 / 侧移 / 拉远）  
镜头运动节奏（慢推 / 快切 / 手持感）  

人物发色、身形不变  
服饰延续衔接，不跳变  
动作表情是上一个镜头的自然推进  
背景环境连续递进

高清画面  
电影级光影  
真实材质  
无噪点无畸变  
可作为下一张分镜生成基础

输出时以Next Scene:开头，后面马上接文字。每一段文字是连续的，没有特殊符号，没有多余的解释，每一段文字100字左右，直接输出内容
```
此次输入需求文本可参考：<br>这是一部关于宠物狗冒险的3d卡通风格动漫 场景镜头，参考图片，帮我生成9张童趣的分镜图片，从花园到街道，小狗开始从一个箱子里面跳出，随后，在花园玩耍，突然草地跳出一直青蛙，随后追逐青蛙，来到一个马路街道的场景，青蛙跳入马路的井盖中，消失，小狗在井盖旁边看着，不同运镜和角度，不同的视角和景别
生成的分镜数量图片也是由这里的提示词进行控制，可自行输入：生成多少张童趣的分镜图片
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/bbcfb07b-b0c8-41fd-b8ac-003bd9bb920b/36ed4a26-082c-4d41-bdee-2948e2a7004b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2WDPDXJ%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T091856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIQDoRyX1Zf%2BrMU1P5uOivWxMffQGckr8PVRdbhCSiRG9EgIfR4J449FyI%2B3uruG%2FcFqujM2jtYYlOOzctde91McVxiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy%2FlNoRtEbBHMEMNiKtwDbs0xpY9ukLwAw1YSCKSpp0%2FZBTjPsXUwjjDvvJR%2FQtfD8qAevF%2FD%2FKi%2BWhULu6e4wSjnDT48BAg1%2Bx4R98JsSQOGvnNGuMVUpUDDVDt74t8hqMpd%2F2wByZqnm7Ojy1gRAqWPZih2ePWC%2FbtCvwNDBF5%2BwhIU5wGrDLyvI5v0glCXuBLAvVVRCgclK9JvzOOx19ne5YyytRCLGGB5XVczx7IsbwSLjsnYKDR2%2BoFlyJuchUx3sECcy288E4kCZCAxRRn3jcCuIdLlrSJdO%2F378gWn9Hy81VYc39hmIbYACgDEG3iarhYEz2sBEMXV5r6EqK7V2%2FKxrMNkn%2Bt%2B152uYR3MtmxNNiTYhg14OcQf5vKgoY8eJHCh4X6WJRHQ2zhJQhiLzv0vBbrT5KgdhtIuEHxWQAhP%2F2oC76eCyc%2BFg%2FZYa8w6FGhZMNKwwsuRKiWYEKnmLrk4in8HGxEjrYxfGAQ%2FYilT7FYAj4Ch%2FfIq34qYElfz3oeRwh2joqjM1WrxeWmTOTscoOupeolqLiV%2BeKnaao7gF4s3fTE9LCzG2RccEWwrkM%2B2ZOz0vf5e3J1rvvvZLrJwzAsgm5CsB%2FGGF71KnI6VaA9%2FQFQpCjpwewjx43k5KVO%2FQnjMiJgw89LM1gY6pgE4pMbhbnpjy7A85cLF9YIhC3Dbcg2i0zkcqqosr0FiZzTs0OAwUhZfMK%2Fyk5FjAcAbmWBNReAO5lslCMOL2%2FEioJ25CFfmi3lMI98lx6cZbCtjSJYXlQhveZhx3t9RtMu6QZKcny7WQkcuNCJMTBiCl56fseIA5kv%2BC%2BcAPhWX%2FdSC2C0j3%2BX9C7PKWg7JbhICbEFywNAaCoZ%2Bf0ZOpmNbmerFZsHJ&X-Amz-Signature=f94a8bf9e99b2fa7952f307cbbd4dd5f76ed852ec1a4833c7b7887a3c74473e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject#notion_record=block.305079fd-bc38-809e-a54f-d51581c64105.bbcfb07b-b0c8-41fd-b8ac-003bd9bb920b)
