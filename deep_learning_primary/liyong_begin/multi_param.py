import matplotlib.pyplot as plot
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def function01(x1,x2):
	return 0.1*x1**2+x2**2-3*x2
fig=plot.figure()
ax=fig.add_subplot(111,projection='3d')

x1=np.arange(-10,10,0.2)
x2=np.arange(-10,10,0.2)
y1=function01(x1,x2)
plot.plot(x1,x2,y1)
plot.show()
