# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os,sys,time


class PySelenium(object):

    def __init__(self, browser="ff"):

        try:
            if browser == "firefox" or browser == "ff":
                self.driver = webdriver.Firefox()
            elif browser == "chrome":
                self.driver = webdriver.Chrome()
            elif browser == "internet explorer" or browser == "ie":
                self.driver = webdriver.Ie()

        except Exception:
            raise NameError(u"没有找到（%s） 浏览器," % browser)

    def open_url(self, url):
        '''
        打开目标网址
        :param url:URL地址
        :return:
        '''
        self.driver.get(url)

    def window_max(self):

        self.driver.maximize_window()

    def close(self):
        '''
        退出浏览器
        :return:
        '''
        self.driver.close()

    def get_element(self, data_type):
        '''

        :param data_type: data_type类型如下：css=>#id,xpath=>//,id=>kw,name=>name,class=>class
        :return:
        '''
        if '=>' not in data_type:
            raise NameError(u"data_type格式错误，请输入正确的格式，如：css:#id")
        type = data_type.split('=>')[0]
        value = data_type.split('=>')[1]

        if type == 'id':
            element = self.driver.find_element_by_id(value)
        elif type == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif type == 'name':
            element = self.driver.find_element_by_name(value)
        elif type == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif type == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif type == 'css':
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(u'value值错误')
        return element

    def element_wait(self, data_type, sec=3):

        if '=>' not in data_type:
            raise NameError(u"data_type格式错误，请输入正确的格式，如：css=>#id")
        type = data_type.split('=>')[0]
        value = data_type.split('=>')[1]

        if type == 'id':
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.ID, value)))
        elif type == 'name':
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.NAME, value)))
        elif type == 'class':
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.CLASS_NAME, value)))
        elif type == 'xpath':
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.XPATH, value)))
        elif type == 'css':
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif type == 'link_text':
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.LINK_TEXT, value)))
        else:
            raise NameError(u"找不到type类型，请输入正确的类型")

    def set_window_size(self, width, height, windowhandle='current'):
        '''

        :param width:
        :param height:
        :param windowhandle:
        :return:
        '''

        self.driver.set_window_size(width, height, windowHandle=windowhandle)

    def input_type(self, data_type, text):
        '''
        适用于填充框的输入
        :param data_type:
        :param text:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        el.clear()
        el.send_keys(text)

    def click(self, data_type):
        '''
        适用于点击控件
        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        el.click()

    def right_click(self, data_type):
        '''
        右键点击element
        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, data_type):
        '''
        移动鼠标指针到element
        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, data_type):
        '''
        双击某个element
        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, data_type, target_data):
        '''
        拖动鼠标到某个element
        :param data_type:
        :param target_data:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        self.element_wait(target_data)
        el_target = self.get_element(target_data)
        ActionChains(self.driver).drag_and_drop(el, el_target).perform()

    def click_text(self, text):
        '''
        Click the element by the link_text
        :param text:
        :return:
        '''
        self.driver.find_element_by_link_text(text).click()

    def quit(self):
        '''
        关闭所有的窗口,退出driver
        :return:
        '''
        self.driver.quit()

    def data_commit(self, data_type):
        '''

        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        el.submit()

    def refresh(self):
        '''
        刷新当前页面
        :return:
        '''
        self.driver.refresh()

    def get_text(self, data_type):

        self.element_wait(data_type)
        el = self.get_element(data_type)
        return el.text

    def get_attribute(self, data_type, attr):

        self.element_wait(data_type)
        el = self.get_element(data_type)
        return el.get_attribute(attr)

    def is_display(self, data_type):
        '''
        element是否已经显示
        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        return el.is_displayed()

    def is_selected(self,data_type):
        '''
        element是否已经选择
        :param data_type:
        :return:
        '''
        self.element_wait(data_type)
        el = self.get_element(data_type)
        return el.is_selected()

    def get_title(self):
        '''
        得到当前窗口名称
        :return:
        '''
        return self.driver.title

    def get_url(self):
        '''
        返回当前页的网址
        :return:
        '''
        return self.driver.current_url

    def get_window_screenshots(self, file_path):
        '''
        获取屏幕截图保存到相应目录
        :param file_path:
        :return:
        '''

        self.driver.get_screenshot_as_file(file_path)

    def alert_accept(self):
        '''
        确认点击警告对话框
        :return:
        '''
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        '''
        关闭警告对话框
        :return:
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        根据css属性切换到对应frame框架
        :param css:
        :return:
        '''
        el = self.driver.find_element_by_css_selector(css)
        self.driver.switch_to.frame(el)

    def forward(self):
        '''
        控制当前窗口前进或者后退
        :return:
        '''
        self.driver.forward()

    def get_window_handle(self):
        '''
        获取当前窗口句柄
        :return:
        '''
        return self.driver.current_window_handle

    def switch_to_new_window(self, window_old_handle):
        '''
        适用于点击某个控件后，跳转到新的窗口,配合get_window_handle使用
        :param window_old_handle:
        :return:
        '''

        all_handles = self.driver.window_handles

        for handle in all_handles:
            if handle != window_old_handle:
                self.driver._switch_to.window(handle)

