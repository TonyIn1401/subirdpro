# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-16 15:54:39
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-16 15:54:39
'''

import unittest
import json
import logging
import requests

class WeatherCommonApi(unittest.TestCase):
    """ 用于测试天气的通用接口 """
    def tearDown(self):
        """ 每个测试用例执行之后做操作 """
        logging.info("tearDown for each testcase")
        super(WeatherCommonApi, self).tearDown()

    def setUp(self):
        """ 每个测试用例执行之前做操作 """
        logging.info("setUp for each testcase")

    @classmethod
    def tearDownClass(cls):
        """ 必须使用 @ classmethod装饰器, 所有test运行完后运行一次 """
        logging.info("tearDown Class for testcase")

    @classmethod
    def setUpClass(cls):
        """ 必须使用@classmethod 装饰器,所有test运行前运行一次 """
        logging.info("SetUp Class for testcase")
        cls.host = 'http://apis.haoservice.com/weather'

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

    def test_normal(self):
        """ 测试正常情况下返回 """
        payload = {"key":"80def4e6b50e4a118c14c1d20f6ab50d", "paybyvas":"false", "cityname":"上海"}
        resp = requests.get(self.host, params=payload)
        resp_json = json.loads(resp.text)
        self.assertEqual(resp_json['error_code'], 0)

    def test_without_key(self):
        """ 测试不传入app key情况下返回 """
        payload = {"paybyvas":"false", "cityname":"上海"}
        resp = requests.get(self.host, params=payload)
        resp_json = json.loads(resp.text)
        self.assertEqual(resp_json['error_code'], 10001)

    def test_without_cityname(self):
        """ 测试不传入城市名情况下返回 """
        payload = {"key":"80def4e6b50e4a118c14c1d20f6ab50d", "paybyvas":"false"}
        resp = requests.get(self.host, params=payload)
        resp_json = json.loads(resp.text)
        self.assertEqual(resp_json['error_code'], 200601)

    def test_without_paybyvas(self):
        """ 测试不传入paybyvas情况下返回 """
        payload = {"key":"80def4e6b50e4a118c14c1d20f6ab50d", "cityname":"上海"}
        resp = requests.get(self.host, params=payload)
        resp_json = json.loads(resp.text)
        self.assertEqual(resp_json['error_code'], 0)
