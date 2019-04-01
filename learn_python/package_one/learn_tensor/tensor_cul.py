import tensorflow as tf


def tt01():
    # 变量类型为：numpy.ndarray
    cons = tf.constant((23, 26))
    cons1 = tf.constant([12, 32, 232])
    with tf.Session() as sess:
        result = sess.run(cons1)
        print(type(result))
        print(result)


tt01()
