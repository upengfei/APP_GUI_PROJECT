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


class ISetlockdetail(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/lockmoney.ini')
        self.md = MysqlDB.MysqlDB(r'/config/lockmoney.ini')
        self.userId=""
        self.token=""
        self.addlockdetail()
    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()

    def addlockdetail(self):
        """ 添加锁定金额"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        # print sql
        self.md.execute(sql)
        self.userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        self.token = self.s.getBackToken()
        value=['QTYW','99',30,'ceshi']
        data={
            "userId":"%s" % self.userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % self.token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        self.s.post(url,data=json.dumps(data),headers=header,verify=False)
    # 正常流程
    def test_setlockdetail(self):
        """ 修改锁定金额 -正常流程-修改金额"""
        # 获取用户userID
        sql = 'select id from lock_detail where user_id="%s"; '% (self.userId,)
        self.md.execute(sql)
        lockdetail_id = self.md.fetchone()[0]
        # print lockdetail_id


        data={

            "detailId":"%s" % lockdetail_id

        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % self.token
        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","setlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        print "返回报文为：{0}".format(r.content)

        # 校验数据库lock_detail
        sql1 = 'select status from lock_detail where user_id = "%s";'% self.userId
        self.md.execute(sql1)
        istatus = self.md.fetchone()[0]
        if int(istatus)==0:
            logger.info("校验数据库成功，校验sql：%s,修改后的状态为:%s" % (sql1,istatus))
            print "校验数据库成功，校验sql：%s,修改后的状态为:%s" % (sql1,istatus)
        else:
            logger.error("校验数据库失败，校验sql：%s,修改后的状态为:%s" % (sql1,istatus))
            print "校验数据库失败，校验sql：%s,修改后的状态为:%s" % (sql1,istatus)

        #初始化sql
        sql2 = 'Delete from lock_detail where user_id="%s";commit; '% (self.userId,)
        self.md.execute(sql2)

if __name__=='__main__':
    suite = unittest.TestSuite(map(ISetlockdetail,[
        "test_setlockdetail",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("setlockdetail_report")

    filename = HttpFunc.HttpFunc.get_report("setlockdetail_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷预锁定金额接口测试报告',description="修改锁定金额接口测试详情:")
    runner.run(suite)       #