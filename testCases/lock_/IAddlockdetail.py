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


class IAddlockdetail(unittest.TestCase):
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
    def test_addlockdetail(self):
        """ 添加锁定金额 -正常流程"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()
        value=['QTYW','5000',3,'ceshi']
        data={
            "userId":"%s" % userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        print "返回报文为：{0}".format(r.content)

        # 校验数据库lock_detail
        sql1 = 'select count(*) from lock_detail where user_id ="%s" and business_type="%s"' %(userId,value[0])
        self.md.execute(sql1)
        icount = self.md.fetchone()[0]
        if int(icount)>=1:
            logger.info("校验数据库表lock_detail 成功，校验sql:%s"% sql1)
            print "校验数据库表lock_detail 成功，校验sql:%s"% sql1
        else:
            logger.error("校验数据库表lock_detail 失败，校验sql：%s" % sql1)
            print "校验数据库表lock_detail 失败，校验sql：%s" % sql1

        # 初始化sql
        # sql2 = 'Delete from lock_detail where user_id="%s"; '% (userId,)
        # self.md.execute(sql2)
        # sql3 = 'update account set lock_amount="0.00" where user_id="%s";commit;'% (userId,)
        # self.md.execute(sql3)
    # 异常流程
    def test_addlockdetailExcept_01(self):
        """添加锁定金额 - 备注大于10个字符"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()

        value=['QTYW','99',30,'ceshiasfasdf']
        data={
            "userId":"%s" % userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        print "返回错误信息为: {0}".format(r.json()["resultCode"]["message"])
        assert r.json()["resultCode"]["code"] == 'REMARKS_LENGTH_LONG',"错误信息不匹配！"

    def test_addlockdetailExcept_02(self):
        """添加锁定金额 - 业务类型错误"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()

        value=['DFBQW','99',30,'ceshi01']
        data={
            "userId":"%s" % userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        print "返回错误信息为: {0}".format(r.json()["resultCode"]["message"])
        assert r.json()["resultCode"]["code"] == 'BUSINESSTYPE_NOT_CONFIG',"错误信息不匹配！"

    def test_addlockdetailExcept_03(self):
        """添加锁定金额 - 有效期格式错误"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()

        value=['QTYW','99',-1,'ceshi01']
        data={
            "userId":"%s" % userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        print "返回错误信息为: {0}".format(r.json()["resultCode"]["message"])
        assert r.json()["resultCode"]["code"] == 'VALIDITY_ERROR',"错误信息不匹配！"

    def test_addlockdetailExcept_04(self):
        """添加锁定金额 - 金额格式错误"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()

        value=['QTYW','-10',0,'ceshi01']
        data={
            "userId":"%s" % userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        print "返回错误信息为: {0}".format(r.json()["resultCode"]["message"])
        assert r.json()["resultCode"]["code"] == 'MONEY_FORMAT_ERROR',"错误信息不匹配！"

    def test_addlockdetailExcept_05(self):
        """添加锁定金额 - 金额为空"""
        # 获取用户userID
        sql = 'select id from user where tel_num="%s" '% (self.rf.get_option_value("user","user"),)
        print sql
        self.md.execute(sql)
        userId = self.md.fetchone()[0]
        # print userId
        # 获取后台token
        token = self.s.getBackToken()

        value=['QTYW','',0,'ceshi01']
        data={
            "userId":"%s" % userId,
            "businessType":"%s" % value[0],
            "amount":"%s" % value[1],
            "validity":'%d' % value[2],
            "remark":"%s" % value[3]
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }

        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","addlockdetail_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        print "返回错误信息为: {0}".format(r.json()["faultedProperties"][0])
        assert r.json()["status"] == 417,"错误信息不匹配！"

if __name__=='__main__':
    suite = unittest.TestSuite(map(IAddlockdetail,[
        "test_addlockdetail",
        "test_addlockdetailExcept_01",
        "test_addlockdetailExcept_02",
        "test_addlockdetailExcept_03",
        "test_addlockdetailExcept_04",
        "test_addlockdetailExcept_05"


    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("Addlockdetail_report")

    filename = HttpFunc.HttpFunc.get_report("Addlockdetail_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷预锁定金额接口测试报告',description="测试详情:")
    runner.run(suite)
