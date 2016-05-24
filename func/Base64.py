import base64
import configparser
from func import otherFunc

class BaseChange:

    def __init__(self):
        file_path = otherFunc.Func.get_root_path()+r'/config/config.ini'
        cp = configparser.ConfigParser()
        cp.read(file_path)
        self.username = cp.get(section='user', option='username')
        self.passwd = cp.get(section='user', option='passwd')

    def user_encode(self):

        bs = base64.b64encode('%s:%s' % (self.username, self.passwd))
        return r'Basic %s' % (bs,)

