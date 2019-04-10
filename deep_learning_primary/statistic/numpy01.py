import numpy as np
import tensorflow.keras.backend as K


def square():
    a1 = np.array([[12, 323, 4],
                    [12, 32, 89]])
    a_q = np.square(a1)
    print(a_q)
    a_sum = np.sum(a1)
    print(a_sum)


def sub():
    a1 = np.array([[12, 323, 4],
                    [12, 32, 89]])
    a2 = np.square([[14, 323, 4],
                    [12, 32, 89]])
    a3 = a1 - a2
    a3_a = np.subtract(a1, a2)
    print(a3_a)

def sum():
    '''
    sum函数处理张量和常量的差别
    '''
    a = K.placeholder((2,3))
    a_sum = np.array([[12, 323, 4],
                    [12, 32, 89]])
    print(np.sum(a))
    print(K.sum(a))
    print(np.sum(a_sum))

sum()
