# -*- coding:utf-8 -*-
import time,re
import unittest,urllib

from func import HTMLTestRunner, HttpFunc, MysqlDB, conf_read,BasicFunc,HttpConfig


class TestCases(unittest.TestCase):

    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.rf = conf_read.ReadFile(r'/config/config.ini')
        self.hf = HttpFunc.HttpFunc()
        self.md = MysqlDB.MysqlDB()
        self.hc = HttpConfig.HttpConfig()

    def tearDown(self):
        self.hf.buf_close()
        self.md.cursor_close()
        self.md.conn_close()

# 二十一、加盟店理财用户已完成理财金额-正常流程
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

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 加盟店理财用户已完成理财金额-异常流程
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
        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', "errorCodes:"+find_content1[0]

    def test_JMD_querytotalexpense_02(self):
        u"""加盟店接口测试-加盟店理财用户已完成理财金额-ssoid格式错误"""
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
            "ssoId":"%sfdsre243",
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

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', "errorCodes:"+find_content1[0]

    def test_JMD_querytotalexpense_03(self):
        u"""加盟店接口测试-加盟店理财用户已完成理财金额-token错误"""
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
            "ssoId":"%s" % sso_id ,
            "token":"fdasre45784545"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalexpense_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', "errorCodes:"+find_content1[0]

    def test_JMD_querytotalexpense_04(self):
        u"""加盟店接口测试-加盟店理财用户已完成理财金额-token为空"""
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
            "ssoId":"%s" % sso_id ,
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalexpense_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', "errorCodes:"+find_content1[0]

    def test_JMD_querytotalexpense_05(self):
        u"""加盟店接口测试-加盟店理财用户已完成理财金额-ssoid不存在"""
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
            "ssoId":"46548774541212",
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

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', "errorCodes:"+find_content1[0]

#二十二、 加盟店理财用户理财中金额-正常流程
    def test_JMD_querytotallending(self):
        u"""加盟店接口测试-加盟店理财用户理财中金额"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotallending_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 加盟店理财用户理财中金额-异常流程
    def test_JMD_querytotallending_01(self):
        u"""加盟店接口测试-加盟店理财用户理财中金额-token为空"""
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
            "ssoId":"%s" % sso_id ,
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotallending_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotallending_02(self):
        u"""加盟店接口测试-加盟店理财用户理财中金额-token错误"""
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
            "ssoId":"%s" % sso_id ,
            "token":"fdasfdsa454565654"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotallending_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotallending_03(self):
        u"""加盟店接口测试-加盟店理财用户理财中金额-ssoid错误"""
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
            "ssoId":"4654787945445",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotallending_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotallending_04(self):
        u"""加盟店接口测试-加盟店理财用户理财中金额-ssoid为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotallending_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotallending_05(self):
        u"""加盟店接口测试-加盟店理财用户理财中金额-ssoid格式错误"""
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
            "ssoId":"%sdrfrere4324",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotallending_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]


# 二十三、加盟店用户账户可用余额接口-正常流程
    def test_JMD_queryavailableamount(self):
        u"""加盟店接口测试-根据SSOID查询加盟店用户可用余额"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryavailableamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 加盟店用户账户可用余额接口-异常流程
    def test_JMD_queryavailableamount_01(self):
        u"""加盟店接口测试-根据SSOID查询加盟店用户可用余额-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailableamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailableamount_02(self):
        u"""加盟店接口测试-根据SSOID查询加盟店用户可用余额-token错误"""
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
            "token":"uuurufjd4343"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailableamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailableamount_03(self):
        u"""加盟店接口测试-根据SSOID查询加盟店用户可用余额-SSOID错误"""
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
            "ssoId":"8487454545321",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailableamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailableamount_04(self):
        u"""加盟店接口测试-根据SSOID查询加盟店用户可用余额-SSOID为空"""
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
            "ssoId":" ",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailableamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailableamount_05(self):
        u"""加盟店接口测试-根据SSOID查询加盟店用户可用余额-SSOID格式错误"""
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
            "ssoId":"%sfdfdsr4324",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailableamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

