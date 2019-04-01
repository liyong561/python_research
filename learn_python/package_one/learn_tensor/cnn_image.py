import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plot
import numpy as np


def tt_ft(file):
    im = Image.open(file)  # not open(file)
    im_arr = np.asarray(im, dtype='float32')  # 233.0这样的浮点数
    im_arr = im_arr / 256
    print(im_arr.shape)
    # print(im_arr[:,2,2])
    plot.figure()
    plot.subplot(221)
    plot.imshow(im_arr)  # float,integer is ok

    with tf.Session() as sess:
        filter_input = np.random.rand(4, 4, 3, 10)
        b = np.random.randint(2, 19, size=(10))
        # print(im_arr[1,:,1]) 0.4数值比较均匀。
        print(filter_input[2, :, :, 2])

        # im_arr要广播一下? ,且要求float16, bfloat16, float32, float64
        h, w, c = im_arr.shape
        im_arr = im_arr.reshape(1, h, w, c)

        ops_cnn = tf.nn.conv2d(im_arr, filter_input, strides=[1, 3, 3, 1], padding='SAME', name='im_cnn')

        ops_cnn1 = tf.nn.bias_add(ops_cnn, bias=b)

        ops_cnn2 = tf.nn.sigmoid(ops_cnn1, name='ss')

        im_cnn = sess.run(ops_cnn2)  # 卷积运算后，im_cnn超过了image的显示范围。fliter的值不应该是整数。不应该使用randint

        plot.subplot(222)
        print(im_cnn[0, 1, :, 2])  # 都到达了10.1
        im_normal = normal_normal1(im_cnn[0, :, :, 0:3])
        plot.imshow(im_normal)

    plot.show()  # 最后统一展示


def x_mean():
    x = np.array([[12, 15, 54], [14, 323, 23], [232, 23, 234]])
    # numpy.ndarray object

    x_image = np.array(Image.open('/Users/yongli/Pictures/flower.jpeg'))
    print(x_image.shape)
    # rgb格式数据的均值
    x_image_mean = x_image.mean(axis=1)
    x_image_sum = x_image.sum(axis=1)
    print(x_image_mean.shape, x_image_mean)
    print(x_image_sum)
    print(x.mean())


def deprocess_image(x):
    x -= x.mean()
    x /= (x.std() + 1.24 * 1e-5)


def line_normal(x):
    # 线性归一化
    max_value = x.max()
    min_value = x.min()
    x = (x - min_value) / (max_value - min_value)
    return x


def normal_normal(x):
    x -= x.mean()
    # 映射到正态分布上。
    x /= (x.std() + 1e-5)
    x *= 0.1

    x += 0.5
    x = np.clip(x, 0, 1)
    x *= 255
    x = np.clip(x, 0, 255).astype('int8')
    return x


def normal_normal1(x):
    x -= x.mean()
    # 映射到正态分布上。
    x /= (x.std() + 1e-5)
    x *= 0.1

    x += 0.5
    x = np.clip(x, 0, 1)
    # not in 255,but the result is different
    return x


tt_ft('/Users/yongli/Pictures/flower.jpeg')
