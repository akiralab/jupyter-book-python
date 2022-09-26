#!/usr/bin/env python
# coding: utf-8

# # [torchvision] model 
# 
# ### 概要
# - torchvisionには、pretrain済のmodelが多数準備してあり、簡単に読み込むことができる
# 
# ### どんな時に便利か
# - 同じモデルでも異なるweightを読み込むことができる
# - tryしてみたがまだ実装中だった機能、後日再チャレンジ
# - https://pytorch.org/blog/easily-list-and-initialize-models-with-new-apis-in-torchvision/?utm_source=twitter&amp;utm_medium=organic_social&amp;utm_campaign=blog-newAPIs

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import torchvision
print(torchvision.__version__)


# In[2]:


model_name = "resnet50"
model = torchvision.models
# model.__dict__
# from torchvision.models import  get_model_weights, get_weight, list_models


# In[ ]:




