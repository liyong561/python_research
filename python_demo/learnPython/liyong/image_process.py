from PIL import Image,ImageFilter

im = Image.open("E:/TestFile/test01.jpg")  # in是python的key word
w, h = im.size
print("Original image size :%s,%s" % (w, h))
im.thumbnail((w/2, h/2))  # 缩放图片，多么简单啊。
w1, h1 = im.size
print(w1)
im.save("E:/TestFile/test01_reduce.jpg")
im.show()

