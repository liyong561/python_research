import numpy as np
#这些优化器函数相当于过滤器，不需要返回值，直接在原基础上修改即可
class Sgd:
	#梯度下降的数学公式:x=-n(dx/de)
	def __init__(self, lr=0.01):
		self.lr =lr
	def update(self, params ,grads):
		for key in params.keys():
			params[key] -= self.lr * grads[key]

class AdaGrad:
	def __init__(self,lr=0.01):
		self.lr =lr
		self.h = None
	def update(self, params, grads): #吧单词写对
		if self.h is None:
			self.h= dict()
			for key ,val in params.items():
				self.h[key]= np.zeros_like(val)
				
		for key in params.keys():
			# 逐元素相乘
			self.h[key] += grads[key] * grads[key]
			# 这些参数大小还是应该考虑的
			params[key] -= self.lr * grads[key] /(np.sqrt(self.h[key])+1e-7)

class Momentu:
	# 动量方法
	def __init__(self, lr = 0.1,momentum =0.9):
		self.lr = lr
		self.v =None
		self.momentum = momentum
	def update(self, params, grads):
		if self.v is None:
			self.v = dict()
			# iterms是一个列表，列表是可迭代的
			for key,val in params.items():
				self.v[key] = np.zeros_like(val) #理解这句话的意思
		for key in params.keys():
			self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
			params[key] += self.v[key]

