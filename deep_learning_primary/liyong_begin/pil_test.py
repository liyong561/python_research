# -*- coding: utf-8 -*-
from PIL import Image

import matplotlib.pyplot as plt
pil_in=Image.open("E:/Data/Images/Architecture/chongqing_finance.jpg").convert('L')
# pil_in02=pil_in.thumbnail((128,128)) # on itself
# pil_in.show() # a action,so use mehtod,not attribure,and use os' app
box=(100,100,200,400)
region=pil_in.crop(box)
region=region.transpose(Image.ROTATE_180)
#region=region.rotate(180)
pil_in.paste(region,box)
plt.imshow(region)
plt.title("this is a picture")
plt.show()
print(pil_in.size)
plt.imshow(pil_in)

plt.show()