from func import Func
from xml.sax import saxutils
import os
p = 'D:\CloudMusic'
def delete_file(path):
    if os.listdir(path):
        for item in os.listdir(path):
            file_path = os.path.join(path,item)
            if file_path:
              os.remove(file_path)

delete_file(p)