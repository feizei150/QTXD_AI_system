import requests
import datetime
import json
import os

def fetch_zhihu_hot():
    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=20"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        print("状态码：", response.status_code)
        print("响应预览：", response.text[:200])

        data = response.json()

        hot_list = []
        for item in data.get("data", []):
            entry = {
                "title": item["target"]["title"],
                "url": "https://www.zhihu.com/question/" + str(item["target"]["id"]),
                "hot": item["detail_text"]
            }
            hot_list.append(entry)

        os.makedirs("outputs", exist_ok=True)
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")
        output_path = f"outputs/zhihu_hot_{today_str}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(hot_list, f, ensure_ascii=False, indent=2)

        print(f"✅ 成功抓取知乎热榜，共 {len(hot_list)} 条，保存至 {output_path}")
    except Exception as e:
        print(f"❌ 抓取失败：{e}")

if __name__ == "__main__":
    fetch_zhihu_hot()
