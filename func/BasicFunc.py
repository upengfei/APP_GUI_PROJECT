# -*- coding:utf-8 -*-

import os,sys
import yaml
from functools import wraps

NAME = lambda p : os.path.basename(p).split('.')[0]

class Func(object):
    """
    功能介绍：获取项目根目录
    注意：在get_root_path方法中如果更改项目名称，比如：将‘APP_GUI_PROJECT’更改为‘abc’,则需要将get_root_path方法下的‘APP_API_PROJECT’修改为‘abc’
    """
    def __init__(self):
        pass

    @staticmethod
    def get_root_path():
        """
        回到工程根目录
        :return:
        """
        path = os.getcwd()
        _list = path.split("\\")
        return '\\'.join(_list[:_list.index('APP_GUI_PROJECT')+1])



    @staticmethod
    def getLogDir():
        """
        返回logfile文件路径
        :return:
        """
        logFilePath = Func.get_root_path()+ r'\log_file'
        if not os.path.exists(logFilePath):
            os.mkdir(logFilePath)
            return os.path.abspath(logFilePath)
        else:
            return os.path.abspath(logFilePath)

    @staticmethod
    def create_report(f_name):
        """
        在当前工程指定目录下创建测试报告模板
        :return:
        """
        if not os.path.exists(Func.get_root_path() + '\\report'):
            os.mkdir(Func.get_root_path() + r'\report')

        if not os.path.exists(Func.get_root_path() + r'\\report\\%s.html' % (f_name,)):
            os.chdir(Func.get_root_path() + r'\report')
            f = open(os.getcwd() + '\\%s.html' % (f_name,), 'wb')
            f.close()
            return os.path.join(os.getcwd(), '%s.html' % (f_name,))
        else:
            return os.path.join(Func.get_root_path() + r'\\report', '%s.html' % (f_name,))


def yaml_load(filename):
    """
    读取yaml配置文件
    :param filename: 要读取的文件名
    :return: 
    """
    dirname = Func.get_root_path()+'\\gui\\'+ filename+'.yaml'
    try:
        ft = yaml.load(open(dirname))

    except Exception as e:
        sys.stderr("读取文件错误，请查看文件名称是否正确！")
    return ft


def get_screenshots(driver,imgName=None):
    """
    对macaca 截图方法的重新封装。
    截图并保存到指定目录
    默认截图名称为image,如需指定截图名称需输入名称+格式，如：image.png
    """
    if imgName is None: imgName = NAME(sys.argv[0])

    imgPath = Func.get_root_path()+'\\report\\image\\'+imgName+'.png'
    driver.save_screenshot(imgPath)


def get_screenshots_add(driver,file_name,imgName=None):
    """依据文件名保存截图"""
    if not os.path.exists(Func.get_root_path()+'\\report\\'+file_name):
        os.mkdir(Func.get_root_path()+'\\report\\'+file_name)
    if imgName is None: imgName = NAME(sys.argv[0])
    imgPath = Func.get_root_path() + '\\report\\'+file_name +'\\'+ imgName + '.png'
    driver.save_screenshot(imgPath)


def skipTestIf(port=None):
    """适用于unittest里面跳过某个测试用例，依据参数port，后续可测试在多机的情况下运行不同测试用例"""
    def wrap(func):
        @wraps(func)
        def deco(self):
            if self.port == port and self.port:
                self.skipTest("根据需要，端口为:{0}的跳过该测试用例".format(port))
        return deco
    return wrap


# def init_set(appType='android'):
#     if not appType.lower() in ['ios','android']:sys.stderr("appType类型错误！")
#     if appType == 'android':




if __name__ == '__main__':
    print Func.getLogDir()
