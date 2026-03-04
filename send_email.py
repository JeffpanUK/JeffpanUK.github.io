#!/usr/bin/env python3
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

def send_email(to_email, subject, message, from_name, from_email):
    """发送邮件"""
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    
    if not sender_email or not sender_password:
        raise Exception("缺少邮件配置")
    
    # 创建邮件
    msg = MIMEMultipart()
    msg["From"] = f"{from_name} <{sender_email}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    
    # 邮件正文
    body = f"""
来自 {from_name} <{from_email}> 的联系信息：

主题：{subject}

内容：
{message}
"""
    
    msg.attach(MIMEText(body, "plain"))
    
    # 发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, to_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"发送邮件失败: {e}")
        return False

def main():
    import sys
    import cgi
    
    print("Content-Type: application/json")
    print()
    
    if os.environ.get("REQUEST_METHOD") == "POST":
        # 读取 POST 数据
        form = cgi.FieldStorage()
        name = form.getfirst("name", "").strip()
        email = form.getfirst("email", "").strip()
        subject = form.getfirst("subject", "").strip()
        message = form.getfirst("message", "").strip()
        
        if not name or not email or not subject or not message:
            print(json.dumps({"status": "error", "message": "缺少必填项"}))
            return
        
        # 发送邮件
        success = send_email(
            to_email="2359501@qq.com",
            subject=subject,
            message=message,
            from_name=name,
            from_email=email
        )
        
        if success:
            print(json.dumps({"status": "success", "message": "邮件发送成功"}))
        else:
            print(json.dumps({"status": "error", "message": "邮件发送失败"}))
    else:
        print(json.dumps({"status": "error", "message": "只接受 POST 请求"}))

if __name__ == "__main__":
    main()