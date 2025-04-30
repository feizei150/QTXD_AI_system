# QTXD_task_fetcher_v2 - 兼职任务抓取示例

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_sample_tasks():
    url = "https://www.taskcn.com"  # 示例地址，请替换为目标任务平台
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        print("✅ 成功抓取任务平台首页")
        # 示例逻辑：提取任务标题
        for item in soup.find_all("a")[:5]:
            print("任务标题:", item.get_text(strip=True))
    else:
        print("❌ 抓取失败，状态码：", response.status_code)

if __name__ == "__main__":
    print("📦 启动兼职任务爬虫：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    fetch_sample_tasks()
