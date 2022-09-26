#!/usr/bin/env python
# coding: utf-8

# # [numpy, torch] transpose
# 
# ### 概要
# - numpyとtorchとでtransposeの用法が若干異なるので注意が必要
# 
# ### どんな時に便利か
# - (ch, H, W) -> (H, W, ch)に変換する際などに便利

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import torch


# In[2]:


a = np.random.random((100, 100, 3))
print(a.shape)


# In[3]:


# numpyのtransposeは、shapeそのものを入れ替えてしまう
a_transposed = a.transpose(2, 0, 1)
print(a_transposed.shape)


# In[4]:


b = torch.rand((100, 100, 3))
print(b.shape)


# In[5]:


# torchのtransposeは、
b_transposed = b.transpose(2, 0)
print(b_transposed.shape)


# In[ ]:





# In[ ]:





# In[ ]:




