import tensorflow.keras.losses as losses
import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as back


def my_loss(y_true, y_pre):
    return losses.categorical_crossentropy(y_true, y_pre)


def fn(x):
    h1, w1 = x.shape
    w = np.random.randint(1, 10, (4, 8)).astype('float32')
    b = np.random.randint(1, 4, (h1,)).astype('float32')
    y = tf.matmul(x, w) + b
    return y


def lambda_tt():
    fn1 = lambda x: 3 * x + 1
    x1 = 33
    y = fn1(x1)
    print(y)


lambda_tt()
