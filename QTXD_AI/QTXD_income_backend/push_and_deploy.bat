@echo off
echo 🚀 正在推送代码到 GitHub...
git add .
git commit -m "自动上传更新"
git push origin main

echo.
echo 🌐 正在连接服务器并部署...
ssh ubuntu@110.42.248.51 "bash ~/QTXD_income_backend/deploy_backend.sh"

echo.
echo ✅ 部署完成！网页端访问测试：https://qingtianxiaodou.com/run-income-task
pause
