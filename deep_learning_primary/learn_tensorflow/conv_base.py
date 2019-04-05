from keras.applications import VGG16
from keras.preprocessing import image
from keras import models
from keras import layers
import numpy as np
from keras import optimizers
import matplotlib.pyplot as plt


def conv():
    #  使用数据增强的特征提取
    #  这种方法虽然没有更改权重，但是数据还是跑了一个来回，还是很费时间
    model = models.Sequential()
    #  理解这些参数的意思，现在我就不用从头训练卷积层了
    conv_base = VGG16(weight='imagenet', include_top=False, input_shape=(150, 150, 3))
    conv_base.trainable = False  # 不更改其权重。
    model.add(conv_base)
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))


def extract_feature(directory, sample_count):
    #  VGG16总共有200多万个参数，从github上下载。
    conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))
    datagen = image.ImageDataGenerator(rescale=1. / 255)
    batch_size = 30
    features = np.zeros(shape=(sample_count, 4, 4, 512))
    labels = np.zeros(sample_count)
    generator = datagen.flow_from_directory(
        directory, target_size=(150, 150), batch_size=batch_size, class_mode='binary'
    )
    i = 0
    for images_batch, labels_batch in generator:
        #  predict应该很费时间。
        features_batch = conv_base.predict(images_batch)
        #  could not broadcast input array from shape (30,4,4,512) into shape (10,4,4,512)
        #  这里为什么会抱这样的错误？10我从来都没有定义过
        #  运行很费时间，没有调对，不能运行
        # 133
        # (10, 4, 4, 512)
        print(i)  # 这个i可以看进度
        features[i * batch_size:(i + 1) * batch_size] = features_batch
        labels[i * batch_size:(i + 1) * batch_size] = labels_batch
        i += 1
        if (i + 1) * batch_size >= sample_count:
            break
        # 从这里看相当于对数据进行了预处理。
    return features, labels


def train():
    train_data_dir = r'E:\Data\cat-and-dog\training_set'
    test_data_dir = r'E:\Data\cat-and-dog\test_set'
    #  将数据经过卷积层的运算后结果输出。
    train_features, train_labels = extract_feature(train_data_dir, 4000)
    train_features = np.reshape(train_features, (4000, 4 * 4 * 512))
    test_features, test_labels = extract_feature(test_data_dir, 1000)
    test_features = np.reshape(test_features, (1000, 4 * 4 * 512))

    model = models.Sequential()
    model.add(layers.Dense(256, activation='relu', input_dim=4 * 4 * 512))  # 第一层网络要定义输入数据的特征
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))
    # 1e-4没有空格，注意一下格式。
    model.compile(optimizer=optimizers.RMSprop(lr=1e-4), loss='binary_crossentropy',
                  metrics=['acc'])
    history = model.fit(train_features, train_labels, batch_size=30, epochs=30,
                        validation_data=(test_features, test_labels))
    return history


def visualize_result():
    #  最后一步， 绘制图表，展现结果
    history = train()
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    #  绘制精度图
    plt.plot(epochs, acc, 'bo', label='Train acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')

    #  绘制损失函数值图
    plt.figure()

    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()


visualize_result()
