import numpy as np;
# softmax:将其值映射成概率分布。
def softmax_1d(x):
	c=np.max(x)
	exp_a=np.exp(x-c)
	return exp_a/sum(exp_a) #这是一个数和一维张量运算。sum函数直接降到了一维
def softmax_2d(x): #适用于2d张量
	y=np.max(x,axis=1)
	x=x.T-y
	x2=x.T
	x1=np.exp(x)/np.sum(np.exp(x2),axis=1)
	x1=x1.T                                                                           
	return x1
def numerical_diff(f,x): # 能不能适应x是二维向量的情况？
	grad=np.zeros_like(x)
	h=1e-4
	# for i in range(x.size): # 为什么说越界，这里是没有问题
	it=np.nditer(x,flags=['multi_index'],op_flags=['readwrite'])
	while not it.finished: 
		idx=it.multi_index # 可以获得元素的脚标，很方便
		temp=x[idx]
		x[idx]=float(temp)+h #有了这个迭代器，找到下脚标，非常方便。
		f2=f(x)
		x[idx]=float(temp)-h
		f1=f(x)
		grad[idx]=(f2-f1)/(2*h)
		x[idx]=temp
		it.iternext()
	return grad
def sigmoid(x):
	return 1/(1+np.exp(-x))
class SimpleNet:
	def __init__(self,input_size,hidden_size,output_size,weight_init=0.01):
		#已经规定了网络的层数，只有每层个数可以自己决定
		self.param={}
		self.param['w1']=weight_init*np.random.randn(input_size,hidden_size)
		self.param['b1']=np.zeros(hidden_size)
		self.param['w2']=weight_init*np.random.randn(hidden_size,output_size)
		self.param['b2']=np.zeros(output_size)
	def predict(self,x):#给定输入，给出输出
		w1,w2=self.param['w1'],self.param['w2']
		b1,b2=self.param['b1'],self.param['b2']
		z=np.dot(x,w1)+b1 # 进行了广播
		z1=sigmoid(z)
		z2=np.dot(z1,w2)+b2
		z3=softmax_2d(z2) #直接将结果映射成概率
		return z3
	def cross_entropy_error(self,y,t): #多个样本
		if y.ndim==1:
			t=t.reshape(1,t.size)
			y=y.reshape(1,y.size)
		count=y.shape[0]
		return -np.sum(t*np.log(y+1e-7))/count #这个sum的用法
	def loss_function(self,x,t):  # 损失函数,x,t是不变的，由样本决定，我们要找的是其映射关系
		z=self.predict(x)
		#y=softmax(z)
		#print(y)
		loss=self.cross_entropy_error(z,t)
		return loss
	def accuracy(self,x,t): # 计算正确率
		y=self.predict(x)
		y=np.argmax(y,axis=1) #关于轴的选择问题
		t=np.argmax(t,axis=1)
		accuracy=np.sum(y==t)/float(x.shape[0])
		return accuracy
	def numerical_gradient(self,x,t): # 损失函数在某点，相对于任意变量的梯度。
		def loss_w(w): # 这个w是伪参数，后面根本没用到
			return self.loss_function(x,t)
		grads={}
		grads['w1']=numerical_diff(loss_w,self.param['w1'])
		# 想想能不能计算出数值梯度值，更改了对象的值，会重新计算一遍结果
		grads['b1']=numerical_diff(loss_w,self.param['b1'])
		grads['w2']=numerical_diff(loss_w,self.param['w2'])
		grads['b2']=numerical_diff(loss_w,self.param['b2'])
		return grads
		