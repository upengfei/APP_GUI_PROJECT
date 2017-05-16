# coding:utf-8

import subprocess
import platform
import os
PATH = lambda p: os.path.abspath(p)


# 判断系统类型，windows使用findstr，linux使用grep
system = platform.system()
if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"

# 判断是否设置环境变量ANDROID_HOME
if "ANDROID_HOME" in os.environ:
    if system == "Windows":
        command = os.path.join(
            os.environ["ANDROID_HOME"],
            "platform-tools",
            "adb.exe")
    else:
        command = os.path.join(
            os.environ["ANDROID_HOME"],
            "platform-tools",
            "adb")
else:
    raise EnvironmentError(
        "Adb not found in $ANDROID_HOME path: %s." %
os.environ["ANDROID_HOME"])


class ADBtools(object):

    def __init__(self,device_id=""):
        if device_id:
            self.device_id = "-s %s" % device_id
        else:
            self.device_id=""

    def adb(self, args):
        cmd = "%s %s %s" % (command, self.device_id, str(args))
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def shell(self, args):
        cmd = "%s %s shell %s" % (command, self.device_id, str(args),)
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def get_device_id(self):
        """
        获取设备udid号，return serialNo
        """

        return self.adb("get-serialno").stdout.read().strip()

    def get_android_version(self):
        """
        获取设备中的Android版本号，如4.2.2
        """
        return self.shell(
            "getprop ro.build.version.release").stdout.read().strip()

    def get_device_model(self):
        """
        获取设备型号
        """
        return self.shell("getprop ro.product.model").stdout.read().strip()

    def get_focused_package_and_activity(self):
        """
        获取当前应用界面的包名和Activity，返回的字符串格式为：packageName/activityName
        """
        out = self.shell(
            "dumpsys activity activities | %s mFocusedActivity" %
            find_util).stdout.read().strip().split(' ')[3]
        return out

    def get_current_package_name(self):
        """
        获取当前运行的应用的包名
        """
        return self.get_focused_package_and_activity().split("/")[0]

    def get_current_activity(self):
        """
        获取当前运行应用的activity
        """
        return self.get_focused_package_and_activity().split("/")[-1]

    def get_battery_temp(self):
        """
        获取电池温度
        """
        temp = self.shell("dumpsys battery | %s temperature" %
                            find_util).stdout.read().split(": ")[-1]
        return int(temp) / 10.0

    def get_battery_level(self):
        """
        获取电池电量
        """
        level = self.shell("dumpsys battery | %s level" %
                            find_util).stdout.read().split(": ")[-1]

        return int(level)

    def get_battery_status(self):
        """
        获取电池充电状态
        BATTERY_STATUS_UNKNOWN：未知状态
        BATTERY_STATUS_CHARGING: 充电状态
        BATTERY_STATUS_DISCHARGING: 放电状态
        BATTERY_STATUS_NOT_CHARGING：未充电
        BATTERY_STATUS_FULL: 充电已满
        """
        status_dict = {1: "BATTERY_STATUS_UNKNOWN",
                        2: "BATTERY_STATUS_CHARGING",
                        3: "BATTERY_STATUS_DISCHARGING",
                        4: "BATTERY_STATUS_NOT_CHARGING",
                        5: "BATTERY_STATUS_FULL"}
        status = self.shell("dumpsys battery | %s status" %
                            find_util).stdout.read().split(": ")[-1]
        return status_dict[int(status)]

    def get_matching_app_list(self, keyword):
        """
        模糊查询与keyword匹配的应用包名列表
        usage: getMatchingAppList("qq")
        """
        matApp = []
        for packages in self.shell(
                        "pm list packages %s" %
                        keyword).stdout.readlines():
             matApp.append(packages.split(":")[-1].splitlines()[0])
        return matApp

    def is_install(self, packageName):
        """
        判断应用是否安装，已安装返回True，否则返回False
        usage: isInstall("com.example.apidemo")
        """
        if self.get_matching_app_list(packageName):
            return True
        else:
            return False

    def remove_app(self, packageName):
        """
        卸载应用
        args:
        - packageName -:应用包名，非apk名
        """
        return self.adb("uninstall %s" % packageName)

if __name__ == '__main__':
    adb = ADBtools(ADBtools().get_device_id())
    print adb.get_device_id()