# coding:utf-8

import sys,os
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])

from func import test_case_dicovery,get_suite,run_case
from testCases.YKJ_APP_GUI.YKJ_func_sample import Test


def run(pattern=1,cls=None,args=None):
    if pattern==1:
        run_case(test_case_dicovery('./YKJ_APP_GUI', pattern='YKJ_func_sample.py'), u'测试报告')
    elif pattern==2:
        run_case(get_suite(cls,args),u'测试报告')
    else:
        sys.stderr("pattern参数只接受1 or 2,请检查pattern的值！")


if __name__=='__main__':
    # 按顺序执行
    # testcases=['test_login','test_logout']
    # run(2,Test,testcases)

    run(1)