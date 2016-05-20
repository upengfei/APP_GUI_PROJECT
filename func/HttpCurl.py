# -*- coding:utf-8 -*-
import StringIO
import pycurl


class PyCurl:

    def __init__(self):

        self.c = pycurl.Curl()
        self.c.s = StringIO.StringIO()
        self.c.setopt(pycurl.COOKIEFILE, 'cookie_file')
        self.c.setopt(pycurl.COOKIEJAR, 'cookie_file')
        self.c.setopt(pycurl.FOLLOWLOCATION, 1)
        self.c.setopt(pycurl.ENCODING, 'gzip')
        self.c.setopt(pycurl.VERBOSE, 1)
        self.c.setopt(pycurl.WRITEFUNCTION, self.c.s.write)

    def set_cookie(self):
        '''
        设置cookie
        :return:
        '''
        self.c.setopt(pycurl.COOKIEFILE, 'cookie_file')
        self.c.setopt(pycurl.COOKIEJAR, 'cookie_file')

    def set_url(self, url):
        '''
        设置请求的地址
        :param url:
        :return:
        '''
        self.c.setopt(pycurl.URL, url)

    def set_user_agent(self, user_agent):
        '''
        设置user-agent
        :param user_agent:
        :return:
        '''
        self.c.setopt(pycurl.USERAGENT, user_agent)

    def set_refer(self, url):
        '''
        设置安全连接
        :param url:
        :return:
        '''
        self.c.setopt(pycurl.REFERER, url)

    def get_info_code(self):
        return self.c.getinfo(pycurl.HTTP_CODE)

    def get_value(self):

        return self.c.s.getvalue()

    def buffer_close(self):
        self.c.s.close()

    def set_header(self, header):
        """

        :param header:header列表
        :return:
        """
        # self.c.setopt(pycurl.HEADER, True)
        self.c.setopt(pycurl.HTTPHEADER, header)

    def perform(self):
        self.c.perform()

    def post_data(self, data=None, num=1):
        """

        :param data:
        :param num: 0表示get请求，1表示post
        :return:
        """
        if num==0:
            self.c.setopt(pycurl.CUSTOMREQUEST,"GET")
        elif num==1:
            self.c.setopt(pycurl.CUSTOMREQUEST,"POST")

        if data is not None:
            self.c.setopt(pycurl.POSTFIELDS, data)
        else:
            self.c.setopt(pycurl.POSTFIELDS, "")

    def set_write(self):
        self.c.setopt(pycurl.WRITEFUNCTION, self.c.s.write)

    def seek_end(self):
        self.c.s.seek(2)

    def set_read(self):
        self.c.setopt(pycurl.READFUNCTION, self.c.s.read)

    def buf_tell(self):
        return self.c.s.tell()

    def buf_seek(self, offset):
        self.c.s.seek(offset, 0)

    def buf_read(self):
        return self.c.s.read()

    def get_cookie(self):
        return self.c.getinfo(pycurl.INFO_COOKIELIST)

    def get_header(self):
        return self.c.getinfo(pycurl.INFOTYPE_HEADER_IN)

    def get_resource_code(self):
        return self.c.getinfo(pycurl.RESPONSE_CODE)
