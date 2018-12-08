import urllib3
import gzip
import numpy as np
import pickle


#  import zipfile  专门处理zip文件，不处理.gz文件
#  并将读取好的格式数据，存储为对象

def data_test():
    http = urllib3.PoolManager()
    url = 'http://yann.lecun.com/exdb/mnist/'
    resources = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz'
        , 't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz']

    for i in range(len(resources)):
        resp = http.request('GET', url=url + resources[i])
        # print(resp.status) ,resp应该是一个对象，还有content等属性,HttpResponse对象

        with open('my_load/' + resources[i], 'wb') as f:
            # 是什么格式文件就存成什么格式文件，否则打不开
            # data = gzip.decompress(resp.data)  # 直接解压.gz文件
            f.write(resp.data)  # 下载得到是.gz文件，要使用一定的规则读取

        with gzip.open('my_load/' + resources[i], 'rb') as f:
            with open('my_load/' + resources[i].split('.')[0], 'wb') as f1:
                f1.write(f.read())


def load_data(file_name, offset, size):  # 这个读取函数是和idx1-ubyte的格式相关的。
    #  根据起始值和unit的大小读取
    with gzip.open('my_load/' + file_name, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=offset)
    data = data.reshape(-1, size)
    return data


def data_tensor():  # 重复的操作就需要定义一格函数
    resources = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz'
        , 't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz']

    dataset = dict()  # 将所有数据存储为一个字典对象，然后存储为hdf5文件
    dataset['train_img'] = load_data(resources[0], 16, 784)
    dataset['train_label'] = load_data(resources[1], 8, 1)  # 784个像素对应于一个标签，显然不是one_hot数据
    dataset['test_img'] = load_data(resources[2], 16, 784)
    dataset['test_label'] = load_data(resources[3], 8, 1)
    with open('mnist.pkl', 'wb') as f:
        pickle.dump(dataset, f)  # 后一个参数不要，好像没有什么影响


# data_tensor()  已经存好了，现在我取出这个对象
def display_data():
    with open('mnist.pkl','rb') as f:   # 还需要打开方式，否则出错。
        dataset = pickle.load(f)
    train_img = dataset['train_img']
    print(train_img.shape)


display_data()