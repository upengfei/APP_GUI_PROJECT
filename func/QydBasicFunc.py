# -*- coding:utf-8 -*-

import MysqlDB
import conf_read
import Base64
import BasicFunc
import requests, json, re, urllib
from func.logInfo import logger
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class QydForeground(object):
    """
        获取轻易贷前台token，以及后续操作。
    """
    def __init__(self):
        self.s = requests.session()
        self.rf = conf_read.ReadFile(r'/config/qyd_func.ini')

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

        url = self.rf.get_option_value("fore_ground","host")\
            + self.rf.get_option_value("fore_ground","login_url")

        r=self.s.post(url,data=json.dumps(param),headers=headers,verify=False)
        # print "请求返回报文："+str(r.content)
        find_content = re.findall('.*?"xAuthToken":"(.*?)","sessionId"', str(r.content), re.S)
        # print u'获取的token值为:%s' % (find_content[0],)
        return find_content[0]

    def post(self,url,data=None,json=None,**kwargs):
        try:
            r = self.s.post(url,data=data,json=json,**kwargs)

            return r
        except Exception as e:
            logger.info("发送post请求错误，错误信息为:",e)
            sys.exit()

    def get(self,url,**kwargs):
        try:
            r = self.s.get(url,**kwargs)
            return r
        except Exception as e:
            logger.info("发送get请求错误，错误信息为:",e)
            sys.exit()

    def get_headers(self):
        return self.s.headers

    def get_cookies(self):
        '''
        获取cookie值
        :return:
        '''
        return self.s.cookies

    def header_update(self,*args,**kwds):
        '''
        增加header参数
        :param args:
        :param kwds:
        :return:
        '''
        self.s.headers.update(*args,**kwds)


    def header_get(self,key,default=None):
        '''
        获取header对应key的值
        :param key:
        :param default:
        :return:
        '''
        return self.s.headers.get(key,default=default)


class QydBackGround(object):
    """
        用于轻易贷后台获取token及后续操作。
    """
    def __init__(self):
        self.s = requests.session()
        self.rf = conf_read.ReadFile(r'/config/qyd_func.ini')

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
        '''

        :param url:
        :param data:
        :param json: 支持直接使用json体参数进行请求
        :param kwargs:
        :return:
        '''
        try:
            r = self.s.post(url, data=data, json=json, **kwargs)
            return r
        except Exception as e:
            logger.info("发送post请求错误，错误信息为:",e)
            sys.exit()

    def get(self, url, **kwargs):
        try:
            r = self.s.get(url, **kwargs)
            return r
        except Exception as e:
            logger.info("发送get请求错误，错误信息为:",e)
            sys.exit()

    def get_headers(self):
        return self.s.headers

    def get_cookies(self):
        return self.s.cookies

    def header_update(self,*args,**kwds):
        self.s.headers.update(*args,**kwds)

    def header_get(self,key,default=None):
        return self.s.headers.get(key,default=default)

