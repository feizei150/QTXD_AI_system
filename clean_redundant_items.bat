@echo off
echo 🔍 正在清理冗余文件...

:: 删除根目录无用文件
del /f /q "E:\QTXD_AI_system\daima.txt"
del /f /q "E:\QTXD_AI_system\.gitignore"
del /f /q "E:\QTXD_AI_system\notion_writer.py"
del /f /q "E:\QTXD_AI_system\chatgpt_interaction.py"

:: 删除 QTXD_AI 中的无用内容
del /f /q "E:\QTXD_AI_system\QTXD_AI\README.md.md"
del /f /q "E:\QTXD_AI_system\QTXD_AI\notion_log.txt"
del /f /q "E:\QTXD_AI_system\QTXD_AI\pull_from_github.bat"
del /f /q "E:\QTXD_AI_system\QTXD_AI\upload_to_github.bat"
del /f /q "E:\QTXD_AI_system\QTXD_AI\upload_to_ssh.bat"

:: 删除 QTXD_income_backend 中已转移的脚本
del /f /q "E:\QTXD_AI_system\QTXD_income_backend\push_and_deploy.bat"
del /f /q "E:\QTXD_AI_system\QTXD_income_backend\push_to_github_and_deploy.bat"
del /f /q "E:\QTXD_AI_system\QTXD_income_backend\deploy_backend.sh"

echo ✅ 清理完成！请检查是否一切正常。
pause
