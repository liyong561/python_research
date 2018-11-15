# -*- coding: utf-8 -*-
import numpy as np

def im2col(input_data,filter_h,filter_w,stride=1,pad=0):
	#输出的维度是由上面的决定的
	N,C,H,W = input_data.shape
	out_h = (H + 2*pad -filter_h)//stride +1
	out_w = (W + 2*pad -filter_w)//stride +1
	img = np.pad(input_data,((0,0),(0,0),(pad,pad),(pad,pad)),'constant')
	col = np.zeros((N,C,filter_h,filter_w,out_h,out_w))
	for y in range(filter_h):
		y_max = y + out_h *stride
		for x in range(filter_w):
			x_max = x + out_w *stride
			# 这个操作反过来吧。
			col[:,:,y,x,:,:]= img[:,:,y:y_max:stride,x:x_max:stride]
	col = col.transpose(0,4,5,1,2,3).reshape(N*out_h*out_w,-1)
	return col
	# (c*fh*fw,n*oh*ow),col转化为4D数据,col还有数据冗余.dd

def col2im(col, input_shape, filter_h, filter_w, stride=1, pad=0):
	N,C,H,W = input_shape  #参数传递出来的是一个元组。
	out_h =(H + 2*pad -filter_h)//stride + 1
	out_w =(W + 2*pad -filter_w)//stride + 1
	col= col.reshape(N,out_h,out_w,C,filter_h,filter_w).transpose(0,3,4,5,1,2)
	#为什么还要加步长呢？
	img = np.zeros((N,C,H+ 2*pad +stride -1,W + 2*pad +stride -1))
	# img = np.zeros(N,C,H+2*pading,W)
	for y in range(filter_h):
		y_max = y + out_h *stride
		for x in range(filter_w):
			x_max = x + out_w *stride
			#逆过程，非常不好理解
			img[:,:,y:y_max:stride,x:x_max:stride] =col[:,:,y,x,:,:]
	return img[:,:,pad:H+pad,pad:W+pad] 
# 使用im2col实现卷积层
class Convelution:
	def __init__(self,W,b,stride=1,pad=0):
		#w就是filter，相当于full-connected的权重
		# 和全连接层的参数命名一样,只是维度不一样
		self.W = W
		self.b =b
		self.stride =stride 
		self.pad = pad
		#  应该就是申明一下变量，没有别的意思。
		self.x = None
		self.col = None
		self.col_w = None
		# 注意这里输入的变量为4D的图像数据。
		self.dW =None
		self.db =None
	def forward(self,x):
		self.x =x
		N,C,H,W = x.shape
		# self.N,self.C,H,Width = X.shape,这样随意设置实例变量非常不是编码习惯
		FN, C,FH,FW = self.W.shape  #出现了两个C，会覆盖吧
		# filter_h = self.W.shape[2]
		# filter_w = self.W.shape[3]
		self.out_h = (H+ 2*self.pad -FH)//self.stride +1
		self.out_w = (W+ 2*self.pad -FW)//self.stride +1
		# self.col.shape=(N*oh*ow,c*fh*fw)
		self.col = im2col(x,FH,FW,self.stride,self.pad)
		# W = self.W.transpose(1,2,3,0).reshape(),这种写法确实有些臃肿
		self.col_W = self.W.reshape(FN,-1).T #W 的矩阵化很简单
		out = np.dot(self.col,self.col_W) +self.b #对b进行广播
		# 理解这个为什么分两步走（N,Oh,ow,fn)
		out = out.reshape(N,self.out_h,self.out_w,-1).transpose(0,3,1,2)
		return out
	#反向传播的函数
	def backward(self,dout):
		FN,C,FH,FW = self.W.shape # 虽然有些参数不用，但是也要列出来
		dout =dout.transpose(0,2,3,1).reshape(-1,FN)  # 其逆过程
		self.db = np.sum(dout,axis =0)  # 对所有求和
		#dx 和dx都要计算
		self.dW = np.dot(self.col.T,dout)
		self.dW = self.dW.transpose(1,0).reshape(FN,C,FH,FW)
	#np.dot(self.col.T,dout).transpose(1,0).reshape(self.fn,self.C,self.filter_h,self.filter_w)
		dx = np.dot(dout,self.col_W.T)#这个维度大于4，要转化成img
		# col2im(dx,self.x.shape,FH,FW,self.stride=1,self.pad =0),
		# 这是在写啥，混在一起了
		dx = col2im(dx,self.x.shape,FH,FW,stride=1,pad =0)
		return dx
class Pooling:
	def __init__(self,pool_h,pool_w,stride=1,pad=0):
		self.pool_h = pool_h
		self.pool_w = pool_w
		self.stride = stride 
		self.pad =pad 
		self.x=None
		self.arg_max = None # 都是在反向传播时会用
	def forward(self,x):
		self.x =x
		N,C,H,W = x.shape
		# stride，不应该为1,否则意义不大 
		out_h = int(1+(H-self.pool_h)/self.stride)
		out_w = int(1+(W -self.pool_w)/self.stride)
		# 和卷积的处理有点稍微不同,但也是展开成矩阵，且元素间存在重叠
		col= im2col(x,self.pool_h,self.pool_w,self.stride,self.pad)
		# 取最大值是需要根据通道再切分。
		col = col.reshape(-1,self.pool_h*self.pool_w)
		self.arg_max = np.argmax(col,axis=1) 
		out = np.max(col,axis=1)
		# 理解reshape的顺序，结合变换图来理解。由那个图就知道了，最后划分通道。
		out=out.reshape(N,out_h,out_w,C).transpose(0,3,1,2)
		return out
	def backward(self,dout):
		dout  = dout.transpose(0,2,3,1)
		pool_size = self.pool_h*self.pool_w
		# 构造一个矩阵用于返回
		dmax = np.zeros((dout.size,pool_size))
		# arg_max为什么药展开？,先将其广播成相同维度，然后在依次对应,在这里，展开和不展开没有影响
		dmax[np.arange(self.arg_max.size),self.arg_max.flatten()]= dout.flatten()
		# 这里和原文不一样,这样是错的，还要把通道合并,同一个通道有多少行？
		dmax = dmax.reshape(dout.shape+(pool_size,))
		dcol = dmax.reshape(dmax.shape[0]*dmax.shape[1]*dmax.shape[2],-1)
		dx = col2im(dcol,self.x.shape,self.pool_h,self.pool_w,self.stride,self.pad)
		return dx