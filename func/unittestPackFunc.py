# coding:utf-8


"""
用于加载并运行某文件夹下的测试用例，以及生成相应测试报告
"""
import sys,os

from unittest import TestLoader,TestSuite
from func import HTMLTestRunner
from func import Func
reload(sys)
sys.setdefaultencoding('utf-8')



def test_case_dicovery(dir, pattern='*.py',top_lever_file=None):
    """加载某文件下所有.py下的测试用例，并返回suite(一个套件)"""
    if dir is None:suite = TestLoader().discover('.')
    suite = TestLoader().discover(dir,pattern=pattern,top_level_dir=top_lever_file)
    return suite


def run_case(suite,report__file_name=None,title='APP GUI TEST REPORT',description=None):
    """生成测试报告"""
    if report__file_name is None:report__file_name='test_report_sample'
    filename = Func.create_report(report__file_name)
    # fp = open(filename, 'wb')
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=description)
        runner.run(suite)



def get_suite(cls,args):
    """
    按顺序加载测试用例，并返回一个suite
    agument:
        args 需要list类型，如:['test_01','test_02']
    """
    if isinstance(args,list):
        suite = TestSuite(map(cls,args))
        return suite
    else:
        sys.stderr("args参数需为list类型")

if __name__ == '__main__':
    run_case(test_case_dicovery('./YKJ_APP_GUI',pattern='YKJ_func_sample.py'),u'注册流程测试报告')

