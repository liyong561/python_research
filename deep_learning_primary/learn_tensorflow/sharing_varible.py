import tensorflow as tf
from tensorflow.python.client import device_lib


def layer(input1, w_shape, b_shape):
    weight_init = tf.random_uniform_initializer(minval=0, maxval=10)
    # ctl + p 显示构造器参数
    bias_init = tf.constant_initializer(value=0)
    weight = tf.get_variable('W', w_shape, initializer=weight_init)
    bias = tf.get_variable("b", b_shape, initializer=bias_init)
    output = tf.matmul(input1, weight) + bias
    return output


def my_network(input1):  # input是一个build-in函数
    with tf.variable_scope("layer1"):  # scope的意思，可能是命名空间
        output1 = layer(input1, [784, 100], [100])
    with tf.variable_scope('layer2'):
        output2 = layer(output1, [100, 50], [50])
    with tf.variable_scope('layer3'):
        output3 = layer(output2, [50, 10], [10])
    return output3


def test01():
    input01 = tf.placeholder(tf.float32, [100, 784])
    input02 = tf.placeholder(tf.float32, [2000, 784])
    my_network(input01)
    my_network(input02)  # 在此调用，就提示variable already exits


def test02():
    with tf.variable_scope(name_or_scope='share', reuse=tf.AUTO_REUSE):
        # reuse ：在该作用的区域内的变量对象，都自动重用吗？
        # 自动重用，和书上的略有差别
        input02 = tf.placeholder(tf.float32, [2000, 784])
        my_network(input02)
        input01 = tf.placeholder(tf.float32, [100, 784])
        my_network(input01)


def cpu_and_gpu():
    print(device_lib.list_local_devices())  # 和系统相关，列举出device

    sess = tf.Session()
    a = tf.constant(2)
    b = tf.constant(3)
    multiply = tf.multiply(a, b)
    sess.run(multiply)


def variable_name():
    var = tf.Variable(tf.random_normal([32, 3]), name='var_1')
    print(var.name)  # 为什么会是var_1:0?


variable_name()
