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
