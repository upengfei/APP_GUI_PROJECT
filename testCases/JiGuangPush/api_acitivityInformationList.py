# coding:utf-8
import time
import unittest
import uuid,json
from func import *
from func.logInfo import logger
from testCases.app_init import GesturePwdInit

class ActivityInfoList(GesturePwdInit):

    def test_activityinfo(self):
        """普通用户获取活动信息列表"""
        # 获取token
        token = self.qa.getToken()
        data = {
            "pageNumber":"1",
            "pageSize":"20"
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))
    def test_activityinfo_01(self):
        """特定用户获取活动详情列表"""
        # 获取token
        token = self.qa.getToken(section='activity_user')
        data = {
            "pageNumber":"1",
            "pageSize":"10"
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                          % response.content
        print("返回报文如下:{0}".format(response.content))
    def test_activityinfo_02(self):
        """用户未登录获取活动详情列表"""
        # 获取token
        # token = self.qa.getToken(section='activity_user')
        data = {
            "pageNumber":"1",
            "pageSize":"10"
        }
        # header={
        #     "X-Auth-Token":"%s" % token
        # }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        print("返回报文如下:{0}".format(response.content))
    def test_activityinfo_exception_pageNumber_01(self):
        """获取活动详情列表-pageNumber为空"""
        # 获取token
        token = self.qa.getToken(section='activity_user')
        data = {
            "pageNumber":"",
            "pageSize":"10"
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content
        # print("返回报文如下:{0}".format(response.content))
    def test_activityinfo_exception_pageNumber_02(self):
        """获取活动详情列表-pageNumber不合法，如取值为:-1"""
        # 获取token
        token = self.qa.getToken(section='activity_user')
        data = {
            "pageNumber":"-1",
            "pageSize":"10"
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content

    def test_activityinfo_exception_pageSize_01(self):
        """获取活动详情列表-pageSize为空"""
        # 获取token
        token = self.qa.getToken(section='activity_user')
        data = {
            "pageNumber":"1",
            "pageSize":""
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                               % response.content

    def test_activityinfo_exception_pageSize_02(self):
        """获取活动详情列表-pageSize取值不合法，如：-16"""
        # 获取token
        token = self.qa.getToken(section='activity_user')
        data = {
            "pageNumber":"1",
            "pageSize":"-16"
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','activityinfo_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content

if __name__ == '__main__':
    suite = unittest.TestSuite(map(ActivityInfoList,[
        "test_activityinfo",
        "test_activityinfo_01",
        "test_activityinfo_02",
        "test_activityinfo_exception_pageNumber_01",
        "test_activityinfo_exception_pageNumber_02",
        "test_activityinfo_exception_pageSize_01",
        "test_activityinfo_exception_pageSize_02",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("ActivityInfoList_report")

    filename = HttpFunc.HttpFunc.get_report("ActivityInfoList_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷App获取活动列表详情测试报告',
                                           description="轻易贷APP获取活动列表详情接口测试详情:")
    runner.run(suite)