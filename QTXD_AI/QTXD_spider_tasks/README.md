# QTXD_spider_tasks_v2

该模块用于抓取知乎、微博、抖音、小红书等平台的热榜内容，并自动写入 Notion 内容采集库中。

## 功能包含
- 多平台内容抓取
- 自动写入 Notion
- 可配置的定时任务执行

## 使用方法
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动虚拟环境（Windows）：
   ```bash
   .\activate_venv.bat
   ```

3. 运行脚本：
   ```bash
   python run_all_spiders_to_notion.py
   ```
