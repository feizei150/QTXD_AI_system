import os

# Obsidian 路径设置
obsidian_path = "E:/QTXD_AI_system/QTXD_AI_obsidian/obsidian/learning_logs/"

# 将每日记录写入 Obsidian
def write_to_obsidian(title, content, date, tags, summary):
    # 格式化日期为文件名（YYYY-MM-DD）
    file_name = f"{date}.md"
    
    # 构造文件内容
    content_to_write = f"## {title}\n\n"
    content_to_write += f"**日期**: {date}\n\n"
    content_to_write += f"**标签**: {', '.join(tags)}\n\n"
    content_to_write += f"**内容**:\n{content}\n\n"
    content_to_write += f"**总结**:\n{summary}\n"

    # 创建文件并写入内容
    try:
        with open(os.path.join(obsidian_path, file_name), "w", encoding="utf-8") as file:
            file.write(content_to_write)
        print(f"成功写入 Obsidian: {file_name}")
    except Exception as e:
        print(f"写入 Obsidian 时出错: {e}")

# 示例：将当天的对话记录写入 Obsidian
write_to_obsidian(
    "ChatGPT 对话记录_2025-04-29",
    "今天学习了如何使用 Notion API...",
    "2025-04-29",
    tags=["Notion", "API", "学习"],
    summary="今天学习了 Notion API 的使用方法，并成功实现了写入功能。"
)
# 这里的示例日期和内容可以根据实际需要进行修改