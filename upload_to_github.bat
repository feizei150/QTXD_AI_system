@echo off
REM 一键上传到GitHub

REM 进入项目目录
cd /d E:\QTXD_AI_SYSTEM

REM 拉取最新的GitHub内容
git pull --rebase

REM 添加所有变动的文件
git add .

REM 提交到本地仓库
git commit -m "自动提交更新"

REM 推送到GitHub远程仓库
git push origin main

REM 完成
echo 更新已成功提交到 GitHub！
pause
