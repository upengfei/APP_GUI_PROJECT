# coding:utf-8
import time,sys
import unittest
import requests,urllib
import json
from func import HTMLTestRunner, HttpFunc,MysqlDB, ReadFile,BasicFunc,QydBasicFunc


reload(sys)
sys.setdefaultencoding("utf-8")


class ApiRecharge(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = ReadFile.ReadFile(r'/config/recharge_self.ini')
        self.md = MysqlDB.MysqlDB(r'/config/recharge_self.ini')


    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()

    def test_queryAccountAmount(self):
        u"""查询账户余额"""

        header1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token": "{}".format(self.s.getBackToken())
        }
        # self.s.headers.update({"X-Auth-Token":"{}".format(self.r.headers["X-Auth-Token"])})

        url_api = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL","queryaccountamount")
        # param = {
        #
        # }

        r=self.s.post(url_api, headers=header1, verify=False)
        print '请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, '请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryAccountAmount_01(self):
        u"""查询账户余额-token为空"""

        header1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            # "X-Auth-Token": "{}".format(self.r.headers["X-Auth-Token"])
        }
        # self.s.headers.update({"X-Auth-Token":"{}".format(self.r.headers["X-Auth-Token"])})

        url_api = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL","queryaccountamount")
        param = {

        }
        r=self.s.post(url_api,data=json.dumps(param), headers=header1,verify=False)
        print '请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, '请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryAccountAmount_02(self):
        u"""查询账户余额-token输入错误"""

        header1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token": "fdsarierioew432432"
        }
        # self.s.headers.update({"X-Auth-Token":"{}".format(self.r.headers["X-Auth-Token"])})

        url_api = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL","queryaccountamount")
        param = {

        }
        r=self.s.post(url_api,data=json.dumps(param), headers=header1,verify=False)
        print '请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, '请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction(self):
        """查询交易明细"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id)
        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction_01(self):
        """查询交易明细-type为recharge"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "type":"RECHARGE"

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction_02(self):
        """查询交易明细-type为withdraw"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "type":"WITHDRAW"

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction_03(self):
        """查询交易明细-type为空"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "type":""

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction_04(self):
        """查询交易明细-type为其他值"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "type":"1"

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code != 200, u'请求返回状态码与预期不一致，实际返回状态码为：'+str(r.status_code)

    def test_queryTransaction_05(self):
        """查询交易明细-amount为空"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "amount":""

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code != 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction_06(self):
        """查询交易明细-amount为负数"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "amount":"-1"

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code != 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryTransaction_07(self):
        """查询交易明细-amount为非负数"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "querytransaction")

        params = {
            "pageSize":"10",
            "curPageNo":"1",
            "id":"{}".format(_id),
            "amount":"10"

        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_tranasctionExcelExport(self):
        """交易明细导出"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        params = {
            "pageSize":10,
            "curPageNo":1,
            "id":"{}".format(_id)


        }

        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "tranasctionexcelexport")\
            + "?"\
            + urllib.urlencode(params)


        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.get(_url, headers=header,verify=False)
        # print u'请求返回报文为:%s' % (unicode(r.content),)
        # assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_tranasctionExcelExport_01(self):
        """交易明细导出-缺少用户类型参数"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        _id = self.md.fetchone()[0]

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        params = {
            "pageSize":10,
            "curPageNo":1


        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "tranasctionexcelexport")\
            + "?"\
            + urllib.urlencode(params)

        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.get(_url,headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        # assert r.status_code != 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_tranasctionExcelExport_02(self):
        """交易明细导出-用户类型参数值为空"""

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        params = {
            "pageSize":10,
            "curPageNo":1,
            "id":""


        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "tranasctionexcelexport")\
            + "?"\
            + urllib.urlencode(params)

        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.get(_url, headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        # assert r.status_code != 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryAvailableBankcard_01(self):
        """查询银行卡信息-id参数为空"""
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "queryAvailableBankcard")

        params = {
            "id":""


        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_queryAvailableBankcard(self):
        """查询银行卡信息"""
        sql = "select id from user where name=%s;"
        self.md.execute(sql, "垫富宝投资有限公司")
        user_id = self.md.fetchall()[0]

        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "queryAvailableBankcard")

        params = {
            "id":"{}".format(user_id)


        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backgroundOfflineRecharge(self):
        """自有账户线下充值"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundOfflineRecharge")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"BackgroundOffline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankName":"中信银行",
            "amount":"100",


        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backgroundOfflineRecharge_01(self):
        """自有账户线下充值-金额小于10"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundOfflineRecharge")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"ForegroundOffline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankName":"中信银行",
            "amount":"1",


        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backgroundOfflineRecharge_02(self):
        """自有账户线下充值-流水号重复"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundOfflineRecharge")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"BackgroundOffline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankName":"中信银行",
            "amount":"100",
            "serialNo":"abbbnnnofffoo-01"


        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backgroundOfflineRecharge_03(self):
        """自有账户线下充值-加入流水号"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundOfflineRecharge")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"BackgroundOffline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankName":"中信银行",
            "amount":"100",
            "serialNo":"abbfghnnofffffdfoo-01"


        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)
        print u'请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, u'请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backGroundoOfflineWithdrawal(self):
        """自有账户线下提现"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundofflinewithdrawal")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"ForegroundOffline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankName":"中信银行",
            "amount":"100",



        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)

        print '请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, '请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backGroundoOfflineWithdrawal_01(self):
        """自有账户线下提现-amount为负数"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundofflinewithdrawal")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"ForegroundOffline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankName":"中信银行",
            "amount":"-10",



        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)

        print '请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, '请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)

    def test_backGroundOnlineWithdrawal(self):
        """自有账户线上提现"""
        sql = "select id from user where name='垫富宝投资有限公司';"

        self.md.execute(sql)
        user_id = self.md.fetchone()[0]
        print user_id
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"{}".format(self.s.getBackToken())
        }
        _url = self.rf.get_option_value("http","host")\
            + self.rf.get_option_value("URL", "backgroundonlinewithdrawal")

        params = {
            "userId":"{}".format(user_id),
            "operationType":"BackgroundOnline",# 操作类型：ForegroundOnline、BackgroundOnline 、ForegroundOffline、BackgroundOffline
            "bankCard":"2171",
            "amount":"100",



        }
        # print header
        # print url_api.decode('utf-8')
        # print params
        r = self.s.post(_url,data=json.dumps(params),headers=header,verify=False)

        print '请求返回报文为:%s' % (r.content,)
        assert r.status_code == 200, '请求返回状态码与预期不一致，返回状态码为：'+str(r.status_code)


if __name__ == "__main__":

    suite = unittest.TestSuite(
        map(
            ApiRecharge,
            [
                "test_queryAccountAmount",
                "test_queryAccountAmount_01",
                "test_queryAccountAmount_02",
                "test_queryTransaction",
                "test_queryTransaction_01",
                "test_queryTransaction_02",
                "test_queryTransaction_03",
                "test_queryTransaction_04",
                "test_queryTransaction_05",
                "test_queryTransaction_06",
                "test_queryTransaction_07",
                "test_tranasctionExcelExport",
                # "test_tranasctionExcelExport_01",
                # "test_tranasctionExcelExport_02",
                "test_queryAvailableBankcard",
                "test_backgroundOfflineRecharge",
                "test_backgroundOfflineRecharge_01",
                "test_backgroundOfflineRecharge_02",
                "test_backgroundOfflineRecharge_03",
                "test_backGroundoOfflineWithdrawal",
                "test_backGroundoOfflineWithdrawal_01",
                "test_backGroundOnlineWithdrawal"
            ]
        )
    )
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HttpFunc.HttpFunc.create_report("rechargeSelf_report")

    filename = HttpFunc.HttpFunc.get_report("rechargeSelf_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告',description=u"测试详情")
    runner.run(suite)