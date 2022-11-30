#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


fig, ax = plt.subplots()


# In[3]:


fig, ax = plt.subplots()

ax.plot(np.arange(5), [1,4,3,2,5])


# In[4]:


# 複数のプロットを表示する
fig, ax = plt.subplots(2, 2)


# In[5]:


# 複数のグラフを表示する
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadartic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('Simple Plot')
plt.legend()


# In[6]:


# 軸の最大値を設定する
fig = plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
plt.show()


# In[ ]:





# In[ ]:




