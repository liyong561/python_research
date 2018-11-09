# -*- coding: utf-8 -*
import affine
import numpy as np
class MultiLayerNet:
	
	def __init__(self,input_size,hidden_size_list,output_size,weight_init=0.01):
		
		self.hidden_size_list = hidden_size_list # 保存后其他实例方法可用
		self.W ,self.dW,self.b,self.db,self.layers=dict(),dict(),dict(),dict(),dict()
		self.relu = affine.ReLu()
		self.softmaxWithLoss = affine.SoftmaxWithLoss() 
		# 高斯分布默认是float类型
		self.W[0] = np.random.randn(input_size,hidden_size_list[0]) * weight_init
		self.b[0] = np.zeros(hidden_size_list[0],dtype=float)
		self.layers[0] = affine.Affine(self.W[0], self.b[0])
		
		for i in range(len(hidden_size_list)-1):
			
			self.W[i+1] = np.random.randn(hidden_size_list[i],hidden_size_list[i+1])
			self.b[i+1] = np.zeros(hidden_size_list[i+1],dtype=float)
			self.layers[i+1] = affine.Affine(self.W[i+1], self.b[i+1])
	# 预测函数
	def predict(self,x):  # 方法传递过来的值是否可以直接用？
		# x= x
		i = 0
		for i in range(len(self.hidden_size_list)-1):
			x = self.layers[i].forward(x)
			self.relu = affine.ReLu()
		x = self.layers[i+1].forward(x)
		return x
	
	# bp计算梯度,要知道反向输入值，也就是损失函数值
	def loss(self, x, t):
		x = self.predict(x)
		loss = self.softmaxWithLoss.forward(x, t)
		return loss
	
	# 每一次样本训练时，其梯度值都是不一样的,
	def gradient(self,x,t):
		# 调用softmaxWithLoss(self,x,t),最后的值要保存在该层中
		y = self.predict(x)
		self.softmaxWithLoss.forward(y,t) # y 值已经保存在这个对象中了，反向传播时使用
		#求梯度，输入值应该为1
		y = self.softmaxWithLoss.backward() # 最后一层传入的值为1
		length = len(self.layers)
		# 逐层循环
		for i  in range(length-1):
			y = self.layers[length-1-i].backward(y)
			self.dW[length-1-i] = self.layers[length-1-i].dw  #遵循之前的大小写
			self.db[length-1-i] = self.layers[length-1-i].db
			self.relu.backward(y)
		self.layers[0].backward(y)
		self.dW[0] = self.layers[0].dw
		self.db[0] = self.layers[0].db
		return self.dW,self.db   #我是怎么返回grad的，就怎么调用
	
	# 作为补充，写一个计算准确度的函数，时不需要计算损失函数值
	def accuracy(self,x,t):
		y = self.predict(x)
		y = np.argmax(y,axis = 1) #两个y的含义应该不同
		t = np.argmax(t,axis = 1) # 改变了原始数据
		return np.sum(y==t)/float(t.shape[0])
		
		