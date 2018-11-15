# -*- coding: utf-8 -*-
import numpy as np
'''x3 = np.random.randn(3,4,5)
print(x3)
x2 = x3.reshape(12,5)
print(x2)
x21 = x3.reshape(4,15)
print(x21)'''
# 给举着周围填充一圈的函数
def padding2(a,num):
	shape= np.array(a.shape)
	shape= shape+2*num # 每个维度增加相应的维度,用向量表示维度没有问题
	m = np.zeros(shape,dtype= float)
	print(m.shape)
	'''
	for j in range(a.shape[0]):   # 使用for循环，使用迭代器呢？
		for i in range(a.shape[1]):
			m[j+num,i+num] = a[j,i]'''
	iter_a = np.nditer(a, flags = ['multi_index'],op_flags=['readonly'])
	while not iter_a.finished: #python中非运算
		# print(iter_a.multi_index) # 元组类型的数据
		# new_multi =iter_a.multi_index + 2 返回tuple运算
		idx = np.array(iter_a.multi_index)
		idx +=num
		print(idx)
		print(iter_a.value)
		# ,m[idx+num] = iter_a.value   # 把它理解成广播运算,这种操作相当于分片
		m[idx[0],idx[1]] = iter_a.value # 
		iter_a.iternext()  #下一个
	return m
def padding(a,num):
	shape= np.array(a.shape)
	shape= shape+2*num # 每个维度增加相应的维度,用向量表示维度没有问题
	m = np.zeros(shape,dtype= float)
	m[num:shape[0]-num,num:shape[1]-num] = a # 以块为单位计算，广播更快，而不用for
	return m
# 这个简单函数只处理二阶张量的运算,无填充,可调整步长
def im2col_simple(a,b,strid):
	#a_shape = a.shape
	# b_shape = b.shape
	if a.shape[0]<b.shape[0] or a.shape[1] < b.shape[1]:
		raise Exception("the first matrix is too samll")
	oh = int((a.shape[0] - b.shape[0])/ strid +1) # 向下取整
	ow = int((a.shape[1] - b.shape[1])/ strid +1)
	print(oh,ow)
	result = np.zeros((ow,oh),dtype = float)
	# numpy中建议不用for，但是还是要用for
	for  j in range(ow):
		for i in range(oh):
			result[j,i]= np.sum(a[i:i+b.shape[0],j:j+b.shape[1]]*b)
	return result
def test():
	a = np.linspace(0,4,20) # 不是np.ndarray类型 
	# a = a.resize(4,5) # 该函数作用于其本身
	a.resize(4,5)
	b = np.linspace(0,4,6)
	print(b)
	b.resize(2,3)
	print(b)
	result = im2col_simple(a,b,80)
	print(result) # 矩阵生成时就说随机的。

# 二维张量计算，可调步长，可填充，用0填充，保持形状不变
def im2col_simple2(a,b,strid):
	#a_shape = a.shape
	# b_shape = b.shape
	if a.shape[0]<b.shape[0] or a.shape[1] < b.shape[1]:
		raise Exception("the first matrix is too samll")
	oh = int((a.shape[0] - b.shape[0])/ strid +1) # 向下取整
	ow = int((a.shape[1] - b.shape[1])/ strid +1)
	
	result = np.zeros((ow,oh),dtype = float)
	# numpy中建议不用for，但是还是要用for
	for  j in range(ow):
		for i in range(oh):
			result[j,i]= np.sum(a[i:i+b.shape[0],j:j+b.shape[1]]*b)
	return result
def test01():
	a = np.linspace(0,14,20)
	a.resize(4,5)
	print(a)
	a_index = np.array([0,1,2])
	print(a[a_index,a_index]) #也可以使用向量，
	# print(padding2(a,2))
test01()