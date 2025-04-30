@echo off
title 🚀 一键上传并部署 QTXD_income_backend
echo ========================================
echo 🔄 正在提交更新并推送到 GitHub...
echo ========================================
git add .
git commit -m "🧠 本地更新：自动上传并触发部署"
git push origin main

echo.
echo ========================================
echo 🌐 正在连接远程服务器部署 Flask 系统...
echo ========================================
ssh ubuntu@110.42.248.51 "bash ~/QTXD_income_backend/deploy_backend.sh"

echo.
echo ✅ 自动上传 + 部署完成！可访问：https://qingtianxiaodou.com/run-income-task
pause
