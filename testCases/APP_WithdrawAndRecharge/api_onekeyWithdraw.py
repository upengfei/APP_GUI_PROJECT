# coding:utf-8
import time,sys
import unittest,json
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class OneKeyWithdraw(GesturePwdInit):

    # 正常流程
    def test_onekeyWithdraw_equal10(self):
        """ 一键提现-用户提现金额等于10元"""
        # 获取前台token
        token = self.qa.getToken(section='withdraw')





        header={
            "X-Auth-Token":"%s" % token

        }
        data = {
            "bankCode":"CCB",
            "bankCard":"6217000010075576820",
            "bankProvince":"北京市",
            "bankCity":"北京市",
            "bankBranch":"中关村软件园支行",
            "amount":"10",
            "busWay":"02",
            "bankName":"建设银行",
            "userName":"张永强"
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","onekeyWithdraw_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_onekeyWithdraw_lt10(self):
        """ 一键提现-用户提现金额小于10元"""
        # 获取前台token
        token = self.qa.getToken(section='withdraw')

        header={
            "X-Auth-Token":"%s" % token

        }
        data = {
            "bankCode":"CCB",
            "bankCard":"6217000010075576820",
            "bankProvince":"北京市",
            "bankCity":"北京市",
            "bankBranch":"中关村软件园支行",
            "amount":"9",
            "busWay":"02",
            "bankName":"建设银行",
            "userName":"张永强"
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","onekeyWithdraw_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_onekeyWithdraw_gt500W(self):
        """ 一键提现-用户提现金额大于上限500w元"""
        # 获取前台token
        token = self.qa.getToken(section='withdraw')

        header={
            "X-Auth-Token":"%s" % token

        }
        data = {
            "bankCode":"CCB",
            "bankCard":"6217000010075576820",
            "bankProvince":"北京市",
            "bankCity":"北京市",
            "bankBranch":"中关村软件园支行",
            "amount":"5000001",
            "busWay":"02"
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","onekeyWithdraw_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(OneKeyWithdraw,[
        "test_onekeyWithdraw_equal10",
        # "test_onekeyWithdraw_lt10",
        # "test_onekeyWithdraw_gt500W"


    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("onekeyWithdraw_report")

    filename = HttpFunc.HttpFunc.get_report("onekeyWithdraw_report")
    fp = file(filename, 'wb')
    runner = HtmlReportTemplate.HTMLTestRunner(stream=fp, title='一键提现接口测试报告', description="一键提现接口接口测试详情:")
    runner.run(suite)