import numpy as np
from PIL import Image
import matplotlib.pyplot as plot


def array_flatten():
    '''
    ndarry中又很多的列表
    ndarry中和tensor中一个明显的区别就是ndarry中，对应元素的长度不必相等,比如x2
    这时候flatten的情况也就不相同了，即展平到list就不在展了
    '''
    x = np.array([
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ])

    x1 = np.array([
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7,8, 9],
            [10, 11, 12]
        ]
    ])
    x2 = np.array([
        [
            [1, 2, 3],
            [4, 5, 6],
            [33,34,35]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ])

    x_flatten = x2.flatten()
    print(x_flatten)


def image_flatten():
    '''
    在图片操作中，flatten和reshape互为逆操作
    :return:
    '''
    im = Image.open('/Users/yongli/Pictures/flower.jpeg')
    im_arr = np.array(im)
    h,w,c = im_arr.shape
    im_arr = np.expand_dims(im_arr, axis=0)
    print(im_arr.shape)
    im_arr_flatten = im_arr.flatten()
    print(im_arr_flatten.shape)

    im_rec = im_arr_flatten.reshape((h,w,c))
    print(im_rec.shape)

    plot.imshow(Image.fromarray(im_rec))
    plot.show()


image_flatten()
