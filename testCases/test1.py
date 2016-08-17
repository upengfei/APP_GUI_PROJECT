# -*- coding:utf-8 -*-
import multiprocessing as mul
import sys,time,json
from func import QydBasicFunc,MysqlDB
import hashlib,re
import uuid
reload(sys)
sys.setdefaultencoding('utf-8')


def buyPlans():
    orderNo1=uuid.uuid1()
    print orderNo1
    a=['%s'% orderNo1,'ceshi12','DFBXT','4861697244785127170','13002635546','垫富宝投资有限公司','130530000007116',
       '4861697244785127170','13002635546','垫富宝投资有限公司','130530000007116','0','72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727']


    md5 = hashlib.md5()
    md5.update(''.join(a))



    print '!!!!!!!!!',md5.hexdigest()
    qyd = QydBasicFunc.QydForeground()
    url = "https://www.stg-qyd.com/entrance/account/wbauthorizeplaceorder/json"
    # header = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    #         # "X-Auth-Token": "{}".format(qyd.get_token())
    # }
    params = {
        "sign": "%s" % md5.hexdigest(),
        "payerSSOID":"%s" % a[3],
        "payerPhone":"%s" % a[4],
        "payerName":"%s" % a[5],
        "payerNum":"%s" % a[6],
        "payeeSSOID":"%s" % a[7],
        "payeePhone":"%s" % a[8],
        "payeeName":"%s" % a[9],
        "payeeNum":"%s" % a[10],
        "orderNo":"%s" % a[0],
        "channel":"%s" % a[2],
        "businessType":"%s" % a[1],
        "ifSendCode":"%s" % a[11]
    }
    r = qyd.post(url,data=json.dumps(params),verify=False)
    print "The Interface response message : %s" % r.content

    # sql = "select body from messagepayload where subject= '验证码-TRANSFERTODFB'  order by senddate desc limit 2"
    # md = MysqlDB.MysqlDB(r'/config/withholdAgent.ini')
    # md.execute(sql)
    # md.fetchone()[0]
    # re.findall("")
def get_orderno():
    qyd = QydBasicFunc.QydForeground()
    orderNo,verifiCode,channel =['2ce06a40-637f-11e6-bda2-14dda9800e2a','0000','DFBXT']

    MD5_SIGN_DEFAULT_KEY = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"
    md5 = hashlib.md5()
    md5.update(orderNo+verifiCode+channel+MD5_SIGN_DEFAULT_KEY)
    sign = md5.hexdigest()

    data = {
        "sign":"%s" % sign,
        "orderNo":"%s" % orderNo,
        "verifiCode":"%s" % verifiCode,
        "channel":"%s" % channel
    }
    url = 'https://www.stg-qyd.com/entrance/account/wbauthorizeconfirm/json'
    r = qyd.post(url,data=json.dumps(data),verify=False)
    print r.content
    content = re.findall('.*?"items":\[\{"orderNo":"(.*?)","authorizeCode":".*?"}]',r.content,re.S)
    print content

if __name__=='__main__':
    # buyPlans()
    get_orderno()