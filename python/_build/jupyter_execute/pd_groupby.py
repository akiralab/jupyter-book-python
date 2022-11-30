#!/usr/bin/env python
# coding: utf-8

# # Pandasの基本コマンド
# - df.groupby(by=None, axis=0, level=None, sort=True, dropna=True)

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


# In[14]:


df.head()


# In[ ]:





# # groupごとに集計する

# In[21]:


# 文脈としては、Pclassベースで、Survivedがそれぞれどれくらいの割合で存在しているか
df[["Pclass", "Survived"]].groupby(["Pclass"]).describe()


# In[ ]:





# # uniqueを頻出順に並べる

# In[21]:


df["Sex"].nunique()


# In[5]:





# In[15]:


df["Age"].nunique()


# In[ ]:




