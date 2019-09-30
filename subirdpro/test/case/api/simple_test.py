# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-17 17:47:28
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-17 17:47:28
'''
import time
import logging
import unittest


class SimpleTest(unittest.TestCase):
    """ 用于测试天气的通用接口 """
    def tearDown(self):
        """ 每个测试用例执行之后做操作 """
        logging.info("tearDown for each testcase")
        super(SimpleTest, self).tearDown()

    def setUp(self):
        """ 每个测试用例执行之前做操作 """
        logging.info("setUp for each testcase")

    def test_plus(self):
        """ 测试1+1 """
        self.assertEqual(1+1, 2)

    def test_subtract(self):
        """ 测试1-1"""
        self.assertEqual(1-1, 2)

    def test_multiply(self):
        """ 测试1*1 """
        self.assertEqual(1*1, 1)

    def test_division(self):
        """ 测试1/1 """
        self.assertEqual(1/1, 1)
