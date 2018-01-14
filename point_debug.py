from matplotlib import pyplot as plt
from PIL import Image


# 调试用
# 用来打开一张图片，get具体像素点坐标
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
    get_point()
