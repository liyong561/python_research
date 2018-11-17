# -*- coding: utf-8 -*-
import pickle
import os

def test01():
	c1 = ['fee', 'fie', 'foe', 'fum'] 
	b1 = {1: 'One', 2: 'Two', 3: 'Three'} 
	# open是一个内置方法,这样访问文件，真的很方便。
	with open('test_pkl.pkl','wb') as f:
		pickle.dump(c1,f)
		pickle.dump(b1,f)
	
	#然后取出来
	with open('test_pkl.pkl','rb') as f:  # 后面是访问模式。
		read_c1 = pickle.load(f)  # 
		read_b1 = pickle.load(f)  #不用指定数据，根据存取时间取出
	print(read_c1)
	print(read_b1[2])
	#这才是其神奇之处，一个程序运行完毕后，另一个程序可以访问。
	# 还要思考一个问题，怎么在磁盘中彻底的删除。
def test02():
	with open('test_pkl.pkl','rb') as f:  # 后面是访问模式。
		read_c1 = pickle.load(f)  # 
		read_b1 = pickle.load(f)  #不用指定数据，根据存取时间取出
	print(read_c1)
	print(read_b1[2])
	# os.removedirs(path) # 移除path
	os.remove('test_pkl.pkl') #这就删除了pkl文件，所以它存在哪里对我完全是个未知
test01() 

