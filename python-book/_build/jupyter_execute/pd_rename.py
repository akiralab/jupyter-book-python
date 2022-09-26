#!/usr/bin/env python
# coding: utf-8

# # df.rename(columns={変更する前の名前: 変更後の名前}, inplace=False)
# - inplaceはdfを返すか返さないか
# - 単一のカラム名だけでも変更できる

# In[1]:


import pandas as pd
import os
import numpy as np


# In[2]:


# pathの確認
path = '../src/titanic/train.csv'
os.path.exists(path)


# In[3]:


df = pd.read_csv(path)
df.info()


# In[40]:


df.head(3)


# ### PassengerIdをrenameしてみる

# In[45]:


# まずは適当に全カラムの名前を変更してみる
df.rename(columns={'PassengerId': 'Id',
                   'Survived': 'survived',
                   'Name': 'name', 
                   'Sex': 'sex', 
                   'Age': 'age',
                   'SibSp': 'sibsp',
                   'Parch': 'parch',
                   'Ticket': 'ticket', 
                   'Fare': 'fare',
                   'Cabin': 'cabin',
                   'Embarked': 'embarked'}, 
                inplace=True)
# df.head()


# In[46]:


df.head()


# In[47]:


df.rename(columns={'Id': 'passengerid'}, inplace=True)
df.head()


# In[49]:


renamed_df = df.rename(columns={'passengerid': 'id'}, inplace=False)
renamed_df.head()


# In[ ]:




