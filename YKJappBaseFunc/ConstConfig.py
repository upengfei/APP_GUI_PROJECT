# coding:utf-8

"""移动端参数设置"""
from enum import Enum

class AppBase(Enum):
    platformName = 'Android',  # 当前用例运行的平台（Ios，Android，Desktop）
    browserName = "Chrome",  # 当前测试的浏览器名称{ iOS: Safari } { Android: Chrome } { Desktop: Chrome / Electron }
    deviceName = "",  # 模拟器的名称，例如 ‘iPhone 6’ 或者 ‘Nexus 5x’。
    app = "C:\\Users\Administrator\\Desktop\\esnformal.apk",  # .ipa，.app 或者 .apk 文件的绝对地址或者远程地址，或者是包含上述文件格式的 Zip 文件。
    udid = "",  # 测试设备的唯一设备 ID
    reuse = 3,  # number类型： 0: 启动并安装 app。1 (默认): 卸载并重装 app。 2: 仅重装 app。3: 在测试结束后保持 app 状态。
    package = "Chrome",  # Android app 的 package name
    activity = "",  # 启动时的 Activity name
    androidProcess = "",  # 使用 chromedriver 测试 webview 时需要的自定义的进程名.
    bundleId = "",  # 应用的 Bundle ID，例如 com.apple.Maps。
    autoAcceptAlerts = False,  # 自动接受所有的系统弹窗信息。默认是 false。
    autoDismissAlerts = False,  # 自动拒绝所有的系统弹窗信息。默认是 false

