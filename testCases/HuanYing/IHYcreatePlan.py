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


class IHYcreateplan(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/HYconf.ini')
        self.md = MysqlDB.MysqlDB(r'/config/HYconf.ini')
        self.loanId=""

    def tearDown(self):
        if self._testMethodName == "test_createplan":
            self.db_check()
        self.md.cursor_close()
        self.md.conn_close()

    # 数据库校验
    def db_check(self):
        # 校验组包后的loan的cb_status
        sql='select l.cb_status from loan as l where l.id=%s'
        self.md.execute(sql,(self.loanId,))
        # self.md.scroll(0,mode='absolute')
        cb_status=self.md.fetchone()[0]

        if int(cb_status)==5:
            logger.info("校验成功，组包后的loan的cb_status更新为已打包欢盈,校验sql:%s" %sql)
            print "校验成功，组包后的loan的cb_status更新为已打包欢盈,校验sql:%s" %sql
        else:
            logger.error("校验失败，组包后的loan的cb_status更新为:%s,校验的sql为:%s"% (cb_status,sql))
            print"校验失败，组包后的loan的cb_status更新为:%s,校验的sql为:%s"% (cb_status,sql)

        #校验loan表是否有新的组建包
        sql1="select count(*) from loan l where l.id in (select cb_loan_id from loan where id ='%s')"% self.loanId
        self.md.execute(sql1)
        icount= self.md.fetchone()[0]
        # logger("aaaaaaaa%s"% icount)
        if int(icount)==1:
            logger.info("校验成功，组包后的loan表中存在新组包的数据,校验的sql：%s" % sql1)
            print"校验成功，组包后的loan表中存在新组包的数据,校验的sql：%s" % sql1
        else:
            logger.error("校验失败，组包后的loan表中不存在新组包的数据,校验的sql：%s" % sql1)
            print "校验失败，组包后的loan表中不存在新组包的数据,校验的sql：%s" % sql1
    # 正常流程

    def test_createplan(self):
        """ 欢盈创建计划"""
        sql="select l.id from loan as l left join contract as ct on ct.loan_id=l.id left join user_profile as up " \
            "on up.id=l.borrow  where l.status='CLOSE' and l.cb_status=1 and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " and ct.user_id=l.borrow order by l.repay_date desc limit 0,1;"
        try:
            self.md.execute(sql)
            self.loanId=self.md.fetchone()[0]
        except Exception as e:
            logger.error(e)
            print e
        # self.loanId='430e5d9e-6dc7-4c49-9369-bb8653b0262e'
        logger.info("待组包的loanID为：%s" % self.loanId)
        print "待组包的loanID为：%s" % self.loanId

        # 获取管理台token
        token = self.s.getBackToken()
        logger.info("管理台获取的token为:%s" % token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"%s" % self.loanId,
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    # 异常流程
    def test_createplan_except_01(self):
        """欢盈创建计划-异常流程-销售比例为空"""
        # sql="select l.id from loan as l left join contract as ct on ct.loan_id=l.id left join user_profile as up " \
        #     "on up.id=l.borrow  where l.status='CLOSE' and l.cb_status=1 and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
        #     " and ct.user_id=l.borrow order by l.repay_date desc limit 0,1;"
        # self.md.execute(sql)
        # self.loanId=self.md.fetchone()[0]
        # logger.info("待组包的loanID为：%s" % self.loanId)
        # print "待组包的loanID为：%s" % self.loanId

        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        data={
            "saleRatio":"",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)
    def test_createplan_except_02(self):
        """ 欢盈创建计划-异常流程-销售比例等于0"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        data={
            "saleRatio":"0",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"159",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_03(self):
        """ 欢盈创建计划-异常流程-销售比例小于0"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        data={
            "saleRatio":"-1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"159",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_04(self):
        """ 欢盈创建计划-异常流程-销售比例大于100"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        data={
            "saleRatio":"2",
            "amount":"1000",
            "interestRate":"8.03",
            "copiesAmount":"100",
            "day":"159",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_05(self):
        """ 欢盈创建计划-异常流程-总金额为负数"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"-1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"159",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_06(self):
        """ 欢盈创建计划-异常流程-总金额为0"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        data={
            "saleRatio":"1",
            "amount":"0",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_07(self):
        """ 欢盈创建计划-异常流程-年利率为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_08(self):
        """ 欢盈创建计划-异常流程-每份价格为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"80",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"",
            "day":"159",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_09(self):
        """ 欢盈创建计划-异常流程-每份价格介于0-100"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"99",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_10(self):
        """ 欢盈创建计划-异常流程-每份价格大于100"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"101",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_11(self):
        """ 欢盈创建计划-异常流程-每份价格等于0"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"0",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_12(self):
        """ 欢盈创建计划-异常流程-每份价格小于0"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"-10",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_13(self):
        """ 欢盈创建计划-异常流程-赎回天数为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_14(self):
        """ 欢盈创建计划-异常流程-计息理财前几天为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_15(self):
        """ 欢盈创建计划-异常流程-组包债权为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
    def test_createplan_except_16(self):
        """ 欢盈创建计划-异常流程-组包债权不存在"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5fffffd9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_17(self):
        """ 欢盈创建计划-异常流程-组包债权已使用"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)


    def test_createplan_except_18(self):
        """ 欢盈创建计划-异常流程-起投金额为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_19(self):
        """ 欢盈创建计划-异常流程-起投金额为0"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"0",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_20(self):
        """ 欢盈创建计划-异常流程-起投金额为负数"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"-100",
            "product":"HY"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_21(self):
        """ 欢盈创建计划-异常流程-product为空"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":""

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_createplan_except_22(self):
        """ 欢盈创建计划-异常流程-product为取值错误"""
        # 获取管理台token
        token = self.s.getBackToken()
        logger.info(token)

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        data={
            "saleRatio":"1",
            "amount":"1000",
            "interestRate":"14.6",
            "copiesAmount":"100",
            "day":"152",
            "beforeDay":"4",
            "loanIdS":"430e5d9e-6dc7-4c49-9369-bb8653b0262e",
            "investMinAmount":"100",
            "product":"gd"

        }
        url = self.rf.get_option_value("http","back_base_url")+self.rf.get_option_value("api","createplan_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYcreateplan,[
        # "test_createplan",
        "test_createplan_except_01",
        "test_createplan_except_02",
        "test_createplan_except_03",
        "test_createplan_except_04",
        "test_createplan_except_05",
        "test_createplan_except_06",
        "test_createplan_except_07",
        "test_createplan_except_08",
        # "test_createplan_except_09",
        # "test_createplan_except_10",
        "test_createplan_except_11",
        "test_createplan_except_12",
        "test_createplan_except_13",
        "test_createplan_except_14",
        "test_createplan_except_15",
        "test_createplan_except_16",
        "test_createplan_except_17",
        "test_createplan_except_18",
        "test_createplan_except_19",
        "test_createplan_except_20",
        "test_createplan_except_21",
        "test_createplan_except_22"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYcreateplan_report")

    filename = HttpFunc.HttpFunc.get_report("HYcreateplan_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)