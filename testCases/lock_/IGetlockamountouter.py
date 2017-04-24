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


class IGetlockamountouter(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydBackGround()
        self.rf = conf_read.ReadFile(r'/config/lockmoney.ini')
        self.md = MysqlDB.MysqlDB(r'/config/lockmoney.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def test_getlockamountouter(self):
        """ 添加锁定金额 -正常流程"""

        MD5_SIGN_DEFAULT_KEY='72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727'

        # 获取用户ssoID
        sql = 'select a.sso_id from user_profile a,user b where b.id=a.id and b.tel_num="%s";'% (self.rf.get_option_value("user","user"),)
        # print sql
        self.md.execute(sql)
        ssoId = self.md.fetchone()[0]

        # 获取md5加密
        md5 = hashlib.md5()
        md5.update(ssoId+MD5_SIGN_DEFAULT_KEY)

        sign = md5.hexdigest()

        data={
            "ssoId":"%s" % ssoId,
            "sign":"%s" % sign
        }

        url = self.rf.get_option_value("http","fro_base_url")+self.rf.get_option_value("api","getlockamountouter_url")

        r = self.s.post(url,data=json.dumps(data),verify=False)
        print "返回报文为：{0}".format(r.content)


if __name__=='__main__':
    suite = unittest.TestSuite(map(IGetlockamountouter,[
        "test_getlockamountouter",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("Getlockamountouter_report")

    filename = HttpFunc.HttpFunc.get_report("Getlockamountouter_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷预锁定金额接口测试报告',description="查询预锁定金额外部接口测试详情:")
    runner.run(suite)