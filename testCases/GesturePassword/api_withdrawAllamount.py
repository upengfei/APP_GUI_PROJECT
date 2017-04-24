# coding:utf-8
import time
import unittest

from func import *
from func.logInfo import logger
from testCases.app_init import GesturePwdInit


class WithDrawAble(GesturePwdInit):
    """可提现金额测试用例"""
    def test_withdrawAmountAble_normal(self):
        """可提现金额正常流程"""
        token = self.qa.getToken()
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,
        }

        _url = self.rf.get_option_value("app",'host')+self.rf.get_option_value("api",'withdraw_url')

        response = self.qa.post(_url,headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content,))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content,))

if __name__=='__main__':
    suite = unittest.TestSuite(map(WithDrawAble,[
        "test_withdrawAmountAble_normal",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("withdrawAble_report")

    filename = HttpFunc.HttpFunc.get_report("withdrawAble_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷可提现金额接口测试报告',
                                           description="可提现金额接口测试详情:")
    runner.run(suite)