import tensorflow as tf


def test_1():
    a = tf.Variable([10, 20])
    b = tf.assign(a, [20, 30])
    c = a + [10, 20]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print("test_1 run a : ", sess.run(a))  # => [10 20]
        print("test_1 run c : ", sess.run(c))  # => [10 20]+[10 20] = [20 40] 因为b没有被run所以a还是[10 20]
        print("test_1 run b : ", sess.run(b))  # => ref:a = [20 30] 运行b，对a进行assign
        print("test_1 run a again : ", a)  # => [20 30] 因为b被run过了，所以a为[20 30]
        print("test_1 run c again : ",
              sess.run(c))  # => [20 30] + [10 20] = [30 50] 因为b被run过了，所以a为[20,30], 那么c就是[30 50]


def test_2():
    a = tf.Variable([10, 20])
    b = tf.assign(a, [20, 30])
    c = b + [10, 20]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(sess.run(a))  # => [10 20]
        print(sess.run(c))  # => [30 50] 运行c的时候，由于c中含有b，所以b也被运行了
        print(sess.run(a))  # => [20 30]


test_1()
test_2()


if __name__ == '__main__()':  # __name__这个方法主要是用来import，.py文件执行时使用。
    main()