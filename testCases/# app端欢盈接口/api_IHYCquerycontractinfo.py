# coding:utf-8
import time,sys
import unittest
import json
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCquerycontractinfo(GesturePwdInit):

    # 正常流程
    def test_querycontractinfo(self):
        """ 欢盈投资(撤资)协议接口测试-正常流程-查看范本"""
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"T"
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_01(self):
        """ 欢盈投资(撤资)协议接口测试-正常流程-非范本"""
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"%s" % orderno,
            "type":"1",
            "isModel":"F"
        }
        header={
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content
    # 异常流程
    def test_querycontractinfo_except_01(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-order为空，ismodel为否"""
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"F"
        }
        header={
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_except_02(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-order为空，type为其他"""
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"",
            "type":"abc",
            "isModel":"T",
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_except_03(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-order为空，type为空"""
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"",
            "type":"",
            "isModel":"T"
        }
        header={
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_except_04(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-terminal填写错误"""
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"T",
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}，报文错误信息提示为：{1}".format(r.content,r.json()['resultCode']['message']))
        print "返回报文为：{0},报文错误信息提示为：{1}".format(r.content,r.json()['resultCode']['message'])
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_except_05(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-ismodel填写错误"""
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"G",
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_except_06(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-terminal为空"""

        # 获取订单号
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"%s" % orderno,
            "type":"1",
            "isModel":"F",
        }
        header={
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_querycontractinfo_except_07(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-ismodel为空"""
        # 获取订单号
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"%s" % orderno,
            "type":"1",
            "isModel":"",
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_except_08(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-orderNO值不存在"""
        # 获取订单号
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.qa.getToken()
        data={

            "orderNo":"fdasfdasfds",
            "type":"0",
            "isModel":"F",
        }
        header={
            "X-Auth-Token":"%s" % token
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCquerycontractinfo,[
        "test_querycontractinfo",
        "test_querycontractinfo_01",
        "test_querycontractinfo_except_01",
        "test_querycontractinfo_except_02",
        "test_querycontractinfo_except_03",
        "test_querycontractinfo_except_05",
        "test_querycontractinfo_except_07",
        "test_querycontractinfo_except_08"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCquerycontractinfo_report")

    filename = HttpFunc.HttpFunc.get_report("HYCquerycontractinfo_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="欢盈投资(撤资)协议接口测试详情:")
    runner.run(suite)
