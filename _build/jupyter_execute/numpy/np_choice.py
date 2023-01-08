#!/usr/bin/env python
# coding: utf-8

# # [np] choice
# 
# ### 概要
# - 複数の選択肢からランダムに要素を選択するためのメソッド
# 
# ### どんな時に便利か
# - 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[4]:


number_list = np.arange(10)
chosed_number = np.random.choice(number_list, 2)
chosed_number


# ## 時間を計測してみる

# In[12]:


import time


# In[20]:


total_num = 10
number_list = np.arange(total_num)
for select_num in range(1, 10):
    start = time.time()
    for it in range(100):
        chosed_number = np.random.choice(number_list, select_num)
    end = time.time()
    print('---from total {} choose {} ---> {:.3f} ms'.format(select_num, total_num, (end-start)*1000))


# In[21]:


total_num = 100
select_num = 2
number_list = np.arange(total_num)

for select_num in range(1, 100):
    start = time.time()
    for it in range(100):
        chosed_number = np.random.choice(number_list, select_num)
    end = time.time()
    print('---from total {} choose {} ---> {:.3f} ms'.format(select_num, total_num, (end-start)*1000))
    


# In[22]:


total_num = 1000
select_num = 2
number_list = np.arange(total_num)
for select_num in range(1, 100):
    start = time.time()
    for it in range(1000):
        chosed_number = np.random.choice(number_list, select_num)
    end = time.time()
    print('---from total {} choose {} ---> {:.3f} ms'.format(select_num, total_num, (end-start)*1000))


# In[ ]:




