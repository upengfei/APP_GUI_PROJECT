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


class CYtransferList(GesturePwdInit):
    """轻易创盈-理资产组合页业务接口测试"""
    def test_CYtransferList_normal(self):
        """轻易创盈-资产组合页业务正常流程"""
        # 获取token
        token = self.qa.getToken()

        header = {
            "X-Auth-Token":"%s" % token
        }

        data={
            "pageNumber":"1",
            "pageSize":"10"
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','cytransferList_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))

if __name__ == '__main__':
    suite = unittest.TestSuite(map(CYtransferList,[
        "test_CYtransferList_normal",


    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("CYtransferList_report")

    filename = HttpFunc.HttpFunc.get_report("CYtransferList_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷App创盈资产组合页测试报告',
                                           description="轻易贷App创盈资产组合页接口测试详情:")
    runner.run(suite)