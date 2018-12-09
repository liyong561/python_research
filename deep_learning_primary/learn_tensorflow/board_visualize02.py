import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random

# 训练参数,定义的全局变量
learning_rate = 0.01

traing_epochs = 1000

display_step = 50

logs_path = "logs2"
# 训练数据
train_X = np.asarray([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                      7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
train_Y = np.asarray([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
                      2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])

n_samples = train_X.shape[0]  # 数据为一个值


def test_train():

    # X,Y为占位符，在TensorFlow中很常见,no shape param,可以用任意的形状
    X = tf.placeholder("float")
    Y = tf.placeholder("float")

    # 初始化w,b
    W = tf.Variable(random.random(), name="weight")  # 一个数，默认0-1的随机数
    b = tf.Variable(random.random(), name="bias")

    # 构造线性模型,这里涉及广播，
    pred = tf.add(tf.multiply(X, W), b)

    # 均方误差
    # reduce_sum是对每一项进行加和
    # reduce_sum(x,0)是每一列进行加和，reduce_sum(x,1)是对每一行进行加和
    cost = tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * n_samples)

    # 梯度下降,目标是cost最小
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    # 初始化所有的变量jj
    init = tf.global_variables_initializer()

    # 创建summary来观察损失值
    tf.summary.scalar("loss", cost)  # 形成了tensorboard的图表
    merged_summary_op = tf.summary.merge_all()

    # 以上都是构造op，只是为了告诉tensorflow 模型的数据流动方向


    # 使用session 启动默认图
    with tf.Session() as sess:
        sess.run(init)  # 初始化

    # op 把需要的记录数据写入文件
        summary_writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

        for epoch in range(traing_epochs):
            for (x, y) in zip(train_X, train_Y):
                # 这里train_X应该是笔误吧
                sess.run(optimizer, feed_dict={X: train_X, Y: train_Y})

            if (epoch + 1) % display_step == 0:
                # c, summary = sess.run([cost, merged_summary_op], feed_dict={X: train_X, Y: train_Y})
                c = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
                summary = sess.run(merged_summary_op, feed_dict={X: train_X, Y: train_Y})
                summary_writer.add_summary(summary, epoch * n_samples)  # 迭代的次数。

                # c=sess.run(cost,feed_dict={X:train_X,Y:train_Y})
                print("Epoch:", '%04d' % (epoch + 1), "cost=", "{:.9f}".format(c),
                  "W=", sess.run(W), "b=", sess.run(b))

        print("optimization Finished")
        training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
        print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), "\n")

    '''
        # 画图
        plt.plot(train_X, train_Y, 'ro', label="Original data")
        plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label="Fitted line")
        plt.legend()
        plt.show()
        plt.savefig('linear_train.png')
        
        # 测试数据
        test_X = np.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
        test_Y = np.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])

        print("Testing... (Mean square loss Comparison)")
        testing_cost = sess.run(
            tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * test_X.shape[0]),
            feed_dict={X: test_X, Y: test_Y})  # same function as cost above
        print("Testing cost=", testing_cost)
        print("Absolute mean square loss difference:", abs(
            training_cost - testing_cost))

        plt.plot(test_X, test_Y, 'bo', label='Testing data')
        plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
        plt.legend()
        plt.show()
        plt.savefig('linear_test.png')
    '''

test_train()