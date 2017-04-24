# coding:utf-8

import unittest
import sys

from func import *
from func.logInfo import logger
reload(sys)
sys.setdefaultencoding("utf-8")


class GesturePwdInit(unittest.TestCase):
    """手机密码验证、登录密码验证等接口初始化方法"""
    def setUp(self):
        """★★★★★运行初始化方法★★★★"""
        logger.info("★★★★★运行初始化方法★★★★★")
        BasicFunc.Func().get_root_path()
        self.qa = QydBasicFunc.QydAppToken(path=r'\config\AppConfig.ini')
        self.rf = ReadFunc.ReadFile('\\config\\AppConfig.ini')
        self.md = MysqlDB.MysqlDB('\\config\\AppConfig.ini')

    def tearDown(self):
        """测试用例运行结束，开始后续处理"""
        logger.info("测试用例运行结束，开始后续处理★★★★★")
        self.md.cursor_close()
        self.md.conn_close()

