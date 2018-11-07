import numpy as np
import matplotlib.pyplot as plot
def softmax(x):
	 exp_a=np.exp(x)
	 sum_exp_a=np.sum(exp_a)
	 y=exp_a/sum_exp_a #sum_exp_a是一个数值，存在广播，非常奇怪
	 return y
a=np.array([0.2,3,5.0043])
exp_a=np.exp(a)  #指数运算，注意溢出
print(exp_a)
x1=np.arange(-23,12,0.1)
y1=softmax(x1)
plot.plot(x1,y1)
plot.show()




