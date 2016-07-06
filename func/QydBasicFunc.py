# -*- coding:utf-8 -*-

import MysqlDB
import ReadFile
import Base64
import BasicFunc
import requests, json, re, urllib


class QydForeground(object):
    """
        获取轻易贷前台token，以及后续操作。
    """
    def __init__(self):
        self.s = requests.session()
        self.rf = ReadFile.ReadFile(r'/config/qyd_func.ini')

    def get_token(self):
        bs = Base64.BaseChange(r'/config/qyd_func.ini')

        param = {
            "authorization": "%s" % (bs.user_encode(),)
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive"
        }

        url = self.rf.get_option_value("fore_ground","host")+":"+self.rf.get_option_value("fore_ground","port")\
            + self.rf.get_option_value("fore_ground","login_url")

        r=self.s.post(url,data=json.dumps(param),headers=headers)
        # print "请求返回报文："+str(r.content)
        find_content = re.findall('.*?"xAuthToken":"(.*?)","sessionId"', str(r.content), re.S)
        print u'获取的token值为:%s' % (find_content[0],)
        return find_content[0]

    def post(self,url,data=None,json=None,**kwargs):
        r = self.s.post(url,data=data,json=json,**kwargs)
        return r

    def get(self,url,**kwargs):
        r = self.s.get(url,**kwargs)
        return r

    def get_headers(self):
        return self.s.headers

    def get_cookies(self):
        return self.s.cookies

    def header_update(self,*args,**kwds):
        self.s.headers.update(*args,**kwds)

    def header_get(self,key,default=None):
        return self.s.headers.get(key,default=default)


class QydBackGround(object):
    """
        用于轻易贷后台获取token及后续操作。
    """
    def __init__(self):
        self.s = requests.session()
        self.rf = ReadFile.ReadFile(r'/config/qyd_func.ini')

    def getBackToken(self):
        bs = Base64.BaseChange(r'/config/qyd_func.ini')
        _url = self.rf.get_option_value("back_ground","host")+ \
            self.rf.get_option_value("back_ground","validator_url")

        rt = self.get(_url,verify=False)

        param = {
            "name": "%s" % (self.rf.get_option_value("back_ground","username"),),
            "password":"%s" % (self.rf.get_option_value("back_ground","passwd"),)
        }
        header={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Authorization":"%s" % (bs.user_encode_back(),),
            "Cookie":"JSESSIONID=%s" % (rt.cookies['JSESSIONID'],)
        }

        url = self.rf.get_option_value("back_ground","host")\
            + self.rf.get_option_value("back_ground","url_login") \
            + '?' + urllib.urlencode(param)

        r = self.post(url, headers=header,verify=False)
        print "X-Auth-Token为:{}".format(r.headers["X-Auth-Token"])
        return r.headers["X-Auth-Token"]

    def post(self, url, data=None, json=None, **kwargs):
        r = self.s.post(url, data=data, json=json, **kwargs)
        return r

    def get(self, url, **kwargs):
        r = self.s.get(url, **kwargs)
        return r

    def get_headers(self):
        return self.s.headers

    def get_cookies(self):
        return self.s.cookies

    def header_update(self,*args,**kwds):
        self.s.headers.update(*args,**kwds)

    def header_get(self,key,default=None):
        return self.s.headers.get(key,default=default)

