#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 可読性を上げるために、関数には説明を加える

# """
# This script is for some specific situation.
# Usage:
#     calculate something
# """

# In[1]:


def template_short(some_inputs):
    """This explanation is used for plain method."""
    some_outputs = some_inputs
        
    return some_outputs


# In[2]:


def template_long(some_inputs):
    """
    This explanation is used for complex methoc.
    
    Parameters
    ----------
    some_inputs  : tuple, optional
        arguments for `some.method()`.
    """
    some_outputs = some_inputs
        
    return some_outputs


# In[ ]:




