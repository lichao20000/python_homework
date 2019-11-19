#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#设置发送邮件的邮箱属性
host = 'smtp.chinaunicom.cn'#服务器
port = 25#端口
user = 'zhangk126@chinaunicom.cn'#用户名
password = '***'#口令

#拼装邮件内容
sender = 'zhangk126@chinaunicom.cn'
message = MIMEText('张凯的Python作业 ', 'plain', 'utf-8')
message['From'] = Header("zhangk126@chinaunicom.cn", 'utf-8')
message['To'] = Header('zhangk126', 'utf-8')
subject = 'zhangk126的Python作业'
message['Subject'] = Header(subject, 'utf-8')
recvList = []

#打开文件，获取接收邮件的列表
with open("emailList.csv", "rb") as emails_file:
    lines = csv.reader(emails_file)
    for line in lines:
        recvList = recvList + line

#开始发送邮件
try:
    #连接邮箱服务器
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host, port)
    smtpObj.login(user, password)
    smtpObj.sendmail(sender, recvList, message.as_string())  # 发送邮件
    print("邮件发送成功")
    smtpObj.quit() #断开连接
except smtplib.SMTPException:
    print("Error: 无法发送邮件" + smtplib.SMTPException.message)
