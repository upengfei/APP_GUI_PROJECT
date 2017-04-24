# coding:utf-8
import time
import unittest

from func import *
from func.logInfo import logger
from testCases.app_init import GesturePwdInit


class GesturePasswd(GesturePwdInit):

    def test_gesturePsswd_normal_unlock(self):
        """ 查询手势密码是否锁定-正常流程-未锁定 """
        # 获取token
        token = self.qa.getToken()
        logger.info("获取的token为:{0}".format(token,))
        header={
            "X-Auth-Token":"%s" % token
        }

        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','query_url')

        contxt = self.qa.post(_url,headers=header,verify=False)

        logger.info("返回报文如下:{0}".format(contxt.content))
        assert contxt.json()['status'] == 200 and contxt.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % contxt.content

        print "返回报文如下:{0}".format(contxt.content,)

    def test_gesturePsswd_normal_lock(self):
        """ 查询手势密码是否锁定-正常流程-锁定 """
        # 获取token
        token = self.qa.getToken()
        header={
            "X-Auth-Token":"%s" % token,
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','query_url')

        contxt = self.qa.post(_url,headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(contxt.content))
        assert contxt.json()['status'] == 200 and contxt.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % contxt.content

        print "返回报文如下:{0}".format(contxt.content,)

if __name__=='__main__':
    suite = unittest.TestSuite(map(GesturePasswd,[
        # "test_gesturePsswd_normal_unlock",
        "test_gesturePsswd_normal_lock"

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("gesturePasswd_report")

    filename = HttpFunc.HttpFunc.get_report("gesturePasswd_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷手势密码验证查询接口测试报告',
                                           description="手势密码验证查询接口测试详情:")
    runner.run(suite)