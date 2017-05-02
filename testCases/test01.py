import os

from func import BasicFunc

# r = os.popen("adb shell getprop ro.product.model")
# print r.readlines()[1].index("device")
r = os.popen("adb shell dumpsys battery")
print r.read()
# print BasicFunc.get_android_phone_udid()
#
# print BasicFunc.get_android_Phone_model()