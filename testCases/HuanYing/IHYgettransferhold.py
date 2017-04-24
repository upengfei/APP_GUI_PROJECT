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


class IHYgettransferhold(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydForeground()
        self.rf = conf_read.ReadFile('/config/HYconf.ini')
        self.md = MysqlDB.MysqlDB('/config/HYconf.ini')
        self.rowNum=0


    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()

    def db_check(self):
        sql="select count(*) from loan_lender_detail as ld JOIN (loan as l,user as u) ON (ld.loan_id = l.id and u.id=" \
            "ld.user_id) where u.tel_num=%s and ld.hold_amount!=0 and ld.status!=1 and l.debttype='HY' order by ld.create_time desc;"

        self.md.execute(sql,(self.rf.get_option_value("user","username"),))
        self.rowNum = self.md.fetchone()[0]


    # 正常流程
    def test_gettransferhold(self):
        """ 欢盈理财中债权列表-正常流程-业务参数不为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType": "HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"Entity=1-10"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_gettransferhold_01(self):
        """ 欢盈理财中债权列表-正常流程-业务可选参数为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"HY"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    # 异常流程
    def test_gettransferhold_ex_01(self):
        """ 欢盈理财中债权列表-异常流程-page错误输入"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"HY",
            "page":"ad"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_02(self):
        """ 欢盈理财中债权列表-异常流程-size错误输入"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"HY",
            "size":"ad"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_03(self):
        """ 欢盈理财中债权列表-异常流程-productType为空"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"",
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_04(self):
        """ 欢盈理财中债权列表-异常流程-productType输入错误"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"hg",
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_05(self):
        """ 欢盈理财中债权列表-异常流程-Range参数输入错误"""
        # 获取前台token
        token = self.s.get_token()
        data={
            "productType":"HY",
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            "Range":"2"

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    # def test_gettransferhold_ex_06(self):
    #     """ 欢盈理财中债权列表-异常流程-Range参数为空"""
    #     # 获取前台token
    #     token = self.s.get_token()
    #     data={
    #         "productType":"HY",
    #     }
    #     header={
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    #         "X-Auth-Token":"%s" % token,
    #         "Range":""
    #
    #     }
    #     url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")
    #
    #     r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
    #     logger.info("返回错误信息报文为：{0}".format(r.content))
    #     print "返回错误信息报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYgettransferhold,[
        "test_gettransferhold",
        "test_gettransferhold_01",
        "test_gettransferhold_ex_01",
        "test_gettransferhold_ex_02",
        "test_gettransferhold_ex_03",
        "test_gettransferhold_ex_04",
        "test_gettransferhold_ex_05",
        # "test_gettransferhold_ex_06",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYgettransferhold_report")

    filename = HttpFunc.HttpFunc.get_report("HYgettransferhold_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)
