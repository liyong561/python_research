import numpy as np
class Affine:
	def __init__(self,w,b):
		self.w=w
		self.b=b
		self.x=None
		self.db=None  #其导数，要输出的
		self.dw=None
	def forward(self,x):
		self.x=x
		out=np.dot(x,self.w)+self.b # 和java的差别，对象变量都要带上self
		return out
	def backward(self,dout):
		dx=np.dot(dout,self.w.T)
		self.dw=np.dot(self.x.T,dout)
		self.db=np.sum(dout,axis=0)
		return dx #why return this?
w=np.random.randn(3,2)
b=np.random.randn(2)
affine=Affine(w,b)
x=np.random.randn(4,3)
print(affine.forward(x))