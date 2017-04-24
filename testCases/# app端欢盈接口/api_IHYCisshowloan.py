# coding:utf-8
import time,sys
import unittest
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCisshowloan(GesturePwdInit):

    # 正常流程
    def test_isshowloan(self):
        """ 欢盈是否显示新手标-正常流程"""
        # 获取前台token
        token = self.qa.getToken()

        header={
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","isshowhyloan_url")

        r = self.qa.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCisshowloan,[
        "test_isshowloan",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYisshow_report")

    filename = HttpFunc.HttpFunc.get_report("HYisshow_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈是否显示新手标接口测试报告',description="是否显示新手标接口测试详情:")
    runner.run(suite)