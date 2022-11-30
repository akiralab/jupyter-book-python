#!/usr/bin/env python
# coding: utf-8

# # globalの使い方

# In[1]:


a = 1
print('[関数外部]時点でのaの値は, ', a)

def test():
    global a
    print('---[関数内部]時点でのaの値も, ', a)
    a = 2
    print('---[関数内部]時点でのaの値は, ', a)


test()
print('[関数外部]時点でのaの値は, ', a)
print('関数呼び出しによって、global変数と定義したaの値が変化する')


# In[ ]:




