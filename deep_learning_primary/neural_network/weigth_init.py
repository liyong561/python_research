# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt
def sigmoid(x):
	return 1/(np.exp(-x)+1) # 既可以对数值变量计算，还可以对向量进行计算

x = np.random.randn(1000,100) # 1000组数据

node_num = 100

hidden_layer_size = 5

activations = dict() # 在数字索引时和列表一样

# 开始逐层迭代运算，主要是我对绘图函数还是不熟悉

for i in range(hidden_layer_size):
	if i !=0:
		x = activations[i-1]
	# w = np.random.randn(node_num,node_num) *1
	w = np.random.randn(node_num,node_num) *0.01
	z=np.dot(x,w)
	z= sigmoid(z)
	activations[i]=z
# 开始根据activations绘图
plt.rcParams['figure.figsize']=(10,5)
#plt.rcParams['figure.dpi'] = 300
for i,a in activations.items():
	plt.subplot(1,len(activations),i+1)
	plt.title(str(i+1)+"layer")
	plt.hist(a.flatten(),30,range=(0,1))
plt.show()