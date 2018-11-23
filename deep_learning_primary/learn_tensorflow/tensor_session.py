# -*- coding: utf-8 -*-
# 第一个基于TensorFlow的程序调通了，虽然是按照官网教程写的，我饿根本不知道它在做什么。
# 但是凭着基本的python知识和一些深度学习的知识，我要能够大致看懂它
# 这应该是一个小的函数拟合过程。

import tensorflow as tf
import  numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 忽略cpu的警告

x_data = np.float32(np.random.rand(2,100))   # 元素值在0-1之间张量。
y_data = np.dot([0.100, 0.200], x_data) + x_data   # dot运算，张量广播

b = tf.Variable(tf.zeros([1]))  # tf.Variable不知道在干什么，
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))  #
y = tf.matmul(W,x_data) +b  # 这个就是线性模型。

loss = tf.reduce_mean(tf.square(y -y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 制定了一个很熟悉的优化器，根据名字可以看出来。同时，0.5是学习率。
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()  # Session 到底是什么？
sess.run(init)

for step in range(0,201):
    # 这个过程就类似我在训练自己的神经网络。
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(W),sess.run(b))