@echo off
cd /d %~dp0
git add .
git commit -m "📦 自动上传：更新所有模块和脚本"
git push origin main
pause
