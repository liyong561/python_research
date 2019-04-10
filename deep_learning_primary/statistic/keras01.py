import tensorflow.keras.backend  as K
import numpy as np


def square():
    '''
    numpy和keras基本相同
    :return:
    '''
    a1 = K.placeholder((2,3))
    a1_sum = K.square(a1)
    a1_sum_np = np.square(a1_sum)
    print(a1_sum_np)
    print(a1_sum)

square()