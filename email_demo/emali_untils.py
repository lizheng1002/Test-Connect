# encoding: utf-8
#@author: lizheng
#@file: emali_utils.py
#@time: 2020/10/29 11:56
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import configs

class EmaliUtils:
    def __init__(self,smtp_body, attch_path =None):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_prot = 25
        self.smtp_send = '1697744867@qq.com'
        self.smtp_password = 'tuzsiapjjpqeeced'
        self.smtp_receiver = configs.SMTP_RECEIVER
        self.smtp_cc = '1670638524@qq.com,1697744867@qq.com'
        self.smtp_subject = '考试内容自动化邮件发送'
        self.smtp_body = smtp_body
        self.attch_path = attch_path

    def email_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_send
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach(MIMEText(self.smtp_body, 'html', 'utf-8'))
        # print(self.attch_path)
        if self.attch_path:
            attach_file_obj = MIMEText(open(self.attch_path,'rb').read(), 'base64', 'utf-8')
            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.attch_path)))
            message.attach(attach_file_obj)
        return message


    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server, self.smtp_prot)
        smtp.login(self.smtp_send, self.smtp_password)
        smtp.sendmail(self.smtp_send, self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                      self.email_message_body().as_string())
        smtp.close()




if __name__ == '__main__':
    email_u = EmaliUtils('考试内容自动化邮件发送', '全栈测试班李争-接口测试（requests+httprunner）试卷.docx')
    email_u.send_mail()

