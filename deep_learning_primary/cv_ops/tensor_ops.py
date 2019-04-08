import numpy as np
from PIL import Image


def tt_axis():
    arr = np.array([[23, 32, 32, 35], [12, 13, 15, 17]])
    print(arr.shape)  # (2,3)
    arr_t = arr.T
    print(arr_t.shape)


def tt_img():
    im = Image.open('/Users/yongli/Pictures/flower.jpeg')
    '''
     JpegImageFile object,has no attribute shape
    '''
    arr = np.array(im)  # (600, 500, 3)
    print(arr.shape)
    arr1 = arr[:, :, 1]
    arr2 = arr[:, :, 0]

    im1 = Image.fromarray(arr1)
    im2 = Image.fromarray(arr2)

    # im1.show("flower")

    im2_arr = np.array(im2)
    print('im2_arr:' + str(im2_arr.shape))  # im2_arr变成了两个通道。
    im2.show("flower1")


def tt_des():
    im = Image.open('/Users/yongli/Pictures/shot.jpeg').convert('RGB')  # 对于非rgb格式的图片。
    arr = np.array(im)
    C, H, W = arr.shape
    arr1 = arr.transpose((2, 1, 0))  # 这代表了轴的位置，可以说改变了维度的优先级。
    print(arr1.shape)
    '''
    arr2 = arr1.reshape((1500,600))
    im2 = Image.fromarray(arr2)
    im2.show("three")
    '''
    arr2 = arr1.reshape((H, C * W))  # 会优先将最后的轴填满，所以会反生像素位置的重排，图片失真。
    print(arr2.shape)
    im2 = Image.fromarray(arr2)
    im2.show("three")


'''
在卷积过程中，将img按照计算规则转换为col
快速把这个计算完成
'''


def im2col(im, fh, fw, stride, pad):
    # im的格式为C,H,W，没有考虑到批处理
    C, H, W = im.shape
    out_h = (H + 2 * pad - fh) // stride + 1
    out_w = (W + 2 * pad - fw) // stride + 1

    im_pad = np.zeros((C, H + 2 * pad, W + 2 * pad))
    im_pad[:, pad:H + pad, pad:W + pad] = im;
    # 开始切小方块，两个for循环进行切割。方块的形状为C*fh*fw,

    out = np.zeros((out_h, out_w, C, fh, fw))
    for i in range(out_h):
        for j in range(out_w):
            out[i, j, :, :, :] = im_pad[:, stride * (i - 1):stride * (i - 1) + fh, stride * (j - 1):stride(j - 1) + fw]
    out.reshape((out_h * out_w, -1))  # 后面的shape刚好是我想要的。
    return out


'''
超过2维的dot计算，张量的计算一般都是多维的，而我接触的二维多一些。
比如（3，5，6），（6，4，8） =（3，5，4，8）
（3，4，5），（5，4，9） =（3，9），形状相似的块相乘求和。
实际上是：两个数列的最后维度上。
'''


def multi_dot():
    a1 = np.random.rand(3, 4, 8)  # 测试有用，np.random.randn表示正态分布。
    a2 = np.random.rand(8, 8, 10)

    b1 = np.random.randn(2, 8)
    b2 = np.random.randn(8, 8)

    print(b2.sum(b2))

    c3 = np.dot(b1, b2)

    print(a1.shape)
    a3 = np.dot(a1, a2)
    print(a3.shape)


# multi_dot()
def slice_x():
    x = np.random.randint(1, 10, (3, 4, 5))
    print(x)
    # 对于不同额维度，应该是代表[:,:,1]
    x[..., 1] = 1
    # 对维度的顺序进行了反转？比如RGB是一个深度值方向
    x = x[..., ::-1]
    print(x.shape)
    print(x)


slice_x()
