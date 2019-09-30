# _*_ coding: utf-8 _*_
'''
    @Author: zhaoxiang.zheng
    @Date: 2019-09-16 16:24:37
    @Last Modified by:   zhaoxiang.zheng
    @Last Modified time: 2019-09-16 16:24:37
'''

import os
import json

class Config():
    """ 配置类 """

    def __init__(self):
        settings = self._get_config()
        self.email = settings["email"]
        self.suits = settings["suits"]
        self.host = settings["host"]
        self.constant = settings["constant"]

    def _get_config(self):
        """ 获取Json配置文件数据 """
        try:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/settings.json')
            with open(path, 'r', encoding='UTF-8') as f:
                conf_str = json.load(f)
            return conf_str.decode() if isinstance(conf_str, bytes) else conf_str
        except Exception as exception:
            print("exception occurred while getting config: ", exception)
            return ""

if __name__ == '__main__':
    SUITS = Config().suits
    for case in SUITS:
        print(case)
