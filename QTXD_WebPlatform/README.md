# QTXD_WebPlatform · 擎天小豆 智能化客户申请系统
 
 🚀 这是一个基于 Flask + Notion API 的轻量级客户申请与激活管理平台。
 
 - 支持客户申请填写 ➔ 自动写入 Notion
 - 支持激活码激活 ➔ 自动验证并写入 Notion
 - 支持后台邮件通知提醒（SMTP集成）
 - 自动记录申请与激活日志
 - 支持本地开发与服务器部署
 
 ## 📦 目录结构
 
 app.py # 主程序 
 notion_writer.py # 处理Notion写入 
 email_sender.py # 发送邮件提醒 
 .env # 本地环境配置文件（未上传） 
 notion_log.txt # 写入日志（未上传） 
 requirements.txt # 依赖列表
 
 
 ## 🔧 使用说明
 
 1. 配置 `.env` 文件（存放密钥、数据库ID、SMTP信息）
 2. 安装依赖：
 
     ```bash
     pip install -r requirements.txt
     ```
 
 3. 启动服务：
 
     ```bash
     python app.py
     ```
 
 4. 本地访问：http://localhost:5001
 
 ## 🛡️ 注意事项
 
 - 请保护好 `.env` 文件，不要上传到GitHub！
 - notion_log.txt 为本地记录日志，也不上传。
 
 ---
 
 © 2025 擎天小豆 QTXD · All Rights Reserved.
