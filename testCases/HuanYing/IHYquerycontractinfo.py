# coding:utf-8
import time,sys
import unittest
import re
import json,uuid
import hashlib
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYquerycontractinfo(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydForeground()
        self.rf = conf_read.ReadFile('/config/HYconf.ini')
        self.md = MysqlDB.MysqlDB('/config/HYconf.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def test_querycontractinfo(self):
        """ 欢盈投资(撤资)协议接口测试-正常流程-查看范本"""
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"T",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_01(self):
        """ 欢盈投资(撤资)协议接口测试-正常流程-非范本"""
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"%s" % orderno,
            "type":"1",
            "isModel":"F",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
    # 异常流程
    def test_querycontractinfo_except_01(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-order为空，ismodel为否"""
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"F",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_except_02(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-order为空，type为其他"""
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"",
            "type":"abc",
            "isModel":"T",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_except_03(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-order为空，type为空"""
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"",
            "type":"",
            "isModel":"T",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_except_04(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-terminal填写错误"""
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"T",
            "terminal":"3"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}，报文错误信息提示为：{1}".format(r.content,r.json()['resultCode']['message']))
        print "返回报文为：{0},报文错误信息提示为：{1}".format(r.content,r.json()['resultCode']['message'])

    def test_querycontractinfo_except_05(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-ismodel填写错误"""
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"",
            "type":"1",
            "isModel":"G",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_except_06(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-terminal为空"""

        # 获取订单号
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"%s" % orderno,
            "type":"1",
            "isModel":"F",
            "terminal":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_querycontractinfo_except_07(self):
        """ 欢盈投资(撤资)协议接口测试-异常流程-ismodel为空"""
        # 获取订单号
        sql = 'select order_no from loan where debttype=\'HY\' and status=\'CLOSE\' limit 1 offset 0;'
        self.md.execute(sql)
        orderno = self.md.fetchone()[0]
        logger.info("获取的订单号为:%s" % orderno)
        # 获取前台token
        token = self.s.get_token()
        data={

            "orderNo":"%s" % orderno,
            "type":"1",
            "isModel":"",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
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
        token = self.s.get_token()
        data={

            "orderNo":"fdasfdasfds",
            "type":"0",
            "isModel":"F",
            "terminal":"0"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","querycontractinfo_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYquerycontractinfo,[
        # "test_querycontractinfo",
        # "test_querycontractinfo_01"
        # "test_querycontractinfo_except_01",
        # "test_querycontractinfo_except_02",
        # "test_querycontractinfo_except_03",
        # "test_querycontractinfo_except_04",
        # "test_querycontractinfo_except_05",
        # "test_querycontractinfo_except_06",
        # "test_querycontractinfo_except_07",
        "test_querycontractinfo_except_08"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYquerycontractinfo_report")

    filename = HttpFunc.HttpFunc.get_report("HYquerycontractinfo_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="欢盈投资(撤资)协议接口测试详情:")
    runner.run(suite)
