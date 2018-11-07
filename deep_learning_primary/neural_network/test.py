import numpy as np
import matplotlib.pyplot as plot
def one_hot(x):
	m=np.zeros((x.size,10),dtype=int)
	m[np.arange(x.size),x]=1 # don't use for
	return m
def softmax(x):
	y=np.max(x,axis=1)   #axis=0
	y=x.T-y 
	y=np.exp(y)/np.sum(np.exp(y),axis=0) #让人有点晕,x变化了
	return y.T
x=np.array([2,3,8,9])
x2=np.array([[5,4,5,],[4,5,9]])
x23=[34,34,78,43]
print(one_hot(x))
print(x2.T)
print(np.max(x2,axis=0))
print(np.max(x2,axis=1))
print(np.sum(x2,axis=0))
print(np.sum(x2,axis=1))
print(softmax(x2))
x3=np.array(range(len(x23)))
print(x3)
plot.plot(x3,x)
plot.show()