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


# In[8]:





# # uniqueを抽出する

# In[12]:


df["Sex"].unique()


# In[9]:





# # uniqueを頻出順に並べる

# In[22]:


df["Sex"].value_counts()


# In[5]:





# In[15]:


df["Age"].nunique()


# In[ ]:




