# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os,sys,time


class PySelenium(object):

    def __init(self, browser="ff"):
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

        :param data_type: data_type类型如下：css:#id,xpath://,id:kw,name:name,class:class
        :return:
        '''
        if ':' not in data_type:
            raise NameError(u"data_type格式错误，请输入正确的格式，如：css:#id")
        type = data_type.split(':')[0]
        value = data_type.split(':')[1]

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

        if ':' not in data_type:
            raise NameError(u"data_type格式错误，请输入正确的格式，如：css:#id")
        type = data_type.split(':')[0]
        value = data_type.split(':')[1]

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

