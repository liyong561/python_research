# -*- coding: utf-8 -*-
# 随便看一副图像，看cnn对其做了什么样的变换。
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from cnn_layer import Convelution
import pickle

def test():
	im= np.array(Image.open(r'E:\Data\Images\Person\zhanghan01.png'))
	im2= np.array(Image.open(r'E:\Data\Images\Person\black_girl.jpg'))
	print(im.shape)   # 已经是ndarray
	im2_R = im2[:,:,2] #每个通道的值都是一样的？
	plt.imshow(im2_R)
	plt.show()
	# im2_pic = Image.fromarray(im2_R)
	# im2_pic2 =Image.open(im2_pic)
	#im2_pic2.imshow()
	print(im2.shape)
def test01():
	# 为甚不是np.array([data])?>
	im = np.array(Image.open(r'E:\Data\Images\Architecture\chongqing_finance.jpg'))
	#通道在后要转化一下。（H,W,C)
	H,W,C =im.shape
	im =im.reshape(1,H,W,C).transpose(0,3,1,2)
	weight_init =0.1
	filter_num=3
	filter_size = 5
	W = weight_init*np.random.randn(filter_num,3,
			 filter_size,filter_size)
	b = np.zeros(1)
	cnn = Convelution(W,b)
	im_cnn = cnn.forward(im)   #经过卷积运算后为什么会有那么多负值,因为卷积核中元素为负值
	N,C,H,W =im_cnn.shape
	im_cnn =im_cnn.reshape(C,H,W).transpose(1,2,0)  #其显示格式为H,W,C
	im = Image.fromarray(np.uint8(im_cnn))  #im_cnn中的元素有的是float等类型，同意转换为unit8类型
	# plt.imshow(im_cnn)  #这个图片完全没有格式，可能是W是任选的，且其像素值的范围范围可能不对，但是读取函数进行了规范。
	im.save(r'E:\Data\Images\Architecture\chongqing_finance03.jpg')
	
def display_w():
	with open('w1_file.pkl','rb') as f:
		w =pickle.load(f)
	N,C,H,W = w.shape
	w = w.transpose(1,0,2,3).reshape(N,H,W)
	w = np.uint8(256*w)
	for i  in range(w.shape[0]):
		plt.subplot(5,6,i+1)
		plt.imshow(w[i],cmap= plt.cm.binary)  #非黑即
	plt.show()

def w_convelution():
	with open('w1_file.pkl','rb') as f:
		w = pickle.load(f)
	FN,FC,FH,FW= w.shape
	w = w[5]
	w = w.reshape(1,FC,FH,FW)
	b =np.zeros(1)
	cnn = Convelution(w,b)
	
	im = np.array(Image.open(r'E:\Data\Images\Architecture\chongqing_finance01.jpg'))
	H,W =im.shape
	im =im.reshape(1,H,W)
	im =im.reshape(1,H,W,1).transpose(0,3,1,2)
	
	im_cnn = cnn.forward(im) #经过一层卷积运算
	print(im_cnn.shape)
	N,FN,OH,OW = im_cnn.shape
	im_cnn =im_cnn.reshape(OH,OW)
	im_cnn = np.uint8(im_cnn)
	im = im.reshape(H,W)
	
	plt.subplot(1,2,1)
	plt.imshow(im)
	plt.subplot(1,2,2)
	plt.imshow(im_cnn)
	plt.show()


w_convelution()