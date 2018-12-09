import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def test01():
    sess = tf.Session()
    w = tf.Variable([0.3], dtype=tf.float32, name='w')
    b = tf.Variable([-0.3], dtype=tf.float32, name='b')
    x = tf.placeholder(tf.float32, name='x')
    c = tf.constant(3)
    init = tf.variables_initializer([w, b], name='init')  # 定义的操作，没有run就是没有执行 [x,],
    # 试图去初始化一个placeholder，当然出错
    liner = tf.reduce_sum(tf.add(tf.multiply(w, x), b))  # 当然这里也可以使用Python的*，+写，但是tf.add处理张量操作
    tf.summary.scalar('loss', liner)  # [] != [4] (tag 'loss'),这是一个向量和标量的问题
    tf.summary.scalar("constant", c)
    merged = tf.summary.merge_all()

    train_writer = tf.summary.FileWriter('log_test01', sess.graph)

    sess.run(init)
    result1 = sess.run(liner, feed_dict={x: [1, 2, 3, 9]})
    result2 = sess.run(merged, feed_dict={x: [1, 2, 3, 5]})
    '''
    scalar是向文件中写入标量。
    '''
    train_writer.add_summary(result2)   # 使用它的value属性
    print(result1)
    print(type(result2))  # class 'bytes'


def test02():
    session = tf.Session()

    w = tf.Variable([.3], dtype=tf.float32, name="w")  # 很多参数，这个还是不能省的

    b = tf.Variable([-.3], dtype=tf.float32, name="b")

    x = tf.placeholder(tf.float32, name="x")

    # linear = w * x + b
    linear = tf.add(tf.multiply(w, x), b)

    train_writer = tf.summary.FileWriter('log_test02', session.graph)

    init = tf.global_variables_initializer()

    session.run(init)

    print(session.run(linear, {x: [1, 2, 3, 4]}))

def global_test():
    # 系统会自动更新这个值吗？做个试验
    x = tf.placeholder(tf.float32, [None, 1], name= 'x')
    y = tf.placeholder(tf.float32, [None, 1], name= 'y')
    w = tf.Variable(tf.constant(1.0, 1.0))
    # tf.train.exponential_decay
    global_step = tf.Variable(0, trainable=False)
    learning_rate = tf.constant(0.01)
    loss = tf.pow(tf.subtract(tf.multiply(w, x), y), 2)
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(10):
            sess.run(train_step, feed_dict={x : np.linspace(1, 2, 10).reshape([10,1]),
                                            y : np.linspace(1,3,10).reshape([10, 1])})
            print(sess.run(global_step))


def global_test01():
    global_step = tf.Variable(0, trainable=False)
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(10):
        print(sess.run(global_step))

global_test01()