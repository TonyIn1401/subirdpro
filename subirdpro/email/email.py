# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-16 17:45:24
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-16 17:45:24
'''

import logging
import smtplib
from os import path
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from subirdpro.share.config import Config

class Email():
    """ 邮件类 """

    def __init__(self):
        #邮件配置
        conf = Config().email
        #邮件主题
        self.subject = 'subject'
        #邮件内容
        self.body = 'body'
        #邮件内容格式
        self.body_type = conf["body_type"]
        #附件路径
        self.attached_file = ''
        #邮箱用户名，发件人邮箱
        self.user = conf["username"]
        #邮箱密码
        self.pwd = conf["password"]
        #邮箱昵称
        self.nick_name = conf["nick_name"]
        #收件人列表
        self.to_email_list = conf["to"]
        #邮箱服务器地址
        self.host = conf["smtp_server"]
        #邮箱服务端口号
        self.port = conf["smtp_port"]
        #发件人信息
        self.email_from = '{} {}'.format(self.nick_name, self.user)
        #收件人信息
        self.email_to = str(self.to_email_list)
        self.email_cc = str(conf["cc"])

    def set_attached_file(self, attached_file):
        """添加附件，因为默认html格式，不太支持添加html格式的附件，暂时还不太想研究这个

        Arguments:
            attached_file {[string]} -- [附件路径]

        Returns:
            [MIMEMultipart] -- [MIMEMultipart]
        """
        msg = MIMEMultipart()
        self.attached_file = attached_file
        if path.exists(self.attached_file):
            attached_content = ''
            with open(self.attached_file, 'r', encoding='utf-8') as f:
                attached_content = f.read()

            attached_file = MIMEText(attached_content, 'html', 'utf-8')
            file_name = path.basename(self.attached_file)
            msg.add_header("Content-Disposition", "attachment", filename=file_name)
            msg.attach(attached_file)
        return msg

    def set_body(self, body):
        """ 设置邮件内容 """
        self.body = body

    def set_body_type(self, body_type):
        """ 设置邮件内容格式，默认html """
        self.body_type = body_type

    def set_subject(self, subject):
        """ 设置邮件主题 """
        self.subject = subject

    def init_msg(self):
        """初始化邮件内容、标题、邮件内容格式

        Returns:
            [MIMEText] -- [邮件格式类]
        """
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.body, self.body_type, 'utf-8'))
        msg['From'] = self.email_from
        msg['To'] = self.email_to
        msg['Cc'] = self.email_cc
        msg['Subject'] = self.subject
        return msg

    def send(self):
        """ 发送邮件 """
        try:
            msg = self.init_msg()
            #邮箱服务
            server = smtplib.SMTP(self.host, int(self.port))
            loginer = server.login(self.user, self.pwd)
            if loginer[0] == 235:
                server.sendmail(self.user, self.to_email_list, msg.as_string())
                print("Email has been send successfully.")
            else:
                output = "Email login failed, please check your username name password."
                logging.info(output)
                print(output)
            server.quit()
        except Exception as exception:
            error = 'Send email failed, Exception: %s' % exception
            logging.info(error)
            print(error)
