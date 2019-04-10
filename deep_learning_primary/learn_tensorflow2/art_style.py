import tensorflow.keras.applications.vgg16 as vgg16
import tensorflow.keras.backend as K
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import scipy.optimize as  optimize
import tensorflow as tf


class Ld():
    '''
    先调用get_loss函数,所以get_loss_and_grad函数之调用一次
    返回的loss和grad用于fmin函数调用
    '''

    def __init__(self, content_path, style_path):
        self.loss_value = None
        self.grads_values = None
        self.content_path = content_path
        self.style_path = style_path
        self.vgg_model = vgg16.VGG16(include_top=False, weights='imagenet')
        self.c_im = np.array(Image.open(content_path).resize((224, 224))).astype('float64').reshape((1,224,224,3))
        self.s_im = np.array(Image.open(style_path).resize((224, 224))).astype('float64').reshape((1,224,224,3))

    def get_loss(self, x):
        self.loss_value, self.grads_values = self.get_loss_and_grad(x)
        print(self.loss_value)
        return self.loss_value

    def get_style_loss(self, x):
        layer_names = ['block3_conv1', 'block4_conv1']
        style_loss = 0

        for layer_name in layer_names:
            x_feature = self.get_feature_map(layer_name)([x])
            s_feature = self.get_feature_map( layer_name)([self.s_im])
            # (56,56,256)
            print(x_feature.shape)
            h, w, l = x_feature.shape

            for i in range(l):
                gram = np.dot(x_feature[:, :, i], np.transpose(s_feature[:, :, i], (1, 0)))
                el = np.sum(np.square(x_feature[:, :, 1] - gram)) / (4 * l * l * h * h * w * w)
                style_loss += el

        return style_loss

    def get_content_loss(self, x):
        layer_names = ['block3_conv1', 'block4_conv1']
        content_loss = 0
        print('ss1 :' + str(x.shape))
        for layer_name in layer_names:
            x_feature = self.get_feature_map(layer_name)([x])
            c_feature = self.get_feature_map(layer_name)([self.c_im])
            l = x_feature.shape[2]
            for i in range(l):
                content_loss += 0.5 * np.sum(np.square(x_feature[:, :, i] - c_feature[:, :, i]))

        return content_loss

    def get_grad(self, x):
        grads = np.copy(self.grads_values)
        self.loss_value = None
        self.grads_values = None
        return grads.flatten().astype('float64')

    def get_feature_map(self,layer_name):
        '''
        在这个函数中，K.funcion函数的使用就相当于定义一个model
        Requested Tensor connection between nodes "input_1" and "input_1" would create a cycle.
        是不是不应该在函数类调用fn1_value = fn1([x])
        :param x: 输入的迭代值
        :param layer_name: 层名
        :return: 某层的输出
        '''
        vgg = vgg16.VGG16(include_top=False, weights='imagenet')
        output1 = vgg.get_layer(layer_name).output
        fn1 = K.function([vgg.input], [output1])
        # fn1_value = fn1([x])
        # print(fn1_value.shape)
        # fn1_value = fn1_value[0]
        # print(fn1_value.shape)
        return fn1

    def get_loss_and_grad(self, x):
        '''
        x和im有点类似实参和形参
        loss要是一个tensor
        :param x: 迭代值
        :return:
        '''
        im_pl = K.placeholder((1, 224, 224, 3))
        vgg = vgg16.VGG16(include_top=False, weights='imagenet')
        im = vgg.input
        x = x.reshape((1,224,224,3))



        loss = K.sum([self.get_style_loss(im_pl),self.get_content_loss(im_pl)])
        print(x.shape)
        grads = tf.gradients(loss, im_pl)

        outputs = []
        outputs += grads
        print('k_function'+ str(x))
        iteration = K.function([im], outputs)

        outs = iteration([x])
        loss_val = outs[0]
        grads_val = outs[1]
        print(grads_val)

        grads_val = grads_val.flatten().astype('float64')

        return loss_val, grads_val


def train():
    content_path = '/Users/yongli/Pictures/flower.jpeg'
    style_path = '/Users/yongli/Pictures/flower02.jpeg'
    ld = Ld(content_path, style_path)
    x = np.random.randint(1, 255, (224, 224, 3)).flatten()
    print(x.shape)
    xopt, f_val, info = optimize.fmin_l_bfgs_b(ld.get_loss, x, fprime=ld.get_grad, bounds=[(0, 256)] * 224 * 224 * 3,
                                               disp=True,maxiter=5)
    print(xopt.shape)


train()
