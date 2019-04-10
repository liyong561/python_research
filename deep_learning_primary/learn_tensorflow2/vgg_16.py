import tensorflow.keras.applications.vgg16 as vgg16
import tensorflow.keras.backend as K
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import scipy.optimize as  optimize
import tensorflow as tf
from  tensorflow.keras.models import Model

'''
尝试将多个层拼接起来
'''

vgg = vgg16.VGG16(include_top=False, weights='imagenet')
inputs1 = vgg.inputs


def get_feature_map(layer_name):
    '''
    在这个函数中，K.funcion函数的使用就相当于定义一个model
    Requested Tensor connection between nodes "input_1" and "input_1" would create a cycle.
    是不是不应该在函数类调用fn1_value = fn1([x])
    :param x: 输入的迭代值
    :param layer_name: 层名
    :return: 某层的输出
    '''
    output1 = vgg.get_layer(layer_name).output
    fn1 = K.function(inputs1, [output1])
    return fn1.outputs


def get_feature_map1():
    inputs2 = get_feature_map('block3_conv1')
    output2 = K.mean(inputs2[0] +90)
    fn2 = K.function(inputs2, [output2])
    return fn2.outputs


def use_feature_map():
    '''
    [[[[<tf.Tensor 'add:0' shape=(?, ?, ?, 256) dtype=float32>
    <tf.Tensor 'add_1:0' shape=(?, ?, ?, 256) dtype=float32>
    <tf.Tensor 'add_2:0' shape=(?, ?, ?, 256) dtype=float32> ...
    '''
    inputs2 = get_feature_map('block3_conv1')
    # outputs2 = inputs2 + np.array(np.random.randint(1,10,(1,14,14,512))).astype('float32')
    outputs2 = K.sum(inputs2 + np.array(np.random.randint(1, 10, (1, 14, 14, 256))).astype('float32'))
    print(outputs2)


def combine():
    fn = K.function(inputs1, get_feature_map1())
    return fn


'''
fn = combine()
a = np.random.randint(0,225,(1,224,224,3)).astype('float64')
x = fn([a])
print(x)
'''


def get_mean():
    '''
    K.mean相当于一层，参数是形参，返回的是张量
    tensor object is not callable这和K.function还不一样
    可以理解这个run方法
    '''
    a1 = np.array([[12, 3, 3],
                   [14, 78, 3]
                   ])
    a1_pl = K.placeholder((2, 3))

    a2 = K.mean(a1_pl)
    with tf.Session() as sess:
        tf.global_variables_initializer()
        a2_run = sess.run(a2, feed_dict={a1_pl: a1})
        print(a2_run)
    print(a2)


def vgg16_model():
    '''
    Input tensors to a Model must come from `tf.layers.Input`.
    Received: Tensor("Placeholder_52:0", shape=(1, 224, 224, 3), dtype=float32)
    model和function还是有很多不同的。
    :return:
    '''
    model = vgg16.VGG16(weights='imagenet', include_top=False)
    x = K.placeholder((1, 224, 224, 3),dtype='float32')
    output = model(x)
    layer_names = ['block3_conv1', 'block3_conv2']
    layers_outputs = []
    for i in range(len(layer_names)):
        layer = model.get_layer(layer_names[i])
        # 只有最后一层才有outputs
        layers_outputs.append(layer.output)

    print(output)
    model1 = K.function([x],layers_outputs)
    return model1




# vgg16_model()
use_feature_map()