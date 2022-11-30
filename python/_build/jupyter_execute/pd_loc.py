#!/usr/bin/env python
# coding: utf-8

# # loc

# In[1]:


import pandas as pd
import os


# In[2]:


# pathの確認
path = '../src/titanic.csv'
os.path.exists(path)


# ### read_csv()

# In[3]:


# 氏名をindexとして指定してみる
df = pd.read_csv(path, index_col=3)
df.head()


# ### loc["item名"] -> itemについての情報を取り出すことができる

# In[28]:


df.loc['Heikkinen, Miss. Laina']


# ### データを絞り込むことも可能

# In[33]:


df_survived = df.loc[df["Survived"] == 1]
df_survived


# In[34]:


df_survived_female = df.loc[(df["Survived"] == 1) & (df["Sex"] == "female")]
df_survived_female


# In[ ]:




