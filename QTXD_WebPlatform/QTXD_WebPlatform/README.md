# 🚀 QTXD_WebPlatform · 擎天小豆 智能客户系统

> 智能化申请、激活管理平台｜基于 Flask + Notion API｜助力副业变现 🚀

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

---

## ✨ 项目亮点

- 📝 申请信息 ➔ 自动写入 Notion 数据库
- 🔑 激活码验证 ➔ 动态写入激活记录
- 📧 邮件提醒 ➔ 每次申请/激活实时通知
- 🧹 自动日志记录 ➔ 本地日志追踪操作
- 🛡️ 本地 .env 管理敏感配置 ➔ 保障安全

---

## 🗂️ 目录结构

```bash
QTXD_WebPlatform/
├── app.py                # Flask主程序
├── notion_writer.py      # Notion数据写入模块
├── email_sender.py       # 邮件发送模块
├── requirements.txt      # 依赖列表
├── .env                  # 本地环境配置（不上传）
├── notion_log.txt        # 本地日志记录
├── .gitignore            # Git忽略配置
├── README.md             # 项目说明
```

---

## 📦 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/feizei150/QTXD_WebPlatform.git
cd QTXD_WebPlatform
```

### 2. 配置 .env 文件（根目录下）

```env
NOTION_TOKEN=你的Notion集成Token
DATABASE_APPLY_ID=申请记录库ID
DATABASE_ACTIVATE_ID=激活码记录库ID
SMTP_SERVER=smtp.qq.com
SMTP_PORT=465
SMTP_EMAIL=你的邮箱@qq.com
SMTP_PASSWORD=你的SMTP授权码
SMTP_RECEIVER=接收提醒的邮箱
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行项目

```bash
python app.py
```

浏览器访问：[http://localhost:5001/](http://localhost:5001/)

---

## 🛡️ 注意事项

- `.env` 和 `notion_log.txt` 文件已在 `.gitignore` 中保护，默认不会上传。
- 请妥善保管你的 Notion Token 和 SMTP 邮件授权码。

---

## ✨ 后续计划

- ✅ 接入前端动效美化
- ✅ 申请/激活跳转成功页
- ⏳ 后台管理中心开发中...
- ⏳ 多客户分区隔离管理中...

---

## 🔥 联系作者

- 🚀 项目发起：擎天小豆
- 🌟 GitHub主页：[feizei150](https://github.com/feizei150)
- 📧 邮箱：82823766@qq.com

---

© 2025 擎天小豆 · QTXD_WebPlatform · All Rights Reserved.
