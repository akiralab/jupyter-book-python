#!/usr/bin/env python
# coding: utf-8

# # 概要
# - Normalは標準分布に従って乱数を生成する

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


sample_1 = np.random.normal(loc=0, scale=1, size=1000)
sample_2 = np.random.normal(loc=0, scale=3, size=1000)

plt.figure(figsize=[5, 5])
plt.plot(sample_1, 'ro', markersize=1)
plt.plot(sample_2, 'bo', markersize=1)
plt.show()
plt.figure(figsize=[12, 5])
plt.subplot(1, 2, 1)
plt.hist(sample_1, bins=40, color='red')
plt.subplot(1, 2, 2)
plt.hist(sample_2, bins=40, color='blue')
plt.show()


# In[ ]:





# In[ ]:




