from datetime import datetime
from notion_client import Client
import os

# 初始化 Notion 客户端
notion = Client(auth="your_notion_token")
notion_database_id = "your_notion_database_id"

# Obsidian 目录
obsidian_directory = "E:\\QTXD_AI_system\\QTXD_AI\\Obsidian\\学习笔记"

# 创建 Notion 页面的函数
def write_to_notion(question, answer):
    today = datetime.now().strftime("%Y-%m-%d")
    # 创建 Notion 页
    notion.pages.create(
        parent={"database_id": notion_database_id},
        properties={
            "标题": {"title": [{"text": {"content": question}}]},
            "内容": {"rich_text": [{"text": {"content": answer}}]},
            "日期": {"rich_text": [{"text": {"content": today}}]},
            "标签": {"multi_select": [{"name": "ChatGPT"}]}
        }
    )

    print(f"成功写入 Notion：{question}")

# 创建 Obsidian 文件的函数
def write_to_obsidian(question, answer):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"ChatGPT_对话记录_{today}.md"
    filepath = os.path.join(obsidian_directory, filename)

    # 创建 Obsidian 文件
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"## {today} ChatGPT 对话记录\n\n")
        file.write(f"### 问题：\n{question}\n\n")
        file.write(f"### 回答：\n{answer}\n\n")
        file.write(f"\n\n**标签：** ChatGPT\n- 学习\n")

    print(f"成功写入 Obsidian：{question}")

# 示例使用
question = "什么是机器学习?"
answer = "机器学习是人工智能的一个分支，专注于通过数据分析让机器学习并做出预测或决策。"
write_to_notion(question, answer)
write_to_obsidian(question, answer)
