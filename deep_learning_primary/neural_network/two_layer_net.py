import numpy as np
import affine
from collections import OrderedDict

class TwoLayerNet:
	def __init__(self,input_size,hidden_size,output_size,weigth_init=0.01):
		self.param={} #对象应该带有哪些属性
		self.param['w1']=weigth_init*np.random.randn(input_size,hidden_size)
		self.param['b1']=np.zeros(hidden_size)
		self.param['w2']=weigth_init*np.random.randn(hidden_size,output_size)
		self.param['b2']=np.zeros(output_size)
		
		self.layers=OrderedDict()
		self.layers['Affine1']=affine.Affine(self.param['w1'],self.param['b1'])
		self.layers['ReLu1']=affine.ReLu()
		self.layers['Affine2']=affine.Affine(self.param['w2'],self.param['b2'])
		self.lastLayer=affine.SoftmaxWithLoss()
		
	def predict(self,x):
		self.layers['Affine1'].w=self.param['w1']
		self.layers['Affine1'].b=self.param['b1']
		self.layers['Affine2'].w=self.param['w2']
		self.layers['Affine2'].b=self.param['b2']
		for layer in self.layers.values():
			x=layer.forward(x) # 调用封装好的层
		return x
	def loss(self,x,t):
		y=self.predict(x)
		loss_value=self.lastLayer.forward(y,t)
		return loss_value
	def accuracy(self,x,t):
		y=self.predict(x)
		y=np.argmax(y,axis=1)
		if t.ndim!=1: # 如果t不是one-hot数据，则转换
			t=np.argmax(t,axis=1)
		accuracy=np.sum(y==t)/float(t.shape[0]) # 防止整除，保留了小数部分
		return accuracy
	def gradient(self,x,t):
		# 正向传播
		self.loss(x,t)
		#反向传播
		dout=1
		dout=self.lastLayer.backward(dout)
		layers=list(self.layers.values())
		layers.reverse()
		for layer in layers:
			dout=layer.backward(dout)
			#print(dout)
			#print("dout")
		grads={}
		grads['w1']=self.layers['Affine1'].dw
		# print(grads['w1']其梯度值为零
		grads['w2']=self.layers['Affine2'].dw
		grads['b1']=self.layers['Affine1'].db
		grads['b2']=self.layers['Affine2'].db
		
		return grads