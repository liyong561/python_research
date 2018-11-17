# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def test_pie():
	x = [3,4,5]
	x_labels = ['China','America','India']
	plt.pie(x,labels= x_labels)
	plt.title('economy')
	plt.show()
# 柱状图 bar
def test_bar():
	y = [3,4,5]
	x = range(len(y))
	plt.bar(x,y)  # 还要间距啥的需要调整 
	plt.title('economy')
	plt.show()
	
def test_histgram():
	# |一般没有1w条数据，看分布图都没什么意义。
	# y = range(1,100)/5 无法进行此操作
	# y = range(1,100) 是一个矩形，怎么解释kkk''''''''
	'''y = list(range(1,100))  #是range对象，而不是list对象
	print(type(y))  list对象中可以存储各种对象，没有定义除法操作。
	y = y/5  '''
	# y = np.linspace(1,100,100)
	# x = np.random.randint(0,100,(10000,)) randint最后分布就比较平均了
	# x = range(len(y))
	x = np.random.normal(loc =4,scale =4,size =100000)
	plt.hist(x,20,color="green")    #理解这个意思，是看这段数据的分布情况，，有一个步长选择
	plt.show()

def test_sub():
	#在比较中会经常用到
	# 思考绘制子图的思想是什么，其实就是将几个图，安装顺序排列
	plt.figure(figsize=(2,3))  # 先绘制张大图
	A = plt.subplot(1,1,1) # 为什么需要3个数字，很难理解
	y1 = np.random.randint(0,100,50)
	x1 = np.arange(y1.size)
	plt.plot(x1,y1)
	plt.show()
	plt.subplot(1,1,1)  #最后一个数指代figure
	y1 = np.random.randint(0,100,50)
	x1 = np.arange(y1.size)
	plt.scatter(x1,y1)
	plt.subplot(1,3,1)
	plt.show()
	y1 = np.random.randint(0,100,50)
	x1 = np.arange(y1.size)
	plt.bar(x1,y1)
	plt.show()
	
def test_sub01():
	x=[1,2,3,4]
	y=[5,4,3,2]
	plt.subplot(2,2,1)#呈现2行3列，第一幅图
	plt.plot(x,y)
	plt.subplot(222)#呈现2行3列，第一幅图，可以注意到在subplot里面的数字，可以用逗号隔开，也可以直接写在一起 
	
	plt.barh(x,y)
	plt.subplot(224)#这就是知道4代表什么意思·了。
	plt.bar(x,y)
	plt.show()
test_sub01()
