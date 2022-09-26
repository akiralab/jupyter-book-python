#!/usr/bin/env python
# coding: utf-8

# # [numpy] np.full 
# 
# ### 概要
# - 特定の値を持つ配列を作成する
# 
# ### 使い方
# - np.full(shape, fill_value, dtype, order)
# 
# ### どんな時に便利か
# - np.ones() * valueでも同じ処理だけれど、可読性が上がる

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


np.full((2, 2), 10)


# In[3]:


np.full((2, 2), 10, np.float32)


# In[4]:


np.full(shape=(2, 2), fill_value=10, dtype=np.float32)


# In[5]:


np.full(shape=(2, 2), fill_value=10, dtype=np.float32, )

