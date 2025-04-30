from notion_client import Client
from datetime import datetime

# 初始化 Notion 客户端
notion = Client(auth="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")

# 实际的数据库 ID
database_id = "1d3e27577ab880e89986c7efefb6aa45"  

# 将日期转换为 ISO 8601 格式 (YYYY-MM-DD)
def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date().isoformat()
    except ValueError:
        return None

# 将每日记录写入 Notion
def write_to_notion(title, content, date, tags, summary):
    try:
        # 格式化日期为正确的格式
        formatted_date = format_date(date)

        if formatted_date is None:
            print("日期格式无效")
            return

        notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "标题": {"title": [{"text": {"content": title}}]},
                "内容": {"rich_text": [{"text": {"content": content}}]},
                "日期": {"date": {"start": formatted_date}},  # 使用日期字段
                "标签": {"multi_select": [{"name": tag} for tag in tags]},  # 添加标签
                "总结": {"rich_text": [{"text": {"content": summary}}]},  # 添加总结
            }
        )
        print(f"成功写入 Notion: {title}")
    except Exception as e:
        print(f"写入 Notion 时出错: {e}")

# 示例：将当天的对话记录写入 Notion
write_to_notion(
    "ChatGPT 对话记录_2025-04-29",
    "今天学习了如何使用 Notion API...",
    "2025-04-29",
    tags=["Notion", "API", "学习"],  # 示例标签
    summary="今天学习了 Notion API 的使用方法，并成功实现了写入功能。"  # 示例总结
)
