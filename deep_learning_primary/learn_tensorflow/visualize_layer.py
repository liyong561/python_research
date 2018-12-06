from keras.models import load_model
from keras import models
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt


def test01():
    model = load_model('cat_and_dog_small.h5')
    layers = [layer for layer in model.layers]  # for语句组成list,对各个layer详细分析
    length = len(layers)
    print(length)
    print(layers[0].output)  # 返回的是一个Tensor对象。
    model.summary()  # summary中就显示了多少层


def ac_model():
    model = load_model('cat_and_dog_small.h5')
    layer_outputs = [layer.output for layer in model.layers[:8]]  # 每层显示都是输出
    activation_model = models.Model(inputs=model.input, outputs=layer_outputs)
    return activation_model


def image_tensor(img_path=r'E:\Data\cat-and-dog\training_set\cats\cat.1.jpg'):
    # 函数名和变量名重复了
    img_path = img_path
    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    return img_tensor


def display_conv(layer_output_index):
    activation_model = ac_model()  # 返回训练好的多输出模型
    img_tensor = image_tensor()
    activations = activation_model.predict(img_tensor)  # 这是一个多输出模型
    # python中又一种object叫function objectfd
    first_layer_ac = activations[layer_output_index]  # 不能这样调用[0].[0]
    N, H, W, C = first_layer_ac.shape
    first_layer_ac = first_layer_ac[0]
    # plt.imshow(first_layer_ac[0, :, :, 7: 10])  #指定第一维为0的意义。
    #  将各个通道展平到一张图中,将一个立体怎么展成一个平面
    rows = 10  # 每行展示10个通道，未能填满的一行以0代替,这时不判断可能越界
    #  cols = C // 10 + 1
    cols = C // rows  # 简单点就不全部展示
    display_grid = np.zeros((cols * H, rows * H))
    # 使用二重循环填满这个矩阵
    for i in range(cols):
        for j in range(rows):
            if i * rows + j >= C - 1:
                break
            display_grid[i * H:(i + 1) * H, j * H:(j + 1) * H] = first_layer_ac[:, :, i * rows + j]
    return display_grid


def test04():
    plt.figure()  # 画总图不熟悉，就这样吧
    for i in range(8):
        ax = plt.axes([0.1, 1*0.125, 0.8, 0.1])
        # plt.subplot(8, 1, i+1)  #  子图的索引从1开始，想要写好程序，得熟悉每个细节
        # ax.title(str(i)+ 'output')
        ax.imshow(display_conv(i))   # 真实显示图像太小,只能使用figure，即画布   plt.show()
    plt.show()

test04()
