# -*-coding:utf-8 -*-
import ConfigParser
import cookielib
import urllib2
import urllib
import json
import Base64
import os
import re


class HttpConfig:

    def __init__(self, filename):
        cp = ConfigParser.ConfigParser()
        cp.read(filename)
        self.host = cp.get('http', 'host')
        self.port = cp.get('http', 'port')
        self.headers = {}
        # 加载cookie

        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        urllib2.install_opener(opener)

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host

    def get_port(self):
        return self.port

    def set_port(self,port):
        self.port = port

    def set_header(self, headers):
        self.headers = headers

    def get(self, url, **kwargs):
        if kwargs:
            data = urllib.urlencode(kwargs)
            request = urllib2.Request(url, data)
            response = urllib2.urlopen(request)
        else:

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        return u"状态返回码为:%s,响应报文为:%s" % (response.code, response.read())

    def post_params(self, url, headers, params=None):
        """
        普通参数的请求
        :param url: 接口地址
        :param params: 请求参数
        :param headers: 请求头信息
        :return: 返回值
        """

        self.set_header(headers)

        try:
            if params:
                data = urllib.urlencode(params)
                req_url = self.host + ":" + self.port + url + '? '+data

            else:
                req_url = self.host + ":" + self.port + url

            req = urllib2.Request(req_url, headers=self.headers)

            response = urllib2.urlopen(req)
        except Exception, e:
            print e
            raise e

        print response.read()

    def post_json(self, url, params, headers):
        """
        json体参数
        :param url:接口地址
        :param params:请求参数
        :param headers:请求头信息
        :return:
        """

        self.set_header(headers)



        try:

            request = urllib2.Request(url, params, headers=self.headers)

            response = urllib2.urlopen(request)
        except Exception as e:
            print e
            raise e
        return response.read()

    def get_token(self):
        u"""
        获取token
        """

        hc = Base64.BaseChange(os.getcwd() + r'/config/config.ini')
        data = {"authorization": "%s" % (hc.user_encode(),)}
        data_json = json.dumps(data)
        req_api_url = self.host+':'+self.port+r'/entrance/security/login/json'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Content-Type": "application/json; charset=UTF-8",
            "Connection": "keep-alive"
        }
        print u'请求地址：%s' % (req_api_url,)

        res = self.post_json(req_api_url, data_json, headers)
        find_content = re.findall('.*?"xAuthToken":"(.*?)","sessionId"', res, re.S)
        print u'获取的token值为:%s' % (find_content[0],)
        return find_content[0]







