# coding:utf-8
import base64
import configparser
from func import BasicFunc,ReadFunc

class BaseChange(object):
    """后续视情况,进行方法的补充"""
    def __init__(self,path):
        file_path = BasicFunc.Func.get_root_path() + path
        self.rf = ReadFunc.ReadFile(path)
    """
    def user_encode(self,section='user'):

        bs = base64.b64encode('%s:%s' % (self.rf.get_option_value(section,"username"),
                                         self.rf.get_option_value(section,"passwd")))
        return r'Basic %s' % (bs,)

    def user_encode_new(self, user, passwd):

        bs = base64.b64encode('%s:%s' % (user, passwd))
        return r'Basic %s' % (bs,)

    def user_encode_back(self):
        bs = base64.b64encode('%s:%s:0000' % (self.rf.get_option_value("buser","username"),
                                              self.rf.get_option_value("buser","passwd")))
        return r'Basic %s' % (bs,)
    """
