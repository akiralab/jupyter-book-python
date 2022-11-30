#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# 素点の計算
x = np.linspace(0, 100, 100)
print(x)
lin_x = x / 100
log_x = np.log(x+1) / np.log(6)
tanh_x = np.tanh(x)

plt.plot(x, lin_x, 'y--')
plt.plot(x, log_x, 'b--')
plt.plot(x, tanh_x, 'r--')
plt.legend(['x', 'log(x+1)/log(6)', 'tanh'])
plt.axis([0, 5, 0, 1])


# In[ ]:




