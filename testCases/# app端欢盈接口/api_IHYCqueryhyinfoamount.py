# coding:utf-8
import time,sys
import unittest
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCgetplaninfo(GesturePwdInit):

    # 正常流程
    def test_gethyplaninfo(self):
        """欢盈计划介绍/剩余可投金额/最多可购买金额接口-正常流程-有数据可查询 """
        # 获取前台token
        token = self.qa.getToken()

        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","getplaninfo_url")

        r = self.qa.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

        # 校验数据库剩余可投金额是否一致
        sql = "select sum(if((a.amount - IFNULL(a.already_amount, 0) - " \
              "IFNULL(a.finish_amount, 0) - IFNULL(a.lock_copies, 0) * l.copiesamount)<0,0," \
              "a.amount - IFNULL(a.already_amount, 0) - IFNULL(a.finish_amount, 0) - " \
              "IFNULL(a.lock_copies, 0) * l.copiesamount)) as remainamount from assignment a left outer join loan l on " \
              "a.loan_id=l.id where l.isshow='T' and l.debttype='HY' and a.status='OPEN' and l.status='CLOSE';"
        self.md.execute(sql)
        sremainamount=self.md.fetchone()[0]
        # logger.info("@@@@@@@@@"+sremainamount)
        if float(sremainamount)==float(r.json()['mapData']['totalAmount']):
            logger.info("数据库校验成功，接口返回数据与数据库查询数据一致，数据库查询数据为:{0},查询sql:{1}".format(sremainamount,sql))
            print("数据库校验成功，接口返回数据与数据库查询数据一致，数据库查询数据为:{0},查询sql:{1}".format(sremainamount,sql))
        else:
            logger.error("数据库校验失败，接口返回数据与数据库查询数据不一致，数据库查询数据为:{0},查询sql:{1}".format(sremainamount,sql))
            print("数据库校验失败，接口返回数据与数据库查询数据不一致，数据库查询数据为:{0},查询sql:{1}".format(sremainamount,sql))


if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCgetplaninfo,[
        "test_gethyplaninfo",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCgetplaninfo_report")

    filename = HttpFunc.HttpFunc.get_report("HYCgetplaninfo_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="计划介绍&剩余可投金额&本次最多可购买金额接口测试详情:")
    runner.run(suite)