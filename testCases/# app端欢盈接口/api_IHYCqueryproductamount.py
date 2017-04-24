# coding:utf-8
import time,sys
import unittest
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYqueryproductamount(GesturePwdInit):
    """欢盈持有中金额、理财中金额、撤资审核中金额"""
    # 正常流程
    def test_queryproductamount(self):
        """欢盈持有中金额、理财中金额、撤资审核中金额-正常流程 """
        # 获取前台token
        token = self.qa.getToken()

        header={
            "X-Auth-Token":"%s" % token,
        }

        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","queryproductamount_url")

        r = self.qa.post(url,headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

        # 校验数据库loan_lender_detail理财中金额
        sql = "select sum(ld.hold_amount) as financingAmount  from loan_lender_detail ld LEFT JOIN loan l on l.id = " \
              "ld.loan_id LEFT JOIN user u on u.id = ld.user_id where u.tel_num='%s' and ld.`status`=0 and " \
              "l.debttype='HY' and (ld.lock_amount+ ld.hold_amount)>0;"% self.rf.get_option_value("Appuser","username")
        self.md.execute(sql)
        famount = self.md.fetchone()[0]
        logger.info(famount)

        if str(famount) == r.json()['mapData']['financingAmount']:
            logger.info("数据库校验成功，数据库查询的理财中金额为:{0},与接口返回一致,查询的sql为:{1}".format(famount, sql))
            print("数据库校验成功，数据库查询的理财中金额为:{0},与接口返回一致,查询的sql为:{1}".format(famount, sql))
        else:
            logger.error("数据库校验失败，数据库查询的理财中金额为:{0},查询的sql为:{1}".format(famount, sql))
            raise AssertionError,"数据库校验失败，数据库查询的理财中金额为:{0},查询的sql为:{1}".format(famount, sql)

        # 校验数据库中撤资审核中的金额

        sql1 = "select sum(a.amount) as disinvestAmount from assignment as a left OUTER JOIN loan l on l.id = a.loan_id " \
               "LEFT JOIN user u on u.id = a.user_id where u.tel_num='%s' and a.status='REPO' and l.debttype='HY';" \
               % self.rf.get_option_value("Appuser","username")
        self.md.execute(sql1)
        damount=self.md.fetchone()[0]
        if float(damount) == float(r.json()['mapData']['disinvestAuditAmount']):
            logger.info("数据库校验成功，查询到的撤资审核的金额为:{0},与接口返回一致,查询sql为：{1}".format(damount,sql1))
            print("数据库校验成功，查询到的撤资审核的金额为:{0},与接口返回一致,查询sql为：{1}".format(damount,sql1))
        else:
            logger.error("数据库校验失败，查询到的撤资审核的金额为:{0},查询sql为：{1}".format(damount,sql1))
            raise AssertionError, "数据库校验失败，查询到的撤资审核的金额为:{0},查询sql为：{1}".format(damount,sql1)

        #校验持有中的金额
        if float(famount)+float(damount) == float(r.json()['mapData']['holdAmount']):
            logger.info("校验成功，数据库中查询的理财中的金额与撤资审核中的金额之和与接口返回的持有中的金额一致！")
            print("校验成功，数据库中查询的理财中的金额与撤资审核中的金额之和与接口返回的持有中的金额一致！")
        else:
            logger.error("校验失败，数据库中查询的理财中的金额与撤资审核中的金额之和与接口返回的持有中的金额不一致！")
            raise AssertionError, "校验失败，数据库中查询的理财中的金额与撤资审核中的金额之和与接口返回的持有中的金额不一致！"

if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYqueryproductamount,[
        "test_queryproductamount"
    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCqueryproductamount_report")

    filename = HttpFunc.HttpFunc.get_report("HYCqueryproductamount_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="持有中金额&理财中金额&撤资审核中金额测试详情:")
    runner.run(suite)
