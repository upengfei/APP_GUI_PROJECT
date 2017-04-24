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


class IGetlockdetail(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/lockmoney.ini')
        self.md = MysqlDB.MysqlDB(r'/config/lockmoney.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def test_getlockdetail(self):
        """ 添加锁定金额 -正常流程"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()

        data={
            "userId":"%s" % userId,
            "curPageNo":"1",
            "pageSize":"10"

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","getlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        print "返回报文为：{0}".format(r.content)

        # 校验数据库lock_detai

if __name__=='__main__':
    suite = unittest.TestSuite(map(IGetlockdetail,[
        "test_getlockdetail",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("Getlockdetail_report")

    filename = HttpFunc.HttpFunc.get_report("Getlockdetail_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷预锁定金额接口测试报告',description="获取锁定业务明细接口测试详情:")
    runner.run(suite)
