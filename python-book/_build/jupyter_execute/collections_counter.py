#!/usr/bin/env python
# coding: utf-8

# # collectionsとは？
# 
# ### 概要
# 
# - リストの集計や並び替えに重宝するモジュール
# 
# ### 使用するメリット
# 
# - 配列データを簡易的に分析するのに便利

# ## Counter

# In[1]:


from collections import Counter


# In[2]:


# ランダムな変数を作成する
import numpy as np
sample = np.random.randint(10, size=[100])
print(sample)


# In[3]:


# カウントする -> {key: 出現数}の辞書配列を出力する
Counter(sample)


# In[4]:


# もっとも頻出の項目をリストアップする
Counter(sample).most_common(3)


# In[ ]:





# ## OrderdDict
# - pythonの標準dictの強化版
# - dict要素に順序が付いており、並び替えなどができる

# In[5]:


from collections import OrderedDict


# In[6]:


# 最頻値で並び替え
sample_list = Counter(sample).most_common(len(sample))
od = OrderedDict(sample_list)

for key, value in (od.items()):
    print(key, value)


# In[ ]:




