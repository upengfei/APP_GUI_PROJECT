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


class IHYCqueryassetslist(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydAppToken()
        self.rf = ReadFunc.ReadFile(r'/config/newHYconf.ini')
        self.md = MysqlDB.MysqlDB(r'/config/newHYconf.ini')

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
    # 正常流程
    def test_queryassetslist(self):
        """ 欢盈资产组合列表-正常流程"""
        # 获取前台token
        token = self.s.getToken()

        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            # "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","queryhyassetslist_url")

        r = self.s.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

        # 校验数据库
        sql="select count(*) from loan as l join  assignment as a on l.id=a.loan_id where  l.isshow='T' and l.debttype='HY'" \
            "and a.`status` in('OPEN','CLOSE') and l.status IN ('CLOSE','START_REPAY','FINISH')  limit 0,100;"
        self.md.execute(sql)
        icount = self.md.fetchone()[0]
        if int(icount)==int(r.json()['mapData']['totalItemsCount']):
            logger.info("校验成功，数据库的数据与接口返回数据一致，查询的数据为：%s,查询sql：%s" % (icount,sql))
            print("校验成功，数据库的数据与接口返回数据一致，查询的数据为：%s,查询sql：%s" % (icount,sql))
        else:
            logger.error("校验失败，数据库的数据与接口返回数据不一致，查询的数据为：%s,查询sql：%s" % (icount, sql))
            raise AssertionError, "校验失败，数据库的数据与接口返回数据不一致，查询的数据为：%s,查询sql：%s" % (icount, sql)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCqueryassetslist,[
        "test_queryassetslist",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYqueryassetslist_report")

    filename = HttpFunc.HttpFunc.get_report("HYqueryassetslist_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="资产组合列表接口测试详情:")
    runner.run(suite)