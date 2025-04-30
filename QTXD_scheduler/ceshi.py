from notion_client import Client
from datetime import datetime
import os
import logging

# 初始化 Notion 客户端
notion = Client(auth="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")
database_id = "1d7e27577ab8807a9561ff8ce82f8b4f"

# 确保目录存在
log_dir = "F:/QTXD_AI_system/QTXD_scheduler"
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "task_log.log")

# 设置日志
logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("程序已启动")  # 记录程序是否启动

# 创建任务的函数
def create_task(task_name, task_description, task_type="爬虫", status="待执行", priority="中", task_link=None):
    try:
        logging.info(f"开始创建任务：{task_name}")
        created_page = notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "标题": {"title": [{"text": {"content": task_name}}]},
                "任务描述": {"rich_text": [{"text": {"content": task_description}}]},
                "类型": {"select": {"name": task_type}},
                "状态": {"select": {"name": status}},
                "优先级": {"select": {"name": priority}},
                "日期": {"date": {"start": str(datetime.now().date())}}}
        )
        page_id = created_page['id']  # 获取页面 ID

        # 如果有任务链接，更新任务链接
        if task_link:
            notion.pages.update(
                page_id=page_id,
                properties={
                    "任务链接": {"url": task_link}  # 任务链接字段传递有效的 URL 或 None
                }
            )

        logging.info(f"任务 '{task_name}' 创建成功，Page ID: {page_id}")
        return page_id
    except Exception as e:
        logging.error(f"任务 '{task_name}' 创建失败: {e}")
        return None

# 示例调用
create_task("测试任务", "这是一个测试任务", task_type="爬虫", task_link="https://example.com")
create_task("测试任务2", "这是一个测试任务2", task_type="爬虫", task_link=None)  # 无任务链接
