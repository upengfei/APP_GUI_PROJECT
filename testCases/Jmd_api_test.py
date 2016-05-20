# -*- coding:utf-8 -*-
import time
import unittest,urllib

from func import HTMLTestRunner, HttpFunc, MysqlDB, ReadFile,otherFunc,HttpConfig


class TestCases(unittest.TestCase):

    def setUp(self):
        otherFunc.Func().get_root_path()
        self.rf = ReadFile.ReadFile()
        self.hf = HttpFunc.HttpFunc()
        self.md = MysqlDB.MysqlDB()
        self.hc = HttpConfig.HttpConfig()

    def tearDown(self):
        self.hf.buf_close()
        self.md.cursor_close()
        self.md.conn_close()

    def test_JMD_querytotalexpense(self):
        u"""加盟店接口测试-加盟店理财用户已完成理财金额"""
        sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "ssoId":"%s" % sso_id,
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalexpense_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        print u"请求返回报文：", self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)

        assert(self.hf.get_code() == 200)

    def test_JMD_querytotalexpense_01(self):
        u"""加盟店接口测试-加盟店理财用户已完成理财金额-ssoid为空"""
        sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "ssoId":"",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalexpense_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        print u"请求返回报文：", self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)

        assert self.hf.get_code() == 200

if __name__ == '__main__':

    suite = unittest.TestSuite(
        map(
            TestCases,
            [
                # "test_JMD_querytotalexpense",
                "test_JMD_querytotalexpense_01"


            ]
        )
    )
    # suite.addTest(TestCases('test_rechargebankinfoget'))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HttpFunc.HttpFunc.create_report("jmd_api_report")

    filename = HttpFunc.HttpFunc.get_report("jmd_api_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口测试报告', description=u'测试报告详情： ')
    runner.run(suite)
