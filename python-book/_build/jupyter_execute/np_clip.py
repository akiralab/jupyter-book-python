#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# np.clip(array, low, high)
x = np.random.randn(100)
x_clipped_high = np.clip(x, 0, None)
x_clipped_low = np.clip(x, None, 0)

plt.subplot(211)
plt.plot(x, 'b')
plt.axis([0, 100, -3, 3])

plt.subplot(212)
plt.plot(x_clipped_high, 'c')
plt.plot(x_clipped_low, 'm')
plt.axis([0, 100, -3, 3])


# In[3]:


# np.clip(array, low, high)
x = np.linspace(0, 2 * np.pi, 128)
y = np.sin(x)
y_clipped_high = np.clip(y, 0, 1)
y_clipped_low = np.clip(y, -1, 0)

plt.subplot(211)
plt.plot(x, y, 'b')

plt.subplot(212)
plt.plot(y_clipped_high, 'c')
plt.plot(y_clipped_low, 'm')


# In[ ]:





# In[ ]:




