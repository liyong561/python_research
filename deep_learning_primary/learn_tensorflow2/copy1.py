# *_*coding:utf-8 *_*
# author: 许鸿斌
# 邮箱:2775751197@qq.com


import numpy as np
import time
import argparse

from scipy.misc import imsave
from scipy.optimize import fmin_l_bfgs_b
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import vgg19
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
style_reference_image_path ='/Users/yongli/Pictures/flower.jpeg'
result_prefix ='dd'
iterations =10



# 几个不同loss的权重参数
total_variation_weight = 0.0025
style_weight = 1.0
content_weight = 1.0

width, height = load_img(base_image_path).size  # 获取内容图片的尺寸
img_nrows = 400  # 设定生成的图片的高度为400
img_ncols = int(width * img_nrows / height)  # 与内容图片等比例，计算对应的宽度


# 图像预处理
def preprocess_image(image_path):
    # 读入图像，并转化为目标尺寸。
    img = load_img(image_path, target_size=(img_nrows, img_ncols))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)  # 3
    # vgg提供的预处理，主要完成（1）去均值（2）RGB转BGR（3）维度调换三个任务。
    img = vgg19.preprocess_input(img)
    return img


# 图像后处理
def deprocess_image(x):
    if K.image_dim_ordering() == 'th':
        x = x.reshape((3, img_nrows, img_ncols))
        x = x.transpose((1, 2, 0))
    else:
        x = x.reshape((img_nrows, img_ncols, 3))

    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    # 'BGR'->'RGB'
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype('uint8')
    return x


# 读入内容图和风格图，预处理，并包装成变量。这里把内容图和风格图都做成尺寸相同的了，有点不灵活。
base_image = K.variable(preprocess_image(base_image_path))
style_reference_image = K.variable(preprocess_image(style_reference_image_path))

# 给目标图片定义占位符，目标图像与resize后的内容图大小相同。
if K.image_dim_ordering() == 'th':
    combination_image = K.placeholder((1, 3, img_nrows, img_ncols))
else:
    combination_image = K.placeholder((1, img_nrows, img_ncols, 3))

# 将三个张量串联到一起，形成一个形如（3,3,img_nrows,img_ncols）的张量
# 三张图一同喂入网络中，以batch的形式
input_tensor = K.concatenate([base_image, style_reference_image, combination_image], axis=0)

# 加载vgg19预训练模型，模型由imagenet预训练。去掉模型的全连接层。
model = vgg19.VGG19(input_tensor=input_tensor,
                    weights='imagenet', include_top=False)
print('Model loaded.')

# get the symbolic outputs of each "key" layer (we gave them unique names).
outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])


# 计算特征图的格拉姆矩阵，格拉姆矩阵算两者的相关性，这里算的是一张特征图的自相关。
# 个人理解为是像素或者区域间的相关性。用这个相关性来代表风格是的表示。
def gram_matrix(x):
    assert K.ndim(x) == 3
    if K.image_data_format() == 'channels_first':
        features = K.batch_flatten(x)
    else:
        features = K.batch_flatten(K.permute_dimensions(x, (2, 0, 1)))
    gram = K.dot(features, K.transpose(features))
    return gram


# 计算风格图的格拉姆矩阵
# 计算生成图的格拉姆矩阵
# 计算风格图与生成图之间的格拉姆矩阵的距离，作为风格loss
def style_loss(style, combination):
    assert K.ndim(style) == 3
    assert K.ndim(combination) == 3
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = img_nrows * img_ncols
    return K.sum(K.square(S - C)) / (4. * (channels ** 2) * (size ** 2))


# 内容图和生成图之间的距离作为内容loss
def content_loss(base, combination):
    return K.sum(K.square(combination - base))


# 计算变异loss(不太明白)
def total_variation_loss(x):
    assert K.ndim(x) == 4
    if K.image_data_format() == 'channels_first':
        a = K.square(x[:, :, :img_nrows - 1, :img_ncols - 1] - x[:, :, 1:, :img_ncols - 1])
        b = K.square(x[:, :, :img_nrows - 1, :img_ncols - 1] - x[:, :, :img_nrows - 1, 1:])
    else:
        a = K.square(x[:, :img_nrows - 1, :img_ncols - 1, :] - x[:, 1:, :img_ncols - 1, :])
        b = K.square(x[:, :img_nrows - 1, :img_ncols - 1, :] - x[:, :img_nrows - 1, 1:, :])
    return K.sum(K.pow(a + b, 1.25))


