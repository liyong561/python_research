from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

def process_data():
    data_dir = r'E:\Data\cat-and-dog\training_set'
    #  这个函数的用法，不能指定具体的文件夹
    train_data_gen = ImageDataGenerator(rescale=1. / 255)
    test_data_gen = ImageDataGenerator(rescale=1. / 255)
    #  它的编程思想很清楚，路径下有多少个文件夹就是有多少个类，同时从两个文件中取出相同的文件，然后计算。
    #  按照子文件夹的排列顺序，则cat为0，dog为1
    train_gen = train_data_gen.flow_from_directory(
        data_dir,
        target_size=(200, 200),
        batch_size=20,
        class_mode='binary'
    )
    i =1
    for train_batch, train_label in train_gen:
        # 根据两个class,返回一个包含两个元素的元组
        # 这和处理mnist数据时大同小异。
        plt.imshow(train_batch[i])
        plt.show()
        #  这个方法验证了猫的类别为0，
        #  所以这个ImageDataGenerator为这类图片分类问题提供给了统一的数据预处理方法。
        print(train_label[i])
        i+= 1
        if i>10:
            break


def conv():
    #  构建网络的函数，主要要考虑的问题是数据的维度相容
    model = models.Sequential()  # 这是一个顺序网络
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(32, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    # 把多维向量拉平的类，自己多动脑经，印象深刻.
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    #  有了框架后，搭建这个网络就是这么快。
    return model


def train():
    # 所有的训练部分放在此处
    # 回顾一下训练的流程：1、加载数据。2、生成网络。3、运行代码
    train_dir = r'E:\Data\cat-and-dog\training_set'
    test_dir = r'E:\Data\cat-and-dog\test_set'

    train_data = ImageDataGenerator(rescale=1. / 255)
    test_data = ImageDataGenerator(rescale=1. / 255)

    train_data_gen = train_data.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary'
    )
    test_data_gen = test_data.flow_from_directory(
        test_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary'
    )
    model = conv()  # 我只是给这个网络加入了一些信息，在调用方法还是框架的
    #  指定网络的优化器，损失函数等。
    model.compile(optimizer=optimizers.RMSprop(lr=1e-4), loss='binary_crossentropy', metrics=['acc'])
    history = model.fit_generator(train_data_gen, steps_per_epoch=250, epochs=50, validation_data=test_data_gen,
                                  validation_steps=50)  # validation_steps是什么意思？

    print(history.history['acc'])
    # 要把训练好的模型保存下来，这是经过很长时间的计算的到的参数，不是运行完了就没事了。
    model.save("cat_and_dog_small.h5")
    #  保存之后怎么用的问题？

train()
