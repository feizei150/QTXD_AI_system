from flask import Flask, request, jsonify
from write_chatgpt_to_notion import write_chatgpt_to_notion
from write_chatgpt_to_obsidian import write_chatgpt_to_obsidian

app = Flask(__name__)

# 创建保存ChatGPT记录的API接口
@app.route('/save_chatgpt', methods=['POST'])
def save_chatgpt():
    data = request.json
    question = data.get("question")
    answer = data.get("answer")

    # 打印日志，检查是否有传入question和answer
    print(f"Received Question: {question}")
    print(f"Received Answer: {answer}")

    if question and answer:
        # 清理数据，去除不必要的符号或乱码
        print(f"Cleaned Question: {question.strip()}")
        print(f"Cleaned Answer: {answer.strip()}")

        # 保存到Notion和Obsidian
        write_chatgpt_to_notion(question, answer)
        write_chatgpt_to_obsidian(question, answer) # 这里是文件路径的定义

        return jsonify({"message": "记录已成功保存"}), 200
    else:
        return jsonify({"message": "问题或答案为空"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
