import os
import time


# 适配小米6
# 屏幕分辨率1920x1080
def auto_breaking():
    while (True):
        os.system('adb shell input tap 1 1')
        os.system('adb shell input tap 1 1')
        # 点击'进入战斗'
        os.system('adb shell input tap 1650 800')
        time.sleep(0.5)
        # 点击'开始战斗'
        os.system('adb shell input tap 1550 400')
        time.sleep(2)


if __name__ == '__main__':
    auto_breaking()
