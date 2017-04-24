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


class GetTransferHolding(GesturePwdInit):
    """轻易创盈-获取理财中列表接口测试"""
    def test_gettransferholding_normal(self):
        """轻易创盈-获取理财中列表正常流程"""
        # 获取token
        token = self.qa.getToken()

        header = {
            "X-Auth-Token":"%s" % token
        }

        data={
            "pageNumber":"1",
            "pageSize":"10"
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','gettransferholding_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))

if __name__ == '__main__':
    suite = unittest.TestSuite(map(GetTransferHolding,[
        "test_gettransferholding_normal",
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("gettransferholding_report")

    filename = HttpFunc.HttpFunc.get_report("gettransferholding_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷App创盈获取理财中列表详情测试报告',
                                           description="轻易贷App创盈获取创盈理财中列表接口测试详情:")
    runner.run(suite)