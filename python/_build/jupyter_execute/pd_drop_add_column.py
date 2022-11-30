#!/usr/bin/env python
# coding: utf-8

# # Pandasの基本コマンド
# - df.drop(labels=None, axis=0, index=None, columns=None)

# In[1]:


import pandas as pd
import os


# In[2]:


# pathの確認
path = '../src/titanic/test.csv'
os.path.exists(path)


# ### read_csv()

# In[3]:


df = pd.read_csv(path)
len(df)


# In[5]:


df.head()


# # PassengerIdの列を消去する

# In[8]:


df.drop(["PassengerId"], axis=1, inplace=True)


# In[11]:


# "PassengerId"は消去されている
df.info()


# # Columnを挿入する
# - df.insert(loc='where to insert', column='column_name', value='df or series or some values')
# 

# In[17]:


df.insert(1, 'column', 1)


# In[18]:


df.head()


# In[ ]:




