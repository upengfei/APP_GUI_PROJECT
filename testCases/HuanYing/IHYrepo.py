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


class IHYrepo(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/HYconf.ini')
        self.md = MysqlDB.MysqlDB(r'/config/HYconf.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()

    # 后台校验
    def db_check(self):
        # 校验invest表
        pass



    # 正常流程

    def test_buyback(self):
        """ 欢盈回购-正常流程"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        data={
            "assignmentId":"61918c75-9128-490a-9a65-4b3f3e9be481",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","buyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
    # 异常流程

    def test_buyback_ex_01(self):
        """ 欢盈回购-异常流程-productType类型为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        data={
            "assignmentId":"61918c75-9128-490a-9a65-4b3f3e9be481",
            "productType":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","buyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyback_ex_02(self):
        """ 欢盈回购-异常流程-productType类型取值错误"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        data={
            "assignmentId":"61918c75-9128-490a-9a65-4b3f3e9be481",
            "productType":"gg"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","buyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyback_ex_03(self):
        """ 欢盈回购-异常流程-assignmentId重复回购"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        data={
            "assignmentId":"61918c75-9128-490a-9a65-4b3f3e9be481",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","buyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)


    def test_buyback_ex_04(self):
        """ 欢盈回购-异常流程-assignmentId不存在"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        data={
            "assignmentId":"61fff918c75-9128-490a-9a65-4b3f3e9be481",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","buyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyback_ex_05(self):
        """ 欢盈回购-异常流程-assignmentId为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        data={
            "assignmentId":"",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","buyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__ == '__main__':
    suite = unittest.TestSuite(map(IHYrepo,[
        "test_buyback",
        # "test_buyback_ex_01",
        # "test_buyback_ex_02",
        # "test_buyback_ex_03",
        # "test_buyback_ex_04",
        # "test_buyback_ex_05"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYbuyback_report")

    filename = HttpFunc.HttpFunc.get_report("HYbuyback_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)