import base64
import configparser


class BaseChange:

    def __init__(self, filename):
        cp = configparser.ConfigParser()
        cp.read(filename)
        self.username = cp.get(section='user', option='username')
        self.passwd = cp.get(section='user', option='passwd')

    def user_encode(self):

        bs = base64.b64encode('%s:%s' % (self.username, self.passwd))
        return r'Basic %s' % (bs,)

