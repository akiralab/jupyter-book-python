#!/usr/bin/env python
# coding: utf-8

# # pltでerrorbarを表示する方法
# - 平均と標準偏差がもとまっている場合は可視化すると見やすい
# - [公式ドキュメント](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html)
# 
# ## 使い方
# - plt.errorbar(x, y, yerr=error, ecolor='black', linestyle='')
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


# ### サンプルデータの確認

# In[2]:


sample = np.random.normal(loc=10, scale=1., size=(10, 1000))
mean = sample.mean(axis=1)
std = sample.std(axis=1)
error = std / np.sqrt(10)


# In[3]:


plt.hist(sample[0], bins=40)
plt.show()


# ### plt.plotを用いてplotしてみる
# - 分散の表現がとてもわかりづらい

# In[4]:


for i in range(sample.shape[0]):
    plt.bar(i, mean[i], color='gray')
    plt.plot(i, error[i],  'ro', markersize=4)

plt.legend(['mean', 'error'])
plt.show()


# ### plt.errorbartを用いてerrorをplotしてみる
# - errorbarに用いる値は標準偏差を用いる

# In[5]:


for i in range(sample.shape[0]):
    plt.plot(x, mean, 'ro', markersize=4)
    plt.errorbar(x, mean, yerr=error[i], ecolor='gray', linestyle='')

plt.ylim([0, 12])
plt.legend(['mean'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




