# -*- coding:utf-8 -*-
import configparser
import os
from .BasicFunc import Func
from .logInfo import logger
import sys


class ReadFile(object):

    def __init__(self,file_name):

        self.conf =Func.get_root_path() + '\\config\\'+file_name
        # logger.info("读取的配置文件为: "+self.conf)
        try:
            self.hc = configparser.ConfigParser()
            self.hc.read(self.conf,encoding='utf-8')
        except Exception as e:
            print e
            sys.stderr(e)

    def get_sections(self):
        """
        u'得到所有sections'
        :return:
        """
        return self.hc.sections()

    def get_options(self, section):
        """
        得到某一section下所有的选项
        :param section:
        :return:
        """
        return self.hc.options(section)

    def get_option_value(self, section, option):

        """
        获取option相应的字段值
        :param section:
        :param option:
        :return:
        """
        try:

            return self.hc.get(section, option)
        except Exception as e:
            raise e

    def set_option_value(self, section, option, value):

        """
        增加某项字段值
        :param section:
        :param option:
        :param value:
        :return:
        """
        return self.hc.set(section, option, value)

    def write(self,fp,attr=True):

        self.hc.write(fp,space_around_delimiters=attr)


    def getFileFullPath(self):
        return self.conf

