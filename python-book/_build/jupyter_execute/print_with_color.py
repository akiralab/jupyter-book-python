#!/usr/bin/env python
# coding: utf-8

# # pythonのprintに革命を起こす！

# In[ ]:





# In[ ]:





# In[1]:


class F_COLORS:
    BLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEST = '\33[6m'
    
class B_COLORS:
    BLUE = '\33[44m'
    WARNING = '\33[43m'
    FAIL = '\33[101m'
    NORMAL = '\033[0m'
    
        


# In[2]:


print('pythonのprintには、色をつけることができる')
print(F_COLORS.BLUE + "-------OK-------" + F_COLORS.NORMAL)
print(F_COLORS.WARNING + "-------WARNING-------" + F_COLORS.NORMAL)
print(F_COLORS.FAIL + "-------FAILED-------" + F_COLORS.NORMAL)


# In[3]:


print('太字や下線も引くことができる')
print(F_COLORS.BOLD + "-------BOLD-------" + F_COLORS.NORMAL)
print(F_COLORS.UNDERLINE + "-------UNDERLINE-------" + F_COLORS.NORMAL)


# In[4]:


print('背景に色をつけることができる')
print(B_COLORS.BLUE + "-------OK-------" + B_COLORS.NORMAL)
print(B_COLORS.WARNING + "-------WARNING-------" + B_COLORS.NORMAL)
print(B_COLORS.FAIL + "-------FAILED-------" + B_COLORS.NORMAL)


# In[ ]:





# In[5]:


print("組み合わせはたくさんあり")


# In[6]:


x = 0
for i in range(24):
    colors = ""
    for j in range(5):
        code = str(x+j)
        colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
    print(colors)
    x = x + 5


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




