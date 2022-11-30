#!/usr/bin/env python
# coding: utf-8

# # 多変量正規乱数
#  mean:平均
# cov: 共分散行列を指定

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


# In[2]:


x = np.linspace(0, 5, 10, endpoint=False)
y = multivariate_normal.pdf(x, mean=2.5, cov=0.5)
plt.figure()
plt.subplot(111)
plt.plot(x, y)
plt.show()　


# In[34]:


x, y = np.mgrid[-1:1:.01, -1:1:.01]
pos = np.dstack((x, y))
rv = multivariate_normal([0, 0])
plt.subplot(111)
plt.contourf(x, y, rv.pdf(pos))
plt.xlim([-1, 1])
plt.ylim([-1, 1])


# In[ ]:




