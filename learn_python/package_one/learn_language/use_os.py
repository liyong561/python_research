#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import six

# os的常用api，比如文件功能，path功能等
def os_path():
    print(os.path.abspath("."))
    file_name = "pytest"
    print(os.path.isfile(file_name))


print(six.PY3)
print(six.PY2)
