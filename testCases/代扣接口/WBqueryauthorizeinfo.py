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



    def test_queryauthorizeinfo(self):
        """ 根据订单查询授权信息-正常流程 """


        # 订单号
        orderno = '5c6ce340-62c8-11e6-93ed-14dda9800e2a' # QYDSQ1471252350864
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

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_01(self):
        """ 根据订单查询授权信息-渠道传入值错误 """


        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
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

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_07(self):
        """ 根据订单查询授权信息-渠道来源为空 """


        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        channel = ''

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

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_02(self):
        """根据订单查询授权信息-签名错误 """


        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(channel+orderno+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_03(self):
        """根据订单查询授权信息-渠道参数值错误（格式正确，但与实际值不匹配） """


        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        channel = 'JMDXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+channel+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel1":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_04(self):
        """ 根据订单查询授权信息-缺少参数"""


        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        # channel = 'DFBXT'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            # "channel1":"%s" % channel
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_05(self):
        """ 根据订单查询授权信息-订单错误 """


        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a3'
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

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_queryauthorizeinfo_06(self):
        """ 根据订单查询授权信息-订单已解除授权 """


        # 已解除授权订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
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

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbqueryauthorizeinfo_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)


if __name__=='__main__':
    suite = unittest.TestSuite(map(WBqueryauthorizeinfo,[
        "test_queryauthorizeinfo",
        "test_queryauthorizeinfo_01",
        "test_queryauthorizeinfo_02",
        "test_queryauthorizeinfo_03",
        "test_queryauthorizeinfo_04",
        "test_queryauthorizeinfo_05",
        "test_queryauthorizeinfo_06",
        "test_queryauthorizeinfo_07"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("wbqueryauthorizeinfo_report")

    filename = HttpFunc.HttpFunc.get_report("wbqueryauthorizeinfo_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'代扣接口-根据订单查询授权信息测试报告',description=u"测试详情")
    runner.run(suite)
