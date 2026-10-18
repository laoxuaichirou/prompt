# JSON提示词

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 4 |
| 模型 | Nano Banana |
| 场景 | 提示词工程 |
| Notion | [JSON提示词](https://app.notion.com/p/JSON-305079fdbc388021a8dfed7bcb7cae02) |

**备注**：UI/电商JSON工作流扎实；示例JSON有多余逗号小错

---

## 正文

<page url="https://app.notion.com/p/305079fdbc38804cb31adb1d08721535">红包封面生成</page>
# Step1： 制作 Agent
使用元提示词，得到一个 UI Agent 提示词。
以产品设计图为例，我制作的元提示词如下，你可以直接copy使用：
```plain text
请为我设计一个 AI Agent 的提示词，请遵循提示词工程规范，包含：角色、任务、few-shot 等工程技巧 。

AI Agent 将用于生成 JSON 格式 UI设计语言，基本要求如下：
- 完全使用JSON格式编写
- 支持跨平台。既能制作web也能制作app（并不是指同一份json可以用来生成web和app）
- 组件化设计。将每一个UI元素视为一个组件来对待，复杂组件使用嵌套式表示
- 设计一致。所有组件视觉设计风格保持一致
- 样式精确。包含但不限于：位置、大小、字体、内容、颜色等属性描述
- 风格迁移。需要方便整体迁移风格，比如暗系，亮系，等
- 真实。使用有意义的数据展示界面
- 语言。若无要求，界面元素默认使用中文
- 完整。JSON需要描述一张完整的UI设计图，而不是渲染图或者demo
- 其他要求，你觉得有助于生成UI图的要求

在开始制作 JSON 之前，我希望AI主动询问我一些信息（给我做选择题而不是开放式问答），以确保最终制作的UI图符合用户的要求。
```
元提示词书写有几个关键之处：
1. **提示词工程**。说明你的目的是为了制作Agent，并且使用提示词工程，这样得到的Agent提示词会更鲁棒。
2. **提出基本要求**。提出要支持多平台、组件化、真实数据等要求，这样生成的JSON更精准。
3. **不限制**。着重说明不要限制在你提的要求之内，这样AI会**主动反思**并制作出更完整设计图提示词。
4. **主动提问**。让AI在动手前根据你的需求针对性提问，降低后期返工的概率。这利用到了**AI规划**的能力。
你会得到一个 Agent 提示词：
```plain text
# ====== SYSTEM / ROLE ======
你是一名 **专业 UI 图描述工程师 & JSON UI 生成器（Role: UI JSON Generator Agent）**。
擅长根据用户输入需求生成 **完整 UI 设计图 JSON**，该 JSON 将用于 **渲染真实 UI 画面**。

# ====== OBJECTIVE / 目标 ======
你的任务是：
1️⃣ 在开始制作 UI JSON 前，通过**选择题**主动向用户确认设计偏好和需求
2️⃣ 根据确认后的信息生成 **完整、规范、可渲染的 JSON UI 设计语言**

# ====== UI JSON 必须遵循的规范 ======
- 输出 strictly 使用 JSON 格式（使用代码块包裹）
- JSON 描述内容为 **一整张 UI 设计图**，不是 Demo，不是代码逻辑
- 组件化设计，支持任意嵌套组件
- 必须包含：位置、尺寸、字体、字号、颜色等精确样式
- 真实数据填充（避免无意义的 “标题”“文字”）
- 支持跨平台（可用于 web / app 渲染）
- 所有组件在设计风格上保持一致
- 支持风格迁移（如可整体配置主题：light/dark）
- 内容默认使用中文（除非用户明确要求英文）
- UI层级明确，使用语义化命名
- 不生成渲染效果图，只生成 UI 设计图数据结构
- 输出内容必须完整可解析，确保 JSON 格式严谨正确
- 不得包含与 UI 无关内容

# ====== INTERACTION RULES / 交互方式 ======
在第1步中，你必须根据用户的需求，主动提问与用户确定设计图细节，且一次性问完，比如：

A. UI 类型（单选）
- A1: App
- A2: Web
- A3: 小程序

B. 主题风格（单选）
- B1: 暖色系
- B2: 冷色系
- B3: 暗黑风格
- B4: 简约白底

C. 页面类型（单选）
- C1: 首页
- C2: 列表页
- C3: 详情页
- C4: 用户页
- C5: 其他（由用户补充）

D. 布局风格（单选）
- D1: 顶部Banner → 内容区 → 底部栏
- D2: Tab切换布局
- D3: 多区块分割网格
- D4: 大图主视觉风格

（上述提问只是参考，你需要针对用户需求，灵活调整提问内容。）
全部确认前，不得输出任何 JSON UI。

# ====== FEW-SHOT / 示例学习 ======
以下为示例 JSON 格式片段，仅作结构对照，不允许直接复用：
```json
{
  "platform": "mobile",
  "theme": "light blue",
  "screen": {
    "width": 375,
    "height": 667,
    "model": "iPhone 16 Pro Max",
  },
  "page": [
    {
      "type": "banner",
      "content": "推荐",
      "children": [
         {
            "type": "banner",
            "content": "商务英语必知必会",
            "style": {
               "width": "100%",
               "height": 180,
            },
            "children": [
               {
                  "type": "button",
                  "content": "开始学习",
                  "props": {
                  },
                  "style": {
                     "width": "40%",
                     "height": 40,
                  }
               }
            ]
         }
      ],
      "style": {
        "width": "100%",
        "height": 180,
      }
    },
    {
      "type": "navigation",
      "style": {
         "height": "10%",
         "padding": "1%",
      },
      "children": [
         {
            "type": "tab",
            "content": "首页",
            "icon": "home",
            "props": {
               "active": true
            },
            "style": {
            }
         },
         {
            "type": "tab",
            "content": "课程",
            "icon": "course",
            "props": {
            },
            "style": {
            }
         },
         {
            "type": "tab",
            "content": "我的",
            "icon": "my",
            "props": {
            },
            "style": {
            }
         }
      ]
    }
  ]
}

# ====== ERROR RULES / 错误处理 ======

若用户输入不全或需求模糊：

* 不要擅自假设
* 主动补齐缺失的选择题并提示用户回复选项

# ====== OUTPUT FORMAT ======

确认完毕后：

* 输出 UI JSON 使用 Markdown 代码块包裹
* 严格遵循 UI JSON 规范
* 输出后附上一行 “如需修改，请告诉我”

# ====== FINAL STEP ======

当用户已确认所有信息后，开始制作 JSON UI 设计图。
如用户未确认，继续提问。
```
# Step3：生成图片
提示词：
```plain text
请按要求制作UI设计图：

{
  "platform": "app",
  "screen": {
    "width": 375,
    "height": 812,
    "model": "iPhone 16 Pro"
  },
  "page": [
    {
      "type": "banner",
      "content": "课程推荐",
      "props": {
        "carousel": true,
        "autoplay": true,
        "interval": 5000
      },
      "children": [
        {
          "type": "bannerItem",
          "content": "商务英语必修课",
          "children": [
            {
              "type": "button",
              "content": "开始学习"
            }
          ]
        },
        {
          "type": "bannerItem",
          "content": "口语提升课程",
          "children": [
            {
              "type": "button",
              "content": "立即体验"
            }
          ]
        }
      ]
    },
    {
      "type": "section",
      "content": "学习进度",
      "children": [
        {
          "type": "circleProgress",
          "value": 0.65,
          "unit": "%",
          "label": "总进度"
        },
        {
          "type": "row",
          "children": [
            {
              "type": "progressItem",
              "label": "今日学习时长",
              "value": "45分钟",
              "icon": "clock"
            },
            {
              "type": "progressItem",
              "label": "已完成课程",
              "value": "8/12",
              "icon": "check"
            },
            {
              "type": "progressItem",
              "label": "等级",
              "value": "Lv.3",
              "icon": "star"
            }
          ]
        }
      ]
    },
    {
      "type": "section",
      "content": "口语课程列表",
      "children": [
        {
          "type": "courseCard",
          "title": "日常口语入门",
          "difficulty": "初级",
          "duration": "30分钟",
          "rating": 4.5,
          "image": "https://example.com/course1.jpg"
        },
        {
          "type": "courseCard",
          "title": "商务场景口语",
          "difficulty": "中级",
          "duration": "45分钟",
          "rating": 4.8,
          "image": "https://example.com/course2.jpg"
        },
        {
          "type": "courseCard",
          "title": "旅游口语速成",
          "difficulty": "初级",
          "duration": "25分钟",
          "rating": 4.3,
          "image": "https://example.com/course3.jpg"
        }
      ]
    },
    {
      "type": "navigation",
      "children": [
        {
          "type": "tab",
          "content": "首页",
          "icon": "home",
          "props": {
            "active": true
          }
        },
        {
          "type": "tab",
          "content": "课程",
          "icon": "course",
          "props": {
            "active": false
          }
        },
        {
          "type": "tab",
          "content": "我的",
          "icon": "user",
          "props": {
            "active": false
          }
        }
      ]
    }
  ]
}
```
# 风格迁移
在保证**内容不变**的情况下，我们可以轻松使用JSON 来制作出不同风格的图片。
提示词：
```plain text
按照要求生成系统架构图片：
{
  "entities": [
    {"id": "web_user", "name": "网页端用户", "type": "user", "layer": "presentation"},
    {"id": "app_user", "name": "移动端 App 用户", "type": "user", "layer": "presentation"},
    {"id": "external_partner", "name": "外部合作伙伴 API", "type": "external_api", "layer": "presentation"},
    {"id": "load_balancer", "name": "负载均衡器 (Nginx/SLB)", "type": "component", "layer": "infrastructure"},
    {"id": "api_gateway", "name": "API 网关 (Spring Cloud Gateway)", "type": "component", "layer": "infrastructure"},
    {"id": "user_service", "name": "用户中心微服务", "type": "service", "layer": "domain"},
    {"id": "product_service", "name": "商品中心微服务", "type": "service", "layer": "domain"},
    {"id": "order_service", "name": "订单中心微服务", "type": "service", "layer": "domain"},
    {"id": "cart_service", "name": "购物车微服务", "type": "service", "layer": "domain"},
    {"id": "search_service", "name": "搜索微服务", "type": "service", "layer": "domain"},
    {"id": "payment_service", "name": "支付聚合微服务", "type": "service", "layer": "domain"},
    {"id": "message_queue", "name": "Kafka 消息中间件 (事件驱动)", "type": "message_queue", "layer": "infrastructure"},
    {"id": "main_db", "name": "MySQL 数据库集群 (主从架构)", "type": "db", "layer": "data"},
    {"id": "redis_cache", "name": "Redis 缓存集群 (高可用)", "type": "cache", "layer": "data"},
    {"id": "es_engine", "name": "Elasticsearch 搜索引擎", "type": "component", "layer": "data"},
    {"id": "payment_provider", "name": "第三方支付通道 (支付宝/微信/Stripe)", "type": "external_api", "layer": "external"}
  ],
  "relationships": [
    {"from": "web_user", "to": "load_balancer", "relation_type": "calls", "protocol": "https"},
    {"from": "app_user", "to": "load_balancer", "relation_type": "calls", "protocol": "https"},
    {"from": "external_partner", "to": "load_balancer", "relation_type": "calls", "protocol": "https"},
    {"from": "load_balancer", "to": "api_gateway", "relation_type": "calls", "protocol": "http"},
    {"from": "api_gateway", "to": "user_service", "relation_type": "calls", "protocol": "grpc"},
    {"from": "api_gateway", "to": "product_service", "relation_type": "calls", "protocol": "grpc"},
    {"from": "api_gateway", "to": "order_service", "relation_type": "calls", "protocol": "grpc"},
    {"from": "api_gateway", "to": "cart_service", "relation_type": "calls", "protocol": "grpc"},
    {"from": "api_gateway", "to": "search_service", "relation_type": "calls", "protocol": "grpc"},
    {"from": "user_service", "to": "main_db", "relation_type": "writes_to", "protocol": "mysql"},
    {"from": "product_service", "to": "redis_cache", "relation_type": "reads_from", "protocol": "redis"},
    {"from": "order_service", "to": "payment_service", "relation_type": "calls", "protocol": "grpc"},
    {"from": "order_service", "to": "message_queue", "relation_type": "publishes_to", "protocol": "event"},
    {"from": "payment_service", "to": "payment_provider", "relation_type": "calls", "protocol": "http/rest"},
    {"from": "search_service", "to": "es_engine", "relation_type": "reads_from", "protocol": "internal"},
    {"from": "message_queue", "to": "search_service", "relation_type": "subscribes", "protocol": "kafka"},
    {"from": "product_service", "to": "main_db", "relation_type": "reads_from", "protocol": "mysql"}
  ],
  "layers": [
    {
      "name": "展示层 (Presentation Layer)",
      "entities": ["web_user", "app_user", "external_partner"]
    },
    {
      "name": "基础设施层 (Infrastructure Layer)",
      "entities": ["load_balancer", "api_gateway", "message_queue"]
    },
    {
      "name": "业务领域层 (Domain Layer)",
      "entities": ["user_service", "product_service", "order_service", "cart_service", "search_service", "payment_service"]
    },
    {
      "name": "数据持久层 (Data Layer)",
      "entities": ["main_db", "redis_cache", "es_engine"]
    },
    {
      "name": "外部系统 (External Systems)",
      "entities": ["payment_provider"]
    }
  ]
}
```
# 复刻 APP
首页提示词，+ 淘宝app的截图：
```plain text
按照要求制作UI设计图，鳕小堡是一个虚拟IP，是我提供的图片这样。

{
  "page_name": "鳕小堡商城-首页",
  "style": "淘宝App风格 (紧凑/瀑布流)",
  "theme_color": "#FF5000 (淘宝橙)",
  "layout": {
    "header": {
      "search_bar": {
        "left_icon": "扫一扫",
        "placeholder": "输入关键词搜索鳕小堡周边",
        "right_icons": ["拍照识别", "搜索按钮"]
      },
      "tabs": ["关注", "推荐", "上新", "柴犬社群", "福利周"]
    },
    "grid_nav": [
      {"icon": "88VIP", "label": "会员中心"},
      {"icon": "天猫超市", "label": "柴柴超市"},
      {"icon": "领淘金币", "label": "赚金币"},
      {"icon": "芭芭农场", "label": "柴柴农场"},
      {"icon": "红包签到", "label": "每日红包"}
    ],
    "promotion_zones": [
      {
        "title": "鳕小堡直播",
        "subtitle": "正在直播中",
        "product_image": "shiba_plush_toy.png",
        "price": "¥99"
      },
      {
        "title": "百亿补贴",
        "subtitle": "官方正品",
        "product_image": "shiba_hoodie.png",
        "price": "¥159"
      }
    ],
    "atmosphere_banner": {
      "text": "超级立减 | 鳕小堡粉丝惊喜消费券限时可用",
      "action": "立即领券"
    },
    "main_content": {
      "type": "Waterfall (瀑布流)",
      "columns": 2,
      "items": [
        {
          "image": "shiba_jacket_1.png",
          "title": "鳕小堡原创 | 日系工装柴犬刺绣夹克",
          "tags": ["新品", "热卖"],
          "price": "¥269",
          "sales": "月销500+"
        },
        {
          "image": "shiba_mug.png",
          "title": "鳕小堡陶瓷马克杯 办公室可爱水杯",
          "tags": ["包邮"],
          "price": "¥45",
          "sales": "1.2万人已买"
        }
      ]
    },
    "bottom_nav": ["首页", "逛逛", "消息", "购物车", "我的"]
  }
}
```
商品详情页JSON：
```plain text
制作这个app的另一个界面，确保与之前的页面风格保持一致，尺寸保持一致，设计保持一致：

{
  "page_name": "商品详情-鳕小堡原创外套",
  "screen_dimensions": { "width": 393, "height": 852 },
  "style_reference": "淘宝高密度详情页",
  "ui_components": {
    "top_nav": { "left": "Back", "right": ["Share", "Cart", "More"] },
    "image_gallery": { "current": 1, "total": 5, "image": "鳕小堡日系外套主图" },
    "price_section": {
      "bg_color": "#FF4400",
      "main_price": "¥115",
      "original_price": "¥128",
      "promo_tag": "满800减65",
      "status": "超级立减·新年焕新"
    },
    "product_title": {
      "brand": "IFASHION",
      "text": "鳕小堡自制 秋季日系纯色百搭教练夹克男女款休闲工装外套",
      "tags": ["退货宝", "迪木尔风", "热度+177%"]
    },
    "service_panel": {
      "rows": [
        { "label": "发货", "content": "48小时内发货 · 四川成都 · 快递: 免运费" },
        { "label": "保障", "content": "退货宝 · 7天无理由退货 · 极速退款" },
        { "label": "参数", "content": "男女通用 · 秋季 · 宽松型" }
      ]
    },
    "evaluation_preview": {
      "title": "评价 (15)",
      "photos": ["买家秀1", "买家秀2", "买家秀3", "买家秀4"]
    },
    "footer_actions": {
      "icons": ["店铺", "客服", "收藏"],
      "buttons": [
        { "label": "加入购物车", "color": "#FFBB00" },
        { "label": "领券购买", "color": "#FF5000" }
      ]
    }
  }
}
```
购物车JSON：
```plain text
制作这个app的另一个界面，确保与之前的页面风格保持一致，尺寸保持一致，设计保持一致：
{
  "page_name": "购物车",
  "screen_dimensions": { "width": 393, "height": 852 },
  "style_reference": "淘宝结算页面",
  "ui_components": {
    "header": { "title": "购物车 (186)", "action": "管理" },
    "promo_tip": "您有满800减65元惊喜消费券待使用",
    "shop_group": {
      "shop_name": "鳕小堡 Banish 原放空 >",
      "coupon_get": "领券",
      "items": [
        {
          "selected": true,
          "image": "藏蓝色教练夹克",
          "title": "新年焕新 日系宽松休闲百搭教练外套",
          "sku": "藏蓝色; XL",
          "tags": ["消费券", "退货宝", "7天无理由"],
          "price": "115",
          "old_price": "128",
          "discount_info": "比加入时降¥9",
          "quantity": 1
        },
        {
          "selected": false,
          "image": "条纹刺绣衬衫",
          "title": "新年焕新 原创条纹刺绣泡泡纱衬衫",
          "sku": "米色; XL",
          "price": "97",
          "quantity": 1
        }
      ]
    },
    "checkout_bar": {
      "select_all": true,
      "total_label": "合计:",
      "amount": "¥0",
      "button": "结算",
      "button_color": "#FF5000"
    },
    "bottom_tab_bar": ["首页", "逛逛", "消息(82)", "购物车", "我的淘宝"]
  }
}
```
# 跳过 Agent 直接生成
如果你觉得元提示词太麻烦，你也可以直接一步到位，以生成一个年度报告：
```plain text
生成一个JSON格式描述的 个人代码年度总结报告，JSON需要结构化的描述报告内容，要求包括以下内容：
1. 名字、头像
2. 年度活跃图。类似github的活跃图那样
3. 提交数量、代码行数等细节
4. 合作伙伴
其他内容帮忙补充一下
```
这样你就可以得到一个完整的 JSON 了，直接绕过 Agent 构建。
提示词：
```plain text
生成一个极简风格的个人编码年度报告汇总图片：

{
  "user_profile": {
    "name": "鳕小堡",
    "avatar_url": "https://example.com/avatar.jpg",
    "bio": "热爱编程，喜欢探索新技术和开源项目。",
    "organization": "宇宙条研发团队",
    "position": "后端架构工程师",
    "location": "新加坡"
  },
  "year_summary": {
    "year": 2025,
    "total_commits": 1520,
    "total_prs": 320,
    "total_issues": 85,
    "total_lines_added": 45230,
    "total_lines_deleted": 12340,
    "projects_contributed": 18,
    "languages": [
      {"language": "Python", "percentage": 45, "trend": "↑"},
      {"language": "JavaScript", "percentage": 30, "trend": "→"},
      {"language": "Go", "percentage": 15, "trend": "↑"},
      {"language": "Other", "percentage": 10, "trend": "↓"}
    ],
    "commit_activity": [
      0, 1, 2, 0, 3, 5, 0, 0, 4, 2, 3, 1, 0, 5, 6, 2, 3, 0, 1, 4, 2, 3, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 0, 4, 5, 2, 3, 1, 0, 2, 3, 4, 0, 1, 2, 3, 5, 2, 1, 0, 3, 4, 2, 0, 1, 3, 2, 0, 1, 4, 5, 2, 3, 1, 0
    ],
    "hot_projects": [
      {
        "name": "GenLingua",
        "description": "英语学习 App，负责后端推荐系统与数据处理",
        "commits": 420,
        "lines_added": 12500,
        "lines_deleted": 3400,
        "role": "Backend Architect",
        "main_features": ["推荐系统优化", "数据管道搭建", "API性能优化"],
        "team_size": 5
      },
      {
        "name": "NanoBananaPro",
        "description": "AI 绘图工具，优化批量出图流程",
        "commits": 280,
        "lines_added": 8500,
        "lines_deleted": 2100,
        "role": "Core Contributor",
        "main_features": ["批量出图", "提示词解析", "性能优化"],
        "team_size": 3
      }
    ],
    "top_collaborators": [
      {
        "name": "Alice Zhang",
        "avatar_url": "https://example.com/alice.jpg",
        "projects_together": ["GenLingua", "NanoBananaPro"],
        "interaction_count": 125
      },
      {
        "name": "Bob Li",
        "avatar_url": "https://example.com/bob.jpg",
        "projects_together": ["GenLingua"],
        "interaction_count": 78
      }
    ],
    "contribution_types": {
      "feature": 60,
      "bugfix": 25,
      "documentation": 10,
      "refactor": 5,
      "code_review": 15,
      "ci_cd": 5
    },
    "skills_growth": [
      "掌握Go语言微服务架构",
      "学习Kubernetes与容器化部署",
      "深入了解推荐系统算法优化",
      "熟悉AI图像生成管线设计"
    ],
    "achievements": [
      "GenLingua项目上线用户量突破10万",
      "NanoBananaPro支持批量高效出图，提升用户效率50%",
      "开源贡献合计超过100个PR",
      "团队内部举办技术分享5次"
    ],
    "most_active_months": ["March", "June", "October"],
    "personal_notes": "今年主要专注于推荐系统和AI工具开发，同时尝试优化团队协作流程。计划明年增加跨语言项目贡献，并探索更多开源合作。"
  },
  "visualization": {
    "commit_heatmap": {
      "type": "calendar",
      "data_source": "commit_activity",
      "color_scheme": "green",
      "description": "每一天的提交数量可视化，越深绿色表示提交越多"
    },
    "language_pie_chart": {
      "type": "pie",
      "data_source": "languages",
      "description": "代码语言分布饼图"
    },
    "project_bar_chart": {
      "type": "bar",
      "data_source": "hot_projects",
      "metric": "commits",
      "description": "主要项目提交数量柱状图"
    },
    "contribution_type_chart": {
      "type": "donut",
      "data_source": "contribution_types",
      "description": "不同类型贡献占比环形图"
    }
  }
}
```
