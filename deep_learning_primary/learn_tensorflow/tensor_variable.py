# -*- coding: utf-8 -*-
import tensorflow as tf


def test01():
    place_holder01 = tf.placeholder(tf.float32, name='x', shape=[21, ])
    place_variable = tf.Variable(tf.random_normal([30, 20], stddev=0.5), name='weights')
    random_variable = tf.random_normal(shape=(32, 21), stddev=0.20, mean=0.3)  # shape的list和tuple都可以
    random_uniform = tf.random_uniform(shape=[10, 3], maxval=100)
    tf.variables_initializer([place_variable, ])  # 这个variable对象，不知道初始化是什么意思
    print(place_holder01)
    print(place_variable)  # 这个是Variable对象，大写，placeholder是一个tensor对象，小写
    print(random_variable)  # Tensor("random_normal_1:0", shape=(32, 21), dtype=float32)这个注解random_normal_1:0有意思
    print(random_uniform)  # 随机的均匀分布
    sess = tf.Session()
    print(sess.run(random_uniform))
    sess.close()  # 这个方法，free all resources
    '''
     session.run(mul):  可以认为mul是一个函数，是一系列操作，也算是一种设计模式。返回这个操作的具体结果 
    '''


def test02():
    tf_variable01 = tf.Variable(tf.random_normal([20, 15], stddev=0.3), name="W")
    tf_variable02 = tf.Variable(tf.random_normal([20, 15], stddev=0.3), name="W_1")
    print(tf_variable01.name)
    print(tf_variable02.name)


# test02()
# test02()  # 调用两次时，这个函数的参数竟然发生了变化，很明显，这个参数是一个对象，每次调用都创建了一个对象。
def test03():
    weight_init = tf.random_normal_initializer(mean=3, stddev=4)  # randomNormal object
    weight_init02 = tf.random_normal(shape=[13, 23])  # 区别就是有shape,这个是Tensor
    weight_init03 = tf.get_variable(name='dd', initializer = weight_init, shape = [3,23])
    # 可以自定义形状，返回Variable对象
    print(weight_init)
    print(weight_init02)
    print(weight_init03)


test03()
