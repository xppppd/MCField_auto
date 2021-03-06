import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import pytesseract
import

# 调试个函数用

fig = plt.figure()

# 战利品位置，非洲人暂时取6个掉落
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
power_field = (1100, 1725, 1230, 1882)


# 获取截图
# c = wda.Client()
# s = c.session()


# 按目标区域截取图片
def crop_photo(item):
    # 读取图片并模糊化,减少计算量
    img = Image.open('testfile/auto.jpg')
    img2 = img.crop(item).resize((64, 64))
    img2.save('1.png')
    # plt.imshow(img2)
    # plt.show()


# 确认战利品是否包含魔卡
def check_item():
    count = 0
    img = Image.open('1.png')
    size = img.size[0] * img.size[1]
    list = img.getcolors(size)
    # 通过判断灰色值范围
    for i in list:
        r, g, b = i[1]
        # 排除掉落数不满4个，截取到白色框的情况
        if r == g == b:
            count += i[0]
        if r > 120 and r < 140 and g > 120 and g < 140 and b > 130 and b < 155:
            count += i[0]
    if count * 100 // size > 20:
        print('没有掉落！！')
        return False
    else:
        print("魔卡掉落！！")
        return True


# 确认战斗状态
def check_status():
    crop_photo(item_field)
    count = 0
    img = Image.open('1.png')
    size = img.size[0] * img.size[1]
    list = img.getcolors(size)
    # print(len(list))
    for i in list:
        print(i)
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
    for item in items:
        crop_photo(item)
        if check_item():
            return True
    return False


#   体力检测，图像文字识别精确度有问题；
def power_check():
    img = Image.open('auto.png')
    img2 = img.crop(power_field).rotate(90)
    img2.save('1.png')
    text = pytesseract.image_to_string(img2, lang='chi_sim')
    print(text)
    # if (int(text) < 8):
    #     return False
    # else:
    #     return True


# 模拟点击开始2，夹带了体力逻辑
# def start2():
#     s.double_tap(1, 1)
#     if not power_check():
#         # 点击加体力按钮
#         s.tap(1175, 1950)
#         time.sleep(0.5)
#         # 点击使用中体力
#         s.tap(570, 1500)
#         time.sleep(0.5)
#         # 取消掉体力框
#         s.tap(1, 1)
#         time.sleep(0.3)
#     # 点击'进入战斗'
#     s.tap(330, 1910)
#     print("'进入战斗'")
#     time.sleep(0.5)
#     # 点击'开始战斗'
#     s.tap(765, 1800)
#     print("'开始战斗'")
#     time.sleep(5)


if __name__ == '__main__':
    # auto_card()
    # check_status()
    # crop_photo(power_field)
    # power_check()
    # check_a_lot_of_items()
    crop_photo((400, 555, 533, 685))
