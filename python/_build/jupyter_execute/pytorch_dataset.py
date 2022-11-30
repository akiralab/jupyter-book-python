#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt


# In[2]:


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)


# In[3]:


training_data


# In[35]:


img, label = training_data[0]
# plt.imshow(img.squeeze(), cmap="gray")
plt.imshow(img.squeeze(), cmap="gnuplot")
plt.title(label.item())


# In[21]:


plt.figure(figsize=[9, 9])
for i in range(9):
    img, label = training_data[i]
    plt.subplot(3, 3, i+1)
    plt.imshow(img.squeeze(), cmap="gray")
    plt.title(label.item())
    plt.axis('off')


# In[ ]:




