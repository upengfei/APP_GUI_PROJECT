# coding:utf-8
import time,sys
import unittest
from testCases.app_init import GesturePwdInit
import json
import time
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCbuyproduct(GesturePwdInit):

    # 正常流程
    # def pre_avaliableAmount(self):
    #     sql="select a.available_amount from account a join user u on u.id=a.user_id where u.tel_num='%s' and a.available_amount<>0" % self.rf.get_option_value(
    #         "user","username"
    #     )
    #     self.md.execute(sql)
    #     self.preAmount= self.md.fetchone()[0]
    # def db_check(self):
    #     sql="select a.available_amount from account a join user u on u.id=a.user_id where u.tel_num='%s' and a.available_amount<>0" % self.rf.get_option_value(
    #         "user","username"
    #     )
    #     self.md.execute(sql)
    #     self.afterAmount= self.md.fetchone()[0]
    #     if int(self.preAmount)-int(self.afterAmount)==int(self.amount):
    #         logger.info("校验account表成功,校验sql：%s"% sql)
    #         print "校验account表成功,校验sql：%s"% sql
    #     else:
    #         logger.error("校验account表失败,校验sql：%s"% sql)
    #         print  "校验account表失败,校验sql：%s"% sql
    #
    #     time.sleep(1)
    #     sql1="select count(*) from loan_lender_detail ld join user u on u.id=ld.user_id where u.tel_num='%s' and " \
    #          "TO_DAYS(SYSDATE())=TO_DAYS(ld.create_time);" % self.rf.get_option_value("user","username")
    #     self.md.execute(sql1)
    #     icount = self.md.fetchone()[0]
    #
    #     if int(icount)>=1:
    #         logger.info("校验loan_lender_detail表成功，有数据插入，校验sql：%s" % sql1)
    #         print("校验loan_lender_detail表成功，有数据插入，校验sql：%s" % sql1)
    #     else:
    #         logger.error("校验loan_lender_detail表失败，没有数据插入，校验sql：%s" % sql1)
    #         print("校验loan_lender_detail表失败，没有数据插入，校验sql：%s" % sql1)
    #
    #     assert int(icount)>=1
    def test_buyproduct(self):
        """欢盈投资-正常流程-无代金券"""
        # 购买欢盈时，先查询用户可用余额
        sql="select a.available_amount from account a join user u on u.id=a.user_id where u.tel_num='%s' and a.available_amount<>0" % self.rf.get_option_value(
            "Appuser","username"
        )
        self.md.execute(sql)
        preAmount= self.md.fetchone()[0]

        # 获取前台token
        token = self.qa.getToken()
        amount = 100
        data={
            "money":"%s"% amount,

        }

        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content
        # 购买成功后，校验数据库
        sql="select a.available_amount from account a join user u on u.id=a.user_id where u.tel_num='%s' and a.available_amount<>0" % self.rf.get_option_value(
            "Appuser","username"
        )
        self.md.execute(sql)
        afterAmount= self.md.fetchone()[0]
        if int(preAmount)-int(afterAmount)==int(amount):
            logger.info("校验account表成功,校验sql：%s"% sql)
            print "校验account表成功,校验sql：%s"% sql
        else:
            logger.error("校验account表失败,校验sql：%s"% sql)
            print  "校验account表失败,校验sql：%s"% sql

        time.sleep(5)
        sql1="select count(*) from loan_lender_detail ld join user u on u.id=ld.user_id where u.tel_num='%s' and " \
             "TO_DAYS(SYSDATE())=TO_DAYS(ld.create_time);" % self.rf.get_option_value("Appuser","username")
        self.md.execute(sql1)
        icount = self.md.fetchone()[0]

        if int(icount)>=1:
            logger.info("校验loan_lender_detail表成功，有数据插入，校验sql：%s" % sql1)
            print("校验loan_lender_detail表成功，有数据插入，校验sql：%s" % sql1)
        else:
            logger.error("校验loan_lender_detail表失败，没有数据插入，校验sql：%s" % sql1)
            print("校验loan_lender_detail表失败，没有数据插入，校验sql：%s" % sql1)

        assert int(icount)>=1,"数据库校验失败！校验sql：%s"%sql1


    def test_buyproduct_01(self):
        """欢盈投资-正常流程-有代金券"""
        # 获取代金券ID
        sql = "select r.id from rewards r LEFT JOIN user u on u.id = r.userid where u.tel_num='%s' and r.`status`='normal' " \
              "and r.expirydate>NOW();"% self.rf.get_option_value("Appuser","username")
        self.md.execute(sql)
        rewards_id = self.md.fetchone()[0]

        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"100",
            "couponsId":"%s" % rewards_id

        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    # 异常流程
    def test_buyproduct_ex_01(self):
        """欢盈投资-异常流程-代金券已使用"""
        # 获取已使用的代金券ID
        sql = "select r.id from rewards r LEFT JOIN user u on u.id = r.userid where u.tel_num='%s' and r.`status`='used' " \
              "and r.expirydate>NOW();"% self.rf.get_option_value("Appuser","username")
        self.md.execute(sql)
        rewards_id = self.md.fetchone()[0]
        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"100",
            "couponsId":"%s" % rewards_id

        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_buyproduct_ex_02(self):
        """欢盈投资-异常流程-代金券不存在"""
        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"100",
            "couponsId":"fea60a70-20d46-45e3-aedddcf-bf883f833a4d"

        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content


    def test_buyproduct_ex_03(self):
        """欢盈投资-异常流程-money取值为0"""
        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"0",

        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_buyproduct_ex_04(self):
        """欢盈投资-异常流程-money取值为负数"""
        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"-100"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_buyproduct_ex_05(self):
        """欢盈投资-异常流程-用户余额不足"""
        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"1000000"

        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))

        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_buyproduct_ex_06(self):
        """欢盈投资-异常流程-老用户购买"""
        # 获取前台token
        token = self.qa.getToken(section='olduser')

        data={
            "money":"100"

        }
        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_buyproduct_ex_07(self):
        """欢盈投资-异常流程-代金券状态不对，未审批"""
        # 获取未审批的代金券ID
        sql = "select r.id from rewards r LEFT JOIN user u on u.id = r.userid where u.tel_num='%s' and r.`status`='draft' " \
              "and r.expirydate>NOW();"% self.rf.get_option_value("Appuser","username")
        self.md.execute(sql)
        rewards_id = self.md.fetchone()[0]

        # 获取前台token
        token = self.qa.getToken()

        data={
            "money":"100",
            "couponsId":"%s" % rewards_id

        }
        header={
            "X-Auth-Token":"%s" % token,
            # "Range":"Entity=1-10"
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","buyproduct_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCbuyproduct,[
        "test_buyproduct",
        "test_buyproduct_01",
        "test_buyproduct_ex_01",
        "test_buyproduct_ex_02",
        "test_buyproduct_ex_03",
        "test_buyproduct_ex_04",
        "test_buyproduct_ex_05",
        "test_buyproduct_ex_06",
        "test_buyproduct_ex_07",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYbuyproduct_report")

    filename = HttpFunc.HttpFunc.get_report("HYbuyproduct_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)