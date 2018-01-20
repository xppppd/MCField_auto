from matplotlib import pyplot as plt
from PIL import Image
from auto_materials_android import check_screenshot
from auto_materials import pull_screenshot


# 调试用，截图并打开
# 方便get具体像素点坐标

def get_point():
    fig = plt.figure()
    img = Image.open('auto.png')
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def onclick(event):
    ix, iy = event.xdata, event.ydata
    print("--------------")
    print("x坐标：%d,y坐标:%d" % (ix, iy))


if __name__ == "__main__":
    # ios用pull_screenshot()
    # pull_screenshot()
    # andriod用check_screenshot()
    check_screenshot()
    get_point()
