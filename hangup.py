import wda
import time

c = wda.Client()
s = c.session()

if __name__ == '__main__':
    # s.tap(480, 1100)
    # time.sleep(5)
    # go()
    # time.sleep(5)
    # 点击冒险
    print(1)
    s.tap(80, 600)
    time.sleep(1)
    # 点击历练副本
    print(2)
    s.tap(300, 600)
    time.sleep(1)
    # 点击修行之地
    print(3)
    s.tap(950, 600)
    time.sleep(1)  # 点击'进入战斗'
    s.tap(330, 1910)
    time.sleep(1)
    # 点击'开始战斗'
    s.tap(765, 1800)


