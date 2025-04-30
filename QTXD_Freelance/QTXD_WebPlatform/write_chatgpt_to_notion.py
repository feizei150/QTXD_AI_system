from notion_client import Client
import os
from datetime import datetime

# 获取Notion的API Token和数据库ID
notion = Client(auth=os.getenv('NOTION_TOKEN'))
notion_database_id = "1d3e27577ab880e89986c7efefb6aa45"

# 将ChatGPT记录写入Notion
def write_chatgpt_to_notion(question, answer):
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        #确保传递给Notion时的格式是正确的
        notion.pages.create(
            parent={"database_id": notion_database_id},
            properties={
                "标题": {"title": [{"text": {"content": question}}]},
                "内容": {"rich_text": [{"text": {"content": answer}}]},
                "日期": {"date": {"start": today}},  # 确保传递的是日期格式
                "标签": {"multi_select": [{"name": "ChatGPT"}]}
            }
        )
        print(f"记录已成功写入Notion：{question}")
    except Exception as e:
        print(f"写入Notion失败: {e}")

