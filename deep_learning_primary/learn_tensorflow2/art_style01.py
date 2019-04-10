import tensorflow.keras.applications.vgg16 as vgg16
import tensorflow.keras.backend as K
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import scipy.optimize as  optimize
import tensorflow as tf

'''
作为全局变量使用
重点是返回一个以x为输入，loss为输出（tensor）的函数层。
x不用placeholder是为了显示和output的关系，否则我还要再创建一个function层
'''
vgg_model = vgg16.VGG16(include_top=False, weights='imagenet',input_shape=(224,224,3))
x = vgg_model.input
# x = K.placeholder((1, 224, 224, 3))

content_path = '/Users/yongli/Pictures/flower.jpeg'
style_path = '/Users/yongli/Pictures/flower02.jpeg'
c_im = np.array(Image.open(content_path).resize((224, 224))).astype('float64').reshape((1, 224, 224, 3))
s_im = np.array(Image.open(style_path).resize((224, 224))).astype('float64').reshape((1, 224, 224, 3))


def get_style_loss():
    '''
    这不是通常意义上的函数，这是一个函数调用。因为不用向其传递引用。
    x_feature是一个tensor，shape未知
    '''
    layer_names = ['block3_conv1', 'block4_conv1']
    style_loss = K.variable(0)

    for layer_name in layer_names:
        x_feature = get_feature_map(layer_name)[0][0]
        s_feature = get_feature_val(layer_name, s_im)
        # (56,56,256)
        size, size1, channels = x_feature.shape

        for i in range(channels):

            C = x_feature[:, :, i]
            S = s_feature[:,:,i].transpose()
            el = K.sum(K.square(S - C))

            el = el / (4.0 * int(channels) * int(channels) *int(size) * int(size))
            style_loss = style_loss + el
    return style_loss


def get_content_loss():
    layer_names = ['block3_conv1', 'block4_conv1']
    content_loss = 0
    print('ss1 :' + str(x.shape))
    for layer_name in layer_names:
        x_feature = get_feature_map(layer_name)[0][0]
        c_feature = get_feature_val(layer_name, c_im)
        channels = x_feature.shape[2]
        for i in range(channels):
            content_loss = content_loss + 0.5 * np.sum(np.square(x_feature[:, :, i] - c_feature[:, :, i]))

    return content_loss


def get_feature_val(layer_name, im):
    '''
    和全局变量比较，可能算是变量冗余吧
    这里想要得到中间激活层的数据，就得使用K.function或者Model
    '''
    vgg = vgg16.VGG16(include_top=False, weights='imagenet')
    output1 = vgg.get_layer(layer_name).output
    fn1 = K.function([vgg.input], [output1])
    fn1_value = fn1([im])[0]
    fn1_value = fn1_value[0]
    print(fn1_value.shape)
    return fn1_value


def get_loss_grad():
    '''
    loss是个张量，需要有输入，才能有输出
    '''
    loss = get_style_loss() + get_style_loss()
    grads = K.gradients(loss, x)[0]
    iteration = K.function([x], [loss, grads])
    return iteration


def get_loss(x1):
    '''
    自己更加提示找错误，才是最强的技能
    '''
    global loss_val, grads_val
    x1 = x1.reshape((1,224,224,3))
    loss_val, grads_val = get_loss_grad()([x1])
    return loss_val


def get_grads(x1):
    return grads_val.flatten().astype('float64')


def get_feature_map(layer_name):
    output1 = vgg_model.get_layer(layer_name).output
    fn1 = K.function([x], [output1])
    return fn1.outputs


def train():
    '''
    在python中，写一个class有时候还不如一个function方便
    :return:
    '''
    x = np.random.randint(1, 255, (224, 224, 3)).flatten()
    print(x.shape)
    xopt, f_val, info = optimize.fmin_l_bfgs_b(get_loss, x, fprime=get_grads, bounds=[(0, 256)] * 224 * 224 * 3,

                                               disp=True, maxiter=2)
    im = xopt.reshape((224,224,3))
    im =im.astype('uint8')
    plot.imshow(im)
    plot.show()

    print(xopt.shape)


train()
