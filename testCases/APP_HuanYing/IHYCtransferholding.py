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


class IHYCgettransferhold(unittest.TestCase):
    def setUp(self):
        BasicFunc.Func().get_root_path()
        self.s = QydBasicFunc.QydAppToken()
        self.rf = ReadFunc.ReadFile('/config/newHYconf.ini')
        self.md = MysqlDB.MysqlDB('/config/newHYconf.ini')
        self.rowNum=0


    def tearDown(self):

        self.md.cursor_close()
        self.md.conn_close()



    # 正常流程
    def test_gettransferhold(self):
        """ 欢盈理财中债权列表-正常流程"""
        # 获取前台token
        token = self.s.getToken()
        data={
            "pageNumber": "1",
            "pageSize":"5"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,


        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回报文为：{0}".format(r.content))
        print "返回报文为：{0}".format(r.content)
    # 校验数据库 涉及到表loan,loan_lender_
        sql = "select count(*) from loan_lender_detail ld  JOIN loan l on l.id = ld.loan_id LEFT OUTER JOIN user u on " \
              "u.id=ld.user_id where u.tel_num='%s' and ld.hold_amount>0 and ld.`status`<>1 and " \
              "l.debttype='HY' limit 100 OFFSET 0;" % self.rf.get_option_value("user","username")

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
        token = self.s.getToken()
        data={
            "pageNumber": "1",
            "pageSize":"ad"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_02(self):
        """ 欢盈理财中债权列表-异常流程-size错误输入"""
        # 获取前台token
        token = self.s.getToken()
        data={
            "pageNumber": "qw",
            "pageSize":"5"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_03(self):
        """ 欢盈理财中债权列表-异常流程-pageSize为空"""
        # 获取前台token
        token = self.s.getToken()
        data={
            "pageNumber": "1",
            "pageSize":""
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)

    def test_gettransferhold_ex_04(self):
        """ 欢盈理财中债权列表-异常流程-pageNumber为空"""
        # 获取前台token
        token = self.s.getToken()
        data={
            "pageNumber": "",
            "pageSize":"5"
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token":"%s" % token,

        }
        url = self.rf.get_option_value("http","base_url")+self.rf.get_option_value("api","gettransfer_url")

        r = self.s.post(url,data=json.dumps(data),headers=header,verify=False)
        logger.info("返回错误信息报文为：{0}".format(r.content))
        print "返回错误信息报文为：{0}".format(r.content)



if __name__=='__main__':
    suite = unittest.TestSuite(map(IHYCgettransferhold,[
        "test_gettransferhold",
        # "test_gettransferhold_ex_01",
        # "test_gettransferhold_ex_02",
        # "test_gettransferhold_ex_03",
        # "test_gettransferhold_ex_04",

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("HYCgettransferhold_report")

    filename = HttpFunc.HttpFunc.get_report("HYCgettransferhold_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷欢盈接口测试报告',description="测试详情:")
    runner.run(suite)
