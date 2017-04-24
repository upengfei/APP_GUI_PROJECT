# coding:utf-8
import time,sys
import unittest
import re
import json,uuid
from testCases.app_init import *
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class GetCySumInterest(GesturePwdInit):
    """轻易创盈-获取收益接口测试"""
    def test_getSumInterest_normal(self):
        """轻易创盈-获取收益正常流程"""
        # 获取token
        token = self.qa.getToken()

        header = {
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','getSuminterest_url')
        response = self.qa.post(_url,headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))

if __name__ == '__main__':
    suite = unittest.TestSuite(map(GetCySumInterest,[
        "test_getSumInterest_normal",
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("getSumInterest_report")

    filename = HttpFunc.HttpFunc.get_report("getSumInterest_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷App创盈获取收益详情测试报告',
                                           description="轻易贷App创盈获取收益接口测试详情:")
    runner.run(suite)