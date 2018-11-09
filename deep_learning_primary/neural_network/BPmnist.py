import numpy as np
import affine
from two_layer_net import TwoLayerNet
import matplotlib.pyplot as plot
import optimizer as op
(images_train,labels_train),(imags_test,labels_test) = affine.process()
train_loss_list=[]
accuracy_list=[]
iters_num=1000
train_size=images_train.shape[0]
batch_size=100
rate=0.01
#网络初始化
network=TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
optimizer = op.Sgd()
for i in range(iters_num):
	batch_mask=np.random.choice(train_size,batch_size)
	x_batch=images_train[batch_mask]  #little bracket is using  function
	t_batch=labels_train[batch_mask]  #在样本中随机选择一小撮
	grads=network.gradient(x_batch,t_batch)
	optimizer.update(network.param,grads)
	# print(loss_value)
	loss_value=network.loss(x_batch,t_batch)
	train_loss_list.append(loss_value)
	accuracy_list.append(network.accuracy(x_batch,t_batch))
	 # 是随机概率，根本就没有提高
y=np.array(accuracy_list)
x=range(len(accuracy_list))
plot.plot(x,y)
plot.show()
