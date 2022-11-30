#!/usr/bin/env python
# coding: utf-8

# # [numpy] logspace
# 
# ### 概要
# - logスケールでのlinspace
# 
# ### どんな時に便利か
# - 片対数グラフを作成するときなど

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


a = np.logspace(start=2, stop=3, num=10, endpoint=True)
a


# In[3]:


plt.plot(a)


# ### 基数を変更することもできる

# In[4]:


b = np.logspace(start=1, stop=10, num=10, base=2, dtype=np.float32)
b


# In[ ]:




