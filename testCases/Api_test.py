# -*- coding:utf-8 -*-
import time
import unittest

from func import HTMLTestRunner, HttpFunc, MysqlDB, ReadFile,otherFunc


class TestCases(unittest.TestCase):

    def setUp(self):
        otherFunc.Func().get_root_path()
        self.rf = ReadFile.ReadFile()
        self.hf = HttpFunc.HttpFunc()
        self.md = MysqlDB.MysqlDB()

    def tearDown(self):
        self.hf.buf_close()
        self.md.cursor_close()
        self.md.conn_close()

    def test_rechargebankinfoget(self):
        u"""  充值绑卡查询  """

        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('API_URL', 'api_url')

        print u'接口请求的地址为:'+req_url

        print u"请求返回报文：", self.hf.hf_post(req_url, headers=header, arg_type=0, location=location)
        assert(self.hf.get_code() == 200)

    def test_getbanklist(self):
        u""" 银行管理-获取银行列表 """
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value('API_URL', 'getbanklist_url')
        print u'接口请求的地址为:'+req_url
        data = {
            "curPageNo": "1",
            "pageSize": "10"
        }
        print u"请求返回报文：", self.hf.hf_post(req_url, data, header, 2, location=location)
        assert(self.hf.get_code() == 200)

    def test_query_banklist(self):
        u""" 前台获取银行列表 """
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bank_query_url")
        data = {
            "buysway": "00",  # 00:pc,01:app
            "service": "00"   # 00:个人网银，01：企业网银，02：快捷支付，03：提现
        }
        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)
        assert(self.hf.get_code() == 200)

    def test_withdrawquery(self):
        u""" 提现绑卡查询 """
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bank_query_withdraw")
        data = {}

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)
        assert(self.hf.get_code() == 200)