# 二十四、加盟店理财用户可用代金券接口-正常流程
    def test_JMD_queryavailablerewards(self):
        u"""加盟店接口测试-根据SSOID查询加盟店理财用户可用代金券总额"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablerewards_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 加盟店理财用户可用代金券接口-异常流程
    def test_JMD_queryavailablerewards_01(self):
        u"""加盟店接口测试-根据SSOID查询加盟店理财用户可用代金券总额-SSOID为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablerewards_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablerewards_02(self):
        u"""加盟店接口测试-根据SSOID查询加盟店理财用户可用代金券总额-SSOID不存在"""
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
            "ssoId":"345658876544",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablerewards_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablerewards_03(self):
        u"""加盟店接口测试-根据SSOID查询加盟店理财用户可用代金券总额-token错误"""
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
            "token":"4345teedaew21"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablerewards_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablerewards_04(self):
        u"""加盟店接口测试-根据SSOID查询加盟店理财用户可用代金券总额-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablerewards_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablerewards_05(self):
        u"""加盟店接口测试-根据SSOID查询加盟店理财用户可用代金券总额-SSOID格式错误"""
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
            "ssoId":"%srew434",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablerewards_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

# 二十五、加盟店借款用户已还本金金额接口-正常流程
    def test_JMD_querytotalborrowed(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户已还本金金额"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowed_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 加盟店借款用户已还本金金额接口-异常流程
    def test_JMD_querytotalborrowed_01(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户已还本金金额-SSOID为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowed_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowed_02(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户已还本金金额-SSOID参数错误"""
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
            "ssoId":"342t4357998765",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowed_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowed_05(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户已还本金金额-SSOID参数格式错误"""
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
            "ssoId":"%srew432",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowed_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowed_03(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户已还本金金额-token参数错误"""
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
            "token":"EXTERNAL_TOKEN_41e73eecf48cc7b5db20469dc42d0956"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowed_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowed_04(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户已还本金金额-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowed_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

# 二十六、加盟店借款用户未还借款金额接口-正常流程
    def test_JMD_querytotalborrowwingamount(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户未还借款金额"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowwingamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 二十六、加盟店借款用户未还借款金额接口-异常
    def test_JMD_querytotalborrowwingamount_01(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户未还借款金额-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowwingamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowwingamount_02(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户未还借款金额-token错误"""
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
            "token":"EXTERNAL_TOKEN_41e73eecf48cc7b5db20469dc42d0955"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowwingamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowwingamount_03(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户未还借款金额-SSOID错误"""
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
            "ssoId":"58978787443434",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowwingamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowwingamount_04(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户未还借款金额-SSOID为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowwingamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotalborrowwingamount_05(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户未还借款金额-SSOID参数格式错误(非全数字)"""
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
            "ssoId":"qweqre123",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotalborrowwingamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

# 二十七、加盟店借款用户可用授信额度接口
    def test_JMD_queryavailablecredit(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户可用授信额度"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablecredit_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 二十七、加盟店借款用户可用授信额度接口-异常流程
    def test_JMD_queryavailablecredit_01(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户可用授信额度-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablecredit_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablecredit_02(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户可用授信额度-token错误"""
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
            "token":"EXTERNAL_TOKEN_c92f8ecd13d3aca4f01f4cc40a342509"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablecredit_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablecredit_03(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户可用授信额度-SSOID格式错误"""
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
            "ssoId":"%s243",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablecredit_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablecredit_04(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户可用授信额度-SSOID不存在"""
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
            "ssoId":"5678875644",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablecredit_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryavailablecredit_05(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户可用授信额度-SSOID为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryavailablecredit_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

# 二十八、加盟店借款用户违约欠款金额接口-正常流程
    def test_JMD_querytotaloverdueamount(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户违约欠款金额"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotaloverdueamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'
# 二十八、加盟店借款用户违约欠款金额接口-异常
    def test_JMD_querytotaloverdueamount_01(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户违约欠款金额-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotaloverdueamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotaloverdueamount_02(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户违约欠款金额-token错误"""
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
            "token":"gsgfdgdsgdfsgd322"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotaloverdueamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotaloverdueamount_03(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户违约欠款金额-ssoid为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'querytotaloverdueamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotaloverdueamount_04(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户违约欠款金额-ssoid格式错误"""
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
            "ssoId":"%sdfdsre123",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotaloverdueamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_querytotaloverdueamount_05(self):
        u"""加盟店接口测试-根据SSOID查询加盟店借款用户违约欠款金额-ssoid用户不存在"""
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
            "ssoId":"787845548745221",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'querytotaloverdueamount_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]
# 二十九、查询轻易贷会员授信状态和授信额度接口-正常
    def test_JMD_queryusercreditinfo(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryusercreditinfo_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'
# 二十九、查询轻易贷会员授信状态和授信额度接口-异常
    def test_JMD_queryusercreditinfo_01(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度-token为空"""
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
            "token":""
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryusercreditinfo_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryusercreditinfo_02(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度-token错误"""
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
            "token":"dfasfdasr234234"
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryusercreditinfo_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryusercreditinfo_03(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度-SSOID为空"""
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
            + self.rf.get_option_value('JMD_API_URL', 'queryusercreditinfo_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryusercreditinfo_04(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度-SSOID格式不正确"""
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
            "ssoId":"%s454tr",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryusercreditinfo_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_queryusercreditinfo_05(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度-SSOID用户不存在"""
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
            "ssoId":"785455648974521",
            "token":"%s" % jmd_token
        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'queryusercreditinfo_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

# 三十、获取所有在轻易贷成为加盟店的用户数据接口
    def test_JMD_getqydjdmuserinfolist(self):
        u"""加盟店接口测试-根据SSOID查询轻易贷会员授信状态和授信额度-正常流程（openStoreSAPID为0000，查询全部加盟店）"""
        # sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        # self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        # sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "token":"%s" % jmd_token,
            "openStoreSAPID":"0000",
            # "realName":"",
            # "updateDate_begin":"",
            # "updateDate_end":"",
            # "phone":""

        }

        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'getqydjdmuserinfolist_url')\
            + "?"\
            + data

        print u'接口请求的地址为:'+req_url

        content = self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)

        assert find_content[0] == '200'

# 三十、获取所有在轻易贷成为加盟店的用户数据接口-异常
    def test_JMD_getqydjdmuserinfolist_01(self):
        u"""加盟店接口测试-根据查询条件查询轻易贷加盟店信息-机构SAPID为空"""
        # sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        # self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        # sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "token":"%s" % jmd_token,
            "openStoreSAPID":"",


        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'getqydjdmuserinfolist_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print find_content
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '400', u"errorCodes:"+find_content1[0]

    def test_JMD_getqydjdmuserinfolist_02(self):
        u"""加盟店接口测试-根据查询条件查询轻易贷加盟店信息-realName模糊查询"""
        # sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        # self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        # sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "token":"%s" % jmd_token,
            "openStoreSAPID":"0000",
            "realName":"user",
            # "updateDate_begin":"",
            # "updateDate_end":"",

        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'getqydjdmuserinfolist_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print u'请求返回状态：', find_content[0]
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_getqydjdmuserinfolist_03(self):
        u"""加盟店接口测试-根据查询条件查询轻易贷加盟店信息-realName精确查找"""
        # sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        # self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        # sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "token":"%s" % jmd_token,
            "openStoreSAPID":"0000",
            "realName":"user104",
            # "updateDate_begin":"",
            # "updateDate_end":"",

        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'getqydjdmuserinfolist_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print u'请求返回状态：', find_content[0]
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

    def test_JMD_getqydjdmuserinfolist_04(self):
        u"""加盟店接口测试-根据查询条件查询轻易贷加盟店信息-updateDate_begin"""
        # sql = "select sso_id from user_profile where id in(select id from user where name =%s)"
        # self.md.execute(sql, (self.rf.get_option_value("user", "username")))
        # sso_id = self.md.fetchone()[0]
        jmd_token = self.hc.get_jmd_token()  # 获得token值

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
            "Content-Type:application/x-www-form-urlencoded"
            # 'X-Auth-Token:'+str(token)
        ]
        data1 = {
            "token":"%s" % jmd_token,
            "openStoreSAPID":"0000",
            "realName":"",
            "updateDate_begin":"2016-05-26 10:14:22",
            "updateDate_end":"2016-05-26 10:14:22",

        }
        data = urllib.urlencode(data1)
        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('JMD_API_URL', 'getqydjdmuserinfolist_url')\
            +"?"\
            +data

        print u'接口请求的地址为:'+req_url

        content=self.hf.hf_post(req_url, headers=header, arg_type=0,action=0)
        print u"请求返回报文：", content
        find_content = re.findall('.*?status":(.*?),',content,re.S)
        print u'请求返回状态：', find_content[0]
        find_content1 = re.findall('.*?"errorCodes":\{"code":(.*?),',content,re.S)
        assert find_content[0] == '200', u"errorCodes:"+find_content1[0]

if __name__ == '__main__':

    suite = unittest.TestSuite(
        map(
            TestCases,
            [
                "test_JMD_querytotalexpense",
                "test_JMD_querytotalexpense_01",
                "test_JMD_querytotalexpense_02",
                "test_JMD_querytotalexpense_03",
                "test_JMD_querytotalexpense_04",
                "test_JMD_querytotalexpense_05",
                "test_JMD_querytotallending",
                "test_JMD_querytotallending_01",
                "test_JMD_querytotallending_02",
                "test_JMD_querytotallending_03",
                "test_JMD_querytotallending_04",
                "test_JMD_querytotallending_05",
                "test_JMD_queryavailableamount",
                "test_JMD_queryavailableamount_01",
                "test_JMD_queryavailableamount_02",
                "test_JMD_queryavailableamount_03",
                "test_JMD_queryavailableamount_04",
                "test_JMD_queryavailableamount_05",
                "test_JMD_queryavailablerewards",
                "test_JMD_queryavailablerewards_01",
                "test_JMD_queryavailablerewards_02",
                "test_JMD_queryavailablerewards_03",
                "test_JMD_queryavailablerewards_04",
                "test_JMD_queryavailablerewards_05",
                "test_JMD_querytotalborrowed",
                "test_JMD_querytotalborrowed_01",
                "test_JMD_querytotalborrowed_02",
                "test_JMD_querytotalborrowed_03",
                "test_JMD_querytotalborrowed_04",
                "test_JMD_querytotalborrowed_05",
                "test_JMD_querytotalborrowwingamount",
                "test_JMD_querytotalborrowwingamount_01",
                "test_JMD_querytotalborrowwingamount_02",
                "test_JMD_querytotalborrowwingamount_03",
                "test_JMD_querytotalborrowwingamount_04",
                "test_JMD_querytotalborrowwingamount_05",
                "test_JMD_queryavailablecredit",
                "test_JMD_queryavailablecredit_01",
                "test_JMD_queryavailablecredit_02",
                "test_JMD_queryavailablecredit_03",
                "test_JMD_queryavailablecredit_04",
                "test_JMD_queryavailablecredit_05",
                "test_JMD_querytotaloverdueamount",
                "test_JMD_querytotaloverdueamount_01",
                "test_JMD_querytotaloverdueamount_02",
                "test_JMD_querytotaloverdueamount_03",
                "test_JMD_querytotaloverdueamount_04",
                "test_JMD_querytotaloverdueamount_05",
                "test_JMD_queryusercreditinfo",
                "test_JMD_queryusercreditinfo_01",
                "test_JMD_queryusercreditinfo_02",
                "test_JMD_queryusercreditinfo_03",
                "test_JMD_queryusercreditinfo_04",
                "test_JMD_queryusercreditinfo_05",
                "test_JMD_getqydjdmuserinfolist",
                "test_JMD_getqydjdmuserinfolist_01",
                "test_JMD_getqydjdmuserinfolist_02",
                "test_JMD_getqydjdmuserinfolist_03",
                "test_JMD_getqydjdmuserinfolist_04"
            ]
        )
    )
    # suite.addTest(TestCases('test_rechargebankinfoget'))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HttpFunc.HttpFunc.create_report("jmd_api_report")

    filename = HttpFunc.HttpFunc.get_report("jmd_api_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'加盟店相关接口测试报告')
    runner.run(suite)
