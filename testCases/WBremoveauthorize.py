# coding:utf-8
import time,sys
import unittest
import urllib
import json
import hashlib
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class WBremoveauthorize(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/withholdAgent.ini')
        self.md = MysqlDB.MysqlDB(r'/config/withholdAgent.ini')
        self.orderno=""
        self.authorizecode=""
    def tearDown(self):
        # pa ss
        if self._testMethodName == 'test_removeauthorize':
            self.db_check()
        self.md.cursor_close()
        self.md.conn_close()

    def db_check(self):

        # 校验 authorize_info表
        print self.authorizecode
        sql = 'select count(*) from authorize_info where authorize_code =\'%s\';'% self.authorizecode
        self.md.execute(sql)
        num = self.md.fetchone()[0]

        if int(num) == 0:
            logger.info("校验正确，校验sql为：%s，查询的数据量num的值为：%s" %(sql,num))
            print "校验正确，校验sql为：%s，查询的数据量num的值为：%s" %(sql,num)
        else:
            logger.error("校验错误，校验sql为：%s，查询的数据量num的值为：%s" %(sql,num))
            print "校验错误，校验sql为：%s，查询的数据量num的值为：%s" %(sql,num)
        # 校验authorize_log 表
        sql1 = 'select count(*) from authorize_log where order_no=\'%s\' and status="2";' % self.orderno
        self.md.execute(sql1)
        num1 = self.md.fetchone()[0]

        if int(num1) == 1:
            logger.info("校验正确，校验sql为：%s，查询的数据量num的值为：%s'" %(sql1,num1))
            print "校验正确，校验sql为：%s，查询的数据量num的值为：%s'" %(sql1,num1)
        else:
            logger.error("校验错误，校验sql为：%s，查询的数据量num的值为：%s'" %(sql1,num1))
            print "校验错误，校验sql为：%s，查询的数据量num的值为：%s'" %(sql1,num1)

    def test_removeauthorize(self):
        """外部解除授权-正常流程 """
        # 订单号
        self.orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        self.authorizecode = 'QYDSQ1471250823483'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(self.orderno+self.authorizecode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % self.orderno,
            "authorizeCode":"%s" % self.authorizecode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)


    def test_removeauthorize_01(self):
        """外部解除授权-授权码不存在 """
        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        authorizeCode = 'QYDSQ14706426739971'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "authorizeCode":"%s" % authorizeCode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_removeauthorize_02(self):
        """外部解除授权-验证签名错误 """
        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        authorizeCode = 'QYDSQ1471250823483'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        # md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)
        md5.update(authorizeCode+orderno+MD5_SIGN_DEFAULT_KEY)
        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "authorizeCode":"%s" % authorizeCode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_removeauthorize_03(self):
        """外部解除授权-验证签名为空 """
        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        authorizeCode = 'QYDSQ1471250823483'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        # md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)
        md5.update(authorizeCode+orderno+MD5_SIGN_DEFAULT_KEY)
        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"" ,
            "orderNo":"%s" % orderno,
            "authorizeCode":"%s" % authorizeCode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_removeauthorize_04(self):
        """外部解除授权-授权码为空"""
        # 订单号
        orderno = '2cc53d95-c943-4e33-a4f2-74fdfe47db60'
        # 验证码
        authorizeCode = 'QYDSQ1470642673997'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "authorizeCode":""
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_removeauthorize_05(self):
        """外部解除授权-订单号错误 """
        # 订单号1
        orderno = '763525de-5d45-11e6-837a-14dda9800e2a'
        # 验证码
        authorizeCode = 'QYDSQ1471250823483'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "authorizeCode":"%s" % authorizeCode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_removeauthorize_06(self):
        """外部解除授权-订单号为空 """
        # 订单号1
        orderno = '8cf97871-a81e-41e9-8de0-494d00d7c8771'
        # 验证码
        authorizeCode = 'QYDSQ1471250823483'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"",
            "authorizeCode":"%s" % authorizeCode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_removeauthorize_07(self):
        """外部解除授权-已解除授权 """
        # 订单号
        orderno = 'cbf82c51-62c4-11e6-9520-14dda9800e2a'
        # 验证码
        authorizeCode = 'QYDSQ1471250823483'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "authorizeCode":"%s" % authorizeCode
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbremoveauthorize_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

if __name__=='__main__':
    suite = unittest.TestSuite(map(WBremoveauthorize,[
        "test_removeauthorize",
        "test_removeauthorize_01",
        "test_removeauthorize_02",
        "test_removeauthorize_03",
        "test_removeauthorize_04",
        "test_removeauthorize_05",
        "test_removeauthorize_06",
        "test_removeauthorize_07"

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("wbremoveauthorize_report")

    filename = HttpFunc.HttpFunc.get_report("wbremoveauthorize_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'代扣接口-解除授权接口测试报告',description=u"测试详情")
    runner.run(suite)