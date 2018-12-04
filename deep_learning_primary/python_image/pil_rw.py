# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

def test01():
	file_path= r'E:\Data\Images\Architecture\yunnan.jpeg'
	# (f_path,f_type)= path.split(file_path)  区分路径名和文件名
	(f_path,f_type)= path.splitext(file_path)
	print(f_path,f_type)
	im = Image.open(file_path)
	im.save(f_path+'.jpg')
	# png的格式为rgbA
	print(im.mode)
	
def test02():
	im_arr = np.array(Image.open(r'E:\Data\Images\Person\zhanghan01.png').convert('L'))
	plt.subplot(2,2,1)
	plt.title("zhanghan")  #title好像不能有英文
	plt.imshow(im_arr)
	plt.subplot(2,2,2)
	plt.title("bar graph")
	plt.hist(im_arr.flatten(),128)  #区间数目
	plt.show()
	print(im_arr.shape)

def test03():
	file_path=r'E:\Data\Images\Person\working_girl.JPEG'
	im = np.array(Image.open(file_path).convert('L'))
	im = 255.0*(im/255.0)**2
	print(im.shape)  # 一维
	plt.imshow(im)
	plt.show()


def figure_display():
	#  python的基本功，对python1的各个模块的理解
	#  file_path= os.path(r'E:\Data\Images\Person')
	file_fold= r'E:\Data\Images\Person'
	file_list =os.listdir(file_fold)
	file_path =[]
	for file in file_list:
		file_path.append(os.path.join(file_fold, file))
	figure = plt.figure()  # figure的属性为默认的，而不是没有



figure_display()