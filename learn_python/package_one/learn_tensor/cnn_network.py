import tensorflow as tf
import numpy as np
'''
测试使用TensorFlow中的conv2
卷积层参考博文：https://blog.csdn.net/zuolixiangfisher/article/details/80528989
net可以搭建起来，但是若何backword去调参呢？
'''
def tt_nn():
    input_data = np.random.randint(10,89,size=(100,323,450,3))  # low,high,size =
    input_data = input_data.astype(np.float32)
    filter_data1 = np.random.randint(0,10,size=(5,5,3,10)) # 卷积核的channel和input的channel应该一样
    filter_data2 = np.random.randint(0,10,size=(5,5,10,3))

    op1 = tf.nn.conv2d(input_data,filter_data1,strides=[1,2,2,1],padding='VALID')  # 一次forward（）
    print(op1.shape)  # op1的形状（100，160，223，10）

    op2 = tf.nn.conv2d(op1,filter_data2,strides=[1,2,2,1],padding="VALID")

    op3 = tf.nn.max_pool(op2,[1,3,3,1],[1,3,3,1],padding="VALID",data_format='NHWC') # pool层，这个ksiz的特性很重要

    sess = tf.Session()
    out = sess.run(op3)  # 继续作为下一个conv的输入。

    print(op2.shape)
    print(out.shape)


def tt_f():
    arr = np.array([13,23,32,23,89],dtype='float32')
    arr_arg = tf.sigmoid(arr)  # tf中函数都是惰性的，等待执行的命令。

    arr_ac = tf.nn.relu(arr)

    print(ar)
    print(arr_arg)

tt_f()
