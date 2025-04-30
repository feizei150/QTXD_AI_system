# app.py

from flask import Flask, render_template_string, request
from QTXD_AI_system.notion_writer import write_apply_to_notion, write_activate_to_notion
from email_sender import send_email
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
    <title>擎天小豆 · 智能平台</title></head><body>
    <h1>擎天小豆 · 自动化创富系统 🧠💸</h1>
    <a href="/apply">📝 申请入口</a><br>
    <a href="/activate">🔑 激活码激活</a>
    </body></html>
    ''')

@app.route('/apply', methods=['GET', 'POST'])
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
    <form method="post">
        <input type="text" name="name" placeholder="姓名" required><br>
        <input type="email" name="email" placeholder="邮箱" required><br>
        <textarea name="note" placeholder="备注"></textarea><br>
        <button type="submit">提交申请</button>
    </form>
    <a href="/">返回首页</a>
    ''')

@app.route('/activate', methods=['GET', 'POST'])
def activate():
    if request.method == 'POST':
        email = request.form.get('email')
        code = request.form.get('code')
        result = "激活成功" if code in ["QTXD2025", "AIINCOME2025", "QTXD666", "小豆飞升2025"] else "激活失败"
        success = write_activate_to_notion(email, code, result)
        if success:
            send_email("激活通知", f"邮箱: {email}\n激活码: {code}\n结果: {result}")
            return f"✅ {result}！"
        else:
            return "❌ 激活失败，请稍后重试。"
    return render_template_string('''
    <form method="post">
        <input type="email" name="email" placeholder="邮箱" required><br>
        <input type="text" name="code" placeholder="激活码" required><br>
        <button type="submit">提交激活</button>
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

# notion_writer.py

from notion_client import Client
from datetime import datetime
import os

notion = Client(auth=os.getenv("NOTION_TOKEN"))
DATABASE_APPLY_ID = os.getenv("DATABASE_APPLY_ID")
DATABASE_ACTIVATE_ID = os.getenv("DATABASE_ACTIVATE_ID")

log_file = "notion_log.txt"

def log(message):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def write_apply_to_notion(name, email, note):
    try:
        notion.pages.create(
            parent={"database_id": DATABASE_APPLY_ID},
            properties={
                "姓名": {"title": [{"text": {"content": name}}]},
                "邮箱": {"email": email},
                "备注": {"rich_text": [{"text": {"content": note or ''}}]},
                "提交时间": {"rich_text": [{"text": {"content": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}]}
            }
        )
        log(f"申请成功：{name} - {email}")
        return True
    except Exception as e:
        log(f"申请失败：{e}")
        return False

def write_activate_to_notion(email, code, result):
    try:
        notion.pages.create(
            parent={"database_id": DATABASE_ACTIVATE_ID},
            properties={
                "邮箱": {"email": email},
                "激活码": {"rich_text": [{"text": {"content": code}}]},
                "激活结果": {"select": {"name": result}},
                "激活时间": {"rich_text": [{"text": {"content": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}]}
            }
        )
        log(f"激活{result}：{email} - {code}")
        return True
    except Exception as e:
        log(f"激活失败：{e}")
        return False

# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os

def send_email(subject, body):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")
    receiver_email = os.getenv("SMTP_RECEIVER")

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = smtp_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_email, smtp_password)
        server.sendmail(smtp_email, [receiver_email], msg.as_string())
        server.quit()
    except Exception as e:
        print(f"发送邮件失败: {e}")

# requirements.txt

Flask
notion-client
python-dotenv
