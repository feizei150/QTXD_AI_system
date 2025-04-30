import schedule
import time
from datetime import datetime
from subprocess import run
import logging

# 设置日志
logging.basicConfig(filename='F:/QTXD_AI_system/QTXD_scheduler/task_log.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 定义任务函数
def run_spiders():
    try:
        logging.info("执行爬虫任务")
        run(["python", "F:/QTXD_AI_system/QTXD_spider_tasks/spider_zhihu_to_notion.py"], check=True)
        logging.info("爬虫任务完成")
    except Exception as e:
        logging.error(f"爬虫任务执行失败: {e}")
        send_failure_email(f"爬虫任务执行失败: {e}")

def run_summary():
    try:
        logging.info("执行总结任务")
        run(["python", "F:/QTXD_AI_system/QTXD_spider_tasks/summarizer.py"], check=True)
        logging.info("总结任务完成")
    except Exception as e:
        logging.error(f"总结任务执行失败: {e}")
        send_failure_email(f"总结任务执行失败: {e}")

def sync_to_notion():
    try:
        logging.info("同步数据到 Notion")
        run(["python", "F:/QTXD_AI_system/QTXD_notion_tasks/notion_writer.py"], check=True)
        logging.info("数据同步到 Notion 完成")
    except Exception as e:
        logging.error(f"Notion 同步失败: {e}")
        send_failure_email(f"Notion 同步失败: {e}")

def commit_to_github():
    try:
        logging.info("提交到 GitHub")
        run(["git", "add", "."], cwd="F:/QTXD_AI_system")
        run(["git", "commit", "-m", f"自动提交：{datetime.now()}"], cwd="F:/QTXD_AI_system")
        run(["git", "push"], cwd="F:/QTXD_AI_system")
        logging.info("提交到 GitHub 完成")
    except Exception as e:
        logging.error(f"GitHub 提交失败: {e}")
        send_failure_email(f"GitHub 提交失败: {e}")

# 定义失败重试机制
def run_with_retry(task_function, retries=3, delay=10):
    for attempt in range(retries):
        try:
            task_function()
            break  # 成功则退出
        except Exception as e:
            if attempt < retries - 1:
                logging.error(f"任务失败，第 {attempt + 1} 次尝试，错误：{e}")
                time.sleep(delay)  # 延时后重试
            else:
                logging.error(f"任务执行失败，已重试 {retries} 次：{e}")
                send_failure_email(f"任务执行失败，已重试 {retries} 次")
                break

# 定义每日任务调度
schedule.every().day.at("08:00").do(run_spiders)  # 每天8点执行爬虫任务
schedule.every().day.at("09:00").do(run_summary)  # 每天9点执行总结任务
schedule.every().day.at("10:00").do(sync_to_notion)  # 每天10点同步到 Notion
schedule.every().day.at("18:00").do(commit_to_github)  # 每天18点提交到 GitHub

# 运行调度任务
while True:
    schedule.run_pending()  # 执行所有待处理的任务
    time.sleep(60)  # 每分钟检查一次任务
