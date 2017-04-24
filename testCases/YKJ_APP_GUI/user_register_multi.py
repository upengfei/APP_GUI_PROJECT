# coding:utf-8
import sys

from macaca import WebDriver
import unittest
from func import get_screenshots
from func.appFunc.ConstConfig import AppBase
from func.appFunc.app_gui_init import AppGuiInit
from func.logInfo import logger
from parameterized import parameterized,param
import time
from func.BasicFunc import skipTestIf
reload(sys)
sys.setdefaultencoding("utf-8")


class Test(AppGuiInit):


    def setUp(self):
        """★★★★★运行初始化方法★★★★"""
        logger.info("测试开始")
        androids=[('17a8606b',3456),('123344',3457)]
        for items in androids:
            self.uuid = items[0]
            self.port = items[1]
            desired_caps = {
                'platformName': '%s' % AppBase.PLATFORMNAME.value,
                'app': '%s' % AppBase.app.value,
                'reuse': '%d' % AppBase.reuse.value,
                'udid': '%s' % self.uuid

            }
            server_url='http://127.0.0.1:%d/wd/hub' % self.port
            self.driver = WebDriver(desired_caps,server_url)
            self.driver.init()
            time.sleep(10)


    def tearDown(self):
        """测试用例运行结束，开始后续处理"""
        get_screenshots(self.driver,imgName='register.png')
        self.driver.quit()
        logger.info("测试用例运行结束，开始后续处理☜☜☜☜☜")

    # 正常流程
    @skipTestIf(port=3457)
    def test_gui_register(self):
        """ 友空间-注册"""
        self.driver \
            .element_by_xpath(self.ft['android']['register']['register']) \
            .click()



