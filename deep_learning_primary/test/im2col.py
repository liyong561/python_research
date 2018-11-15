# -*- coding: utf-8 -*-
def im2col_test(input_data, filter_h, filter_w, stride=1, pad=0):
	# 为了保持卷积后数据的格式不变，需要填充
	c  = input_data.shape[1]
	h = input_data.shape[2]  #(n,c,h,w）格式数据
	w = input_data.shape[3]
	ph = (h* stride -ph - stride) // 2 # 返回整数
	pw = (w* stride -pw - stride) //2
	#这些参数都是经过计算得到的
	data_pad = np.pad(input_data,(0,0),(0,0),(ph,ph),(pw,pw),'constant')
	data_pad3D = np.reshape(c*shape[0],h,w) #4维数据展成3维数据
	data_flatten = np.zeros((input_data.shape[0]*h*w,
						  input_data.shape[1]*filter_h*filter_w),dtype= float)
	#先将长方体展平,还是要用for循环
	#for j in range(h):
	#	for i in range(w):# 对张量的变化改动尽量少，可以使：符号。
# this is a test method
			
def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
	# 为了保持卷积后数据的格式不变，需要填充
	N,C,H,W = input_data.shape # 一起赋值
	ph = (H* stride -H - stride+filter_h)//2+1 # 返回整数
	pw = (W* stride -W - stride+filter_w) //2+1
	data_pad = np.pad(input_data,((0,0),(0,0),(ph,ph),(pw,pw)),'constant')
	data_overlap = np.zeros((N,C,filter_h*H,filter_w*W),dtype=float) #对数据的w和h维进行扩展，其他保持不变
	for j in range(H):
		for i in range(W):
			data_overlap[:,:,j*filter_h:(j+1)*filter_h,i*filter_w:(i+1)*filter_w]=data_pad[:,:,j*stride:j*stride+filter_h,i*stride:i*stride+filter_w]
	data_flatten = data_overlap.reshape(data_pad.shape[0],data_pad.shape[1]*data_pad.shape[2]*data_pad.shape[3])
	return data_flatten
x1 =np.random.rand(1,3,7,7)
x2 =im2col(x1,2,2)
print(x2.shape)

