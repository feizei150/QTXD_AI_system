import os
from datetime import datetime

# 设置Obsidian文件的保存目录
obsidian_directory = "E:\\QTXD_AI_system\\QTXD_AI\\Obsidian\\学习笔记"

# 获取今天的日期
today = datetime.now().strftime("%Y-%m-%d")
filename = f"ChatGPT对话记录_{today}.md"
filepath = os.path.join(obsidian_directory, filename)

# 确保文件夹存在
if not os.path.exists(obsidian_directory):
    os.makedirs(obsidian_directory)

# 确保你在调用这个函数时传递了正确的question和answer参数
def write_chatgpt_to_obsidian(question, answer):
    # 创建文件并写入内容
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"### {today} ChatGPT 对话记录\n\n")
        file.write(f"**问题**: {question}\n\n")
        file.write(f"**回答**: {answer}\n\n")
        file.write(f"**标签**: **ChatGPT** - 学习\n")

# 你应该在调用这个函数时传递 question 和 answer
