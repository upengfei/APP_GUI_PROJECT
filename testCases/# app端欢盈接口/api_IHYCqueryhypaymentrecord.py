# coding:utf-8
import time,sys
import unittest
import json
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCqueryhyrepaymentrecord(GesturePwdInit):
    """欢盈-计划详情-还款记录"""
    # 正常流程
    def test_queryprdrd(self):
        """ 欢盈-计划详情-还款记录-正常流程"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"%s" % loanID,
            "pageNumber": "1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content
        # 校验loan表

        sql = "select count(*) from loan as l where  l.status in ('FINISH','PREPAYMENT_FINISH','OVER_DUE_FINISH') and " \
              "l.cb_loan_id='%s'"% loanID
        self.md.execute(sql)
        scount=self.md.fetchone()[0]
        if int(scount)==int(r.json()['mapData']['totalItemsCount']):
            logger.info("校验loan表成功，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))
            print("校验loan表成功，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))
        else:
            logger.error("校验loan表失败，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))
            print("校验loan表失败，查询的数据条目为:{0},校验的sql为:{1}".format(scount,sql))

    def test_hyrepaymentreord_ex_01(self):
        """ 欢盈-计划详情-还款记录-异常流程-loanId错误"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"@@!",
            "pageNumber": "1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","hyassignmentdetail_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_hyrepaymentreord_ex_02(self):
        """ 欢盈-计划详情-还款记录-异常流程-loanId为空"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"",
            "pageNumber": "1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_hyrepaymentreord_ex_03(self):
        """ 欢盈-计划详情-还款记录-异常流程-pageNumber为空"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"%s" % loanID,
            "pageNumber": "",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_hyrepaymentreord_ex_04(self):
        """ 欢盈-计划详情-还款记录-异常流程-pageNumber错误"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"%s" % loanID,
            "pageNumber": "ad",
            "pageSize":"5"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,


        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_hyrepaymentreord_ex_05(self):
        """ 欢盈-计划详情-还款记录-异常流程-pageSize错误"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"%s" % loanID,
            "pageNumber": "1",
            "pageSize":"dd"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,


        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_hyrepaymentreord_ex_06(self):
        """ 欢盈-计划详情-还款记录-异常流程-pageSize为空"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"%s" % loanID,
            "pageNumber": "1",
            "pageSize":""
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_hyrepaymentreord_ex_07(self):
        """ 欢盈-计划详情-还款记录-异常流程-token错误"""
        # 获取loanID
        sql="select id from loan as l where l.debttype='HY' and l.`status`='CLOSE' and TO_DAYS(l.repay_date)-TO_DAYS(SYSDATE())>0" \
            " order by l.create_time desc limit 1 OFFSET 0;"
        self.md.execute(sql)
        loanID=self.md.fetchone()[0]
        logger.info("@@@@@@@@"+loanID)
        # 获取前台token
        token = self.qa.getToken()
        data={
            "loanId":"%s" % loanID,
            "pageNumber": "1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"fdsrt6fgf-12dfdsdsf-23dsfgg-232ds3tgg",
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryhyrepaymentrecord_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print("返回报文为：{0}".format(r.content))
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCqueryhyrepaymentrecord,[
        "test_queryprdrd",
        "test_hyrepaymentreord_ex_01",
        "test_hyrepaymentreord_ex_02",
        "test_hyrepaymentreord_ex_03",
        "test_hyrepaymentreord_ex_04",
        "test_hyrepaymentreord_ex_05",
        "test_hyrepaymentreord_ex_06",
        "test_hyrepaymentreord_ex_07"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCqueryhyrepaymentrecord_report")

    filename = HttpFunc.HttpFunc.get_report("HYCqueryhyrepaymentrecord_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="欢盈-计划详情-债权详情测试详情:")
    runner.run(suite)