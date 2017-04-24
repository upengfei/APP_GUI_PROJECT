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


class IGetlockamount(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydForeground()
        self.rf = conf_read.ReadFile(r'/config/lockmoney.ini')
        self.md = MysqlDB.MysqlDB(r'/config/lockmoney.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def test_getlockamount(self):
        """ 查询锁定金额 -正常流程"""

        # 获取后台token
        token = self.s.get_token()

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","fro_base_url")+self.rf.get_option_value("api","getlockamount_url")

        r = self.s.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

        # logger.info(len(r.json()["items"]))
        # 校验数据库lock_detail

if __name__=='__main__':
    suite = unittest.TestSuite(map(IGetlockamount,[
        "test_getlockamount",

    ]))
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("Getlockamount_report")

    filename = HttpFunc.HttpFunc.get_report("Getlockamount_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷预锁定金额接口测试报告',description="查询锁定金额接口测试详情:")
    runner.run(suite)