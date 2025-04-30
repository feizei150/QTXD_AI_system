
import os
from docx import Document

MODEL = "mistral:latest"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "party_documents")
OUTPUT_DIR = os.path.join(BASE_DIR, "party_summaries")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def summarize(text):
    return text[:300] + "...（此处省略后续内容）"

for file_name in os.listdir(INPUT_DIR):
    if file_name.endswith(".docx"):
        input_path = os.path.join(INPUT_DIR, file_name)
        document = Document(input_path)
        full_text = "\n".join([p.text for p in document.paragraphs])
        summary = summarize(full_text)
        base_name = os.path.splitext(file_name)[0]
        output_path = os.path.join(OUTPUT_DIR, f"{base_name}_总结.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"✅ 已生成：{output_path}")
