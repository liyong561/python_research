# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import affine
from multi_layer_net import MultiLayerNet
import matplotlib.pyplot as plot
import optimizer as op
(images_train,labels_train),(images_test,labels_test) = affine.process()
# 选取训练数据的前300条，训练样本过少
images_train = images_train[:300]
labels_train = labels_train[:300]
accuracy_list=[]
iters_num=100000
train_size=images_train.shape[0]
batch_size=100
max_epoch =201 # 准确度计算200次
iter_per_epoch = train_size / batch_size # 想想着代表什么意思
epoch_cnt = 0
# rate=0.1 在优化器中不用了
#网络初始化
optimizer = dict()  # 内置函数名。
train_loss = dict()
network = dict() # 对象初始化化，或者说变量初始化
optimizer['sgd'] = op.Sgd()
optimizer['adaGrad'] = op.AdaGrad()
optimizer['momentu'] = op.Momentu() 
# 5层神经网络,对最后的一层神经元有个数要求
network = MultiLayerNet(input_size=784,hidden_size_list=[100,100,100,100,10],output_size=10)
train_loss= [] # 
itetrain_accuracy = []
train_accuracy = []
test_accuracy = []


for i in range(iters_num):
	batch_mask=np.random.choice(train_size,batch_size)
	x_batch=images_train[batch_mask] 
	t_batch=labels_train[batch_mask]  #在样本中随机选择
	grads = dict()
	grads['dW'],grads['db']=network.gradient(x_batch,t_batch)
	optimizer['sgd'].update(network.W,grads['dW'])  #多层过程直接拿掉了param,而直接使用W,b
	optimizer['sgd'].update(network.b,grads['db'])
	loss_value=network.loss(x_batch,t_batch)
	train_loss.append(loss_value)
	
	if i% iter_per_epoch ==0:
		train_acc = network.accuracy(images_train,labels_train)
		test_acc = network.accuracy(images_test, labels_test)
		train_accuracy.append(train_acc)
		test_accuracy.append(test_acc)
		epoch_cnt +=1
		if epoch_cnt >= max_epoch:
			break
x = np.arange(len(train_accuracy))
plot.plot(x,train_accuracy,test_accuracy)
plot.show()
