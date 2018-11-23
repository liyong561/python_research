import numpy as np
from keras.datasets import mnist
from simple_net import SimpleNet
import matplotlib.pyplot as plot


def one_hot(x):
    m = np.zeros((x.size, 10), dtype=int)
    m[np.arange(x.size), x] = 1  # don't use for
    return m


(x_train, t_train), (x_test, t_test) = mnist.load_data()
t_train_one_hot = one_hot(t_train)
t_test_one_hot = one_hot(t_test)
x_train_reshape = x_train.reshape(60000, 784)
x_test_reshape = x_test.reshape(10000, 784)  # 将之转化为我想要的数据格式

train_loss_list = []
iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
rate = 0.1

network = SimpleNet(input_size=784, hidden_size=50, output_size=10)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train_reshape[batch_mask]  # little bracket is using  function
    t_batch = t_train_one_hot[batch_mask]  # 在样本中随机选择一小撮
    grads = network.numerical_gradient(x_batch, t_batch)
    for key in ('w1', 'b1', 'w2', 'b2'):
        network.param[key] -= rate * grads[key]  # 对参数进行了调整,发现梯度值太小
    loss = network.loss_function(x_batch, t_batch)
    print(loss)
    train_loss_list.append(loss)
    print(network.accuracy(x_batch, t_batch))  # 是随机概率，根本就没有提高

y = np.array(train_loss_list)
x = np.array(range(len(train_loss_list)))
plot.plot(x, y)
plot.show()
