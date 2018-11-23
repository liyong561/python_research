import matplotlib.pyplot as plt
from matplotlib.image import imread
from keras.preprocessing import image


img_dir = r'E:/Data/Images/Person/zhanghan01.png'
def display_img():
	img=imread('E:/Data/Images/Person/black_girl.jpg')
	plt.imshow(img) # tell the class method how to plot the picture
	plt.show()

def keras_argument():
	data_gen = image.ImageDataGenerator(
			rotation_range =40,
			width_shift_range = 0.2,
			height_shift_range = 0.2,
			shear_range = 0.2,
			zoom_range = 0.2,
			horizontal_flip = True,
			fill_mode = 'nearest'
			)
	img =image.load_img(img_dir,target_size=(200,200))
	x = image.img_to_array(img)    # 读取的还是一个图像数据，要转化成张量
	x = x.reshape((1,)+x.shape)
	i = 0
	for batch in data_gen.flow(x,batch_size =1):
		# 由一个图片，生成多个图片
		plt.figure(i)
		implot = plt.imshow(image.array_to_img(batch[0]))
		i += 1
		if i%4==0:
			break
	plt.show()
		
keras_argument()