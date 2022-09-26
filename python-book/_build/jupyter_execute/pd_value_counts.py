#!/usr/bin/env python
# coding: utf-8

# # Pandasの基本コマンド
# - index -> rowsの配列を返す
# - columns -> columnsの配列を返す

# In[1]:


import pandas as pd
import os


# In[2]:


# pathの確認
path = '../src/titanic/train.csv'
os.path.exists(path)


# ### read_csv()

# In[3]:


df = pd.read_csv(path)
len(df)


# In[17]:


df.head()


# In[18]:


df.index


# In[19]:


df.columns


# In[10]:


df.count()


# In[22]:


# indexを設定する
df.set_index('PassengerId')


# In[23]:


df.index


# In[24]:


df.set_index('Name')


# In[25]:


df.index


# In[26]:


df.index[0]


# In[ ]:




