# encoding: utf-8
#@author: test_lizheng
#@file: email-test1.py
#@time: 2020/10/28 22:53
import os
import smtplib
from email.mime.text import MIMEText  #普通邮件正文
from email.mime.multipart import MIMEMultipart   #邮件附件

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com', 25)
smtp.login('1697744867@qq.com', 'tuzsiapjjpqeeced')#邮件授权码
email_content = 'from newdraw test001'
msg = MIMEMultipart()  #邮件附件
msg.attach(MIMEText(email_content, 'html', 'utf-8'))
msg['from'] = '1697744867@qq.com' #发送人
msg['to'] = '1697744867@qq.com' #抄送人
msg['Cc'] = '740458160@qq.com' #邮件抄送人
msg['subject'] = '邮件主题加附件的'
attach_file_path = os.path.join(os.path.dirname(__file__), 'API_TEST_V2.0.html')
attach_file_obj = MIMEText(open(attach_file_path, 'rb').read(), 'base64', 'utf-8')
attach_file_obj['Content-Type'] = 'application/octet-stream'
attach_file_obj.add_header('Content-Disposition', 'atachment',
                           filename=('gbk', '', os.path.basename(attach_file_path)))
msg.attach(attach_file_obj)
smtp.sendmail('1697744867@qq.com', ['1697744867@qq.com', '740458160@qq.com'], msg.as_string())  #发件人，收件人

smtp.close()
