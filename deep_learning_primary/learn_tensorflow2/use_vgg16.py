import tensorflow.keras.applications.vgg16 as vgg16
import tensorflow.keras.models as models
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot
import tensorflow.keras.backend as K
import tensorflow as tf
from scipy import optimize


def visualize_inter():
    im = Image.open('/Users/yongli/Pictures/flower.jpeg')
    im = im.resize((224, 224))
    im_arr = np.array(im)
    im_arr = np.expand_dims(im_arr, axis=0)

    conv_base = vgg16.VGG16(include_top=False, weights='imagenet')

    res = conv_base.predict_on_batch(im_arr)
    print(res.shape)

    output1 = conv_base.layers[4].output
    '''
    使用model类，重新构造对象
    从这个方法可以看出，Model类和function具有相同的作用
    function中的input和output中暗含了它们的映射关系。
    '''
    model1 = models.Model(conv_base.input, output1)
    activation1 = model1.predict_on_batch(im_arr)[0]

    fn1 = K.function([conv_base.input], [conv_base.layers[6].output])
    activation = fn1([im_arr])
    activation = activation[0][0]
    print(activation.shape)

    plot.figure()
    plot.subplot(221)
    plot.imshow(activation[:, :, 0])

    plot.subplot(222)
    plot.imshow(activation[:, :, 1])

    plot.subplot(223)
    plot.imshow(activation[:, :, 2])

    plot.subplot(224)
    plot.imshow(activation[:, :, 3])
    plot.show()

    print(activation1.shape)


def visualize_grad():
    '''
    在求梯度时，应该指明在哪个点。
    想定义一个求偏导的函数，然后向函数传值，求出这个参数。
    :return:grad本来返回的是一个张量列表，
    '''
    im = Image.open('/Users/yongli/Pictures/flower.jpeg')
    im = im.resize((224, 224))
    im_arr = np.array(im)
    im_arr = np.expand_dims(im_arr, axis=0)
    conv_base = vgg16.VGG16(include_top=False, weights='imagenet')
    print(len(conv_base.layers))
    output1 = conv_base.layers[10].output

    grad_fn = K.function([conv_base.input], tf.gradients(output1, conv_base.input))
    x = im_arr.astype('float32')
    h1, w1 = x.shape[1:3]
    results = np.zeros((3 * h1, 4 * w1, 3))
    for i in range(12):
        grad = grad_fn([x])[0]
        x -= 2 * grad
        j = i // 4
        k = i - 4 * j
        results[j * h1: (j + 1) * h1, k * w1:(k + 1) * w1, :] = x[0]
        print(x.shape)

    results = np.clip(results, 0, 255).astype('uint8')
    plot.imshow(results)
    plot.show()
    print(grad)



class Loss_grad:
    '''
          :param x: x应该是一个一维数组，
          :return: 返回一个0维数组，也就是标量
          loss_fn之定义了输入和输出的关系，没有数据传入，
          从loss开始就是一个函数了，可以看出，对loss进行了多此包装
          loss的参数和loss_fn不一样
          grad和loss有很多共用参数，给他们创建一个类
          K.gradient返回list
            self.loss也含有参数
          理解K.function的作用，实际上定义一个多输出网络，这也是网络中的函数api
     '''

    def __init__(self):
        self.conv_base = vgg16.VGG16(weights='imagenet', include_top=False)
        layer_name = 'block3_conv1'
        self.output1 = self.conv_base.get_layer(layer_name).output
        self.filter_idx = 0
        self.l = None
        self.g = None
        self.loss = K.mean(self.output1[:, :, :, self.filter_idx])

        self.grads = K.gradients(self.loss, [self.conv_base.input])[0]
        self.grads /= K.sqrt(K.mean(K.square(self.grads)) + 1e-5)

        self.loss_grad_fn = K.function([self.conv_base.input], [self.loss, self.grads])

    def ls(self, x):
        x = x.reshape(1, 224, 224, 3)
        return self.loss_grad_fn([x])

    def loss_fn(self, x):

        return self.ls(x)[0]

    def grad_fn(self, x):
        g1 = self.ls(x)[1]
        print(g1.shape)
        return g1.flatten()

    def scipy_optimizer_input(self):
        '''
        tf.gradients(output1, conv_base.input)，这个提调度函数有点问题,
        通过优化器搜索最小的解
        函数的定义选择了简单的K.mean
        在这里，存在一个输入形状兼容的问题，fmin_bfgs中的迭代输入参数是ndarray,在这里就是一个一层list
        而神经网络的输入是一个4维的数据，所以需要重新定义其中的损失函数
        在神经网络的传播中，是不是要指定一下梯度函数
        :return:
        '''

        im = Image.open('/Users/yongli/Pictures/flower.jpeg')
        im = im.resize((224, 224))
        im_arr = np.array(im).astype('float32')
        im_arr_flatten = im_arr.flatten()
        x  = np.zeros((1,224,224,3)).astype('float32').flatten()
        x = optimize.fmin_l_bfgs_b(self.loss_fn, im_arr_flatten,fprime=self.grad_fn, maxiter=40,disp=True)
        print(type(x))

        results = np.clip(x.reshape(224, 224, 3), 0, 255).astype('uint8')
        print(results.shape)
        plot.imshow(results)
        plot.show()

'''
ld = Loss_grad()
ld.scipy_optimizer_input()
'''

visualize_grad()