# -*- coding:utf-8 -*-

import json
import logging
import os
import re
import urllib

import ReadFile
from func import Base64, HttpCurl,otherFunc

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(message)s")


class HttpFunc:

    """
    封装了进行接口测试时所用到的一些方法
    """
    def __init__(self):
        self.hc = HttpCurl.PyCurl()
        # self.buf = StringIO.StringIO()
        self.rf = ReadFile.ReadFile()

        self.log = logging.getLogger()

    def get_token(self):

        list_data = []

        header = [
            'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Content-Type: application/json; charset=UTF-8'
        ]

        bc = Base64.BaseChange(os.getcwd() + r'/config/config.ini')
        data = {"authorization": "%s" % (bc.user_encode(),)}
        # data_json = json.dumps(data)
        req_api_url = self.rf.get_option_value("http", "host")+':'\
                      + self.rf.get_option_value("http", "port") \
                      + r'/entrance/security/login/json'

        value = self.hf_post(req_api_url, data, header, 2)

        # self.log.info("&&&&&&:{}".format(value))
        find_content = re.findall('.*?"xAuthToken":"(.*?)","sessionId"', value, re.S)

        list_data.append(str(find_content[0]))
        list_data.append(self.hc.buf_tell())
        # print self.hc.buf_tell()
        return list_data

    def hf_post(self, url, params=None, headers=None, arg_type=1, location=None, action=1):
        """

        :param url:
        :param params:
        :param headers:
        :param arg_type: 0没有参数,1为普通参数,2为json体参数
        :param action: 1post,0get
        :return:
        """
        if not range(0, 3).__contains__(arg_type): print u'请填写正确的arg_type(0没有参数,1为普通参数,2为json体参数)'
        self.hc.set_url(url)
        self.hc.set_write()
        self.hc.set_cookie()
        if headers: self.hc.set_header(headers)

        if arg_type == 1:
            data = urllib.urlencode(params)
            # print "%%%%%%", data
            self.hc.post_data(data, action)
        elif arg_type == 2:
            data = json.dumps(params)
            self.hc.post_data(data, action)
        elif arg_type == 0:
            self.hc.post_data(data=None, num=action)
        try:
            self.hc.perform()

            if location is not None:
                self.buf_seek(location)
                return unicode(self.buf_read(), "UTF-8")

            return unicode(self.get_buff_value(), "UTF-8")

        except Exception as e:
            raise e

    @staticmethod
    def create_report(f_name):
        """
        在当前工程指定目录下创建测试报告模板
        :return:
        """


        if os.path.exists(otherFunc.Func().get_root_path()+'\\report'):
            pass
        else:
            os.mkdir(otherFunc.Func().get_root_path()+r'\report')

        if os.path.exists(otherFunc.Func().get_root_path()+r'\\report\\%s.html' % (f_name,)):
            pass
        else:
            os.chdir(otherFunc.Func().get_root_path()+r'\report')
            f = open(os.getcwd()+'\\%s.html' % (f_name,), 'wb')
            f.close()

    @staticmethod
    def get_report(f_name):
        f_name = "%s.html" % (f_name,)

        path = os.getcwd()

        if path.split('\\').__contains__("report"):
            pass
        else:
            os.chdir(path+r'\report')
            path = os.getcwd()
        print u'当前路径为：'+path
        # self.log.info('当前路径为：{}'.format(path))
        if os.path.exists(path):
            listdir = os.listdir(path)

            if listdir.__contains__(f_name):
                os.chdir(path)
                new_path = os.path.join(path, f_name)
                return new_path
            else:
                print u"该文件：%s不存在" % (f_name,)
        else:
            print u'获取测试报告路径不正确'
            return False

    def buf_tell(self):
        return self.hc.buf_tell()

    def buf_seek(self, offset):
        return self.hc.buf_seek(offset)

    def buf_read(self):
        return self.hc.buf_read()

    def buf_close(self):
        self.hc.buffer_close()

    def buf_write(self):
        self.hc.set_write()

    def get_code(self):
        return self.hc.get_info_code()

    def get_buff_value(self):
        return self.hc.get_value()


