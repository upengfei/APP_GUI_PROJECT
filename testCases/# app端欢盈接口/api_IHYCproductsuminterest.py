# coding:utf-8
import time,sys
import unittest
import json
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCgetprdsuminterest(GesturePwdInit):
    """待结算收益&昨日收益"""
    def test_getprdsuminterest(self):
        """ 待结算收益&昨日收益"""
        # 获取前台token
        token = self.qa.getToken()

        # data={
        #
        # }
        header={
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","unsettleincome_url")
        print url
        r = self.qa.post(url,headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content
        holdingCYInterest=r.json()["mapData"]["holdingInterest"]
        yesterCYInterest=r.json()["mapData"]["yesterInterest"]
        logger.info("待结算收益:{0},昨日收益:{1}".format(holdingCYInterest,yesterCYInterest))
        print("待结算收益:{0},昨日收益:{1}".format(holdingCYInterest,yesterCYInterest))
    # 异常案例
    def test_getprdsuminterest_ex_01(self):
        """ 待结算收益&昨日收益-token为空"""
        # 获取前台token
        # token = self.qa.getToken()
        data={
        }
        header={
            "X-Auth-Token":""
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_getprdsuminterest_ex_02(self):
        """ 待结算收益&昨日收益-token失效或者错误"""
        # 获取前台token
        # token = self.qa.getToken()
        data={
        }
        header={
            "X-Auth-Token":"dfsafdsa-4df54fgh-3eff-6tgghhh"
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCgetprdsuminterest,[
        "test_getprdsuminterest",
        "test_getprdsuminterest_ex_01",
        "test_getprdsuminterest_ex_02"

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCgetprdsuminterest_report")

    filename = HttpFunc.HttpFunc.get_report("HYCgetprdsuminterest_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="待结算收益与昨日结算收益测试详情:")
    runner.run(suite)