import base64
import configparser
from func import BasicFunc,conf_read

class BaseChange(object):

    def __init__(self,path):
        file_path = BasicFunc.Func.get_root_path() + path
        self.rf = conf_read.ReadFile(path)

    def user_encode(self):

        bs = base64.b64encode('%s:%s' % (self.rf.get_option_value("fore_ground","username"),\
                                         self.rf.get_option_value("fore_ground","passwd")))
        return r'Basic %s' % (bs,)

    def user_encode_new(self, user, passwd):

        bs = base64.b64encode('%s:%s' % (user, passwd))
        return r'Basic %s' % (bs,)

    def user_encode_back(self):
        bs = base64.b64encode('%s:%s:0000' % (self.rf.get_option_value("back_ground","username"),\
                                              self.rf.get_option_value("back_ground","passwd")))
        return r'Basic %s' % (bs,)

