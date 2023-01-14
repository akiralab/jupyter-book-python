#!/usr/bin/env python
# coding: utf-8

# # pandasでEDA(1)

# In[1]:


import pandas as pd
import os


# In[7]:


path = '../data/world-happiness/2015.csv'
os.path.exists(path)


# ### read_csv()

# In[8]:


df = pd.read_csv(path)
len(df)


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.shape


# In[12]:


df.count()


# In[ ]:





# In[ ]:




