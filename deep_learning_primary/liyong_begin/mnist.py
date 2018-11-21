from keras.datasets import mnist
from keras.datasets import boston_housing
import matplotlib.pyplot as plt


def mnist_test():

    (train_images,train_labels), (test_images,test_labels) = mnist.load_data()
    # 看源码，就没有one hot 参数，要自实现。
    print(type(train_images))
    print(train_images.shape,train_labels.shape) # 标签形式。
    # digit=train_images[4]   # the 4th picture
    print(train_labels[1])


def boston_house():

    (train_data, train_targets),(test_data, test_targets) = boston_housing.load_data()
    print(train_data.shape)  # 看看测试数据长什么样。


boston_house()