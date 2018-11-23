import os


# os module的一些基本使用，还有其他的。
#  把操作文件变得简单就是python语言的目的。
def file_gen():
	file_dir=r'E:/Data/Images/Architecture'
	file_list = os.listdir(file_dir)   # 可以把这个列表改造成生成器。
	for file in file_list:
		print(file)
		outfile=os.path.splitext(file)
		print(outfile)
		
file_gen()
