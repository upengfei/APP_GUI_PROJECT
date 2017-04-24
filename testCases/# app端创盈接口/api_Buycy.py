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


class BuyCy(GesturePwdInit):
    """轻易创盈-购买创盈接口测试"""
    def test_buycy_normal(self):
        """轻易创盈-购买创盈接口正常流程-无代金券"""
        # 获取token
        token = self.qa.getToken()

        header = {
            "X-Auth-Token":"%s" % token
        }
        data={
            "money":"100.00",
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','buycy_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))

    def test_buycy_normal_01(self):
        """轻易创盈-购买创盈接口正常流程-有代金券"""
        # 获取token
        token = self.qa.getToken()
        # 获取代金券id
        sql = "select r.* from rewards r LEFT JOIN user u on u.id = r.userid where u.tel_num='%s' and r.`status`='normal' " \
              "limit 0,1;"% self.rf.get_option_value("Appuser","username")
        self.md.execute(sql)
        rewards_id = self.md.fetchone()[0]
        header = {
            "X-Auth-Token":"%s" % token
        }
        data={
            "money":"100.00",
            "couponsId":"%s" % rewards_id
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','buycy_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))

        print("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content

if __name__ == '__main__':
    suite = unittest.TestSuite(map(BuyCy,[
        "test_buycy_normal",
        "test_buycy_normal_01"

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("BuyCy_report")

    filename = HttpFunc.HttpFunc.get_report("BuyCy_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷App创盈购买测试报告',
                                           description="轻易贷App创盈债购买接口测试详情:")
    runner.run(suite)