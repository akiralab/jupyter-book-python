#!/usr/bin/env python
# coding: utf-8

# # ランダム要素を取得する

# In[13]:


import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt


# ## [0, 1]範囲でのランダムな要素を取得する

# ### np.random.random()は[0, 1]の範囲のランダムな要素を1つ返す

# In[15]:


a = np.random.random()
a


# ### np.random.rand()は[0, 1]の範囲のランダムな要素を指定した形式で返す

# In[17]:


a = np.random.rand(3, 4)

def info(array):
    print('array: ', array)
    print('shape: ', array.shape)
    print('size: ', array.size)
    print('mean: ', array.mean())    
    print('sum: ', array.sum())

info(a)


# ### 整数値の場合

# In[24]:


a = np.random.randint(low=0, high=10, size=(4, 5))
info(a)


# In[25]:


### 予め指定した配列から重複を許して選ぶ場合


# In[29]:


number_list = np.arange(0, 10, 2)
print(f'number_list: {number_list}')
chosed_number = np.random.choice(number_list, size=10)

info(chosed_number)


# ### 正規分布に従ったランダム配列を出力したい場合（np.random.normal）
# - loc: 分布の平均値
# - scale: 標準偏差
# - size: 配列のshape

# In[37]:


sample_1 = np.random.normal(loc=0, scale=1, size=1000)
sample_2 = np.random.normal(loc=0, scale=3, size=1000)

plt.figure(figsize=[15, 5])
plt.subplot(1, 3, 1)
plt.plot(sample_1, 'ro', markersize=1)
plt.plot(sample_2, 'bo', markersize=1)
plt.title('Output(scale=1, scale=3)')
plt.subplot(1, 3, 2), plt.hist(sample_1, bins=40, color='red'), plt.title('Histogram (scale=1)')
plt.subplot(1, 3, 3), plt.hist(sample_2, bins=40, color='blue'), plt.title('Histogram (scale=3)')
plt.show()


# In[ ]:




