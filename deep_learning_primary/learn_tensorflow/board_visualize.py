import  tensorflow as tf


def test_board():
    # 展示张量的计算图
    with tf.name_scope('input'):
        input1 = tf.constant(3.0, name='A')
        input2 = tf.constant(4.0, name='B')
        input3 = tf.constant(5.0, name='C')

    with tf.name_scope('op'):
        add = tf.add(input2, input3)
        mul = tf.multiply(input1, add)

    with tf.Session() as sess:


        writer = tf.summary.FileWriter('logs/', sess.graph)  # 这句话到底干了什么，我们不得而知
        result = sess.run([add, mul])
        print(result)
        '''
        tf.summary.FileWriter函数必须在global_variables_initializer().run()
        函数之前调用，在重命名tensor对象之后调用。
        '''
test_board()