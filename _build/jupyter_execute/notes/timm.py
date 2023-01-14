#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install timm
# !apt install graphviz
# !pip install torchviz

import timm
import torch
from torchviz import make_dot, make_dot_from_trace


# # timmとは
# ```
# `timm` is a deep-learning library created by Ross Wightman and is a collection of SOTA computer vision models, layers, utilities, optimizers, schedulers, data-loaders, augmentations and also training/validating scripts with ability to reproduce ImageNet training results.
# ```
# 

# In[2]:


model = timm.create_model('resnet34')
# model


# In[4]:


x = torch.randn(1,3, 768, 768)
make_dot(model(x), params=dict(model.named_parameters()), show_attrs=True, show_saved=True)


# In[ ]:




