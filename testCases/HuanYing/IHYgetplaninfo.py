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


class IHYgetplaninfo(unittest.TestCase):
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
    def test_gethyplaninfo(self):
        """欢盈计划介绍/剩余可投金额/最多可购买金额接口-正常流程-有数据可查询 """
        # 获取前台token
        token = self.s.get_token()

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","getplaninfo_url")

        r = self.s.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_gethyplaninfo_01(self):
        """欢盈计划介绍/剩余可投金额/最多可购买金额接口-正常流程-无数据可查询 """
        # 获取前台token
        token = self.s.get_token(path=r'/config/HYconf.ini')

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","getplaninfo_url")

        r = self.s.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)


if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYgetplaninfo,[
        "test_gethyplaninfo",
        # "test_gethyplaninfo_01"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYgetplaninfo_report")

    filename = HttpFunc.HttpFunc.get_report("HYgetplaninfo_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)