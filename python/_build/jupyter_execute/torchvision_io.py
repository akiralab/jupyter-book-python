#!/usr/bin/env python
# coding: utf-8

# ## torchvision.ioとは？
# 
# ### 概要
# 
# - IO処理を行うことができる
# - imagesやvideoを読み込んだり出力したりできる
# 
# ### 使用するメリット
# 
# - 出力がTensorなので、pytorchと相性がいい
# 
# ### 参考
# - https://pytorch.org/vision/stable/io.html

# In[1]:


from torchvision.io import read_image, decode_image, encode_jpeg


# In[2]:


### torchvision.io.read_image(path: str) -> return Tensor([ch, h, w])
path = '../src/sample.jpg'
image = read_image(path)
image.shape


# In[55]:


import matplotlib.pyplot as plt
import torchvision.transforms as T

image_size = 228
transform = T.Resize([image_size, image_size])
image = transform(image)
image = image.permute(1, 2, 0)


# In[56]:


plt.imshow(image)


# In[ ]:





# In[ ]:




