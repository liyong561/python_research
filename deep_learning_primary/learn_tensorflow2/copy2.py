# *_*coding:utf-8 *_*
# author: 许鸿斌
# 邮箱:2775751197@qq.com


import numpy as np
import time
import argparse

from scipy.misc import imsave
from scipy.optimize import fmin_l_bfgs_b
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import vgg16
from tensorflow.keras import backend as K

# 配置参数
# base_image_path：内容图片路径
# style_reference_image_path：风格图片路径
# result_prefix：生成图片名前缀
# --iter：迭代次数，默认为10次，基本上10次就足够了，如果不行再加
# --content_weight：内容权重，调整loss中content_loss部分的权重，默认为0.025
# --style_weight：风格权重，调整loss中style_loss部分的权重，默认为1.0
# --tv_weight:整体方差权重，调整loss中total_variation_loss部分的权重，默认为1.0
base_image_path ='/Users/yongli/Pictures/flower.jpeg'
style_reference_image_path ='/Users/yongli/Pictures/flower02.jpeg'
result_prefix ='dd'
iterations =10



# 几个不同loss的权重参数
total_variation_weight = 0.0025
style_weight = 1.0
content_weight = 1.0

width, height = load_img(base_image_path).size  # 获取内容图片的尺寸
img_nrows = 224
img_ncols = 224





# 计算loss和梯度



# this Evaluator class makes it possible
# to compute loss and gradients in one pass
# while retrieving them via two separate functions,
# "loss" and "grads". This is done because scipy.optimize
# requires separate functions for loss and gradients,
# but computing them separately would be inefficient.
class Evaluator(object):
    def __init__(self):
        self.loss_value = None
        self.grads_values = None

    def loss(self, x):
        assert self.loss_value is None
        x = x.reshape(1,224,224,3)
        loss_value, grad_values = self.eval_loss_and_grads(x)
        self.loss_value = loss_value
        self.grad_values = grad_values
        return self.loss_value

    def grads(self, x):
        assert self.loss_value is not None
        grad_values = np.copy(self.grad_values)
        self.loss_value = None
        self.grad_values = None
        return grad_values

    def eval_loss_and_grads(self, x):
        combination_image = K.placeholder((1, img_nrows, img_ncols, 3))
        model = vgg16.VGG16(weights='imagenet', include_top=False, input_tensor=combination_image)

        layer_output = model.get_layer('block3_conv1').output
        # loss = K.mean(layer_output[:, 2, :, 1])
        loss = self.total_variation_loss(x)
        # 计算生成图片关于loss的梯度
        grads = K.gradients(loss, combination_image)
        print(grads)
        outputs = [loss]

        print('grads is list'+str(type(combination_image)))
        outputs += grads
        # 生成一个可调用函数，输入为：[combination_image]，输出为：outputs
        f_outputs = K.function([combination_image], outputs)
        outs = f_outputs([x])
        loss_value = outs[0]
        grad_values = outs[1].flatten().astype('float64')

        return loss_value, grad_values

    def gram_matrix(self,x):
        assert K.ndim(x) == 3
        if K.image_data_format() == 'channels_first':
            features = K.batch_flatten(x)
        else:
            features = K.batch_flatten(K.permute_dimensions(x, (2, 0, 1)))
        gram = K.dot(features, K.transpose(features))
        return gram

    # style loss：
    # 从VGG16网络的特定层可以获取到风格图片和生成图片的特征图(feature map)，
    # 使用feature map计算gram矩阵，即计算出两张图片的风格特征。根据论文中的公式，计算出
    # style loss，即两张图片风格特征的差异。
    def style_loss(self,style, combination):
        assert K.ndim(style) == 3
        assert K.ndim(combination) == 3
        S = self.gram_matrix(style)
        C = self.gram_matrix(combination)
        channels = 3
        size = img_nrows * img_ncols
        return K.sum(K.square(S - C)) / (4. * (channels ** 2) * (size ** 2))

    def content_loss(self,base, combination):
        return K.sum(K.square(combination - base))

    # total variation loss：
    # 第三个loss函数，用来表示生成图片的局部相干性
    def total_variation_loss(self, x):
        a = K.square(x[:, :, 4, 1] - x[:, :, 3, 0])
        b = K.square(x[:, :, 2, 1] - x[:, :, 1, 0])

        return K.sum(K.pow(a + b, 1.25))


evaluator = Evaluator()

x = np.random.uniform(0, 255, (1, img_nrows, img_ncols, 3)) - 128.

# 使用L-BFGS算法来求解非约束优化问题，scipy中提供了实现，使用fmin_l_bfgs_b函数来求解前面得到的总的loss的最小值

x, min_val, info = fmin_l_bfgs_b(evaluator.loss, x.flatten(), fprime=evaluator.grads, maxfun=20)
print('Current loss value: {}'.format(min_val))

