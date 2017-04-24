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


class IHYCbuyproduct(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydForeground()
        self.rf = conf_read.ReadFile('\\config\\newHYconf.ini')
        self.md = MysqlDB.MysqlDB('\\config\\newHYconf.ini')
        self.preAmount=""
        self.amount="100"
        self.pre_avaliableAmount()

    def tearDown(self):
        # pa ss
        if self._testMethodName=="test_buyproduct":
            self.db_check()
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def pre_avaliableAmount(self):
        sql="select a.available_amount from account a join user u on u.id=a.user_id where u.tel_num='%s' and a.available_amount<>0" % self.rf.get_option_value(
            "user","username"
        )
        self.md.execute(sql)
        self.preAmount= self.md.fetchone()[0]
    def db_check(self):
        sql="select a.available_amount from account a join user u on u.id=a.user_id where u.tel_num='%s' and a.available_amount<>0" % self.rf.get_option_value(
            "user","username"
        )
        self.md.execute(sql)
        self.afterAmount= self.md.fetchone()[0]
        if int(self.preAmount)-int(self.afterAmount)==int(self.amount):
            logger.info("校验account表成功,校验sql：%s"% sql)
            print "校验account表成功,校验sql：%s"% sql
        else:
            logger.error("校验account表失败,校验sql：%s"% sql)
            print  "校验account表失败,校验sql：%s"% sql

        sql1="select count(*) from loan_lender_detail ld join user u on u.id=ld.user_id where u.tel_num='%s' and TO_DAYS(SYSDATE())=TO_DAYS(ld.create_time)"\
        % self.rf.get_option_value(
            "user","username"
        )
        self.md.execute(sql1)
        icount = self.md.fetchone()[0]
        if int(icount)>=1:
            logger.info("校验loan_lender_detail表成功，有数据插入，校验sql：%s" % sql1)
            print("校验loan_lender_detail表成功，有数据插入，校验sql：%s" % sql1)
        else:
            logger.error("校验loan_lender_detail表失败，有数据插入，校验sql：%s" % sql1)
            print("校验loan_lender_detail表失败，有数据插入，校验sql：%s" % sql1)
    def test_buyproduct(self):
        """欢盈投资-正常流程-无代金券"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"%s"% self.amount,
            "product":"HY"

        }

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_01(self):
        """欢盈投资-正常流程-有代金券"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"100",
            "product":"HY",
            "couponsId":"fea60a70-2046-45e3-aecf-bf883f833a4d"

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    # 异常流程
    def test_buyproduct_ex_01(self):
        """欢盈投资-正常流程-代金券已使用"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"100",
            "product":"HY",
            "couponsId":"fea60a70-2046-45e3-aecf-bf883f833a4d"

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_02(self):
        """欢盈投资-正常流程-代金券不存在"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"100",
            "product":"HY",
            "couponsId":"fea60a70-20d46-45e3-aedddcf-bf883f833a4d"

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_03(self):
        """欢盈投资-正常流程-product取值错误"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"100",
            "product":"gg",

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_04(self):
        """欢盈投资-正常流程-money取值为0"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"0",
            "product":"HY",

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_05(self):
        """欢盈投资-正常流程-money取值为负数"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"-100",
            "product":"HY",

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_06(self):
        """欢盈投资-正常流程-用户余额不足"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"4000",
            "product":"HY",

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_07(self):
        """欢盈投资-正常流程-老用户购买"""
        # 获取前台token
        token = self.s.get_token()

        data={
            "money":"100",
            "product":"HY",

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buyproduct_ex_08(self):
        """欢盈投资-正常流程-代金券状态不对，未审批"""
        # 获取前台token
        token = self.s.get_token(path='\\config\\newHYconf.ini')

        data={
            "money":"100",
            "product":"HY",
            "couponsId":"eca9bc82-c491-4d68-8ade-fe79f2831e1c"

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","buyproduct_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCbuyproduct,[
        "test_buyproduct",
        # "test_buyproduct_01",
        # "test_buyproduct_ex_01",
        # "test_buyproduct_ex_02",
        # "test_buyproduct_ex_03",
        # "test_buyproduct_ex_04",
        # "test_buyproduct_ex_05",
        # "test_buyproduct_ex_06",
        # "test_buyproduct_ex_07",
        # "test_buyproduct_ex_08"

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYbuyproduct_report")

    filename = HttpFunc.HttpFunc.get_report("HYbuyproduct_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)