import tensorflow.keras.applications.vgg16 as vgg16
import tensorflow.keras.backend as K
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import scipy.optimize as opt
import tensorflow as tf

def keras_fn():
    '''
    对梯度值进行了修改，它是怎么做到不超出图片的数值范围的？
    :return: 更新后的输入值
    '''
    conv_base = vgg16.VGG16(include_top= False,weights ='imagenet')
    im = Image.open('/Users/yongli/Pictures/flower.jpeg')
    im = im.resize((224,224))
    im_arr = np.array(im)
    im_arr =np.expand_dims(im_arr, axis=0)
    im_arr = im_arr.astype('float32')

    layer_name = 'block3_conv1'
    filter_idx = 0

    layer_output = conv_base.get_layer(layer_name).output
    loss = K.mean(layer_output[:,:,:,filter_idx])

    grads = K.gradients(loss, conv_base.input)[0]

    grads /= (K.sqrt(K.mean(K.square( grads))) + 1e-5)
    iterate = K.function([conv_base.input] , [loss, grads])

    step =1
    for i in range(40):
        loss_value, grads_value = iterate([im_arr])
        im_arr += grads_value
    plot.imshow(im_arr[0])
    plot.show()


def loss_wrapper(x):
    im_arr = np.reshape(x ,(1,224,224,3))
    vgg_model = vgg16.VGG16(include_top=False, weights='imagenet')
    output1 = vgg_model.layers[10].output

    loss = K.function([vgg_model.input], [K.mean(output1[:, :, :, 0])])

    return loss([im_arr])[0]


def grad_wrapper(x):
    im_arr = np.reshape(x, (1, 224, 224, 3))
    vgg_model = vgg16.VGG16(include_top=False, weights='imagenet')
    output1 = vgg_model.layers[10].output

    grad = K.function([vgg_model.input], tf.gradients(K.mean(output1[:, :, :, 0]), vgg_model.input))
    return grad([im_arr])[0].flatten()


# keras_fn()
def min_value():
    '''
    使用scipy.fmin_l_bfgs_b,并提供梯度函数,x0为flatten后的结果，grad和loss函数都是使用input参数，接受的参数shape=(？，224，224，3）
    所以应该对grad和loss函数进行包装一下
    loss函数返回一个标量，grad返回一个数组
    tf.gradients(output1, vgg_model.input)),这个有问题，我自己都不知道这是什么意思
    :return: 返回使损失函数达到最小值的，初始值为一张图像，然后展平的值。
    '''

    im = Image.open('/Users/yongli/Pictures/flower.jpeg')
    im = im.resize((224, 224))
    im_arr = np.array(im).flatten()



    a1 = opt.fmin_l_bfgs_b(func = loss_wrapper, x0 = im_arr,fprime= grad_wrapper)
    print(a1)

min_value()