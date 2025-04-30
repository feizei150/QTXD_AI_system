<<<<<<< HEAD
@@ -0,0 +1,120 @@
 # 🤖 QTXD_AI 自动化智能体系
 
 一个集 **副业任务爬取 + 热榜内容采集 + Notion 写入 + 本地模型总结 + 剪映视频生成** 于一体的个人 AI 自动化项目系统。
 
 ---
 
 ## 📁 项目结构
 
 QTXD_AI/ 
 ├── QTXD_spider_tasks/ # 热榜爬虫模块（知乎/B站/微博等） 
 ├── QTXD_notion_tasks/ # Notion 数据写入模块
 ├── QTXD_video_automation/ # 剪映脚本生成 + 视频组合（开发中）
 ├── QTXD_finance_tracking/ # 财务记录与统计模块 
 ├── config/ # 配置（如 Notion Token、数据库 ID） 
 ├── utils/ # 公共函数工具包 
 ├── scripts/ # 主脚本运行入口集合 
 ├── requirements.txt # 所有依赖包 
 ├── run_all_spiders_to_notion.py # 
 ⏱ 一键运行主控脚本
 
 ---
 
 ## ⚙️ 功能模块说明
 
 ### 🔍 1. 爬虫模块（QTXD_spider_tasks）
 - 支持平台：知乎、微博、B站、抖音、小红书、公众号 等
 - 抓取标题 / 发布时间 / 热度 / 链接
 - 自动写入 Notion 内容采集库
 
 ### 🧠 2. 本地模型 + 摘要生成
 - 使用 [Ollama](https://ollama.com) 本地部署模型（支持 deepseek-r1、LLaMA3）
 - 自动总结内容文本
 - 支持强制刷新模式 + 日志记录
 
 ### 🧾 3. Notion 数据写入模块（QTXD_notion_tasks）
 - 内容采集库 / 学习笔记库 / 副业任务库 自动写入
 - 自动标记是否处理
 - 字段支持智能匹配
 
 ### 🎬 4. 剪映视频模块（QTXD_video_automation）
 - 从爬虫内容自动生成视频脚本
 - 剪映专业版导入：封面+旁白+字幕+片尾
 - 后续支持：视频发布（西瓜/B站/抖音国际）
 
 ### 💰 5. 财务记录模块（QTXD_finance_tracking）
 - 自动记录：订阅、域名、服务器、AI模型等费用
 - 输出：Notion 财务库 + Obsidian 归档
 ## 🚀 快速开始使用
 
 ### ✅ 创建虚拟环境并安装依赖
 ```bash
 cd QTXD_AI
 python -m venv venv
 venv\Scripts\activate
 pip install -r requirements.txt
 
 ### ✅ 运行主控脚本
 python run_all_spiders_to_notion.py
 ## 🔄 自动化任务流（GitHub Actions + 本地）
 
 ### 🕒 GitHub Actions（远程计划任务）
 
 - 自动每日运行爬虫任务脚本
     
 - 自动更新 Notion 内容
     
 - Workflow 位于：`.github/workflows/daily_task.yml`
 
 
 
 🖥️ 本地运行同步脚本（推荐）
 @echo off
 cd /d F:\QTXD_AI_system\QTXD_AI
 call venv\Scripts\activate
 git pull origin main
 python run_all_spiders_to_notion.py
 pause
 ## 🧠 开发计划 & 状态
 
 |模块|状态|说明|
 |---|---|---|
 |🔍 爬虫平台整合|✅ 已完成|知乎、微博、B站 等平台|
 |✍️ Notion 自动写入|✅ 已完成|内容、任务、学习、财务|
 |🤖 本地模型总结|✅ 已完成|Deepseek-R1|
 |🎬 视频自动化剪辑|⏳ 开发中|剪映脚本生成中|
 |🔁 GitHub Actions|✅ 已完成|日常任务自动执行|
 |💹 财务记录模块|✅ 已完成|支出与盈利记录|
 |🔄 Obsidian 同步|⏳ 规划中|构建知识闭环系统|
 ## 📌 技术栈 & 依赖
 
 - Python 3.10+
     
 - Notion API SDK
     
 - Ollama 本地模型：Deepseek / LLaMA3
     
 - GitHub Actions
     
 - 剪映专业版（脚本对接）
     
 - requests / schedule / tqdm / rich
 ## 📚 联系作者
 
 - 📘 Obsidian + Notion 全局整合中
     
 - 💻 GitHub: [feizei150](https://github.com/feizei150)
     
 - 🌐 网站主页：正在搭建中...
 
 ---
 
 ## ✅ 最后一步：保存并上传到 GitHub
 
 打开终端：
 
 ```bash
 cd F:\QTXD_AI_system\QTXD_AI
 git add README.md
 git commit -m "修复 README.md 显示格式，优化模块说明"
 git push origin main
=======
from datetime import datetime

# 获取当前时间戳，格式为：2025-04-23 23:59
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# 生成新的 README.md 内容（包含时间戳）
readme_content = f"""# QTXD_AI · 自动化创富系统 🧠💸
> 专为内容创作者、副业工程师设计的全自动赚钱系统！

![language](https://img.shields.io/github/languages/top/feizei150/QTXD_AI)
![last-commit](https://img.shields.io/github/last-commit/feizei150/QTXD_AI)
![repo-size](https://img.shields.io/github/repo-size/feizei150/QTXD_AI)
![license](https://img.shields.io/github/license/feizei150/QTXD_AI)

---

## 🧠 理念：一个人 ≈ 一家公司 💼

本项目旨在帮助“一个人打造自己的 AI 业务体”，用极低的成本实现：
- 多平台内容采集
- 智能脚本生成
- 自动视频发布
- 任务接单与财务结算
- 项目闭环与版本归档
- 本地知识管理与同步采用 Obsidian 构建每日学习日志与 AI 知识地图

你 ≠ 打工人，而是 CEO！本系统就是你的小型自动赚钱公司。

---

## 📦 项目模块导航

| 模块名 | 功能说明 |
|--------|----------|
| 🔍 QTXD_spider_tasks_v2 | 多平台热榜内容采集（知乎 / 小红书 / B站 / 微博） |
| 🧠 QTXD_notion_tasks_v2 | Notion写入 + ChatGPT 日志同步 |
| 🎬 QTXD_video_automation_v2 | 视频脚本生成 + 剪映剪辑发布 |
| 💰 QTXD_finance_tracking | 记账、月支出、财务统计 |
| 📒 QTXD_notion_tasks | Obsidian 日志自动同步 + ChatGPT 对话导出 |
| 💼 QTXD_task_fetcher_v2 | 抓取副业悬赏任务，自动写入 Notion，支持筛选提醒 |

---

## 🧰 技术栈

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=fff)
![Notion API](https://img.shields.io/badge/-Notion-000?logo=notion&logoColor=fff)
![GitHub Actions](https://img.shields.io/badge/-GitHub%20Actions-2088FF?logo=github-actions&logoColor=fff)
![Ollama](https://img.shields.io/badge/-Ollama-green)
![Obsidian](https://img.shields.io/badge/-Obsidian-4B4BFF?logo=obsidian&logoColor=white)
![Scrapy](https://img.shields.io/badge/-Scrapy-88C400?logo=scrapy&logoColor=fff)

---

## 🚀 快速开始

```bash
cd QTXD_xxx_v2
python -m venv venv
activate_venv.bat
pip install -r requirements.txt
>>>>>>> a8729df2013575852f5a8924db9c8a2411d30bac
