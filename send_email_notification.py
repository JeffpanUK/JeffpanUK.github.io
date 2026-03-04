#!/usr/bin/env python3
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    """发送邮件通知"""
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    to_email = os.environ.get("TO_EMAIL", "2359501@qq.com")
    
    if not sender_email or not sender_password:
        print("邮件配置缺失")
        return False
    
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        
        msg.attach(MIMEText(body, "plain"))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        
        return True
    except Exception as e:
        print(f"发送邮件失败: {e}")
        return False

def main():
    event_data = json.loads(os.environ.get("GITHUB_EVENT", "{}"))
    
    subject = "GitHub 通知"
    body = ""
    
    if "issue" in event_data:
        issue = event_data["issue"]
        subject = f"GitHub 问题通知：{issue['title']}"
        body = f"""
问题标题: {issue['title']}
问题描述: {issue['body']}
创建时间: {issue['created_at']}
创建者: {issue['user']['login']}
问题链接: {issue['html_url']}
        """
        
    elif "comment" in event_data:
        comment = event_data["comment"]
        issue = event_data["issue"]
        subject = f"GitHub 评论通知：{issue['title']}"
        body = f"""
问题标题: {issue['title']}
评论作者: {comment['user']['login']}
评论时间: {comment['created_at']}
评论内容: {comment['body']}
问题链接: {issue['html_url']}
        """
    
    if body:
        success = send_email(subject, body)
        if success:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
    else:
        print("未识别的事件类型")

if __name__ == "__main__":
    main()