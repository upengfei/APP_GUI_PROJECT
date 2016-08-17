# -*- coding:utf-8 -*-

import os

class Func(object):
    def __init__(self):
        pass

    @staticmethod
    def get_root_path():
        """
        回到工程根目录
        :return:
        """
        path = os.getcwd()
        list_dir = os.path.split(path)
        if not list_dir[1] == 'Api-project':
            os.chdir(list_dir[0])
            # print list_dir[0]
            return list_dir[0]
        else:
            return path

    def getLogDir(self):
        """
        在当前工程指定目录下创建测试报告模板
        :return:
        """
        if not os.path.exists(Func.get_root_path()+ '\\log_file'):
            os.mkdir(self.get_root_path() + r'\log_file')
            logDir = os.path.join(Func.get_root_path() + r'\log_file')
            return logDir
        else:

            logDir = os.path.join(Func.get_root_path() + r'\log_file')
            return logDir