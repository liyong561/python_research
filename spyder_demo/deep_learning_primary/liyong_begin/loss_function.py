import numpy as np
def mean_squared_error(y,t):
	return 0.5*np.sum((y-t)**2) # so simple in python
   
def cross_entropy_error(y,t):
	 return -np.sum(t*np.log(y))
# y=[0.1,0.2,0,0,0.3,0.3,0.1,0,0,0]
# t=[0,0,0,1,0,0,0,0,0,0] this is list,not tensor
    
y=np.array([0.1,0.2,0,0,0.3,0.3,0.1,0,0,0])
t=np.array([0,0,0,1,0,0,0,0,0,0])
print(mean_squared_error(y,t))
print(np.random.choice((10,1000),10))
print(np.random.choice(10,100,10))