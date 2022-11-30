#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# np.random.random() -> [0, 1]の乱数を返す
print(np.random.random())

a = []
for i in range(1000):
    a.append(np.random.random())
a.sort()

plt.plot(a)


# In[3]:


# np.random.randn() -> 標準正規分布に従った乱数を返す
print(np.random.randn())

b = []
for i in range(1000):
    b.append(np.random.randn())
b.sort()

plt.plot(b)


# In[4]:


# 配列にしたい場合はnp.random.rand(rows, cols)
print(np.random.rand(2,4))

print(np.random.randn(2,4))


# In[ ]:





# In[ ]:




