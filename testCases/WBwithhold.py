# coding:utf-8

import time,sys
import unittest
import re
import json
import hashlib
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")

md = MysqlDB.MysqlDB(r'/config/withholdAgent.ini')
class WBwithhold(unittest.TestCase):
    """外部代扣操作 """

    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/withholdAgent.ini')
        # self.md = MysqlDB.MysqlDB(r'/config/withholdAgent.ini')
        self.amount=""
        self.orderno=""
        self.authorizeCode=""
        # self.avi_amount=""
        # if self._testMethodName == 'test_withholdnormal_02':
        #     self.addCleanup(self.pre_db_check)

    def tearDown(self):
        # pa ss
        if self._testMethodName in ['test_withholdnormal_01','test_withholdnormal_02','test_withholdnormal_03']:
            self.addCleanup(self.db_check)

    @classmethod
    def tearDownClass(cls):
        md.cursor_close()
        md.conn_close()


    def pre_db_check(self):
        self.authorizeCode='QYDSQ1470882311651'
        if self._testMethodName=="test_withholdnormal_02":
            sql = "select a.available_amount from account a,authorize_info b where a.user_id = b.payer_id and b.authorize_code = %s;"
            md.execute(sql,self.authorizeCode)
            self.avi_amount = md.fetchone()[0]
            logger.info("付款方用户可用余额为：%s" % self.avi_amount)
            print "部分还款-代扣金额大于可转金额时，付款方用户可用余额为：%s" % self.avi_amount

    def db_check(self):
        # print '@@@@@@',self.authorizeCode

        sql = "select status, actual_amount from withhold_info where  order_no='%s' and authorize_code='%s';"\
        % (self.orderno,self.authorizeCode)
        # print '!!!!!',sql
        md.execute(sql)
        status = md.fetchone()[0]
        # print '########',status
        md.scroll(0,'absolute')
        actualAmount = md.fetchone()[1]
        # if self._testMethodName in['test_withholdnormal_01','test_withholdnormal_03']:
        if int(status) == 2 :
            logger.info("校验成功，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%d,实际输入值：%d" %(sql,status,int(actualAmount),int(self.amount)))
            print "校验成功，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%d,实际输入值：%d" %(sql,status,int(actualAmount),int(self.amount))
        else:
            logger.info("校验失败，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%d,实际输入值：%d" %(sql,status,int(actualAmount),int(self.amount)))
            print "校验失败，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%d,实际输入值：%d" %(sql,status,int(actualAmount),int(self.amount))
            raise
        # elif self._testMethodName in['test_withholdnormal_02']:
        #     if int(status) == 2 and int(actualAmount) == int(self.avi_amount):
        #         logger.info("校验成功，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%s" %(sql,status,actualAmount))
        #         print "校验成功，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%s" %(sql,status,actualAmount)
        #     else:
        #         logger.error("校验失败，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%s" %(sql,status,actualAmount))
        #         print "校验失败，校验sql：%s,实际查询的status值为：%s,实际付款金额为：%s" %(sql,status,actualAmount)
        #         raise

            # 校验transaction 表
        sql1= 'select count(*) from transaction where order_no =\'%s\''% self.orderno
        md.execute(sql1)
        icount = md.fetchone()[0]
        if int(icount)==1:
            logger.info("校验transaction表成功，校验sql:%s" % sql1)
            print "校验transaction表成功，校验sql:%s" % sql1
        else:
            logger.error("校验transaction表失败，校验sql:%s" % sql1)
            print "校验transaction表失败，校验sql:%s" % sql1

        # 校验transfer表
        sql2 = 'select count(*) from transfer where order_no=\'%s\''% self.orderno
        md.execute(sql2)
        icount1= md.fetchone()[0]
        if int(icount1)==3:
            logger.info("校验transfer表成功，校验sql:%s" % sql2)
            print "校验transfer表成功，校验sql:%s" % sql2
        else:
            logger.error("校验transfer表失败，校验sql:%s" % sql2)
            print "校验transfer表失败，校验sql:%s" % sql2


# 正常流程
    def test_withholdnormal_01(self):
        """ 外部代扣操作-正常流程-部分还款-代扣金额小于或等于可转金额 """


        # 参数设置
        self.orderno,self.authorizeCode,channel,self.amount,ifPartdebit = [
            '2ce06a40-637f-11e6-bda2-14dda9800e2a',
            'QYDSQ1471330896020',
            'DFBXT',
            '101',
            '1' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(self.orderno+self.authorizeCode+channel+self.amount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % self.orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % self.authorizeCode,
            'withholdAmount':'%s' % self.amount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_withholdnormal_02(self):
        """ 外部代扣操作-正常流程-部分还款-代扣金额大于可转金额 """


        # 参数设置
        self.orderno,self.authorizeCode,channel,self.amount,ifPartdebit = [
            '1127f7cf-6359-11e6-bead-14dda9800e2a',
            'QYDSQ1471315526742',
            'DFBXT',
            '5',
            '0' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(self.orderno+self.authorizeCode+channel+self.amount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % self.orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % self.authorizeCode,
            'withholdAmount':'%s' % self.amount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))
        print '请求返回报文为:%s' % (r.content,)
        content = re.findall('.*"withholdAmount":"(.+?)"}]',r.content,re.S)
        print '实际执行的代扣金额为：',content

    def test_withholdnormal_03(self):
        """ 外部代扣操作-正常流程-全额还款 """


        # 参数设置
        self.orderno,self.authorizeCode,channel,self.amount,ifPartdebit = [
            'ca229a40-62ca-11e6-9aea-14dda9800e2a',
            'QYDSQ1471253394803',
            'DFBXT',
            '20',
            '1' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(self.orderno+self.authorizeCode+channel+self.amount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % self.orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % self.authorizeCode,
            'withholdAmount':'%s' % self.amount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)
# 异常流程
    def test_withholdexcept_01(self):
        """ 外部代扣操作-参数不完整"""


        # 参数设置
        orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
            'e82caa61-5df9-11e6-8f2f-14dda9800e2a',
            'QYDSQ1470723901305',
            'PPWXT',
            '20',
            '0' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % authorizeCode,
            'withholdAmount':'%s' % withholdAmount,
            # 'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_withholdexcept_02(self):
        """ 外部代扣操作-金额为负数"""


        # 参数设置
        orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
            'e82caa61-5df9-11e6-8f2f-14dda9800e2a',
            'QYDSQ1470723901305',
            'PPWXT',
            '-1',
            '0' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % authorizeCode,
            'withholdAmount':'%s' % withholdAmount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_withholdexcept_03(self):
        """ 外部代扣操作-金额为0"""


        # 参数设置
        orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
            'e82caa61-5df9-11e6-8f2f-14dda9800e2a',
            'QYDSQ1470723901305',
            'PPWXT',
            '0',
            '0' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % authorizeCode,
            'withholdAmount':'%s' % withholdAmount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_withholdexcept_04(self):
        """ 外部代扣操作-是否进行部分扣款为非法值"""


        # 参数设置
        orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
            'e82caa61-5df9-11e6-8f2f-14dda9800e2a',
            'QYDSQ1470723901305',
            'PPWXT',
            '10',
            '3' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % authorizeCode,
            'withholdAmount':'%s' % withholdAmount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_withholdexcept_05(self):
        """ 外部代扣操作-全额还款-代扣金额大于可转金额"""


        # 参数设置
        orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
            '93bfa030-5f8f-11e6-88b9-14dda9800e2a',
            'QYDSQ1470898110541',
            'DFBXT',
            '200',
            '1' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % authorizeCode,
            'withholdAmount':'%s' % withholdAmount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    def test_withholdexcept_06(self):
        """ 外部代扣操作-代扣订单重复"""


        # 参数设置
        orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
            'ca229a40-62ca-11e6-9aea-14dda9800e2a',
            'QYDSQ1471253394803',
            'DFBXT',
            '20',
            '1' # 0 部分 1 全额
        ]

        # md5 默认key

        MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"

        # MD5 加密
        md5 = hashlib.md5()
        md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        # 传入参数
        data = {
            "sign":"%s" % sign,
            "orderNo":"%s" % orderno,
            "channel":"%s" % channel,
            'authorizeCode':'%s' % authorizeCode,
            'withholdAmount':'%s' % withholdAmount,
            'ifPartdebit':'%s' % ifPartdebit
        }

        url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
        logger.info("接口请求地址："+url)
        # 发送post请求
        r = self.s.post(url,data=json.dumps(data),verify=False)
        logger.info('请求返回报文为:%s' % (r.content,))

        print '请求返回报文为:%s' % (r.content,)

    # def test_withholdexcept_07(self):
    #     """ 外部代扣操作-全额还款-用户可转金额小于代扣金额"""
    #
    #
    #     # 参数设置
    #     orderno,authorizeCode,channel,withholdAmount,ifPartdebit = [
    #         '93bfa030-5f8f-11e6-88b9-14dda9800e2a',
    #         'QYDSQ1470898110541',
    #         'DFBXT',
    #         '100',
    #         '1' # 0 部分 1 全额
    #     ]
    #
    #     # md5 默认key
    #
    #     MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"
    #
    #     # MD5 加密
    #     md5 = hashlib.md5()
    #     md5.update(orderno+authorizeCode+channel+withholdAmount+ifPartdebit+MD5_SIGN_DEFAULT_KEY)
    #
    #     sign = md5.hexdigest()
    #
    #     # 传入参数
    #     data = {
    #         "sign":"%s" % sign,
    #         "orderNo":"%s" % orderno,
    #         "channel":"%s" % channel,
    #         'authorizeCode':'%s' % authorizeCode,
    #         'withholdAmount':'%s' % withholdAmount,
    #         'ifPartdebit':'%s' % ifPartdebit
    #     }
    #
    #     url = self.rf.get_option_value("HTTP","base_url")+self.rf.get_option_value("API","wbwithhold_url")
    #     logger.info("接口请求地址："+url)
    #     # 发送post请求
    #     r = self.s.post(url,data=json.dumps(data),verify=False)
    #     logger.info('请求返回报文为:%s' % (r.content,))
    #
    #     print '请求返回报文为:%s' % (r.content,)


if __name__=='__main__':
    suite = unittest.TestSuite(map(WBwithhold,[
        "test_withholdnormal_01",
        # "test_withholdnormal_02",
        # "test_withholdnormal_03",
        # "test_withholdexcept_01",
        # "test_withholdexcept_02",
        # "test_withholdexcept_03",
        # "test_withholdexcept_04",
        # "test_withholdexcept_05",
        # "test_withholdexcept_06",

    #

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("wbwithhold_report")

    filename = HttpFunc.HttpFunc.get_report("wbwithhold_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'代扣接口-外部代扣操作测试报告',description=u"测试详情")
    runner.run(suite)