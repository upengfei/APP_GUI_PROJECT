# coding:utf-8
import time,sys
import unittest
import json
from testCases.app_init import GesturePwdInit
from func import *
from func.logInfo import logger

reload(sys)
sys.setdefaultencoding("utf-8")


class IHYCgettransferhold(GesturePwdInit):
    """欢盈理财中债权列表"""
    # 正常流程
    def test_gettransferhold(self):
        """ 欢盈理财中债权列表-正常流程"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "pageNumber": "1",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","gettransfer_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content
    # 校验数据库 涉及到表loan,loan_lender_
        sql = "select count(*) from loan_lender_detail ld  JOIN loan l on l.id = ld.loan_id LEFT OUTER JOIN user u on " \
              "u.id=ld.user_id where u.tel_num='%s' and ld.hold_amount>0 and ld.`status`<>1 and " \
              "l.debttype='HY' limit 100 OFFSET 0;" % self.rf.get_option_value("Appuser","username")

        self.md.execute(sql)
        scount= self.md.fetchone()[0]
        if int(scount) == int(r.json()["mapData"]['totalItemsCount']):
            logger.info("校验数据库成功，查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))
            print("校验数据库成功，查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))
        else:
            logger.error("校验数据库失败，查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))

            print("校验数据库失败，查询的数据条目为:{0},查询的sql为:{1}".format(scount,sql))


    # 异常流程
    def test_gettransferhold_ex_01(self):
        """ 欢盈理财中债权列表-异常流程-page错误输入"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "pageNumber": "1",
            "pageSize":"ad"
        }
        header={
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","gettransfer_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_gettransferhold_ex_02(self):
        """ 欢盈理财中债权列表-异常流程-size错误输入"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "pageNumber": "qw",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,
        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","gettransfer_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_gettransferhold_ex_03(self):
        """ 欢盈理财中债权列表-异常流程-pageSize为空"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "pageNumber": "1",
            "pageSize":""
        }
        header={
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","gettransfer_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content

    def test_gettransferhold_ex_04(self):
        """ 欢盈理财中债权列表-异常流程-pageNumber为空"""
        # 获取前台token
        token = self.qa.getToken()
        data={
            "pageNumber": "",
            "pageSize":"5"
        }
        header={
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("app","host")+self.rf.get_option_value("api","gettransfer_url")

        r = self.qa.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)
        assert r.json()['status'] == 200 and r.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % r.content



if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCgettransferhold,[
        "test_gettransferhold",
        "test_gettransferhold_ex_01",
        "test_gettransferhold_ex_02",
        "test_gettransferhold_ex_03",
        "test_gettransferhold_ex_04",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCgettransferhold_report")

    filename = HttpFunc.HttpFunc.get_report("HYCgettransferhold_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)
