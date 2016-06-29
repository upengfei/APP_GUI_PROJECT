# -*- coding:utf-8 -*-
import requests
import bs4,os,sys
import time
import socket

# r= requests.get("http://www.qingyidai.com")
#
# t = bs4.BeautifulSoup(r.content,'lxml')
# print t.p.a.text
# project_dir = os.path.dirname(os.path.abspath(__file__))
# print project_dir
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)# 创建 socket 对象
HOST = socket.gethostbyname("c190158") # 获取本地主机名
print HOST
PORT = 56129
s.bind((HOST, PORT))# 绑定端口
s.listen(2)  # 等待客户端连接
