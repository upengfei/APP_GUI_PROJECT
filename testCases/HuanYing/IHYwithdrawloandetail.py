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


class IHYwithdrawloandetail(unittest.TestCase):
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
    def test_withdrawloandetail(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-正常流程"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"23",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
    # 异常流程
    def test_withdrawloandetail_ex_01(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-金额为负数"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"-23",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_withdrawloandetail_ex_02(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-金额为0"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"0",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_withdrawloandetail_ex_03(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-productType为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"100",
            "productType":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_withdrawloandetail_ex_04(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-productType取值错误"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"100",
            "productType":"gh"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_withdrawloandetail_ex_05(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-productType取值错误"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "amount":"",
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYwithdrawloandetail,[
        "test_withdrawloandetail",
        "test_withdrawloandetail_ex_01",
        "test_withdrawloandetail_ex_02",
        "test_withdrawloandetail_ex_03",
        "test_withdrawloandetail_ex_04",
        "test_withdrawloandetail_ex_05"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYwithdrawloandetail_report")

    filename = HttpFunc.HttpFunc.get_report("HYwithdrawloandetail_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)
