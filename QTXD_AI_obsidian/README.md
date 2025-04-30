# 将美化后的 README 写入到主仓库中的 README.md 文件
readme_content = """
# 💼 QTXD_AI_system · 擎天AI自动化主系统

🚀 **QTXD_AI_system** 是一个“一个人 = 一家公司”理念打造的 AI 自动化系统主仓库。通过整合多种智能技术，提供副业赚钱、内容处理、自动总结、视频生成、平台部署等多个模块，旨在以低成本高效实现 **自动赚钱 + 智能任务分发 + AI文档处理** 的闭环生态。

> **目标：** 通过自动化与人工智能的结合，帮助用户实现轻松赚钱、提高工作效率、节省时间。

---

## 🧩 系统组成模块

| 模块名 | 功能说明 |
|--------|----------|
| **`QTXD_AI`** | 主控中心，整体入口，集成启动脚本与部署配置 |
| **`QTXD_income_backend`** | 自动赚钱系统，集成热榜爬虫、内容总结与 Notion 写入 |
| **`QTXD_notions_tasks`** | Notion 任务管理与自动同步模块 |
| **`QTXD_spider_tasks`** | 多平台爬虫任务（知乎、小红书、微博等） |
| **`QTXD_task_fetcher`** | 任务平台抓取与筛选器，专注副业任务 |
| **`QTXD_video_automation`** | 视频生成与剪辑模块，支持 CapCut 脚本化 |
| **`QTXD_scheduler`** | 任务调度模块，结合定时任务自动化 |
| **`QTXD_WebPlatform`** | Web 展示平台，集成各模块界面入口 |
| **`QTXD_AI_obsidian`** | ChatGPT 与 Obsidian + Notion 写入闭环系统 |

---

## 🔁 写入闭环系统（知识记录系统）

### 💡 **系统实现**：
- **ChatGPT** 生成对话内容与数据 → **Obsidian** 本地记录与结构化 → **Notion** 云端复盘与管理
- 实现 **知识闭环**，记录每日任务、学习、聊天内容，便于后期分析和复盘。

> 通过 `sync_chatgpt_to_obsidian.py` 自动将每日对话内容同步至本地 Obsidian 知识库，
> 然后同步到 Notion 进行云端管理，形成完整的 AI 写入-记录-复盘闭环。

---

## 🗂️ 项目目录结构（核心）

QTXD_AI_system/ 
├── QTXD_AI/ # 主控目录，入口启动器
├── QTXD_income_backend/ # 自动赚钱系统
├── QTXD_notions_tasks/ # Notion 自动任务处理
├── QTXD_spider_tasks/ # 多平台爬虫合集
├── QTXD_task_fetcher/ # 任务信息抓取与筛选
├── QTXD_video_automation/ # 视频生成脚本模块
├── QTXD_scheduler/ # 任务调度模块 
├── QTXD_WebPlatform/ # 网站前端集成页面
├── QTXD_AI_obsidian/ # Obsidian 写入模块
├── scripts/ # 通用脚本工具 
└── config/ # 通用配置文件（如 settings.py、requirements.txt）

---

## ⚙️ 快速使用指南

### 1. 安装依赖
##### bash
##### pip install-r requirements,txt
### 2. 启动主系统

 ##### cd QTXD_AI
###### python app.py
### 3. 使用一键上传脚本（可选）
##### ./scripts/upload_to_github.bat
## ✅ 当前进度与目标

-  **整理主仓目录结构**：规范化文件与模块
    
-  **拆分模块化仓库与文件**：实现高内聚低耦合的系统结构
    
-  **打通 GitHub 自动上传 & Notion 写入**：提升任务效率与管理
    
-  **构建 AI 内容写入闭环系统**
    
-  **接入任务收益统计与财务分析**：实现智能财务功能
    
-  **接入图形 Web 操作界面**：完善用户体验与控制

## 🧠 未来方向

- **添加 AI 记账与账单识别**：实现财务自动化和分析
    
- **打通闲鱼“砍一刀”+二手倒卖系统**：提升副业盈利能力
    
- **构建数据分析助理（QTXD_DataAssistant）**：全面支持数据分析
    
- **构建副业导航页，开放用户定制页面**：用户自定义平台界面与功能

## 📂 相关仓库链接

|仓库|地址|
|---|---|
|**主仓库**|QTXD_AI_system|
|**党建助手**|QTXD_PartySummarizer|
|**Notion任务**|QTXD_notion_tasks|
|**收益后台**|QTXD_income_backend|
|**Obsidian写入**|QTXD_AI_Obsidian|
## 👨‍💻 作者

**擎天小豆**（feizei150）｜用 AI 打造属于自己的副业系统，助力自动化创业