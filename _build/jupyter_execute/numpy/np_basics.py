#!/usr/bin/env python
# coding: utf-8

# # numpyで配列を作成する

# In[68]:


import numpy as np


# ## 要素を直接指定して配列を作成する（np.array）

# In[71]:


a = np.array([[1, 2, 3], [4, 5, 6]])

# 関数化
def info(array):
    print('array: ', array)
    print('shape: ', array.shape)
    print('size: ', array.size)
    print('mean: ', array.mean())    
    print('sum: ', array.sum())
    
info(a)


# ## 要素がゼロの配列を作成する（np.zeros）

# In[70]:


a = np.zeros(4)
info(a)


# ### 要素が1の配列を作成する（np.ones）

# In[34]:


a = np.ones(4)
info(a)


# ### 要素が空の配列を作成する（np.empty）

# In[35]:


a = np.empty(shape=[4])
info(a)


# ### 要素を一意の数値に指定して作成する（np.full）

# In[36]:


a = np.full([5, 4], 10)
info(a)


# ### 順列要素として作成する（np.arange）

# In[37]:


a = np.arange(10)
info(a)


# In[41]:


# stopで指定した数字は入らないので注意
a = np.arange(start=10, stop=20, step=2)
info(a)


# ### 順列を作成する（np.linspace）
# - np.arangeとは異なり、配列の要素数を指定することができる

# In[44]:


a = np.linspace(start=10, stop=20, num=2)
info(a)


# ### 指数ベースでの順列を作成する（np.logspace）
# - 指数ベースでの配列作成（基数は10がデフォルト）

# In[63]:


# 10^1から始まり、10^4で終わる配列を作成。要素数は4
a = np.logspace(start=1, stop=4, num=4)
info(a)


# ### 対数スケール（幾何級数）で等間隔に並んだ数字を返す（np.geomspace）

# In[66]:


a = np.geomspace(1, 1000, num=4)
info(a)


# ### 要素がrandomの配列を作成する（np.random）

# In[67]:


a = np.random.rand(3, 4)
info(a)


# In[ ]:





# In[ ]:




