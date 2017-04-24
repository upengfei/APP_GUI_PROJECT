import requests
import threading as mul
import sys,time,json
from func import *

reload(sys)
sys.setdefaultencoding('utf-8')

def buyPlans():
    qyd = QydBasicFunc.QydForeground()
    url = "https://www.localqyd.com/entrance/payment/buyCY/json"
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "X-Auth-Token": "{}".format(qyd.get_token())
    }
    params = {
        "money": "100"
    }
    r = qyd.post(url,data=json.dumps(params),headers=header,verify=False)
    print "The Interface response message : %s" % r.content
    assert r.status_code == 200


def mulThread(num):
    threads=[]

    for i in range(num):
        p = mul.Thread(target=buyPlans)
        threads.append(p)
    for t in threads:
        t.start()
        time.sleep(2)
    for t in threads:
        t.join()

if __name__=='__main__':
    mulThread(12)