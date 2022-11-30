#!/usr/bin/env python
# coding: utf-8

# # seed_everything
# - pytorch, numpy, python.randomのseedを一括で設定するためのモジュール
# - [document](https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.utilities.seed.html)

# In[1]:


from pytorch_lightning.utilities.seed import seed_everything


# In[2]:


# seedを設定する
seed_everything(10)


# In[ ]:




