# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-18 18:21:11
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-18 18:21:11
'''
import time
from unittest import TestResult

class HtmlResult(TestResult):
    """自定义测试结果类

    Arguments:
        TestResult {[unittest.TestResult]} -- [继承unittest中TestResult]
    """

    def __init__(self, lan=0):
        super().__init__()
        #成功的测试用例个数
        self.success_count = 0
        #失败的测试用例个数
        self.failure_count = 0
        #出错的测试用例个数
        self.error_count = 0
        #跳过的测试用例个数
        self.skip_count = 0
        #测试通过率
        self.pass_rate = float(0)
        self.details = []
        self.start_timestamp = int(round(time.time() * 1000))
        self.stop_timestamp = int(round(time.time() * 1000))
        self.run_stamp = 0
        self.lan = lan
        self.status = {
            "CN":{
                "Success":'通过',
                "Failure": '失败',
                "Skip": '跳过',
                "Error": '错误',
            },
            "EN":{
                "Success":'Success',
                "Failure": 'Failure',
                "Skip": 'Skip',
                "Error": 'Error',
            }
        }


    def startTest(self, test):
        """ 每个测试开始前执行的方法 """
        self.start_timestamp = int(round(time.time() * 1000))

    def stopTest(self, test):
        """ 每个测试结束后执行的方法 """
        self.stop_timestamp = int(round(time.time() * 1000))
        self.run_stamp = self.stop_timestamp - self.start_timestamp
        self.details[-1]["spendTime"] = self.run_stamp

    def addSuccess(self, test):
        """添加成功信息

        Arguments:
            test -- [测试用例]
        """
        TestResult.addSuccess(self, test)
        self.success_count += 1
        self.details.append({"className": '.'.join(test.id().split('.')[:-1]), \
            "methodName": test._testMethodName, \
            "description": test._testMethodDoc,  \
            "spendTime": 0, \
            "status": self.status[self.lan]["Success"], \
            "log": "test passed!!!"})

    def addError(self, test, err):
        """添加错误信息

        Arguments:
            test -- [测试用例]
            exec_info -- [异常信息]
        """
        TestResult.addError(self, test, err)
        self.error_count += 1
        self.details.append({"className": '.'.join(test.id().split('.')[:-1]), \
            "methodName": test._testMethodName, \
            "description": test._testMethodDoc,  \
            "spendTime": 0, \
            "status": self.status[self.lan]["Error"], \
            "log": self._exc_info_to_string(err, test) \
                    .replace("\n", "<br/>")}\
            )

    def addFailure(self, test, err):
        TestResult.addFailure(self, test, err)
        self.failure_count += 1
        self.details.append({"className": '.'.join(test.id().split('.')[:-1]), \
            "methodName": test._testMethodName, \
            "description": test._testMethodDoc,  \
            "spendTime": 0, \
            "status": self.status[self.lan]["Failure"], \
            "log": self._exc_info_to_string(err, test) \
                    .replace("\n", "<br/>")}\
            )

    def addSkip(self, test, reason):
        TestResult.addSkip(self, test, reason)
        self.skip_count += 1
        self.details.append({"className": '.'.join(test.id().split('.')[:-1]), \
            "methodName": test._testMethodName, \
            "description": test._testMethodDoc,  \
            "spendTime": 0, \
            "status": self.status[self.lan]["Skip"], \
            "log": reason})
