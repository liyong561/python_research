import tensorflow.keras.backend as K
import tensorflow.keras.applications.vgg16 as vgg16
from PIL import Image
import numpy as np

'''
这是一个错误的求导，看看自己当时为什么没有做对
'''


def get_feature(x, layer_name):
    g_model = vgg16.VGG16(include_top=False, weights='imagenet')
    output1 = g_model.get_layer(layer_name).output

    fn = K.function([g_model.input], [output1])
    print(x)
    # if x.shape != (224, 224, 3):
    x = np.reshape(x[0], (224, 224, 3))
    output1_val = fn([x])[0]

    return output1_val


def get_loss(gImArr):
    gImArr = get_feature(gImArr, 'block3_conv1')
    im = Image.open('/Users/yongli/Pictures/flower02.jpeg').resize((224, 224))
    imArr = np.array(im).astype('float32')
    if gImArr.shape != (224, 224, 3):
        gImArr = np.reshape(gImArr, (224, 224, 3))
    return K.mean(imArr - gImArr)


def get_grad(gImArr):
    """
    Calculate the gradient of the loss function with respect to the generated image
    K.gradient
    """
    g_model = vgg16.VGG16(include_top=False, weights='imagenet')
    target_width = 224
    target_height = 224
    if gImArr.shape != (1, target_width, target_height, 3):
        gImArr = gImArr.reshape((1, target_width, target_height, 3))
    grad_fcn1 = K.gradients(get_loss([g_model.input]), g_model.input)[0]
    grad_fcn = K.function([g_model.input], grad_fcn1)

    print(type(grad_fcn))

    grad = grad_fcn([gImArr])[0].flatten().astype('float64')
    return grad


def get_grad_tt(im_path):
    im = Image.open(im_path).resize((224, 224))
    im_arr = np.array(im)
    # im_arr = np.expand_dims(im_arr, axis= 0)
    grad = get_grad(im_arr)
    print(type(grad))


get_grad_tt('/Users/yongli/Pictures/flower.jpeg')
