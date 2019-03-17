from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from matplotlib import pyplot as plt

'''
 python有成千上万的包和类，不可能系统的学习，只能边学边用，在用到时记下。
 还有Python的类和方法一般参数众多，但是大部分都可以使用默认值，少部分需要定制
'''

font = ImageFont.truetype('/Library/Fonts/Times New Roman.ttf', 54)  # 印象了可移植性
# 学习数组时怎么转换成坐标的
x = [100, 100, 200, 300, 200, 500, 400, 600]
labels=['cat 0.92','cat 0.78']
x1 = [100, 100]
x2 = [200, 500]
y = [200, 500, 200, 500]

def draw_line(pic_path):
    im = Image.open(pic_path)

    draw = ImageDraw.Draw(im)  # 先得到一个画布，然后在上面绘画。
    draw.rectangle(x, outline=(233, 122, 11), width=10)  # fill去填充图里面的

    draw.text(x1, text='cat 0.92')
    draw.text(x2, text="dog 0.86", font=font)
    plt.imshow(im)  # 只是绘制图像
    plt.show();


def visualize_result(pic, boxes, labels):
    '''
    优化版的结果展示函数，为简化程序设计，很多参数直接内定。作为一个学术demo，重点是算法，其他部分越简单越好。
    :param pic:图片地址
    :param boxes: 矩形的一个对角线点的坐标，拼接成一个4*x的列表
    :param labels: x个类别和概率
    :return:
    '''
    im = Image.open(pic)
    font = ImageFont.truetype('/Library/Fonts/Times New Roman.ttf', 30)
    draw = ImageDraw.Draw(im)

    for i in range(len(labels)): # 这也是同步访问几个列表的设计模式
        draw.rectangle(boxes[i * 4:(i + 1) * 4], outline=(100, 100, 100), width=5)
        draw.text(boxes[i * 4:i * 4 + 2], text=labels[i], font=font)

    plt.imshow(im)
    im.save(pic.split('.')[0]+'-label.'+pic.split('.')[1]) #
    plt.show();


# draw_line("/Users/yongli/Pictures/flower02.jpeg")
visualize_result('/Users/yongli/Pictures/flower02.jpeg',x,labels)
