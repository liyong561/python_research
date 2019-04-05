#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from matplotlib import pyplot as plt
import numpy as np


# In[ ]:


a2=[12.2,32,43,23,32]  # 数组这种奇怪的数据
a1=np.array([1,2,3,3.7,4])
a3=np.arange(1,10,0.3)
print(a3)
a3_sin =np.sin(a3) # 处理的是数组
print(a3_sin)


# In[ ]:


plt.plot(a3,a3_sin)
plt.xlabel("the x label")
plt.ylabel("the y label")
plt.show()


# In[ ]:




