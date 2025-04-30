@echo off
REM 一键上传到SSH服务器

REM 进入项目目录
cd /d E:\QTXD_AI_SYSTEM

REM 拉取最新的GitHub内容
git pull --rebase

REM 添加所有变动的文件
git add .

REM 提交到本地仓库
git commit -m "自动提交更新"

REM 推送到远程SSH服务器
scp -r * user@your_ssh_server:/path/to/remote/folder/

REM 完成
echo 上传已成功！
pause
