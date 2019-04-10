from PIL import Image,ImageDraw,ImageColor,ImageFont
import numpy as np
'''
会用到pil的这些模块，相应的方法，练习一下，熟练应用。
object detetion也将是一个复杂的工程，代码量可能很长，需要提高自己的编码水平，尤其是python。
'''

def image_ops(file_name):
    im = Image.open(file_name).resize((224,224))
    # im.show() # image对象的方法
    print('大小：'+str(im.size)+'，通道：'+im.mode)  # just a porperty,string, not tuple.
    x =np.array(np.zeros((2,4)))
    x.reshape((8))
    print(x.shape)
    return im  # 和java的语言区分开来


def image_resize(file_name,width=500,height=600):
    with Image.open(file_name) as im:
        # 参数要提供正确，这样是不对的。im.resize(width,height).save()
        im.resize((width,height)).save(file_name) #
    print("it's over")

def image_trans(file_nmae):
    im = Image.open(file_nmae);
    im_arr= np.array(im,dtype=np.uint8)  # im-array
    print(max(im_arr[1,1,:]))
    print(im_arr.shape)  # tuple

image_ops("/Users/yongli/Pictures/flower.jpeg")
