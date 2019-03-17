import tensorflow as tf
import numpy as np

def tt_ops():
    arr= tf.Variable([23,24,89,123,43],dtype='float32')  # 定义时用引号
    arr_sin = tf.sin(arr)  # 有init方法中定义才可以这么引用
    print(arr_sin)  # 在TensorFlow中，这只是定义了一个数据运算流，其实并没进行计算，需要Session。


def tt_sss():
    arr = tf.Variable('arr', [123,123,12,12,98],dtype=np.float32)  #  variable还要初始化吗？
    arr_cos = tf.cos(arr)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)  # 这就是一个tensor的flow过程
    result = sess.run(arr_cos)

    print(result)


tt_sss()
