#!/usr/bin/env python3
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_contact_email():
    """发送联系表单邮件"""
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    to_email = os.environ.get("TO_EMAIL")
    
    if not all([sender_email, sender_password, to_email]):
        print("邮箱配置不完整")
        return False
    
    # 解析 Issue 数据
    issue_data = json.loads(os.environ.get("ISSUE_DATA"))
    
    subject = issue_data["issue"]["title"]
    body = issue_data["issue"]["body"]
    issue_url = issue_data["issue"]["html_url"]
    created_at = issue_data["issue"]["created_at"]
    
    # 解析联系信息
    contact_info = {
        "name": "",
        "email": "",
        "subject": "",
        "message": ""
    }
    
    for line in body.split("\n"):
        if line.startswith("姓名:"):
            contact_info["name"] = line.split(":")[1].strip()
        elif line.startswith("邮箱:"):
            contact_info["email"] = line.split(":")[1].strip()
        elif line.startswith("主题:"):
            contact_info["subject"] = line.split(":")[1].strip()
        elif line.startswith("消息:"):
            contact_info["message"] = line.split(":")[1].strip()
    
    # 创建邮件
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    
    email_body = f"""
收到新的联系信息！

{body}

---

详情链接: {issue_url}
创建时间: {created_at}
"""
    
    msg.attach(MIMEText(email_body, "plain"))
    
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
    success = send_contact_email()
    if success:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

if __name__ == "__main__":
    main()