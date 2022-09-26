#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tqdm import tqdm
from time import sleep


# もっとも基本的な使い方

# In[2]:


for i in tqdm(range(100)):
    sleep(0.01)
    pass


# barの長さを変更したいときはncolsを用いる

# In[3]:


for i in tqdm(range(100), ncols=100):
    sleep(0.01)
    pass


# barの更新頻度（default: 0.1s）を変更したい場合はminintervalを変更する

# In[4]:


for i in tqdm(range(100), ncols=100, mininterval=0.01):
    sleep(0.01)
    pass


# barの色を変更したいときはcolourを変更する

# In[5]:


for i in tqdm(range(100), ncols=100, mininterval=0.01, colour='blue'):
    sleep(0.01)
    pass


# iteration内容を記述するときはdescを用いる

# In[6]:


for phase in ['train', 'dev']:
    for i in tqdm(range(100), ncols=100, mininterval=0.01, desc=phase):
        sleep(0.01)
        pass


# In[ ]:




