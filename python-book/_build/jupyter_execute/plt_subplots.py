#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# usage: subplot(nrows, ncols, index)
plt.subplot(211)
plt.plot(np.random.rand(10))
plt.subplot(212)
plt.plot(np.arange(10))


# In[3]:


# usage: subplots(nrows, ncols)
plt.subplots(3, 3)


# In[4]:


fig, a = plt.subplots(2, 2)
x = np.arange(1, 5)
a[0][0].plot(x, x*x)
a[0][0].set_title('square')


# In[5]:


fig, a = plt.subplots(2, 2)
x = np.arange(1, 10)
a[0][0].plot(x, x*x)
a[0][0].set_title('square')
a[0][1].plot(x, np.exp(x))
a[0][1].set_title('exp')
a[1][0].plot(x, np.log10(x))
a[1][0].set_title('log')
a[1][1].plot(x, np.sqrt(x))
a[1][1].set_title('sqrt')


# In[6]:


# subplot2grid(shape, location, rowspan, colspan)
fig1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
fig2 = plt.subplot2grid((3, 3), (0, 2), rowspan = 3)
fig3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=2)


# In[7]:


# subplot2grid + tight_layout()

fig1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
fig2 = plt.subplot2grid((3, 3), (0, 2), rowspan = 3)
fig3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=2)
plt.tight_layout()


# In[8]:


fig, a = plt.subplots(4, 4)
plt.tight_layout()

x = np.arange(1, 10)

for i in range(4):
    for j in range(4):
        a[i][j].plot(x, (i + 1) * x ** (j + 1))


# In[ ]:




