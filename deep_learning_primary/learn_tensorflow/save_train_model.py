import tensorflow as tf


#  使用TensorFlow中的api来保存熟练的网络模型
def test_save(init=0):
    v1 = tf.Variable(tf.random_normal([3, 9]), name='var_v1')
    v2 = tf.Variable(tf.random_normal([4, 9]), name='var_v2')
    save = tf.train.Saver()  # 还要指明放了什么东西吗？空值则表示保存所有变量
    sess = tf.Session()
    init = tf.variables_initializer([v1, v2])
    sess.run(init)  # 需要在会话中init才行。
    save.save(sess, 'model/v1', global_step=1)  # 可能需要在summary或者log中创建回应文件,不是,而是.相对路径


def test_restore(idx =0):
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('model/v1-1.meta')  # 说明这是一个graph文件，
        saver.restore(sess, tf.train.latest_checkpoint('model/'))   # 应该是将session和saver文件关联
        #  tf.train.latest_checkpoint()应该会定位到checkpoint文件
        print(sess.run('var_v1:'+str(idx)))  # 是op还是一个Tensor？没有把这个变量值取出，就是没做好
        '''
        这个0是什么意思呢
        在函数中使用记得Variable变量时，两次调用时其名字不一样
        '''


test_save()
test_restore()
