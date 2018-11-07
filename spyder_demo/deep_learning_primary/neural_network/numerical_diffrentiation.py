import numpy as np
def function01(x):
     return 0.1*x**2+0.1*x
def function02(x):#多元函数的简单定义，
     return x[0]**2+x[1]
def numerical_diff01(f,x):
    h=1e-5
    return (f(x+h)-f(x-h))/(2*h) # 函数值的阶为0
def numerical_gradient(f,x): #get the gradient at x
    h=1e-5
    grad=np.zeros_like(x) #x is a vector
    for idx in range(x.size):
        temp=x[idx]
        x[idx]=temp+h
        f2=f(x)
        x[idx]=temp-2*h
        f1=f(x)
        grad[idx]=(f2-f1)/(2*h)
        x[idx]=temp #还要还原值
    return grad
def gradient_descent(f,init_x,rate,step):  # 完成了一个梯度下降运算
	 x=init_x
	 for i in range(step):# 重复次数
		  grad=numerical_gradient(f,x)
		  x-=rate*grad
	 return x
x=np.arange(-10,10,0.2) #distingush the  array() range-arange
y=function01(x)