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


class IHYCqueryproducttransferlist(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydAppToken()
        self.rf = ReadFunc.ReadFile(r'/config/newHYconf.ini')
        self.md = MysqlDB.MysqlDB(r'/config/newHYconf.ini')
        self.holdingCYInterest=""
        self.yesterCYInterest=""

    def tearDown(self):
        # pa ss
        self.md.cursor_close()
        self.md.conn_close()
        # self.db_check()
    # 正常流程


    def test_queryprodtransferlist(self):
        """ 欢盈-计划详情-交易记录-正常流程"""

        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.s.getToken()
        print token
        data={
            "loanId":"%s" % loanID,
            "pageSize":"5",
            "pageNumber":"1"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","queryproducttransferlist_url")
        print url
        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)

    # 校验数据库 涉及的表:invest,assignment,loan_lender_detail,loan
        sql = "select count(*) from invest i LEFT OUTER JOIN loan_lender_detail as ld on i.loan_lender_detail_id=ld.id" \
          " LEFT OUTER JOIN loan l on ld.loan_id = l.id LEFT OUTER JOIN assignment a on a.id = i.parent_id" \
          " where i.invest_type in('BuyHY','RepoHY') and i.`status`='1' and l.id='%s';"% loanID

        self.md.execute(sql)
        scount=self.md.fetchone()[0]
        if int(scount) == int(r.json()['mapData']['totalItemsCount']):
            logger.info("校验数据库成功，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))
            print("校验数据库成功，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))
        else:
            logger.error("校验数据库失败，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))
            print("校验数据库失败，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))

    # 异常案例
    def test_queryprodtransferlist_ex_01(self):
        """ 欢盈-计划详情-交易记录-异常流程-loanID为空"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        # logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.s.getToken()
        print token
        data={
            "loanId":"",
            "pageSize":"5",
            "pageNumber":"1"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":""

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)

    def test_queryprodtransferlist_ex_02(self):
        """ 欢盈-计划详情-交易记录-异常流程-loanID取值错误"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.s.getToken()
        print token
        data={
            "loanId":"a%s" % loanID,
            "pageSize":"5",
            "pageNumber":"1"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":""

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)

    def test_queryprodtransferlist_ex_03(self):
        """ 欢盈-计划详情-交易记录-异常流程-pageSize为空"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.s.getToken()
        print token
        data={
            "loanId":"%s" % loanID,
            "pageSize":"",
            "pageNumber":"1"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":""

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)

    def test_queryprodtransferlist_ex_04(self):
        """ 欢盈-计划详情-交易记录-异常流程-pageNumber为空"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.s.getToken()
        print token
        data={
            "loanId":"%s" % loanID,
            "pageSize":"5",
            "pageNumber":"1"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":""

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","unsettleincome_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为:{0}".format(r.content))
        print "返回报文为:{0}".format(r.content)

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCqueryproducttransferlist,[
        "test_queryprodtransferlist",
        "test_queryprodtransferlist_ex_01",
        "test_queryprodtransferlist_ex_02",
        "test_queryprodtransferlist_ex_03",
        "test_queryprodtransferlist_ex_04"


    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCqueryproducttransferlist_report")

    filename = HttpFunc.HttpFunc.get_report("HYCqueryproducttransferlist_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="交易记录接口测试详情:")
    runner.run(suite)