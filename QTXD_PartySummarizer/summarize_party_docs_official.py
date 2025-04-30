
import os
from docx import Document
from ollama import Client

MODEL = "deepseek-r1:7b"
client = Client(host='http://localhost:11434')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "party_documents")
OUTPUT_DIR = os.path.join(BASE_DIR, "party_summaries")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def summarize(text):
    response = client.chat(model=MODEL, messages=[
        {
            "role": "user",
            "content": f'''
你是一名长期从事党务材料撰写的高级文稿专家，请阅读以下“学习计划类”Word内容，并输出一篇语言严谨、结构规范、逻辑清晰的总结材料，内容需包含以下模块：

一、总体学习导向（不超过两句话）
二、重点学习内容（结合原文提炼，列出3点以上）
三、阶段性学习安排（按时间段或阶段结构化表述）
四、目标达成预期（体现个人学习成效预判）
五、存在问题（从文件内容中分析逻辑、表达、措施、可操作性等方面的问题，不少于3条）
六、改进建议（逐条对应提出建议，每点建议语言明确、可操作）

总结需以“党建公文风格”输出，语言正式、表达规范、具有结构层次感。不得照搬原文，不得输出“我无法理解”或“请提供更多上下文”之类表述。

原始学习文档如下：
{text}
'''
        }
    ])
    return response["message"]["content"]

for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith(".docx"):
        input_path = os.path.join(INPUT_DIR, file_name)
        document = Document(input_path)
        full_text = "\n".join([p.text for p in document.paragraphs])
        print(f"📄 正在处理：{file_name}")
        summary = summarize(full_text)
        base_name = os.path.splitext(file_name)[0]
        output_path = os.path.join(OUTPUT_DIR, f"{base_name}_正式总结_公文版.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"✅ 已生成：{output_path}")