# 以第5卷积块第2个卷积层的特征图为输出。
loss = K.variable(0.)
layer_features = outputs_dict['block5_conv2']
# 抽取内容特征图和生成特征图
base_image_features = layer_features[0, :, :, :]
combination_features = layer_features[2, :, :, :]
# 计算内容loss
loss += content_weight * content_loss(base_image_features,
                                      combination_features)

feature_layers = ['block1_conv1', 'block2_conv1',
                  'block3_conv1', 'block4_conv1',
                  'block5_conv1']
# 抽取风格图和生成图每个卷积块第一个卷积层输出的特征图
# 并逐层计算风格loss，叠加在到loss中
for layer_name in feature_layers:
    layer_features = outputs_dict[layer_name]
    style_reference_features = layer_features[1, :, :, :]
    combination_features = layer_features[2, :, :, :]
    sl = style_loss(style_reference_features, combination_features)
    loss += (style_weight / len(feature_layers)) * sl
# 叠加生成图像的变异loss
loss += total_variation_weight * total_variation_loss(combination_image)

# 计算生成图像的梯度
grads = K.gradients(loss, combination_image)

# output[0]为loss，剩下的是grad
outputs = [loss]
if isinstance(grads, (list, tuple)):
    outputs += grads
else:
    outputs.append(grads)
# 定义需要迭代优化过程的计算图。
# 前面三张图一起跑了一次网络只是抽取特征而已，而这里定义了真正训练过程的计算图。
# 计算图的前向传导以生成图为输入，以loss和grad为输出，反过来就是优化过程。
# 在初始化之前，生成图仍然只是占位符而已。
f_outputs = K.function([combination_image], outputs)


# 同时取出loss和grad
def eval_loss_and_grads(x):
    if K.image_data_format() == 'channels_first':
        x = x.reshape((1, 3, img_nrows, img_ncols))
    else:
        x = x.reshape((1, img_nrows, img_ncols, 3))
    outs = f_outputs([x])
    loss_value = outs[0]
    if len(outs[1:]) == 1:
        grad_values = outs[1].flatten().astype('float64')
    else:
        grad_values = np.array(outs[1:]).flatten().astype('float64')
    return loss_value, grad_values


# 这个类在前面同时计算出loss和grad的基础上，通过不同的函数分别获取loss和grad。
# 原因在于scipy优化函数通过不同的函数获取loss和grad。
class Evaluator(object):

    def __init__(self):
        self.loss_value = None
        self.grads_values = None

    def loss(self, x):
        assert self.loss_value is None
        loss_value, grad_values = eval_loss_and_grads(x)
        self.loss_value = loss_value
        self.grad_values = grad_values
        return self.loss_value

    def grads(self, x):
        assert self.loss_value is not None
        grad_values = np.copy(self.grad_values)
        self.loss_value = None
        self.grad_values = None
        return grad_values


evaluator = Evaluator()

# run scipy-based optimization (L-BFGS) over the pixels of the generated image
# so as to minimize the neural style loss
# x的初始化，初始化成内容图
# 为什么不是论文中的白噪声图呢？不解。
x = preprocess_image(base_image_path)

# 迭代优化过程
for i in range(iterations):
    print('Start of iteration', i)
    start_time = time.time()
    # 使用L-BFGS-B算法优化
    # 不断被优化的是x，也就是生成图。
    x, min_val, info = fmin_l_bfgs_b(evaluator.loss, x.flatten(),
                                     fprime=evaluator.grads, maxfun=20)
    print('Current loss value:', min_val)
    # save current generated image
    # 图像后处理
    img = deprocess_image(x.copy())
    # 保存图像
    fname = result_prefix + '_at_iteration_%d.png' % i
    imsave(fname, img)
    end_time = time.time()
    print('Image saved as', fname)
    print('Iteration %d completed in %ds' % (i, end_time - start_time))