#!/usr/bin/env python
# coding: utf-8

# # [torch] where
# 
# ### 概要
# - 特定条件で絞り込む
# 
# ### どんな時に便利か
# - 検索したい時など

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


import torch


# In[3]:


a = torch.rand(100)
b = torch.ones(100)

plt.plot(a.numpy(), 'bo', markersize=2)
plt.ylim([0, 1])
plt.show()


# In[4]:


c = torch.where(a<0.5, a, b)

plt.plot(c.numpy(), 'bo', markersize=2)
plt.ylim([0, 1])
plt.show()


# In[5]:


d = torch.where(( (0.3<a) & (a<0.7)), a, b)

plt.plot(d.numpy(), 'bo', markersize=2)
plt.ylim([0, 1])
plt.show()


# In[ ]:





# In[ ]:




