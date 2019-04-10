from scipy import optimize
import matplotlib.pyplot as plot
import numpy as np
import tensorflow as tf


def loss_fn(x):
    '''
    使用2范数，通常损失函数都是标量
    :param x: shape=(2,1)
    :return: 矩阵的2范数，标量，没有使用tensorflow中的张量运算
    x = np.random.randint(2,23,(2,2)).astype('float64')
    print(loss_fn(x))

    '''
    x1 = np.zeros((2, 2), dtype='float64')
    x1[0, :] = x[0:2]
    x1[1, :] = x[2:4]
    w = np.array([[2, -4],
                  [-4.0, 9]])
    b = np.array([[2, 4],
                  [4.0, 9]])
    res = np.dot(x1, w) - b

    res = np.linalg.norm(res)
    return res


def loss_fn1(x):
    '''
    :param x:  传入的可能是多维ndarray,但是在迭代时返回的是一维，可能发生的就是im2col运算
    :return: 传回来的是展平的数组
    '''
    x1 = x[0]
    print(x1)
    print(type(x1))
    return np.linalg.norm(x1)


def loss_fn2(x):
    w = np.array([[2, 4],
                  [4.0, 2]])
    x1 = np.zeros((2, 2), dtype='float64')
    x1[0, :] = x[0:2]
    x1[1, :] = x[2:4]
    x1 -= 3
    print(x1)
    res = x1 * w
    return np.mean(res)

def grad(x):
    pass

def tt_scale():
    y = lambda x: x ** 2 + 10 * x + 4
    x = np.arange(-10, 10, 0.1)
    plot.plot(x, y(x))

    a = optimize.fmin_bfgs(y, 0)
    print(a)
    plot.show()


def tt_vector():
    '''
    `fmin_bfgs输入时一个ndarray类型，不是张量类型，传入的guess形状是(2,2),怎么迭代时就变成了（4）
    :return: 次优解，在迭代的时候，返回的梯度是一个列表，所以在设计loss函数事，传入的也应该地列表，应该函数会自动的进行迭代运算
    '''

    x = np.random.randint(2, 23, (3, 3, 3)).astype('float64')
    print(x)
    a= optimize.fmin_l_bfgs_b(loss_fn, x)
    print(a)


tt_vector()
