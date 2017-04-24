# coding:utf-8
import threading
import random
import json
from time import sleep
from func import *
from datetime import datetime as dt
from datetime import time as t
from datetime import timedelta
from func.logInfo import logger

# reload(sys)
# sys.setdefaultencoding("utf-8")

class BorrowMoney:
    def __init__(self):
        self.mdb = MysqlDB.MysqlDB(r'/config/config.ini')
        self.qf = QydBasicFunc.QydForeground()
        self.qb = QydBasicFunc.QydBackGround()
        self.loan_id=""
        self.btoken=""
        self.creditsponsorid="f1f3bcfe-a974-490a-9e37-f8b5de637c1f"
    def frontProcess(self):

        # sql = "select a.id from creditsponsorcompany a LEFT JOIN user u on a.userid = u.id where u.tel_num='16811220030';"
        # self.mdb.execute(sql)
        # self.creditsponsorid = self.mdb.fetchone()[0]


        token = self.qf.get_token()

        data={
            "creditsponsorid":"%s" % self.creditsponsorid,
            "amount":"1000",
            "debitTerm":"180",
            "debttype":"CAR_BORROW",
            "templateid":"02793e8f-08e9-42af-b0cc-fe2588720940",
            "remark":"test3"

        }
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Content-Type":"application/json; charset=UTF-8",
            "X-Auth-Token":"%s" % token,
            "userid":"3b45ce7b-55cf-4225-8bde-334823ec31b0",
            "version":"67958724"

        }
        r=self.qf.post("http://www.localqyd.com/loan/_",data=json.dumps(data),headers=header,verify=False)
        self.loan_id = r.json()['id']
        logger.info("loan_id ::::{}".format(self.loan_id))
        sleep(1)



    def loanFirstAudity(self):
        self.btoken = self.qb.getBackToken()
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "X-Auth-Token":"%s" % self.btoken,
            "Content-Type":"application/json; charset=UTF-8"
        }

        self.qf.get("http://admin.localqyd.com/loan/_/"+self.loan_id,headers=header,verify=False)

        data ={
            "tenderName":"购车贷",
            "amount":"1000.00",
            "interestRate":"8.50",
            "loanType":"PRINCIPAL_INTEREST",
            "debitTerm":"6",
            "loanAbstract":"购车贷",
            "remark":"1",
            "tenderNo":"%s"% self.loan_id,
            "debitType":"1",
            "copiesamount":"1000.00",
            "debttype":"CAR_BORROW",
            "status":"PASS_ONE",
            "auditType":"CAR_BORROW",
            "fileNumber":"北京测f试XPD%s"% random.randint(1,100000),
            "reply":"TEST",
            "isshow":"T"
        }

        self.qb.put("http://admin.localqyd.com/loan/manager/"+self.loan_id+"?auditType=LOANREPAIR",data=json.dumps(data)
                    ,headers = header,verify=False)
        sleep(0.5)
    def loanReview(self):
        repaydate = dt.now()+timedelta(days=180)
        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "X-Auth-Token":"%s" % self.btoken,
            "Content-Type":"application/json; charset=UTF-8"
        }

        self.qf.get("http://admin.localqyd.com/loan/_/"+self.loan_id,headers=header,verify=False)

        data ={
            "id":"%s"% self.loan_id,
            "createTime":"%s"% dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updateTime":"%s"% dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sponsorname":"汇通担保",
            "amount":"1000.00",
            "currentAmount":"0.00",
            "availableAmount":"1000.00",
            "status":"WAITING",
            "auditType":"CAR_BORROW",
            "interestRate":"8.50",
            "openTime":"%s"% dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "borrow":"",
            "sponsorCompanyId":"1",
            "loanType":"PRINCIPAL_INTEREST",
            "orderNo":"%s" % self.loan_id,
            "tenderNo":"%s"% self.loan_id,
            "tenderName":"购车贷",
            "debitTerm":"6",
            "debitType":"1",
            "repayDate":"%s" % repaydate.strftime('%Y-%m-%d %H:%M:%S'),
            "auditOneTime":"%s"% dt.now().strftime("%Y-%m-%d %H:%M:%S"),
            "payCompany":"KYPAY",
            "loanAbstract":"购车贷",
            "remark":"1",
            "acceptIncomplete":"1",
            "copiesamount":"1000.00",
            "closedperiod":"2",
            "templateid":"02793e8f-08e9-42af-b0cc-fe2588720940",
            "isshow":"T",
            "debttype":"CAR_BORROW",
            "debttypename":"购车贷",
            "creditsponsorid":"%s" % self.creditsponsorid,
            "repayType":"0",
            "sponsorRate":"0.03",
            "creditGuaranteeRate":"0",
            "enumStatus":"PASS_ONE",
            "reply":"test",
            "assignor":"2",
            "lender":"2"
        }

        r=self.qb.put("http://admin.localqyd.com/loan/manager/"+self.loan_id+"?auditType=LOANREPAIR",data=json.dumps(data)
                    ,headers = header,verify=False)
        sleep(0.5)
def main():
    bm=BorrowMoney()
    bm.frontProcess()
    bm.loanFirstAudity()
    bm.loanReview()
    sleep(1)
def run():
    lock = threading.Lock()
    threadpool=[]
    lock.acquire()
    try:
        for i in range(1000):

            tr = threading.Thread(target=main,name="borrowMoney")
            tr.setDaemon(True)

            threadpool.append(tr)
        for tr in threadpool:
            tr.start()
        for tr in threadpool:
            threading.Thread.join(tr)
    finally:
        lock.release()
if __name__=='__main__':

    for i in range(1000):
       main()


