#!/usr/bin/env python
# coding: utf-8

# # pprintとは？
# 
# ### 概要
# 
# - なくても学習や計算に支障はないが、あると出力が見やすくなるモジュール、pprint。
# 
# ### 使用するメリット
# 
# - python標準のprintよりも出力のアレンジが効く
# - 辞書や配列などの出力行数を少なくできる

# In[1]:


import pprint


# In[2]:


l = [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, 
     {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]},
     {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]


# In[3]:


# 辞書式配列は通常のprintだと読みづらい
print(l)


# In[4]:


# pprintだと読みやすい
pprint.pprint(l)


# ## 深さ方向を指定することができる

# In[5]:


print('depth = 1')
pprint.pprint(l, depth=1)
print('depth = 2')
pprint.pprint(l, depth=2)
print('depth = 3')
pprint.pprint(l, depth=3)


# ## import方法を工夫するとpprintと書くだけで使用できる

# In[6]:


from pprint import pprint


# In[7]:


pprint(l)


# In[ ]:




