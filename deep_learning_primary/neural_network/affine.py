import numpy as np
import keras.datasets.mnist as mnist
# 这一层，既有正向传播，又有反向传播
def one_hot(x):
	# m[np.arange(x.size),10]=0 # 0,1可能造成类型歧义，需要明确规定,m还是要define
	# m = np.zeros(np.arange(x.size), 10) dimension 大于32 
	m = np.zeros((x.size,10),dtype=int)
	m[np.arange(x.size),x]=1
	return m
def softmax(x):
	y=np.max(x,axis=1)
	y=x.T-y 
	z=np.exp(y)/np.sum(np.exp(y),axis=0) #让人有点晕
	return z.T
def cross_entropy_error(y,t):
	# 还要考虑t不是one-hot数据 
	if y.ndim ==1: #一般情况下y.ndim ==2
		t=t.reshape(1,t.size)
		y=y.reshape(1,y.size)
	batch_size=t.shape[0]
	# 
	return -np.sum(np.log(y[np.arange(batch_size),t]+1e-7))/batch_size
def process():
	(images_train,labels_train),(images_test,labels_test) = mnist.load_data()
	# images_train.astype(np.float32),对象本身不会变
	images_train = images_train.astype(np.float32)
	images_test = images_test.astype(np.float32)
	images_train /= 256
	images_test /= 256  # 要对像素值进行正则化
	images_train = images_train.reshape(60000,784)
	images_test = images_test.reshape(10000,784)
	labels_train = one_hot(labels_train)
	labels_test = one_hot(labels_test)
	return (images_train,labels_train),(images_test,labels_test) 
	
class Affine:
	def __init__(self,w,b):
		self.w=w
		self.b=b
		self.x=None
		self.origin_x_shape=None
		self.db=None  #其导数，要输出的
		self.dw=None
	def forward(self,x): #x没有被初始化，更改成能处理4维张量的
		# print(x.shape),传递的shape变成了1d
		self.origin_x_shape =x.shape
		x = x.reshape(x.shape[0],-1) # 将其变形
		self.x=x
		out=np.dot(x,self.w)+self.b # 和java的差别，对象变量都要带上self,b not def
		return out
	   #np.random.randn(100,50)
	def backward(self,dout):
		dx=np.dot(dout,self.w.T)
		self.dw=np.dot(self.x.T,dout) #要返回的导数
		self.db=np.sum(dout,axis=0)
		dx = dx.reshape(*self.origin_x_shape)
		return dx #why return this?
class ReLu:
	def __init__(self):
		self.mask=None
	def forward(self,x):
		# 逐元素运算，对与任意维的张量都是可以的。
		self.mask=(x<=0)
		out=x.copy()
		out[self.mask]=0
		return out
	def backward(self,dout):
		dout[self.mask]=0
		dx=dout
		return dx  #感叹python语句真的不能再简单方便了
class SoftmaxWithLoss:
	def __init__(self):  # 放在这里的参数都是要初始化的
		self.loss=None
		self.x=None
		self.y=None
	def forward(self,x,t):  #传入的是得分
		self.y=softmax(x)
		self.t=t # backward时用到
		self.loss=cross_entropy_error(self.y,self.t)
		return self.loss # 想想为什么返回loss
	def backward(self,dout=1):
		batch_size=self.t.shape[0]
		if self.t.size ==self.y.size:
			dx = (self.y -self.t)/batch_size # 提高代码的健壮性
		else:  # 返回不是onehot的数据
			dx = self.y.copy()
			dx[np.arange(batch_size),self.t] -=1  
			dx =dx /batch_size
		return dx 
		