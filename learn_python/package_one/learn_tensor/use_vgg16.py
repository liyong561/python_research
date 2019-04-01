from tensorflow.keras.applications import vgg16 as vgg16
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plot


# vgg16对于图片有着固定的输入格式，即训练网络对于数据的维度很重要。224*224


def pre_process(image_path):
    # 有了框架写的预处理函数，就不需要我写了
    img = image.load_img(image_path, target_size=(224, 224))
    x1 = image.img_to_array(img)
    # 在张量中添加一个维度，这个在开始不好理解，但是是张量的基本操作,再比如，维度交换。
    x = np.expand_dims(x1, axis=0)

    # 不应该是[-1,1]吗,看源码，注意一下mode
    x = vgg16.preprocess_input(x, mode='tf')
    # print(x)
    fig = plot.figure(2)
    # understand the meaning of 121
    plot.subplot(121)
    plot.imshow(x1)
    plot.title('rgb，img1')
    plot.subplot(122)
    plot.imshow(x[0, :, :, :, ])
    plot.show()


pre_process('/Users/yongli/Pictures/flower.jpeg')
