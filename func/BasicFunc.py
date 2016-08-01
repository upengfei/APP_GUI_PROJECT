# -*- coding:utf-8 -*-

import os

class Func:
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

