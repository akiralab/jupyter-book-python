#!/usr/bin/env python
# coding: utf-8

# # Pandasの基本コマンド
# - from_dict(data)

# In[1]:


import pandas as pd
import os
import numpy as np


# In[2]:


test_dict = {}
for i in range(100):
    k = str(i).rjust(4, '0')
    v = np.random.randint(10000)
    
    test_dict.update({k: v})
    


# In[3]:


# dictの確認
len(test_dict)


# In[4]:


df = pd.DataFrame.from_dict(test_dict, orient='index', columns=['value'])
df.info()
df.head()


# In[ ]:




