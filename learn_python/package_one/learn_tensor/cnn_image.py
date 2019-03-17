import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plot
import numpy as np

def tt_ft(file):
    im = Image.open(file) # not open(file)
    im_arr = np.asarray(im,dtype='float32')  # 233.0这样的浮点数
    im_arr = im_arr/256
    print(im_arr.shape)
    # print(im_arr[:,2,2])
    plot.figure()
    plot.subplot(221)
    plot.imshow(im_arr) # float,integer is ok

    with tf.Session() as sess:
        filter_input = np.random.rand(4,4,3,10)
        b = np.random.randint(2,19,size=(10))
        # print(im_arr[1,:,1]) 0.4数值比较均匀。
        print(filter_input[2,:,:,2])

        # im_arr要广播一下? ,且要求float16, bfloat16, float32, float64
        H,W,C = im_arr.shape
        im_arr = im_arr.reshape(1,H,W,C)

        ops_cnn = tf.nn.conv2d(im_arr,filter_input,strides=[1,3,3,1],padding='SAME',name='im_cnn')

        ops_cnn = tf.nn.bias_add(ops_cnn,bias=b)

        im_cnn = sess.run(ops_cnn)  # 卷积运算后，im_cnn超过了image的显示范围。fliter的值不应该是整数。不应该使用randint

        plot.subplot(222)
        print(im_cnn[0,1,:,2])  # 都到达了10.1
        plot.imshow(im_cnn[0,:,:,0:3])




    plot.show()  # 最后统一展示


tt_ft('/Users/yongli/Pictures/flower.jpeg')
