#!/usr/bin/env python
# coding: utf-8

# # [torch] interpolate
# 
# ### 概要
# - 画像の縮尺を変えるときに必要なメソッド
# - 本来はグラフの補完機能として使うための機能
# 
# ### どんな時に便利か
# - 画像学習時にtransformなどで使える

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import torch
import cv2


# In[2]:


img = cv2.imread('src/lena.png')[:, :, ::-1]
img = np.array(img)
print(img.shape)
plt.imshow(img)
plt.show()


# In[36]:


# 1度[batch, ch, H, W]の形に変形する必要あり
img_tensor = torch.tensor(np.copy(img)).unsqueeze(dim=0)

img_small = torch.nn.functional.interpolate(img_tensor, size=None, scale_factor=0.5)
print(img_small.shape)
plt.imshow(img_small[0].transpose(0, 2))
plt.show()


# In[37]:


# 1度[batch, ch, H, W]の形に変形する必要あり
img_tensor = torch.tensor(np.copy(img)).unsqueeze(dim=0)

img_small = torch.nn.functional.interpolate(img_tensor, size=None, scale_factor=0.1)
print(img_small.shape)
plt.imshow(img_small[0].transpose(0, 2))
plt.show()


# In[38]:


# 1度[batch, ch, H, W]の形に変形する必要あり
img_tensor = torch.tensor(np.copy(img)).unsqueeze(dim=0)

img_small = torch.nn.functional.interpolate(img_tensor, size=(20, 20))
print(img_small.shape)
plt.imshow(img_small[0].transpose(0, 2))
plt.show()


# In[ ]:




