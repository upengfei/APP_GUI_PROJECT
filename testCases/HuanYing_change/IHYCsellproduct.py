# coding:utf-8
import time,sys
import unittest
import re
import json,uuid
import hashlib
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYsellproduct(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydForeground()
        self.rf = conf_read.ReadFile(r'/config/HYconf.ini')
        self.md = MysqlDB.MysqlDB(r'/config/HYconf.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def test_sellproduct(self):
        """ 欢盈撤资-正常流程"""
        # 获取前台token
        token = self.s.get_token(r'/config/HYconf.ini')
        data={
            "amount":"900",
            "product":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    # 异常流程
    def test_sellproduct_ex_01(self):
        """ 欢盈撤资-异常流程-amount为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"",
            "product":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_sellproduct_ex_02(self):
        """ 欢盈撤资-异常流程-amount为0"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"0",
            "product":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_sellproduct_ex_03(self):
        """ 欢盈撤资-异常流程-amount为负数"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"-10",
            "product":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_sellproduct_ex_04(self):
        """ 欢盈撤资-异常流程-product为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"10",
            "product":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_sellproduct_ex_05(self):
        """ 欢盈撤资-异常流程-product取值错误"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"10",
            "product":"fh"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYsellproduct,[
        "test_sellproduct",
        # "test_sellproduct_ex_01",
        # "test_sellproduct_ex_02",
        # "test_sellproduct_ex_03",
        # "test_sellproduct_ex_04",
        # "test_sellproduct_ex_05"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYsellproduct_report")

    filename = HttpFunc.HttpFunc.get_report("HYsellproduct_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)