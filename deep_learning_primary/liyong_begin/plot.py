import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,6,0.1)  # 使用numpy的arange函数，而不是range，
y=np.sin(x)
 # plt.plot(x,y)  
 #  plt.show() just a x-y graph,no other information
y1=np.sin(x)
y2=np.cos(x)
y3=np.random.randn(60,2)
print(y3)
#plt.plot(x,y1,'ro',label="sin")  # template method
plt.plot(x,y3,linestyle="--",label="cos") 
# have the same dimension
plt.title("sin & cos")
plt.legend() # combine the label
plt.show()
x_axis = range(len(y1))
plt.plot(x_axis,y1,y2)
 