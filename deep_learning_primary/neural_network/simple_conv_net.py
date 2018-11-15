from collections import OrderedDict
import cnn_layer as cnn
import affine 
import numpy as np

class SimpleConvNet:
	# 将各层组装起来,将各层参数变成实例变量。
	# 为了减小参数，filter的h和x
	def __init__(self,input_dim= (1,28,28),
			  conv_param={'filter_num':30,'filter_size':5,'pad':0,'stride':1},
			  hidden_size =100,output_size=10,weight_init= 0.01):
		# 学习这些python的编程规范和思想
		filter_num = conv_param['filter_num']
		filter_size = conv_param['filter_size']
		filter_pad = conv_param['pad']
		filter_stride = conv_param['stride']
		input_size = input_dim[1]
		conv_output_size = (input_size - filter_size +2*filter_pad)//filter_stride+1
		# 不知道这个参数有什么用？
		pool_output_size = int((filter_num*(conv_output_size/2)*(conv_output_size/2)))
		# 需要int这个函数，中间出现了除法
		self.params= {}
		#  这里就看出W的形状了
		self.params['W1'] =weight_init*np.random.randn(filter_num,input_dim[0],
			 filter_size,filter_size)
		self.params['b1'] = np.zeros(filter_num)
		self.params['W2'] = weight_init*np.random.randn(pool_output_size,hidden_size)
		self.params['b2'] = np.zeros(hidden_size)
		self.params['W3'] = weight_init*np.random.rand(hidden_size,output_size)
		self.params['b3'] = np.zeros(output_size)
		# |一个卷积层，两个全连接层
		self.layers = OrderedDict()
		self.layers['Conv1'] = cnn.Convelution(self.params['W1'],self.params['b1'],
			 conv_param['stride'],conv_param['pad'])
		self.layers['Relu1']=affine.ReLu()
		self.layers['Pool1'] = cnn.Pooling(pool_h=2,pool_w =2,stride =2) # 单独定制
		self.layers['Affine1'] = affine.Affine(self.params['W2'],self.params['b2'])
		self.layers['Relu2'] = affine.ReLu()
		self.layers['Affine2']= affine.Affine(self.params['W3'],self.params['b3'])
		self.last_layer =affine.SoftmaxWithLoss() # 该层用于计算损失函数
		
	# 当各层装配好后，预测很容易
	def predict(self,x):
		for layer in self.layers.values():
			# 可能对于不同的层，输入数据维度不一样
			x = layer.forward(x)
		return x
	
	def loss(self,x,t):
		y = self.predict(x)
		#  思考一下，要对y进行处理吗
		return self.last_layer.forward(y,t)
	# x 是输入数据，t是标签
	def accuracy(self,x,t,batch_size=100):
		# 如果不是one -hot数据，则转换为onehot数据
		if t.ndim !=1:
			t= np.argmax(t,axis=1)
		acc =0.0
		# 在x中随机选择一批数据。
		for  i in range(int(x.shape[0]/batch_size)):
			tx = x[i*batch_size:(i+1)*batch_size]
			tt = t[i*batch_size:(i+1)*batch_size]
			y =self.predict(tx)
			y = np.argmax(y,axis=1)
			acc += np.sum(y==tt)
		return acc/x.shape[0]
	# 求各个参数的梯度，也就是求导
	def gradient(self,x,t):
		self.loss(x,t) #对参数初始化一次
		dout =1
		dout = self.last_layer.backward(dout)
		
		layers = list(self.layers.values())
		layers.reverse()
		for layer in layers:
			dout = layer.backward(dout)
		grads = dict()
		# 从每层取出梯度值
		grads['W1'],grads['b1'] = self.layers['Conv1'].dW,self.layers['Conv1'].db
		# 特别注意dw的取值
		grads['W2'],grads['b2'] = self.layers['Affine1'].dw,self.layers['Affine1'].db
		grads['W3'],grads['b3'] = self.layers['Affine2'].dw,self.layers['Affine2'].db
		return grads
	
	