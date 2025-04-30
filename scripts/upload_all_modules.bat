# Let's generate the batch script content and scheduler directory structure for the user.

import os

# Define the paths for the batch script and scheduler directory structure
batch_script_path = r"F:\QTXD_AI_system\upload_all_modules.bat"
scheduler_directory = r"F:\QTXD_AI_system\QTXD_scheduler"

# Create the batch script content
batch_script_content = """
@echo off
echo 🔼 开始上传所有模块...

cd QTXD_AI
git add .
git commit -m "🔁 更新 QTXD_AI 模块"
git push origin main
cd ..

cd QTXD_WebPlatform
git add .
git commit -m "🔁 更新 QTXD_WebPlatform 模块"
git push origin main
cd ..

cd QTXD_Freelance
git add .
git commit -m "🔁 更新 QTXD_Freelance 模块"
git push origin main
cd ..

cd QTXD_AI_obsidian
git add .
git commit -m "🔁 更新 QTXD_AI_obsidian 模块"
git push origin main
cd ..

cd QTXD_PartySummarizer
git add .
git commit -m "🔁 更新 QTXD_PartySummarizer 模块"
git push origin main
cd ..

echo ✅ 所有模块已上传完毕！
pause
"""

# Create the scheduler directory structure
os.makedirs(scheduler_directory, exist_ok=True)

# Save the batch script to a file
with open(batch_script_path, "w", encoding="utf-8") as batch_file:
    batch_file.write(batch_script_content)

# Output paths for the user to check
batch_script_path, scheduler_directory
