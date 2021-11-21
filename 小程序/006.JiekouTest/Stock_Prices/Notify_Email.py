__author__ = "TANUKI"
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage

import yagmail

import time


def send_email(*args, **kwargs):
    #连接服务器
    #用户名、授权码、服务器地址
    yag_server = yagmail.SMTP(user='fengyongming0311@sohu.com', password='4O79R0ND1GC8', host='smtp.sohu.com')

    if 'address' in kwargs.keys():
        email_to = kwargs['address']
    else:
        email_to = ["fengyongming0311@sohu.com"]   #给自己设个默认值

    #邮件标题
    if 'subject' in kwargs.keys():
        email_title = kwargs['subject']
    else:
        email_title = '系统自动发送邮件....没有传入邮件标题'
    #邮件内容
    if 'msg' in kwargs.keys():
        email_content = kwargs['msg']
        print ("发送邮件内容： \n",kwargs['msg'])
    else:
        email_content = """emmmm,没有找到传入的内容值，这里什么也没有..."""


    # 附件列表
    #email_attachments = ['./attachments/report.png', ]

    #发送邮件
    yag_server.send(email_to, email_title, email_content)


def getTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

