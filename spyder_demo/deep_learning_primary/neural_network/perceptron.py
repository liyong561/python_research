import numpy as np
import matplotlib.pyplot as plot
def AND(x1,x2):
	w1,w2,theta=0.5,0.5,0.7
	temp=w1*x1+x2*w2
	if temp<theta:
		return 0
	else:
		return 1
def sigmoid(x):#我定义函数时默认是适用于整数，但是可以自动用于列表，很神奇。
	return 1/(1+np.exp(-x))
def ReLU(x): #尽量使用库函数，其设置了不同张量的运算。
    return np.maximum(0,x)
print(AND(1,1))
# x1=range(-3,8,0.1),ranghe函数用于创建整数列表
x1=np.arange(-3,8,0.1)
#y=x1>0
#y=y.astype(np.float)#type convert
y=sigmoid(x1)
plot.plot(x1,y)
plot.show()
y1=ReLU(x1)
print(y1)
plot.plot(x1,y1)


