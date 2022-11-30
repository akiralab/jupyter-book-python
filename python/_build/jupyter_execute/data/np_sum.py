#!/usr/bin/env python
# coding: utf-8

# # [np] sum

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


x = np.arange(60).reshape(3, 4, 5)
x


# In[3]:


# axis=0でのsum
x_0 = x.sum(axis=0)
print('x_0', x_0)
print('{} ---> {}'.format(x.shape, x_0.shape))


# In[4]:


# axis=0でのsum
x_0 = x.sum(axis=0, keepdims=True)
print('x_0', x_0)
print('{} ---> {}'.format(x.shape, x_0.shape))


# In[5]:


# axis=0でのsum
x_1 = x.sum(axis=1)
print('x_1', x_1)
print('{} ---> {}'.format(x.shape, x_1.shape))


# In[ ]:




