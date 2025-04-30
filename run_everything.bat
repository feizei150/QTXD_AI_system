@echo off
cd /d %~dp0
echo ========================
echo 🚀 启动：擎天AI自动执行系统
echo ========================

:: 激活虚拟环境（如果你是放在 venv 目录）
call venv\Scripts\activate.bat

:: 启动 知乎热榜爬虫
echo ✅ 正在运行：知乎热榜爬虫 ...
python QTXD_AI\spider_zhihu.py

:: 启动 自动内容总结器
echo ✅ 正在运行：内容总结模块 ...
python QTXD_AI\summarizer.py

:: 启动 Notion 写入模块
echo ✅ 正在运行：Notion 同步 ...
python QTXD_AI\notion_writer.py

:: 可扩展任务（抖音、小红书等）
:: python QTXD_AI\spider_xiaohongshu.py
:: python QTXD_AI\summarizer.py --platform xiaohongshu

:: 可扩展视频脚本生成
:: python QTXD_video_automation\generate_video_script.py

echo ========================
echo ✅ 所有任务执行完毕
echo ========================
pause
