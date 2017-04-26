# coding:utf-8
import sys

from macaca import WebDriver,util,WebElement
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
        self.info="准备开始测试"
        logger.info(self.info)

        # desired_caps = {
        #     'platformName': '%s' % AppBase.PLATFORMNAME.value,
        #     'app': '%s' % AppBase.app.value,
        #     'reuse': '%d' % AppBase.reuse.value,
        #     'udid': '17a8606b'
        #
        # }
        # self.driver = WebDriver(desired_caps)
        # self.driver.init()
    def tearDown(self):
        """测试用例运行结束，开始后续处理"""
        get_screenshots(self.driver)
        # self.driver.quit()
        logger.info("测试用例运行结束，开始后续处理☜☜☜☜☜")

    # 正常流程
    @unittest.skip("跳过注册")
    def test_gui_register(self):
        """ 友空间-注册"""
        self.driver \
            .element_by_xpath(self.ft['android']['register']['register']) \
            .click()
    # @unittest.skip("登录跳过")
    def test_login(self):
        """友空间-登录"""
        self.info=self.info+"--开始进行登录测试"
        logger.info(self.info)
        login = self.ft['android']['login']
        self.driver \
            .element_by_xpath(self.ft['android']['login']['username'])\
            .send_keys("%s" % self.rd.get_option_value("Test_user","user"))

        self.driver \
            .element_by_xpath(login['passwd'])\
            .send_keys('%s' % self.rd.get_option_value("Test_user","pwd"))

        self.driver \
            .element_by_xpath(login['button_login']) \
            .click()

        self.driver \
            .wait_for_element_by_xpath(login['all_status_tag'])

        self.info=self.info+'--友空间登录成功！'
        logger.info(self.info)
        print self.info

    def test_logout(self):
        """友空间-登出功能演示操作"""
        self.info +="→→开始进行登出操作"
        logger.info(self.info)
        logout=self.ft['android']['logout']
        self.info+="→→进入个人设置"
        logger.info(self.info)
        print self.info
        self.driver \
            .element_by_xpath(logout['personal_set'])\
            .click()
        # self.driver \
        #     .wait_for_element_by_xpath(logout['setup_tag'])
        self.info+="→→Now,点击'设置'！"
        print self.info
        time.sleep(1)

        myinvitePeople = self.driver\
                             .element_by_xpath(logout['MyinvitePeople'])

        rect = myinvitePeople.rect
        x_center = rect['x'] + rect['width'] / 2

        y_down = rect['y'] + rect['height']

        self.driver.touch('drag',{'fromX': x_center, 'fromY': y_down, 'toX': x_center, 'toY': rect['height']})
        setButton = self.driver \
                        .element_by_xpath(logout['setup_tag'])
        if setButton.is_displayed():
            setButton.click()

        self.driver \
            .wait_for_element_by_xpath(logout['set_page']['about'])
        print"进入设置页成功"
        self.driver \
            .element_by_xpath(logout['set_page']['button_logout'])\
            .click()
        print "登出成功！"
        logger.info("登出成功！")
