import os
import sys
import subprocess
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import time

screenshot_way = 2


# 获取截图
def pull_screenshot():
    '''
    新的方法请根据效率及适用性由高到低排序
    '''
    global screenshot_way
    if screenshot_way == 2 or screenshot_way == 1:
        process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        screenshot = process.stdout.read()
        if screenshot_way == 2:
            binary_screenshot = screenshot.replace(b'\r\n', b'\n')
        else:
            binary_screenshot = screenshot.replace(b'\r\r\n', b'\n')
        f = open('auto.png', 'wb')
        f.write(binary_screenshot)
        f.close()
    elif screenshot_way == 0:
        os.system('adb shell screencap -p /sdcard/auto.png')
        os.system('adb pull /sdcard/auto.png .')


def check_screenshot():
    '''
    检查获取截图的方式
    '''
    global screenshot_way
    if os.path.isfile('auto.png'):
        os.remove('auto.png')
    if (screenshot_way < 0):
        print('暂不支持当前设备')
        sys.exit()
    pull_screenshot()
    try:
        Image.open('./auto.png').load()
        print('采用方式 {} 获取截图'.format(screenshot_way))
    except Exception:
        screenshot_way -= 1
        check_screenshot()


fig = plt.figure()
cor = [0, 0]
# 小米6，1920x1080分辨率截取坐标
# 战利品位置，非洲人暂时取4个掉落
items = [(223, 464, 345, 584),
         (387, 464, 509, 584),
         (551, 464, 673, 584),
         (715, 464, 837, 584),
         (306, 612, 430, 732),
         (470, 612, 594, 732)
         ]
# 战利品框
item_field = (200, 600, 350, 700)


# 按目标区域截取图片
def crop_photo(item):
    # 读取图片并模糊化,减少计算量
    img = Image.open('auto.png')
    img2 = img.filter(ImageFilter.BLUR).crop(item).resize((64, 64))
    img2.save('1.png')
    # plt.imshow(img2)
    # plt.show()


# 确认战利品是否包含魔卡
def check_item(index=1):
    count = 0
    img = Image.open('1.png')
    size = img.size[0] * img.size[1]
    list = img.getcolors(size)
    # 通过判断灰色值范围
    for i in list:
        r, g, b, d = i[1]
        # 排除掉落数不满4个，截取到白色框的情况
        if r == g == b:
            count += i[0]
        if r > 120 and r < 140 and g > 120 and g < 140 and b > 130 and b < 155:
            count += i[0]
    if count * 100 // size == 100:
        return False
    elif count * 100 // size > 20:
        print('材料掉落..')
        return False
    elif index == 0:
        print('截取到特效小星星,重新判断!')
        return 'BUG'
    else:
        print("魔卡掉落！！")
        return True


# 确认战斗状态
def check_status():
    check_screenshot()
    crop_photo(item_field)
    count = 0
    img = Image.open('1.png')
    size = img.size[0] * img.size[1]
    list = img.getcolors(size)
    for i in list:
        # 坑爹了，windows下的getcoloser返回值是(1,(1,1,1,1))
        r, g, b, d = i[1]
        if r == b == g:
            count += i[0]
    # count记录所有符合条件的像素点，白色比例大如50%判定为战斗结算框
    if count * 100 // size > 50:
        print("当前位于战斗结算页面...")
        return True
    else:
        print("当前位于战斗页面...")
        return False


# 遍历战利品
def check_a_lot_of_items():
    pull_screenshot()
    for item in items:
        crop_photo(item)
        result = check_item(items.index(item))
        # 如果截图bug，递归重新获取截图判定
        if result == 'BUG':
            time.sleep(1)
            return check_a_lot_of_items()
        if result:
            return True
    return False


# 模拟触摸
# adb shell input tap x y //x,y是你想点的屏幕的坐标点
# 模拟点击开始
def start():
    os.system('adb shell input tap 1 1')
    os.system('adb shell input tap 1 1')
    # 点击'进入战斗'
    os.system('adb shell input tap 1650 800')
    print("'进入战斗'")
    time.sleep(0.5)
    # 点击'开始战斗'
    os.system('adb shell input tap 1550 400')
    print("'开始战斗'")
    time.sleep(5)


# 自动重复刷本直到魔卡掉落
def auto_card():
    count = 1
    print('正在肝第%d次' % count)
    start()
    while (True):
        if check_status():
            if check_a_lot_of_items():
                break
            else:
                os.system('adb shell input tap 1550 400')
                count += 1
                start()
                print('正在肝第%d次' % count)
        else:
            time.sleep(5)


if __name__ == '__main__':
    auto_card()
