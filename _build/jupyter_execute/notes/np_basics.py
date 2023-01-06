#!/usr/bin/env python
# coding: utf-8

# # numpy の基本操作

# In[10]:


import numpy as np


# In[30]:


# 配列を作る
# np.array(array)
a = np.array([[1, 2, 3], [4, 5, 6]])

# 配列の情報を取得する
print('array: ', a)
print('a.shape: ', a.shape)
print('a.size: ', a.size)
print('a.sum: ', a.sum())
print('a.ndarray', a.ndarray)

# 関数化
def info(array):
    print('array: ', array)
    print('shape: ', array.shape)
    print('size: ', array.size)
    print('sum: ', array.sum())


# In[23]:


# 要素がゼロの配列
a = np.zeros(4)
info(a)

a = np.zeros((3, 128, 128))
info(a)


# In[24]:


# 配列を作成する
# np.arange(num) out: arary([...num])
b = np.arange(5)

info(b)


# In[25]:


# np.arange(start, end, linspace)
c = np.arange(10, 20, 2)
info(c)


# In[26]:


# np.linspace(start, end, num_divide)
d = np.linspace(1, 10, 10)
info(d)


# In[27]:


# 配列の形を変更する
# np.reshape(num_cols, num_rows)
e = np.linspace(1, 15, 15).reshape(5, 3)
info(e)


# In[28]:


# 要素の数が同じであれば、reshapeできる
f = e.reshape(3, 5)
info(f)

g = np.zeros((128, 128)).reshape(128 * 128)
info(g)


# In[31]:


# np.transpose() np.TでもOK
h = np.arange(10).reshape(2, 5)
info(h)
i = h.T
info(i)


# In[ ]:





# In[4]:





# In[ ]:




