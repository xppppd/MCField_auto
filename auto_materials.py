import wda
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import time
import pytesseract

# 计算战斗结算区域中的固定方框位置中的灰色面积
# 获取图片像素值的二维数组
# 战利品第一格坐标如下：
'''
(572,265)------(705,265)
    |               |
    |               |
    |               |
(572,395)------(705,395)
'''


# 计算目标区域里的灰色像素占比，小于1/5即出魔卡
# 灰色像素RGB范围如下：
# R：120～140
# G：120～140
# B：130～160

# 战斗页面判断：截取战利品栏，判断是否存在白框
# 白色RGB值：R==G==B


def pull_screenshot():
    c.screenshot('auto.png')


fig = plt.figure()

# 战利品位置，非洲人暂时取4个掉落
# 多取几个位置...
items = [(572, 265, 705, 395),
         (572, 455, 705, 585),
         (572, 645, 705, 775),
         (572, 835, 705, 965),
         (400, 365, 533, 495),
         (400, 555, 533, 685),
         ]
# 战利品框
item_field = (400, 220, 550, 370)

# 体力框
power_field = (1140, 1725, 1200, 1790)
# 获取截图
c = wda.Client()
s = c.session()


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
        r, g, b = i[1]
        # 排除掉落数不满4个，截取到白色框的情况,直接退出循环
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
        print('截取到特效小星星')
        return 'BUG'
    else:
        print("魔卡掉落！！")
        return True


# 确认战斗状态
def check_status():
    pull_screenshot()
    crop_photo(item_field)
    count = 0
    img = Image.open('1.png')
    size = img.size[0] * img.size[1]
    list = img.getcolors(size)
    # print(len(list))
    for i in list:
        r, g, b = i[1]
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


# 体力值检查，文字太小，识别准确率不够，暂不用
def power_check():
    img = Image.open('auto.png')
    img2 = img.crop(power_field).rotate(90)
    img2.save('1.png')
    text = pytesseract.image_to_string(img2, lang='chi_sim')
    if (int(text) < 8):
        return False
    else:
        return True


# 模拟点击开始
def start():
    s.double_tap(1, 1)
    # 点击'进入战斗'
    s.tap(330, 1910)
    print("'进入战斗'")
    time.sleep(0.5)
    # 点击'开始战斗'
    s.tap(765, 1800)
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
                s.tap(765, 1800)
                count += 1
                start()
                print('正在肝第%d次' % count)
        else:
            time.sleep(5)


if __name__ == '__main__':
    auto_card()
