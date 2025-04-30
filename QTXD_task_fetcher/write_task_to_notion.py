from datetime import datetime
import os

# Notion API client
from notion_client import Client

# Notion API token
notion = Client(auth="your_notion_token")
notion_database_id = "your_notion_database_id"

# Obsidian directory
obsidian_directory = "E:\\QTXD_AI_system\\QTXD_AI\\Obsidian\\学习笔记"

def write_to_notion(question, answer):
    today = datetime.now().strftime("%Y-%m-%d")
    # Create a page in Notion
    notion.pages.create(
        parent={"database_id": notion_database_id},
        properties={
            "标题": {"title": [{"text": {"content": question}}]},
            "内容": {"rich_text": [{"text": {"content": answer}}]},
            "日期": {"rich_text": [{"text": {"content": today}}]},
            "标签": {"multi_select": [{"name": "ChatGPT"}]}
        }
    )

def write_to_obsidian(question, answer):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"ChatGPT_对话记录_{today}.md"
    filepath = os.path.join(obsidian_directory, filename)
    # Create a markdown file in Obsidian
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(f"# {today} ChatGPT 对话记录\n\n")
        file.write(f"**问题：** {question}\n\n")
        file.write(f"**回答：**\n{answer}\n")
        file.write("\n**标签：**\n- ChatGPT\n- 学习\n")

# Example usage
question = "什么是机器学习？"
answer = "机器学习是人工智能的一个分支，专注于通过数据分析让机器自动学习并做出预测或决策。"

write_to_notion(question, answer)
write_to_obsidian(question, answer)
