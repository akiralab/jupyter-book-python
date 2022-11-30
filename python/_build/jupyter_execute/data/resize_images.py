#!/usr/bin/env python
# coding: utf-8

# # [cv2] resize
# 
# ### 概要
# - 解像度の変更

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import cv2


# In[2]:


img = cv2.imread('src/lena.png')
print(img.shape, img.dtype)
plt.imshow(img[:, :, ::-1])


# In[12]:


half_img = cv2.resize(img, None, fx=0.5, fy=0.5)
print(half_img.shape, half_img.dtype)
plt.imshow(half_img[:, :, ::-1])


# In[13]:


half_img = cv2.resize(img, (200, 200))
print(half_img.shape, half_img.dtype)
plt.imshow(half_img[:, :, ::-1])


# In[14]:


half_img = cv2.resize(img, (10, 10))
print(half_img.shape, half_img.dtype)
plt.imshow(half_img[:, :, ::-1])


# # [torch] nn.functional.interpolate
# 
# ### 概要
# - 解像度の変更

# In[51]:


import torch


# In[74]:


img = torch.tensor(np.copy(img))

half_img = torch.transpose(img, 0, 2).unsqueeze(dim=0)
# half_img = torch.nn.functional.interpolate(half_img, scale_factor=0.5)
half_img = torch.nn.functional.interpolate(half_img, size=(256, 256))
half_img = half_img.squeeze(dim=0)

print(half_img.shape, half_img.dtype)
plt.imshow(half_img.transpose(0, 2))


# In[ ]:





# In[ ]:




