from flask import Flask, render_template_string, request
from QTXD_AI_system.notion_writer import write_apply_to_notion, write_activate_to_notion
from email_sender import send_email
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()

# 获取环境变量
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>申请入口 - 擎天小豆</title>
        <style>
            body {
                font-family: "Microsoft YaHei", sans-serif;
                background: linear-gradient(135deg, #cfd9df 0%, #e2ebf0 100%);
                text-align: center;
                padding: 50px;
            }
            form {
                display: inline-block;
                background: #fff;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            }
            input, textarea {
                display: block;
                margin: 15px auto;
                padding: 12px;
                width: 250px;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 16px;
            }
            button {
                padding: 12px 30px;
                background: #38a169;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>📝 申请使用系统</h1>
        <form method="post">
            <input type="text" name="name" placeholder="请输入姓名" required>
            <input type="email" name="email" placeholder="请输入邮箱" required>
            <textarea name="note" placeholder="备注信息（可选）"></textarea>
            <button type="submit">提交申请</button>
        </form>
        <a href="/">返回首页</a>
    </body>
    </html>
    ''')

@app.route('/apply', methods=['POST'])
def apply():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        note = request.form.get('note')
        success = write_apply_to_notion(name, email, note)
        if success:
            send_email("新申请通知", f"姓名: {name}\n邮箱: {email}\n备注: {note}")
            return "✅ 申请已提交，我们会尽快联系你！"
        else:
            return "❌ 提交失败，请稍后重试。"

    return render_template_string('''
        <form method="POST">
            <input type="text" name="name" placeholder="姓名" required><br>
            <input type="email" name="email" placeholder="邮箱" required><br>
            <textarea name="note" placeholder="备注信息"></textarea><br>
            <button type="submit">提交申请</button>
        </form>
        <a href="/">返回首页</a>
    ''')

@app.errorhandler(404)
def page_not_found(e):
    return render_template_string('''
    <h1>404 - 页面不存在</h1>
    <p>您访问的页面走丢啦！</p>
    <a href="/">返回首页</a>
    '''), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
