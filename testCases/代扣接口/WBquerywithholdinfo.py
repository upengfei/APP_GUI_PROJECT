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


class WBqueryauthorizeinfo(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = ReadFunc.ReadFile(r'/config/withholdAgent.ini')
        self.md = MysqlDB.MysqlDB(r'/config/withholdAgent.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()


# 正常流程
    def test_querywithholdinfo(self):
        """ 根据订单查询授权信息-正常流程 """


        # 订单号
        orderno = '1127f7cf-6359-11e6-bead-14dda9800e2a'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

# 异常流程
    def test_querywithholdinfo_01(self):
        """ 根据订单查询授权信息-订单号不存在 """


        # 订单号
        orderno = '522a42d4-0a2d-4acd-98e2-e53b1f5de61d9'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_querywithholdinfo_02(self):
        """ 根据订单查询授权信息-订单号为空 """


        # 订单号
        orderno = '522a42d4-0a2d-4acd-98e2-e53b15de61d9'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"",
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_querywithholdinfo_03(self):
        """ 根据订单查询授权信息-渠道错误 """


        # 订单号
        orderno = '1127f7cf-6359-11e6-bead-14dda9800e2a'
        # 验证码
        channel = 'CKKXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_querywithholdinfo_04(self):
        """ 根据订单查询授权信息-渠道为空 """


        # 订单号
        orderno = '1127f7cf-6359-11e6-bead-14dda9800e2a'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":""
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_querywithholdinfo_05(self):
        """ 根据订单查询授权信息-渠道为其他值 """


        # 订单号
        orderno = '1127f7cf-6359-11e6-bead-14dda9800e2a'
        # 验证码
        channel = '1'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_querywithholdinfo_06(self):
        """ 根据订单查询授权信息-签名错误 """


        # 订单号
        orderno = '1127f7cf-6359-11e6-bead-14dda9800e2a'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        # md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)
        md5.update(channel+orderno+MD5_SIGN_DEFAULT_KEY)
        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_querywithholdinfo_07(self):
        """ 根据订单查询授权信息-签名为空 """


        # 订单号
        orderno = '1127f7cf-6359-11e6-bead-14dda9800e2a'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        # md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)
        md5.update(channel+orderno+MD5_SIGN_DEFAULT_KEY)
        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"",
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbquerywithholdinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

if __name__=='__main__':
    suite = unittest.TestSuite(map(WBqueryauthorizeinfo,[
        "test_querywithholdinfo",
        "test_querywithholdinfo_01",
        "test_querywithholdinfo_02",
        "test_querywithholdinfo_03",
        "test_querywithholdinfo_04",
        "test_querywithholdinfo_05",
        "test_querywithholdinfo_06",
        "test_querywithholdinfo_07"



    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("wbquerywithholdinfo_report")

    filename = HttpFunc.HttpFunc.get_report("wbquerywithholdinfo_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'代扣接口-查询代扣信息测试报告',description=u"测试详情")
    runner.run(suite)
