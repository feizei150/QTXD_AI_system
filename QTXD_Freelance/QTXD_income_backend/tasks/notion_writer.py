import sys
sys.path.append("config")
from settings import NOTION_API_TOKEN, DATABASE_ID
from notion_client import Client
from datetime import datetime
import os
import json

# ✅ 替换成你的 Notion Token 和数据库 ID
NOTION_API_TOKEN = "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"
DATABASE_ID = "1d5e27577ab8805eb7dff74a442dd9d3"

notion = Client(auth=NOTION_API_TOKEN)

def write_to_notion(data):
    for item in data:
        try:
            notion.pages.create(
                parent={"database_id": DATABASE_ID},
                properties={
                    "标题": {"title": [{"text": {"content": item["title"]}}]},
                    "链接": {"url": item["url"]},
                    "热度": {"rich_text": [{"text": {"content": item["hot"]}}]},
                    "抓取时间": {"rich_text": [{"text": {"content": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}]},
                    "内容摘要": {"rich_text": [{"text": {"content": item["summary"]}}]},
                    "平台来源": {"select": {"name": "知乎"}},
                    "是否已处理": {"checkbox": False}
                }
            )
            print(f"✅ 写入成功：{item['title']}")
        except Exception as e:
            print(f"❌ 写入失败：{item['title']} - {e}")

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    input_path = f"outputs/zhihu_summary_{today}.json"

    if not os.path.exists(input_path):
        print("❌ 总结文件不存在，请先执行 summarizer.py")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    write_to_notion(data)

if __name__ == "__main__":
    main()
