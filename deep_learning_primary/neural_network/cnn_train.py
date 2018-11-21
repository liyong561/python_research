# -*- coding: utf-8 -*-
# 相比于BP_trian,这个要传递的参数多一些吧
from keras.datasets import mnist
from simple_conv_net import SimpleConvNet
import  matplotlib.pyplot as plot 
import pickle

(image_train,label_train),(image_test,label_test) = mnist.load_data() 
# image_trian.shape=(6000,28,28)，要给数据增加一个维度
#  就可以直接使用这么短小的名字
# 有处理非one-hot的情况
# image_train /=256 对于迭代元素,这么写好像不合适
#  image_train =image_train/256 这样不能学习了
# image_test =image_test/256
shape_image1= image_train.shape
shape_image2 = image_test.shape
image_train =image_train.reshape(1,shape_image1[0],shape_image1[1],shape_image1[2]).transpose(1,0,2,3)
image_test =image_test.reshape(1,shape_image2[0],shape_image2[1],shape_image2[2]).transpose(1,0,2,3)
network = SimpleConvNet(input_dim=(1,28,28),
						conv_param= {'filter_num':30,'filter_size':5,'pad':0,'stride':1},
						hidden_size =100,output_size=10,weight_init=0.01)
# 加载数据，然后训练。
batch_size =100
iter_num = 100  # 每次100,训练所有数据
accuracy_list =[] #暂时只统计准确度,这个是训练时的
rate =0.01 # 学习率，非常重要的参数
for i in range(iter_num):
	# print("there are "+str(iter_num)+",this is "+str(i))
	# 可以向用户显示进度
	x = image_train[i*batch_size:(i+1)*batch_size]
	t = label_train[i*batch_size:(i+1)*batch_size]
	grads = network.gradient(x,t)
	#  就使用sgd
	for key in network.params.keys():
		# 将所有的参数放在param中
		network.params[key] -=rate*grads[key]
		#print(key,network.params[key].shape,grads[key].shape)
	acc = network.accuracy(x,t)
	accuracy_list.append(acc)
# 训练完之后将得到的参数持久化
with open('w1_file.pkl','wb') as f:
	# 取出时不用名字，按顺序取就可以了
	pickle.dump(network.params['W1'],f)
plot.plot(range(len(accuracy_list)),accuracy_list)
plot.show()
print(accuracy_list[50:])