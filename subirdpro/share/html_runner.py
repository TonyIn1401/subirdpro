# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-19 17:36:10
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-19 17:36:10
'''

import sys
import time
import json
import datetime
from subirdpro.share.html_templete import TestTemplate
from subirdpro.share.html_result import HtmlResult

class HTMLRunner(TestTemplate):
    """ 执行测试用例并导出HTML测试报告 """

    def __init__(self, \
        language=0, \
        stream=sys.stdout, \
        title=None, \
        test_name=None, \
        description=None, \
        test_person=''):

        self.language = self.LAN[language]

        if title is None:
            self.title = self.LABEL_HTML[self.language]["TitlePage"]
        else:
            self.title = title

        if test_name is None:
            self.test_name = self.DEFAULT_TEST_NAME
        else:
            self.test_name = test_name

        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
        
        self.test_person = self.DEFAULT_TESTER if test_person == '' else test_person

        self.stream = stream
        self.start_time = datetime.datetime.now()
        self.start_timestamp = int(round(time.time() * 1000))
        self.stop_time = datetime.datetime.now()
        self.stop_timestamp = 0
        self.pass_rate = '0.0%'

    def run(self, test):
        "Run the given test case or test suite."
        result = HtmlResult(self.language)
        test(result)
        self.stop_time = datetime.datetime.now()
        self.stop_timestamp = int(round(time.time() * 1000))
        print("self.stop_time ", self.stop_time)
        result_data = self.generate_report(result)
        #print('\nTime Elapsed: %s'.format % (self.stopTime-self.startTime), file=sys.stderr)
        return result_data

    def generate_report(self, result):
        """ 导出报告 """
        result_data = self.generate_result_date(result)
        temp_detail_body = self.generate_detail_body()
        temp_detail_header = self.generate_detail_header()
        summary = self.generate_summary()
        script = self.generate_script()
        output = self.HTML_TEMP % dict(
            title_page=self.LABEL_HTML[self.language]["TitlePage"],
            title_report=self.LABEL_HTML[self.language]["TitleReport"],
            title_summary=self.LABEL_HTML[self.language]["TitleSummary"],
            title_detail=self.LABEL_HTML[self.language]["TitleDetail"],
            title_echart=self.LABEL_SCRIPT[self.language]["TitleEchart"],
            label_show=self.LABEL_SCRIPT[self.language]["LabelShow"],
            label_hidden=self.LABEL_SCRIPT[self.language]["LabelHidden"],
            label_success=self.STATUS[self.language]["Success"],
            label_failure=self.STATUS[self.language]["Failure"],
            label_error=self.STATUS[self.language]["Error"],
            label_skip=self.STATUS[self.language]["Skip"],
            temp_css=self.CSS,
            temp_script=script,
            temp_summary=summary,
            temp_detail_header=temp_detail_header,
            temp_detail_body=temp_detail_body,
            result_data=result_data,
        )
        self.stream.write(output.encode('utf8'))
        return result_data

    def generate_script(self):
        """导出Script的HTML

        Returns:
            [string] -- [Script的HTML]
        """
        script = self.SCRIPT
        return script

    def generate_summary(self):
        """导出Summary的HTML

        Returns:
            [string] -- [Summary的HTML]
        """
        summary = self.HTML_SUMMARY % dict(
            test_name=self.LABEL_SUMMARY[self.language]["TestName"],
            test_count=self.LABEL_SUMMARY[self.language]["TestCount"],
            test_success=self.LABEL_SUMMARY[self.language]["TestSuccess"],
            test_failure=self.LABEL_SUMMARY[self.language]["TestFailure"],
            test_skip=self.LABEL_SUMMARY[self.language]["TestSkip"],
            test_error=self.LABEL_SUMMARY[self.language]["TestError"],
            test_begin=self.LABEL_SUMMARY[self.language]["TestBegin"],
            test_spend=self.LABEL_SUMMARY[self.language]["TestSpend"]
        )
        return summary

    def generate_detail_header(self):
        """导出Detail筛选器的HTML

        Returns:
            [string] -- [Detail筛选器的HTML]
        """
        detail_header = self.HTML_DETAIL_HEADER % dict(
            class_filter=self.LABEL_DETAIL_HEADER[self.language]["ClassFilter"],
            result_filter=self.LABEL_DETAIL_HEADER[self.language]["ResultFilter"],
            total_count=self.LABEL_DETAIL_HEADER[self.language]["TotalCount"],
            success_count=self.STATUS[self.language]["Success"],
            fail_count=self.STATUS[self.language]["Failure"],
            error_count=self.STATUS[self.language]["Error"],
            skip_count=self.STATUS[self.language]["Skip"],
        )
        return detail_header

    def generate_detail_body(self):
        """导出Detail的HTML

        Returns:
            [string] -- [Detail的HTML]
        """
        detail_body = self.HTML_DETAIL_BODY % dict(
            test_id=self.LABEL_DETAIL_BODY[self.language]["TestId"],
            test_class=self.LABEL_DETAIL_BODY[self.language]["TestClass"],
            test_method=self.LABEL_DETAIL_BODY[self.language]["TestMethod"],
            test_desc=self.LABEL_DETAIL_BODY[self.language]["TestDesc"],
            test_stime=self.LABEL_DETAIL_BODY[self.language]["TestSTime"],
            test_result=self.LABEL_DETAIL_BODY[self.language]["TestResult"],
            test_operation=self.LABEL_DETAIL_BODY[self.language]["Operation"],
        )
        return detail_body

    def generate_result_date(self, result):
        """ 导出测试结果 """
        result_data = {}
        pass_rate = float(0) if result.testsRun == 0 \
            else (float(result.success_count) / float(result.testsRun) * 100)
        self.pass_rate = str("%.2f%%" % pass_rate)

        result_data = {
            "testName":self.test_name,
            "testAll": len(result.details),
            "testPass": result.success_count,
            "testFail": result.failure_count,
            "testSkip": result.skip_count,
            "testError": result.error_count,
            "testRate": self.pass_rate,
            "beginTime": str(self.start_time)[:19],
            "totalTime": '{} s'.format(float((self.stop_timestamp -self.start_timestamp)/1000)),
            "testResult":result.details
        }

        return json.dumps(result_data)
