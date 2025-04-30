# QTXD_notion_tasks_v2

该模块负责将 AI 内容、对话日志、学习记录等写入 Notion 的多个数据库中，支持自动分类与字段匹配。

## 功能包含
- ChatGPT 对话写入 Notion 日志库
- 学习笔记结构化同步
- 支持多个数据库（任务库、日志库、内容库）

## 使用方法
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动虚拟环境：
   ```bash
   .\activate_venv.bat
   ```

3. 运行脚本：
   ```bash
   python chatgpt_to_notion.py
   ```
