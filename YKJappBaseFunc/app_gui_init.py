# coding:utf-8

import sys
import unittest

from macaca import WebDriver
from lib import BasicFE
from lib import app_init,read_conf
from lib import logger

reload(sys)
sys.setdefaultencoding("utf-8")
from lib import yaml_load


class AppGuiInit(unittest.TestCase):
    """移动端gui初始化"""
    @classmethod
    def setUpClass(cls):
        """★★★★★运行初始化方法★★★★"""
        logger.info("类初始化。。。")
        cls.ft = yaml_load('AppGui')
        cls.rd = read_conf('userData.ini')
        cls.driver = app_init()






    @classmethod
    def tearDownClass(cls):
        """测试用例运行结束，开始后续处理"""
        cls.driver.quit()


