# -*- coding:utf-8 -*-
import configparser
import os
import BasicFunc

import sys


class ReadFile:
    def __init__(self,filePath):

        path = BasicFunc.Func.get_root_path() + filePath
        try:
            self.hc = configparser.ConfigParser()
            self.hc.read(path)
        except Exception as e:

            sys.exit()

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

            sys.exit()

    def set_option_value(self, section, option, value):

        """
        增加某项字段值
        :param section:
        :param option:
        :param value:
        :return:
        """
        return self.hc.set(section, option, value)
