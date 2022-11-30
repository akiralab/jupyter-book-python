#!/usr/bin/env python
# coding: utf-8

# # globの基本的な使い方
# 
# - 大量のファイルの中から特定のファイルを引っ張ってくる時などに用いる
# - 正規化表現を用いて検索できる
# 
# 1. glob.glob(PATH)

# In[1]:


import glob


# ### 1. 正規化表現を用いて検索する -> `glob.glob(PATTERN)`

# In[2]:


pattern = "../*/*.ipynb"
glob.glob(pattern)


# In[ ]:





# In[ ]:




