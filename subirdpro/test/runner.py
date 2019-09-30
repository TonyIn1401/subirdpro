# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-16 17:15:54
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-16 17:15:54
'''

import os
import time
import logging
import xmlrunner
from subirdpro.test.loader import Loader
from subirdpro.share.config import Config
from subirdpro.share.html_runner import HTMLRunner


class Runner():
    """ 测试用例执行类 """

    def __init__(self, \
        language=0, \
        report_timespan='', \
        report_type='html', \
        report_name='', \
        test_name='', \
        test_person=''):
        self.loader = Loader()
        self.conf = Config().constant
        self.report_lan = language
        self.report_timespan = time.strftime("%Y%m%d%H%M%S") \
            if report_timespan == '' else report_timespan
        self.report_type = report_type
        self.report_name = self.__generate_report_name(report_name)
        self.report_path = self.__generate_report_path()
        self.test_name = self.report_timespan if test_name == '' else test_name
        self.test_person = '' if test_person == '' else test_person

    def __generate_report_path(self):
        path = ''
        abs_path = os.path.abspath(__file__)
        dir_name = os.path.dirname(abs_path)
        path = os.path.join(dir_name, self.conf["RESULT_FOLDER_NAME"], \
            self.report_type, self.report_name)
        return path

    def __generate_report_name(self, report_name):
        name = ''
        if report_name == '':
            name = 'TEST-REPORT-{0}.{1}'.format(self.report_timespan, self.report_type)
        else:
            name = '{0}.{1}'.format(report_name, self.report_type)
        return name

    def run(self):
        """ 执行配置文件中所有测试用例 """
        result = ''
        try:
            suites = self.loader.loads()
            result = self.run_html(suites)

            print("Test cases run successfully, and test report has been generated to {}" \
            .format(self.report_path))
        except Exception as exception:
            print("Test cases run failed, exception: {}".format(exception))
            result = self.conf["ERROR_MSG"]
        return result

    def run_html(self, suites):
        """执行测试用例，最终导出HTML格式测试报告

        Arguments:
            suites {[unittest.TestSuite]} -- [测试用例集合]

        Returns:
            [string] -- [测试报告路径]
        """
        result = ""
        with open(self.report_path, 'wb') as fp:
            runner = HTMLRunner(
                language=self.report_lan,
                stream=fp,
                test_name=self.test_name,
                test_person=self.test_person
                )
            result = runner.run(suites)
        return result
