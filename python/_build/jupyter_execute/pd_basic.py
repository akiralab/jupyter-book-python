#!/usr/bin/env python
# coding: utf-8

# # Pandasの基本コマンド
# - read_csv(path)
# - head()

# In[1]:


import pandas as pd
import os


# In[2]:


# pathの確認
path = '../src/titanic.csv'
os.path.exists(path)


# ### read_csv()

# In[3]:


df = pd.read_csv(path)
len(df)


# In[13]:


df.head()


# In[14]:


df.tail()


# In[8]:


df.shape


# In[10]:


df.count()


# In[ ]:





# In[ ]:




