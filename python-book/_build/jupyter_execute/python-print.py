#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# print出力を改行させずに更新する方法（tqdmのような出力）
# 用法
# 1. \r を先頭につけることで、print出力を常に先頭文字列からスタートさせる
# 2. end=''を指定することで、print出力を強制的に改行させない

# In[2]:


for i in range(10):
    time.sleep(0.2)
    print('\r no.{} this string will start at the beginning of the line'.format(i), end="")


# 簡易的なプログレスバーを作成することもできる

# In[3]:


total_epoch = 100
def epoch_to_progress_bar(epoch, total_epoch):
    '''
        epochから現在の進捗をbar表示するための関数
        input: epoch, total_epoch
        output: bar type: str
    '''
    # progress bar length
    max_length = 50
    # calc current progress
    progress_bar = '*' * (epoch * max_length // total_epoch+1) 
    # progress bar filled with '-'
    progress_bar = progress_bar.ljust(max_length, '-')
    
    return progress_bar


for epoch in range(total_epoch):
    progress_bar = epoch_to_progress_bar(epoch, total_epoch)

    time.sleep(0.1)
    print('\r epoch ({}/{}) |{}|'.format(epoch+1, total_epoch, progress_bar), end='')


# In[ ]:




