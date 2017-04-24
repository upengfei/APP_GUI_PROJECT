# coding:utf-8
import time,sys
import unittest
import urllib
import json,uuid
import hashlib
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")



class WithholdAgent(unittest.TestCase):
    """外部验证短信验证码接口测试"""
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = ReadFunc.ReadFile(r'/config/withholdAgent.ini')
        self.md = MysqlDB.MysqlDB(r'/config/withholdAgent.ini')
        self.get_verifycode()

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()

    def get_verifycode(self_):

        a=['%s'%(uuid.uuid1(),),'ceshi','DFBXT','1344864347848612548','14900000020','李俊','431022199604152831',
       '1292736030143352846','14900000010','苗会超','210381199002241436','0','72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727']


        md5 = hashlib.md5()
        md5.update(''.join(a))

        qyd = QydBasicFunc.QydForeground()
        url = "https://www.stg-qyd.com/entrance/account/wbauthorizeplaceorder/json"

        params = {
            "sign": "%s" % md5.hexdigest(),
            "payerSSOID":"%s" % a[3],
            "payerPhone":"%s" % a[4],
            "payerName":"%s" % a[5],
            "payerNum":"%s" % a[6],
            "payeeSSOID":"%s" % a[7],
            "payeePhone":"%s" % a[8],
            "payeeName":"%s" % a[9],
            "payeeNum":"%s" % a[10],
            "orderNo":"%s" % a[0],
            "channel":"%s" % a[2],
            "businessType":"%s" % a[1],
            "ifSendCode":"%s" % a[11]
        }
        qyd.post(url,data=json.dumps(params),verify=False)

    def test_SMSverify(self):
        """ 外部验证短信验证码-正常流程 """

        # 获取sso_id
        sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14900000020"); '
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 验证码
        verifiCode='0000'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(ssoId+verifiCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "verifiCode":"%s" % verifiCode,
            "payerSSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_SMSverify_01(self):
        """ 外部验证短信验证码-用户信息不存在 """

        # 获取sso_id
        # sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14911884890"); '
        # self.md.execute(sql)
        # ssoId = self.md.fetchone()[0]
        ssoId ='10457845748745'
        # 验证码
        verifiCode='0000'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(ssoId+verifiCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "verifiCode":"%s" % verifiCode,
            "payerSSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_SMSverify_02(self):
        """ 外部验证短信验证码-验证验证码失败 """

        # 获取sso_id
        sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14900000020"); '
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 验证码
        verifiCode='0001'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(ssoId+verifiCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "verifiCode":"%s" % verifiCode,
            "payerSSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_SMSverify_03(self):
        """ 外部验证短信验证码-参数为空"""

        # 获取sso_id
        sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14900000020"); '
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 验证码
        verifiCode='0000'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(ssoId+verifiCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "verifiCode":"%s" % verifiCode,
            # "payerSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)
    def test_SMSverify_04(self):
        """ 外部验证短信验证码-参数错误"""

        # 获取sso_id
        sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14900000020"); '
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 验证码
        verifiCode='0000'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(ssoId+verifiCode+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "verifiCode":"%s" % verifiCode,
            "payerSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_SMSverify_05(self):
        """ 外部验证短信验证码-验证签名错误"""

        # 获取sso_id
        sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14900000020"); '
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 验证码
        verifiCode='0000'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(verifiCode+ssoId+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "verifiCode":"%s" % verifiCode,
            "payerSSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_SMSverify_06(self):
        """ 外部验证短信验证码-验证签名为空"""

        # 获取sso_id
        sql = 'select sso_id from user_profile where id in(select id from user where tel_num="14900000020"); '
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 验证码
        verifiCode='0000'

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(verifiCode+ssoId+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"",
            "verifiCode":"%s" % verifiCode,
            "payerSSOID":"%s" % ssoId
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbverificodeconfirm_url")
        print "接口请求地址："+url
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

if __name__=='__main__':
    suite = unittest.TestSuite(map(WithholdAgent,[
        "test_SMSverify",
        "test_SMSverify_01",
        "test_SMSverify_02",
        "test_SMSverify_03",
        "test_SMSverify_04",
        "test_SMSverify_05",
        "test_SMSverify_06"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("wbverificode_report")

    filename = HttpFunc.HttpFunc.get_report("wbverificode_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'代扣接口-外部验证短信验证码测试报告',description=u"测试详情")
    runner.run(suite)
