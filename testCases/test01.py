import os

from func import BasicFunc

r = os.popen("adb devices -l")
# print r.readlines()[1].index("device")

print BasicFunc.get_android_phone_udid()

print BasicFunc.get_android_Phone_model()