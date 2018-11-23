# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def test_gray():
	w = np.uint8(256*np.random.randn(4,4,1))
	# 一个通道的图片是默认的·两个通道图片
	H,W,C = w.shape
	w = w.transpose(2,0,1).reshape(H,W)
	plt.imshow(w,cmap=plt.cm.binary) # 没有这个就会默认显示彩色。
	plt.show()
	
def test01():
	#int 函数适用于一个数值。
	# 随机生成的过滤器，没有规律。
	w = np.uint8(256*np.random.randn(4,4,3))
	w1 = np.uint8(256*np.random.randn(4,4,3))
	# 同时显示多幅图像
	plt.subplot(1,2,1)
	plt.imshow(w,plt.cm.gray)
	plt.subplot(1,2,2)
	plt.imshow(w1)
	plt.show()

def test02():
	#int 函数适用于一个数值。
	# 随机生成的过滤器，没有规律。
	w = np.uint8(256*np.random.randn(4,4,4,1))
	# 同时显示多幅图像,使用for循环。
	for i in range(w.shape[0]):
		plt.subplot(2,2,i+1)
		plt.imshow(w[i],plt.cm.gray)
	plt.show()
	
test01()