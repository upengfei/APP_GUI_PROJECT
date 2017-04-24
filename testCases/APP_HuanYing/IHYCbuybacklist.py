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


class IHYCbuybacklist(unittest.TestCase):
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
    def test_buybacklist(self):
        """ 欢盈撤资审核中债权-正常流程"""
        # 获取前台token
        token = self.s.getToken()

        data={
            "pageNumber":"1",
            "pageSize":"5"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gethytransferbuyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

        # 校验数据库,涉及的表assignment,loan,user
        sql = "select count(*) from assignment a join user u on a.user_id=u.id LEFT OUTER JOIN loan l on l.id = a.loan_id " \
              "where a.`status`='REPO' and u.tel_num='16800102572' and l.debttype='HY' limit 100 OFFSET 0;"

        self.md.execute(sql)
        scount = self.md.fetchone()[0]
        if int(scount) == int(r.json()['mapData']['totalItemsCount']):
            logger.info("校验数据库assignment表成功,查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))
            print("校验数据库assignment表成功,查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))
        else:
            logger.error("校验数据库assignment表失败,查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))
            print("校验数据库assignment表失败,查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))

    # 异常流程
    def test_buybacklist_ex_01(self):
        """ 欢盈撤资审核中债权-异常流程-pageNumber为空"""
        # 获取前台token
        token = self.s.getToken()

        data={
            "pageNumber":"",
            "pageSize":"5"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gethytransferbuyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buybacklist_ex_02(self):
        """ 欢盈撤资审核中债权-异常流程-pageSize为空"""
        # 获取前台token
        token = self.s.getToken()

        data={
            "pageNumber":"1",
            "pageSize":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,


        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gethytransferbuyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

    def test_buybacklist_ex_03(self):
        """ 欢盈撤资审核中债权-异常流程-pageNumber和pageSize都为空"""
        # 获取前台token
        token = self.s.getToken()

        data={
            "pageNumber":"",
            "pageSize":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",


        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gethytransferbuyback_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCbuybacklist,[
        "test_buybacklist",
        "test_buybacklist_ex_01",
        "test_buybacklist_ex_02",
        "test_buybacklist_ex_03"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYChybuyback_report")

    filename = HttpFunc.HttpFunc.get_report("HYChybuyback_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="撤资审核中债权测试详情:")
    runner.run(suite)