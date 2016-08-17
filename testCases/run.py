
import subprocess

testcases=[
    # 'WBverificode.py',
    'WBqueryauthorizeinfo.py',
    'WBremoveauthorize.py',
    # "WBwithhold.py",
    "WBquerywithholdinfo.py"
]
#
def run(x):
    child = subprocess.Popen(["python.exe",x])
    child.wait()
    # return


if __name__=='__main__':
    map(run,testcases)
