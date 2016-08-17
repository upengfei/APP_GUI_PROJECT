# -*- coding:utf-8 -*-

import time
import unittest

from func import HTMLTestRunner, HttpFunc, MysqlDB, PySelenium, conf_read


class QydTest(unittest.TestCase):

    def setUp(self):
        HttpFunc.HttpFunc().get_root_path()
        self.ps = PySelenium.PySelenium()
        self.rf = conf_read.ReadFile()
        self.msd = MysqlDB.MysqlDB()

    def tearDown(self):
        self.ps.quit()
        # pass

    def test_qyd_login(self):

        self.ps.open_url(self.rf.get_option_value("http","host"))
        if self.ps.is_display(u'link_text=>用户登录'):
            print u"正常打开轻易贷首页，开始进行登录"
            self.ps.window_max()
            self.ps.click_text(u'用户登录')
        else:
            print u'首页打开失败'

        self.ps.input_type('css=>#username', self.rf.get_option_value("user", "username"))

        self.ps.input_type('css=>#password',self.rf.get_option_value("user", "passwd"))

        self.ps.click('css=>#login')

        time.sleep(3)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(QydTest('test_open_qyd'))

    suite = unittest.TestSuite(
        map(
            QydTest,
            [
                "test_qyd_login",

            ]
        )
    )
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HttpFunc.HttpFunc.create_report("test_gui")

    filename = HttpFunc.HttpFunc.get_report("test_gui")
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试报告详情： ')
    runner.run(suite)