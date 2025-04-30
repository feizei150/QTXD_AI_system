import os
import json
from datetime import datetime

def generate_summary(item):
    # 模拟AI总结：可以替换为调用 ChatGPT 或 Ollama
    return f"《{item['title']}》是当前热议话题，点击查看详情：{item['url']}。"

def summarize_zhihu():
    today = datetime.now().strftime("%Y-%m-%d")
    input_path = f"outputs/zhihu_hot_{today}.json"
    output_path = f"outputs/zhihu_summary_{today}.json"

    if not os.path.exists(input_path):
        print(f"❌ 未找到热榜数据文件：{input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    summarized = []
    for item in data:
        summary = generate_summary(item)
        summarized.append({
            "title": item["title"],
            "url": item["url"],
            "hot": item["hot"],
            "summary": summary
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summarized, f, ensure_ascii=False, indent=2)

    print(f"✅ 总结生成完成，输出文件：{output_path}")

if __name__ == "__main__":
    summarize_zhihu()
