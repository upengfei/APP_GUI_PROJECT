# coding:utf-8
import time
import unittest
import uuid,json
from func import *
from func.logInfo import logger
from testCases.app_init import GesturePwdInit


class JiGuangBindingID(GesturePwdInit):

    def setUp(self):
        """★★★★★运行初始化方法★★★★"""
        logger.info("★★★★★重写setup方法，并初始化★★★★★")
        BasicFunc.Func().get_root_path()
        self.qa = QydBasicFunc.QydAppToken(path=r'\config\AppConfig.ini')
        self.rf = ReadFunc.ReadFile('\\config\\AppConfig.ini')
        self.md = MysqlDB.MysqlDB('\\config\\AppConfig.ini',configName='JGdb')

    def test_BindingId(self):
        """极光推送注册ID绑定-数据库不存在id-正常流程"""
        # 获取token
        token = self.qa.getToken(section='Appuser')
        logger.info("****  %s"% token)
        _id = uuid.uuid1()
        data = {
            "registrationId":"%s" % _id
        }

        header = {
            "X-Auth-Token":"%s" % token
        }

        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','jgbinding_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)

        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content


        #  校验数据库
        sql = "select count(*) from registration where registration_id = '%s'and tel_num = '%s'" %(_id,
                                                                                                self.rf.get_option_value('Appuser','username'))

        self.md.execute(sql)
        icount = self.md.fetchone()[0]
        if int(icount)==1:
            logger.info("验证数据库registration成功，验证sql为：%s" % sql)
            print("验证数据库registration成功，验证sql为：%s" % sql)
        else:
            logger.error("验证数据库失败，验证sql为:%s" % sql)
            print("验证数据库失败，验证sql为:%s" % sql)
        # 初始化数据库：
        sql1 = "delete from registration where registration_id='%s';commit"% _id
        self.md.execute(sql1)
        logger.info("初始化数据库成功，初始化sql:%s" % sql1)
        print("初始化数据库成功，初始化sql:%s" % sql1)

    def test_BindingId_01(self):
        """极光推送注册ID绑定-数据库已存在id，并做更新-正常流程"""

        # 获取已存在的registration——id
        sql = "select r.registration_id from registration r where r.tel_num = '%s'"% self.rf.get_option_value('Appuser01','username')
        self.md.execute(sql)
        old_id = self.md.fetchone()[0]

        # 获取token
        token = self.qa.getToken(section='Appuser01')
        _id = uuid.uuid1()
        data = {
            "registrationId":"%s" % _id
        }

        header = {
            "X-Auth-Token":"%s" % token
        }

        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','jgbinding_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)

        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content


        #  校验数据库
        sql1 = "select registration_id from registration where tel_num = '%s'" %(self.rf.get_option_value('Appuser01','username'))

        self.md.execute(sql1)
        new_id = self.md.fetchone()[0]
        if new_id!=old_id:
            logger.info("验证数据库registration成功，验证sql为：%s，先前registrationID为：%s,更新后的id为：%s" % (sql1,old_id,new_id))
            print("验证数据库registration成功，验证sql为：%s，先前registrationID为：%s,更新后的id为：%s" % (sql1,old_id,new_id))
        else:
            logger.error("验证数据库失败，验证sql为：%s，先前registrationID为：%s,更新后的id为：%s" % (sql1,old_id,new_id))
            print("验证数据库失败，验证sql为：%s，先前registrationID为：%s,更新后的id为：%s" % (sql1,old_id,new_id))
        # 初始化数据库：
        # sql1 = "delete from registration where registration_id='%s';commit"% _id
        # self.md.execute(sql1)
        # logger.info("初始化数据库成功，初始化sql:%s" % sql1)
        # print("初始化数据库成功，初始化sql:%s" % sql1)

    def test_BindingId_exception(self):
        """异常处理流程--用户token错误"""
         # 获取token
        token = self.qa.getToken()
        _id = uuid.uuid1()
        data = {
            "registrationId":"%s" % _id
        }

        header = {
            "X-Auth-Token":"dr45fsdddd"
        }

        _url = self.rf.get_option_value('app','host')+self.rf.get_option_value('api','jgbinding_url')
        response = self.qa.post(_url,data=json.dumps(data),headers=header,verify=False)

        logger.info("返回报文如下:{0}".format(response.content))
        assert response.json()['status'] == 200 and response.json()['successful'] == True,"验证错误，返回的报文如下:%s"\
                                                                                      % response.content

if __name__ == '__main__':
    suite = unittest.TestSuite(map(JiGuangBindingID,[
        "test_BindingId",
        "test_BindingId_01",
        "test_BindingId_exception"

    ]))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    HttpFunc.HttpFunc.create_report("JiGuangBindingID_report")

    filename = HttpFunc.HttpFunc.get_report("JiGuangBindingID_report")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='轻易贷极光推送绑定ID接口测试报告',
                                           description="轻易贷极光推送绑定ID接口测试详情:")
    runner.run(suite)