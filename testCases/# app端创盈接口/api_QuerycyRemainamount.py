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


class QueryCYRemainAmount(GesturePwdInit):
    """轻易创盈-理财展示页业务接口测试"""
    def test_querycyremainAmount_normal(self):
        """轻易创盈-理财展示页业务正常流程"""
        # 获取token
        token = self.qa.getToken()

        header = {
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','queryCYremainamount_url')
        response = self.qa.post(_url,headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))

if __name__ == '__main__':
    suite = unittest.TestSuite(map(QueryCYRemainAmount,[
        "test_querycyremainAmount_normal",


    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("QueryCYRemainAmount_report")

    filename = HttpFunc.HttpFunc.get_report("QueryCYRemainAmount_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷App创盈理财展示页测试报告',
                                           description="轻易贷App创盈理财展示页接口测试详情:")
    runner.run(suite)