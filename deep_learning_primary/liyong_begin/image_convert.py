# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

def test():
    pil_in=Image.open("E:/Data/Images/Architecture/chongqing_finance.jpg")
    im_arr=np.array(pil_in) # 对这个张量进行运算，最后反映在图片上
    print(im_arr.shape,im_arr.dtype) # this can import the ndim
    im_arr=255-im_arr
    im=Image.fromarray(im_arr)
    im.save("E:/Data/Images/Architecture/chongqing_finance02.jpg")
    plt.imshow(im)  # 很强大，数学终于发挥作用了，想怎么调参就怎么调参
    plt.show()
if __name__ == "__main__":
    sys.setrecursionlimit(20)
    test()