# -*- coding:utf-8 -*-
import requests,urllib
from func import QydBasicFunc,Base64

bs = Base64.BaseChange(r'/config/qyd_func.ini')
qyd = QydBasicFunc.QydBackGround()
print qyd.getBackToken()
# r = qyd.get("https://admin.stg-qyd.com/image/validator")
# # # s= requests.session()
# # r= s.get("https://admin.stg-qyd.com/image/validator", verify=False)
#
#
# # print r.text
# param = {
#             "name": "36446337TAIaud2" ,
#             "password":"1025"
#         }
#
# header={
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Authorization":"%s" % (bs.user_encode_back(),),
#     "Cookie":"JSESSIONID=%s" % (r.cookies['JSESSIONID'],)
# }
# url = "https://admin.stg-qyd.com/syslogin?"+urllib.urlencode(param)
# t = qyd.post(url,headers=header)
#
# print t.headers["X-Auth-Token"]