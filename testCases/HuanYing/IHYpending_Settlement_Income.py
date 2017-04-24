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


class IHYpendingsettlementincome(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydForeground()
        self.rf = conf_read.ReadFile(r'/config/HYconf.ini')
        self.md = MysqlDB.MysqlDB(r'/config/HYconf.ini')
        self.holdingCYInterest=""
        self.yesterCYInterest=""

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
        # self.db_check()
    # 正常流程


    def test_pendingsettlementincome(self):
        """ 待结算收益&昨日收益"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}，昨日收益为:{1}，待结算收益为:{2}".format(r.content,r.json()["entity"]["yesterInterest"],
                                                      r.json()["entity"]["holdingInterest"]))
        print "返回报文为:{0}，昨日收益为:{1}，待结算收益为:{2}".format(r.content,r.json()["entity"]["yesterInterest"],
                                                      r.json()["entity"]["holdingInterest"])
        self.holdingCYInterest=r.json()["entity"]["holdingInterest"]
        self.yesterCYInterest=r.json()["entity"]["yesterInterest"]

    # 异常案例
    def test_pendingsettlementincome_ex_01(self):
        """ 待结算收益&昨日收益-产品类型错误"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"gh"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)

    def test_pendingsettlementincome_ex_02(self):
        """ 待结算收益&昨日收益-产品类型为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)


if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYpendingsettlementincome,[
        "test_pendingsettlementincome",
        "test_pendingsettlementincome_ex_01",
        "test_pendingsettlementincome_ex_02"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYpendingsettlementincome_report")

    filename = HttpFunc.HttpFunc.get_report("HYpendingsettlementincome_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="待结算收益与昨日结算收益测试详情:")
    runner.run(suite)