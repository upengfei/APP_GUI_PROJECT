# coding:utf-8
import time,sys
import unittest
import json
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCsellproductloandetail(GesturePwdInit):
    """撤资匹配债权明细"""
    # 正常流程
    def test_sploandetail(self):
        """ 撤资匹配债权明细-正常流程"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"100",
            "pageNumber":"1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content
        # 校验数据库



    # 异常流程
    def test_sploandetail_ex_01(self):
        """ 撤资匹配债权明细-异常流程-金额为负数"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"-23",
            "pageNumber":"1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_sploandetail_ex_02(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-金额为0"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"0",
            "pageNumber":"1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_sploandetail_ex_03(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-pageNumber为空"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"100",
            "pageNumber":"",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_sploandetail_ex_04(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-pageSize取值为空"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"100",
            "pageNumber":"1",
            "pageSize":""
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_sploandetail_ex_05(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-amount取值为空"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"",
            "pageNumber":"1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_sploandetail_ex_06(self):
        """ 欢盈撤资审核中债权明细/撤资匹配债权明细-异常流程-amount取值大于0小于100"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "amount":"34",
            "pageNumber":"1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","sellHYLoanDetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCsellproductloandetail,[
        "test_sploandetail",
        "test_sploandetail_ex_01",
        "test_sploandetail_ex_02",
        "test_sploandetail_ex_03",
        "test_sploandetail_ex_04",
        "test_sploandetail_ex_05",
        "test_sploandetail_ex_06"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYsploandetail_report")

    filename = HttpFunc.HttpFunc.get_report("HYsploandetail_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="撤资匹配债权明细接口测试详情:")
    runner.run(suite)
