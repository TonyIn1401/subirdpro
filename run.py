# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-16 16:36:11
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-16 16:36:11
'''
import time
from subirdpro.share.config import Config
from subirdpro.test.runner import Runner
from subirdpro.email.email_handler import EmailHandler

class Run():
    """ 入口类 """

    def __init__(self):
        self.config = Config().constant

    def start(self):
        """ 开始执行 """
        run_time = time.strftime("%Y%m%d%H%M%S")
        runner = Runner(report_timespan=run_time)
        result = runner.run()

        email_handler = EmailHandler(email_timespan=run_time)
        email_handler.send_email(result)

if __name__ == '__main__':
    Run().start()
    