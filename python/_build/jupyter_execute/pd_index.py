#!/usr/bin/env python
# coding: utf-8

# # Pandasの基本コマンド
# - value_counts

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


# In[31]:


df.head()


# In[33]:


df['Survived'].value_counts()


# In[34]:


df['Name'].value_counts()


# In[35]:


df['Ticket'].value_counts()


# In[37]:


# 割合を返すこともできる
df['Age'].value_counts(normalize=True)


# In[38]:


# 割合を返すこともできる
df['Survived'].value_counts(normalize=True)


# In[ ]:




