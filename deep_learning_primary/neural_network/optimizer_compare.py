# -*- coding: utf-8 -*-
import numpy as np
import affine
from two_layer_net import TwoLayerNet
import matplotlib.pyplot as plot
import optimizer as op
(images_train,labels_train),(imags_test,labels_test) = affine.process()
accuracy_list=[]
iters_num=1000
train_size=images_train.shape[0]
batch_size=100
# rate=0.1 在优化器中不用了
#网络初始化
optimizer = dict()  # 内置函数名。
train_loss = dict()
network = dict() # 对象初始化化，或者说变量初始化
optimizer['sgd'] = op.Sgd()
optimizer['adaGrad'] = op.AdaGrad()
optimizer['momentu'] = op.Momentu() 
for key in optimizer.keys():
	network[key] = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
	train_loss[key] = [] # 
'''sgd = op.Sgd() 类型较多可以说考虑使用python中的字典
adagrid = op.AdaGrad()  :前后单词都不一样
momentu = op.Momentu()'''

# 一个优化器依次训练的,所以每次选取的数据是随机的，但是数据量大，在统计上还是能看出差别的
for key in optimizer.keys():
	for i in range(iters_num):
		batch_mask=np.random.choice(train_size,batch_size)
		x_batch=images_train[batch_mask] 
		t_batch=labels_train[batch_mask]  #在样本中随机选择
		grads=network[key].gradient(x_batch,t_batch)
		optimizer[key].update(network[key].param,grads)
		loss_value=network[key].loss(x_batch,t_batch)
		train_loss[key].append(loss_value)
		
# 相互关联的，sgd，momentu名字不能随便取
labels = {'sgd':'o','momentu':'x','adaGrad':'D'}  
x=range(len(train_loss[key]))
for key in optimizer.keys():
	plot.plot(x,train_loss[key],marker = labels[key],markevery=100,label= key)   # 标志都是固定的
plot.legend()
plot.show()