# 充值签约正常流程
    def test_rechargecontract_00(self):
        u""" 充值签约-正常流程"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "6225768712921400",  # 充值银行卡卡号
            "userName": "于鹏飞",  # 持卡人姓名
            "userIdentity": "130622198308057019",  # 用户真实的身份证信息
            "userMobile": "18911884890",  # 用户手机号信息
            "amount": "500",  # 充值金额
            "bankName": "招商银行",  # 银行名称
            "bankCord": "CMB",  # 银行编码
            "bankCardId": "87908f8c-380b-4b8d-b817-7610d13c64e9"  # "b19d5aa2-e29b-4315-b99d-d8e8807a0a93"# bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

# 充值签约异常测试用例
    def test_rechargecontract_01(self):
        u""" 充值签约-输入参数错误:该卡号与指定支付的银行不符"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "6217000010075576820",  # 充值银行卡卡号
            "userName": "张永强",  # 持卡人姓名
            "userIdentity": "371327198202093717",  # 用户真实的身份证信息
            "userMobile": "13811611820",  # 用户手机号信息
            "amount": "12",  # 充值金额
            "bankName": "农业银行",  # 银行名称
            "bankCord": "ABC",  # 银行编码
            "bankCardId": "a65e8305-fb48-410c-aec5-5852cffb3720"  # bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_rechargecontract_02(self):
        u""" 充值签约-下单参数校验出错:银行卡持卡人参数错误(userName为空)"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "6217000010075576820",  # 充值银行卡卡号
            "userName": "nick",  # 持卡人姓名
            "userIdentity": "371327198202093717",  # 用户真实的身份证信息
            "userMobile": "13811611820",  # 用户手机号信息
            "amount": "12",  # 充值金额
            "bankName": "建设银行",  # 银行名称
            "bankCord": "CCB",  # 银行编码
            "bankCardId": "a65e8305-fb48-410c-aec5-5852cffb3720"  # bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_rechargecontract_03(self):
        u""" 充值签约-银行返回的具体错误描述:错误的身份证号"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "6217000010075576820",  # 充值银行卡卡号
            "userName": "张永强",  # 持卡人姓名
            "userIdentity": "371327198202093707",  # 用户真实的身份证信息
            "userMobile": "13811611820",  # 用户手机号信息
            "amount": "12",  # 充值金额
            "bankName": "建设银行",  # 银行名称
            "bankCord": "CCB",  # 银行编码
            "bankCardId": "a65e8305-fb48-410c-aec5-5852cffb3720"  # bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_rechargecontract_04(self):
        u""" 充值签约-银行缩简码为空或不在合作银行范围内"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "6217000010075576820",  # 充值银行卡卡号
            "userName": "张永强",  # 持卡人姓名
            "userIdentity": "371327198202093717",  # 用户真实的身份证信息
            "userMobile": "13811611820",  # 用户手机号信息
            "amount": "12",  # 充值金额
            "bankCord": "ACB",  # 银行编码
            "bankCardId": "a65e8305-fb48-410c-aec5-5852cffb3720"  # bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_rechargecontract_05(self):
        u""" 充值签约-银行卡号参数错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "",  # 充值银行卡卡号 6217000010075576820
            "userName": "张永强",  # 持卡人姓名
            "userIdentity": "371327198202093717",  # 用户真实的身份证信息
            "userMobile": "13811611820",  # 用户手机号信息
            "amount": "12",  # 充值金额
            "bankCord": "CCB",  # 银行编码
            "bankCardId": "a65e8305-fb48-410c-aec5-5852cffb3720"  # bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_rechargecontract_06(self):
        u""" 充值签约-手机号错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargecontract_url")
        data = {
            "bankCard": "6217000010075576820",  # 充值银行卡卡号 6217000010075576820
            "userName": "张永强",  # 持卡人姓名
            "userIdentity": "371327198202093717",  # 用户真实的身份证信息
            "userMobile": "18911884890",  # 用户手机号信息
            "amount": "12",  # 充值金额
            "bankCord": "CCB",  # 银行编码
            "bankCardId": "a65e8305-fb48-410c-aec5-5852cffb3720"  # bank_card_id
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

# 充值确认测试用例
    def test_rechargeok_01(self):
        u""" 充值确认-短信验证码错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargeok_url")
        data = {
            "orderNo": "b40ca38a-6936-4b58-bde6-824e2accd632",  # 订单号
            "checkCode": "574599"  # 短信验证码
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_rechargeok_02(self):
        u""" 充值确认-验证码为空"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "rechargeok_url")
        data = {
            "orderNo": "b40ca38a-6936-4b58-bde6-824e2accd632",  # 订单号
            "checkCode": ""  # 短信验证码
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

# 银行鉴权接口
    def test_bankauthentication_00(self):
        u""" 银行鉴权接口-正常流程"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bankauthentication_url")
        data = {
            "bankId": "CMB",  # 银行代码
            "accountNo": "6226090110503501",  # 银行卡信息
            "bankProvice": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "建国门支行",  #
            "bankName": "招商银行",
            "mobile": "13911253517"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

# 银行鉴权接口异常案例
    def test_bankauthentication_01(self):
        u""" 银行鉴权接口-银行卡卡号错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bankauthentication_url")
        data = {
            "bankId": "CMB",  # 银行代码
            "accountNo": "6226090110503502",  # 银行卡信息
            "bankProvice": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "建国门支行",  #
            "bankName": "招商银行",
            "mobile": "13911253517"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

        # time.sleep(31)

    def test_bankauthentication_02(self):
        u""" 银行鉴权接口-手机号错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bankauthentication_url")
        data = {
            "bankId": "CMB",  # 银行代码
            "accountNo": "6226090110503502",  # 银行卡信息
            "bankProvice": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "建国门支行",  #
            "bankName": "招商银行",
            "mobile": "18911884890"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)
        time.sleep(31)

    def test_bankauthentication_03(self):
        u""" 银行鉴权接口-银行名称错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bankauthentication_url")
        data = {
            "bankId": "CMB",  # 银行代码
            "accountNo": "6226090110503502",  # 银行卡信息
            "bankProvice": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "建国门支行",  #
            "bankName": "交通银行",
            "mobile": "13911253517"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)
        time.sleep(31)

    def test_bankauthentication_04(self):
        u""" 银行鉴权接口-银行代码错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "bankauthentication_url")
        data = {
            "bankId": "ABC",  # 银行代码
            "accountNo": "6226090110503502",  # 银行卡信息
            "bankProvice": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "建国门支行",  #
            "bankName": "招商银行",
            "mobile": "13911253517"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)
        time.sleep(31)
# 一键提现异常用例
    def test_withdrawal_01(self):
        u""" 一键提现-银行卡信息错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "withdraw_url")
        data = {
            "bankCode": "CMB",  # 银行代码
            "bankCard": "62260901105035032",  # 银行卡信息
            "bankProvince": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "建国门支行",  #
            "amount": "12",
            "busWay": "00",
            "bankName": "招商银行"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_withdrawal_02(self):
        u""" 一键提现-bankBranch为空"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "withdraw_url")
        data = {
            "bankCode": "CMBC",  # 银行代码
            "bankCard": "6226090110503501",  # 银行卡信息
            "bankProvince": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "",  #
            "amount": "12",
            "busWay": "00",
            "bankName": "招商银行"
        }

        print u"请求返回报文：%s" %  self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_withdrawal_03(self):
        u""" 一键提现-amount为空"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "withdraw_url")
        data = {
            "bankCode": "CMBC",  # 银行代码
            "bankCard": "6216910105500919",  # 银行卡信息
            "bankProvince": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "长安街支行",  # 长安街支行
            "amount": "",
            "busWay": "00",
            "bankName": "民生银行"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_withdrawal_04(self):
        u""" 一键提现-bankCard为填写错误"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "withdraw_url")
        data = {
            "bankCode": "CMBC",  # 银行代码
            "bankCard": "62169101055009191",  # 银行卡信息
            "bankProvince": "北京",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "长安街支行",  # 长安街支行
            "amount": "12",
            "busWay": "00",
            "bankName": "民生银行"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

    def test_withdrawal_05(self):
        u""" 一键提现-bankProvince为空"""
        token = self.hf.get_token()[0]  # 获得token值
        print u'获取的token值为：'+token
        location = self.hf.buf_tell()   # 获得token后，内存缓存区游标指针的位置
        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8',
            'X-Auth-Token:'+str(token)
        ]

        req_url = self.rf.get_option_value("http", "host")\
            + ':'\
            + self.rf.get_option_value("http", "port")\
            + self.rf.get_option_value("API_URL", "withdraw_url")
        data = {
            "bankCode": "CMBC",  # 银行代码
            "bankCard": "62169101055009191",  # 银行卡信息
            "bankProvince": "",  # 银行所在省
            "bankCity": "北京",
            "bankBranch": "长安街支行",  # 长安街支行
            "amount": "12",
            "busWay": "00",
            "bankName": "民生银行"
        }

        print u"请求返回报文：", self.hf.hf_post(req_url, params=data, headers=header, arg_type=2, location=location)

        assert(self.hf.get_code() == 200)

if __name__ == '__main__':

    suite = unittest.TestSuite(
        map(
            TestCases,
            [
                "test_rechargebankinfoget",
                # "test_getbanklist",
                # "test_query_banklist",
                # "test_withdrawquery"
                # "test_rechargecontract_00",
                # "test_rechargeok_01",
                # "test_rechargeok_02",
                # "test_withdrawal_01",
                # "test_withdrawal_02",
                # "test_bankauthentication_01",
                # "test_bankauthentication_02",
                # "test_bankauthentication_03",
                # "test_bankauthentication_04"
                # "test_bankauthentication_00"

            ]
        )
    )
    # suite.addTest(TestCases('test_rechargebankinfoget'))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HttpFunc.HttpFunc.create_report("test_api")

    filename = HttpFunc.HttpFunc.get_report("test_api")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口测试报告', description=u'测试报告详情： ')
    runner.run(suite)
