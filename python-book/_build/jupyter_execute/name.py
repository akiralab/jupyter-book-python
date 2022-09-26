#!/usr/bin/env python
# coding: utf-8

# # ```__name__```とは？

# In[1]:


print('importしていない場合は、__name__ = __main__となる')
print('__name__: ', __name__)


# In[2]:


from nametest import NameTest


# In[3]:


nametest = NameTest
nametest


# In[ ]:




