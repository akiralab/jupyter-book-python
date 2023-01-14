#!/usr/bin/env python
# coding: utf-8

# In[16]:


import timm
import torch
import pprint
# from torchviz import make_dot, make_dot_from_trace


# # timmとは
# ```
# `timm` is a deep-learning library created by Ross Wightman and is a collection of SOTA computer vision models, layers, utilities, optimizers, schedulers, data-loaders, augmentations and also training/validating scripts with ability to reproduce ImageNet training results.
# ```
# (参考)
# 
# https://timm.fast.ai/
# 
# https://huggingface.co/docs/timm/quickstart

# ## いくつモデルががるのか

# In[112]:


aveil_models = timm.list_models()
avail_pretrained_models = timm.list_models(pretrained=True)

print(f'モデル数: {len(aveil_models)}')
print(f'モデル数(pretrained): {len(avail_pretrained_models)}')


# ## どんなモデルがあるのか

# In[113]:


timm.list_models()[:10]


# In[114]:


# 検索も可能
timm.list_models("*efficientnet*", pretrained=True)


# In[115]:


# 検索も可能
timm.list_models("*YOLO*", pretrained=True)


# In[123]:


# 検索も可能
timm.list_models("*mobilenet*", pretrained=True)


# # それぞれのモデルのサイズを計測してみる
# 
# 参考： https://discuss.pytorch.org/t/finding-model-size/130275

# In[121]:


def calc_model_size(model):
    param_size = 0
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()
    buffer_size = 0
    for buffer in model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()

    size_all_mb = (param_size + buffer_size) / 1024**2
    return size_all_mb


# In[124]:


for model_name in timm.list_models("*mobilenet*", pretrained=True):
    model = timm.create_model(model_name)
    model_size = calc_model_size(model)
    print(f"{model_name:40}: {model_size:6.1f}MB")


# In[122]:


for model_name in timm.list_models("*efficientnet*", pretrained=True):
    model = timm.create_model(model_name)
    model_size = calc_model_size(model)
    print(f"{model_name:40}: {model_size:6.1f}MB")


# In[128]:


for model_name in timm.list_models("*resnet*", pretrained=True):
    model = timm.create_model(model_name)
    model_size = calc_model_size(model)
    print(f"{model_name:40}: {model_size:6.1f}MB")


# # モデルを作成する

# In[132]:


model = timm.create_model('efficientnet_b0', pretrained=True)
# model = timm.create_model('mobilenetv2_050')
output = model(torch.rand(1, 3, 224, 224))
print(output.shape)


# ## 入力や出力のCHを変更することも可能

# In[137]:


model = timm.create_model('efficientnet_b0', pretrained=True, in_chans=10)
output = model(torch.rand(1, 10, 224, 224))
print(output.shape)


# In[138]:


model = timm.create_model('efficientnet_b0', pretrained=True, num_classes=10)
output = model(torch.rand(1, 3, 224, 224))
print(output.shape)


# In[142]:


model = timm.create_model('efficientnet_b0', pretrained=True, in_chans=5, num_classes=5)
output = model(torch.rand(1, 5, 224, 224))
print(output.shape)


# ## weightの読み込み方法の変更
# - https://timm.fast.ai/models#How-is-timm-able-to-use-pretrained-weights-and-handle-images-that-are-not-3-channel-RGB-images?

# In[143]:


from timm.models.resnet import ResNet, BasicBlock, default_cfgs
from timm.models.helpers import load_pretrained
from copy import deepcopy


# In[146]:


resnet34_default_cfg = default_cfgs['resnet34']
resnet34 = ResNet(BasicBlock, layers=[3, 4, 6, 3], in_chans=1)
resnet34.default_cfg = deepcopy(resnet34_default_cfg)

resnet34.conv1


# In[ ]:




