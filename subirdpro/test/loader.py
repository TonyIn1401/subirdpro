# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-16 16:07:43
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-16 16:07:43
'''

import os
import sys
import logging
import unittest
from subirdpro.share.config import Config

class Loader():
    """ 加载测试用例类 """

    def __init__(self):
        self.suits = Config().suits

    def loads(self):
        """加载所有测试用例

        Returns:
            [unittest.TestSuite] -- [返回所有测试用例]
        """
        suites_all = unittest.TestSuite()
        for folder in self.suits:
            try:
                # 添加Path
                file_path = folder["file_path"]
                abs_path = os.path.abspath(__file__)
                dir_name = os.path.dirname(abs_path)
                abs_file_path = os.path.join(dir_name, file_path)
                sys.path.append(abs_file_path)

                suites = unittest.TestSuite()
                for case_file in folder["file"]:
                    try:
                        runable = case_file["runable"]
                        file_name = case_file["name"]
                        class_name = case_file["class"]
                        if not runable:
                            #print("cases in {0}/{1}.py is skiped cause runable status is {2}".format(file_path, file_name, runable))
                            continue
                        cases = unittest.TestSuite()
                        cases_conf = case_file["cases"]
                        module = __import__(file_name)
                        module_obj = getattr(module, class_name)
                        for case in cases_conf:
                            cases.addTest(module_obj(case))
                        suites.addTests(cases)
                    except Exception as exception:
                        suit_error = 'error occured during add the test case, exception: {0}'.format(exception)
                        logging.info(suit_error)
                        print(suit_error)
                        continue
                suites_all.addTests(suites)
            except Exception as exception:
                file_error = 'error occured during the handle the file, exception: {0}'.format(exception)
                logging.info(file_error)
                print(file_error)
                continue
        print("Test suites have beed loaded, and ready for running.")
        return suites_all
