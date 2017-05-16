# -*- coding:utf-8 -*-
"""
功能介绍：封装了一些常用的基础方法
注意：在get_root_path方法中如果更改项目名称，比如：将‘APP_GUI_PROJECT’更改为‘abc’,则需要将get_root_path方法下的‘APP_API_PROJECT’修改为‘abc’
"""
import os,sys
import yaml
from functools import wraps
from configparser import ConfigParser

NAME = lambda p : os.path.basename(p).split('.')[0]




def get_root_path():
    """
    获取工程根目录
    :return:
    """
    path = os.getcwd()
    _list = path.split(os.sep)
    return os.sep.join(_list[:_list.index('APP_GUI_PROJECT')+1])



def getLogDir():
    """
    返回logfile文件路径
    :return:
    """
    logFilePath = get_root_path()+ os.sep+'logFile'
    if not os.path.exists(logFilePath):
        os.mkdir(logFilePath)
        return os.path.abspath(logFilePath)
    else:
        return os.path.abspath(logFilePath)


def create_report(f_name):
    """
    在当前工程指定目录下创建测试报告模板
    :return:
    """
    if not os.path.exists(get_root_path() + os.sep+'report'):
        os.mkdir(get_root_path() + os.sep+'report')

    if not os.path.exists(get_root_path() + os.sep+'report'+os.sep+'%s.html' % (f_name,)):
        os.chdir(get_root_path() + os.sep+'report')
        f = open(os.getcwd() + os.sep+'%s.html' % (f_name,), 'wb')
        f.close()
        return os.path.join(os.getcwd(), '%s.html' % (f_name,))
    else:
        return os.path.join(get_root_path() + os.sep+'report', '%s.html' % (f_name,))


def yaml_load(filename):
    """
    读取yaml配置文件
    :param filename: 要读取的文件名
    :return: 
    """
    dirname = get_root_path()+os.sep+'gui'+os.sep+ filename+'.yaml'
    try:
        ft = yaml.load(open(dirname))

    except Exception as e:
        raise Exception(e)
    return ft


def get_screenshots(driver,imgName=None):
    """
    对macaca 截图方法的重新封装。
    截图并保存到指定目录
    默认截图名称为image,如需指定截图名称需输入名称+格式，如：image.png
    """
    if imgName is None: imgName = NAME(sys.argv[0])

    imgPath = get_root_path()+os.sep+'report'+os.sep+'image'+os.sep+imgName+'.png'
    driver.save_screenshot(imgPath)


def get_screenshots_add(driver,file_name,imgName=None):
    """依据文件名保存截图"""
    if not os.path.exists(get_root_path()+os.sep+'report'+os.sep+file_name):
        os.mkdir(get_root_path()+os.sep+'report'+os.sep+file_name)
    if imgName is None: imgName = NAME(sys.argv[0])
    imgPath = get_root_path() + os.sep+'report'+os.sep+file_name +os.sep+ imgName + '.png'
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




def read_conf(conf_path):
    """

    :param conf_path: ***.ini or ***.txt or ***.conf等格式文件，在config/下。
    :return: 
    """
    try:
        hd = ConfigParser()
        hd.read(get_root_path() + os.sep + 'config' + os.sep + conf_path, encoding='utf-8')
        return hd
    except Exception as e:
        raise e




if __name__ == '__main__':
    print getLogDir()
