# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-17 13:35:29
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-17 13:35:29
'''

import os
import time
import json
from bs4 import BeautifulSoup
from subirdpro.email.email import Email
from subirdpro.share.config import Config

class EmailHandler():
    """ 邮件处理类 """
    def __init__(self, email_timespan=''):
        self.email = Email()
        self.conf = Config().constant
        self.email_timespan = time.strftime("%Y%m%d%H%M%S") \
            if email_timespan == '' else email_timespan


    def set_email(self, result):
        """设置邮件内容相关

        Arguments:
            result_path {string} -- [测试报告路径]
        """

        result_str = self.get_email_body(result)
        self.email.set_body(result_str)

        email_subject = 'TEST-REPORT-{0}'.format(self.email_timespan)
        self.email.set_subject(email_subject)

    def send_email(self, result):
        """发送邮件

        Arguments:
            result_path {[string]} -- [测试报告路径]
        """
        self.set_email(result)
        self.email.send()

    def get_email_body(self, result):
        """获取邮件内容

        Arguments:
            result {[string]} -- [测试报告内容]

        Returns:
            [string] -- [邮件内容]
        """
        content = ''

        if result == self.conf["ERROR_MSG"]:
            content = "Dear All,"
            content += "<label>Error occurred during running the test suites</label><br><br>"
        else:
            obj = json.loads(result)
            content = "Dear All,<br><br>"
            content += "<label>测试<strong>{}</strong>结果如下：</label><br><br>".format(obj["testName"])
            content += "<strong>用例总数: </strong><label>{}</label><br>".format(obj["testAll"])
            content += "<strong>通过个数: </strong><label>{}</label><br>".format(obj["testPass"])
            content += "<strong>失败个数: </strong><label>{}</label><br>".format(obj["testFail"])
            content += "<strong>跳过个数: </strong><label>{}</label><br>".format(obj["testSkip"])
            content += "<strong>开始时间: </strong><label>{}</label><br>".format(obj["beginTime"])
            content += "<strong>测试时长: </strong><label>{}</label><br>".format(obj["totalTime"])

        return content

