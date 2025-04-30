import logging
from notion_client import Client
from datetime import datetime
import schedule
import time
import os

# 确保目录存在
log_dir = "F:/QTXD_AI_system/QTXD_scheduler"
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "task_log.log")

# 设置日志
logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("程序已启动")  # 记录程序是否启动

# 初始化 Notion 客户端
notion = Client(auth="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")
database_id = "1d7e27577ab8807a9561ff8ce82f8b4f"

# 创建任务的函数
def create_task(task_name, task_description, task_type, priority="中", status="待执行", task_link=""):
    try:
        logging.info(f"创建任务：{task_name}")
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
                    "任务链接": {"url": task_link}  # 任务链接
                }
            )
        logging.info(f"任务 '{task_name}' 创建成功")
        return page_id
    except Exception as e:
        logging.error(f"任务 '{task_name}' 创建失败: {e}")
        return None

# 更新任务状态
def update_task_status(task_name, status, error_message=None):
    try:
        logging.info(f"更新任务 '{task_name}' 状态为 {status}")
        pages = notion.pages.query(
            database_id=database_id,
            filter={
                "property": "标题",
                "title": {"equals": task_name}
            }
        )

        if pages['results']:
            page_id = pages['results'][0]['id']
            properties = {
                "状态": {"select": {"name": status}},
                "完成时间": {"date": {"start": str(datetime.now())}}  # 设置完成时间
            }

            if error_message:
                properties["错误信息"] = {
                    "rich_text": [{"text": {"content": error_message}}]
                }

            notion.pages.update(
                page_id=page_id,
                properties=properties
            )
            logging.info(f"任务 '{task_name}' 状态更新成功")
        else:
            logging.error(f"任务 '{task_name}' 找不到相关页面，无法更新状态")
    except Exception as e:
        logging.error(f"任务 '{task_name}' 状态更新失败: {e}")

# 任务分配函数
def task_dispatcher():
    print("进入任务分配器")  # 添加 print 输出，确认是否进入函数
    logging.info("进入任务分配器")  # 添加日志输出，查看是否执行到此处
    current_time = datetime.now().strftime("%H:%M")
    logging.info(f"当前时间: {current_time}")
    
    if "08:00" <= current_time < "12:00":  # 上午
        task_to_do = "爬取知乎热榜"
        task_link = "https://example.com/zhihu_spider"  # 任务链接
    elif "12:00" <= current_time < "18:00":  # 下午
        task_to_do = "生成总结"
        task_link = "https://example.com/summary_task"  # 任务链接
    elif "18:00" <= current_time < "23:59":  # 晚上
        task_to_do = "提交到 GitHub"
        task_link = "https://github.com/your-repo"  # 任务链接
    else:
        task_to_do = None
        task_link = None
    
    if task_to_do:
        logging.info(f"今天的任务是：{task_to_do}")
        page_id = create_task(task_to_do, f"执行任务：{task_to_do}", "爬虫", task_link=task_link)
        if page_id:
            update_task_status(task_to_do, "进行中")

# 只手动触发任务
if __name__ == "__main__":
    logging.info("手动触发任务")
    print("手动触发任务")  # 也添加 print 输出，确认手动触发
    task_dispatcher()  # 手动触发一次任务调度
    logging.info("任务调度完成")
    print("任务调度完成")