import wda
import time

c = wda.Client()
s = c.session()


def auto_breaking():
    print('开始...')
    print('按"control+C"手动结束...')
    while (True):
        s.double_tap(1, 1)
        # 点击'进入战斗'
        s.tap(330, 1910)
        time.sleep(0.5)
        # 点击'开始战斗'
        s.tap(765, 1800)
        time.sleep(2)


if __name__ == '__main__':
    auto_breaking()
