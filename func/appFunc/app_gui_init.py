# coding:utf-8

import unittest
import sys
from macaca import WebDriver,util,WebElement
from func import *
from func.logInfo import logger
from func.appFunc.ConstConfig import AppBase
reload(sys)
sys.setdefaultencoding("utf-8")
from func.BasicFunc import yaml_load,Func

class AppGuiInit(unittest.TestCase):
    """移动端gui初始化"""
    @classmethod
    def setUpClass(cls):
        """★★★★★运行初始化方法★★★★"""
        logger.info("类初始化。。。")
        cls.ft = yaml_load('AppGui')
        cls.rd = ReadFile("Appconfig.ini")

        desired_caps = {
            'platformName': '%s' % AppBase.PLATFORMNAME.value,
            'app': '%s' % AppBase.app.value,
            'reuse': '%d' % AppBase.reuse.value,
            'udid': '17a8606b'

        }
        cls.driver = WebDriver(desired_caps)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        """测试用例运行结束，开始后续处理"""
        cls.driver.quit()


