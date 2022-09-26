#!/usr/bin/env python
# coding: utf-8

# # [plt] cmap
# 
# ### 概要
# - pltにはカラースケールを変更するオプションがある
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import cv2


# grayscaleで読み込んだはずの画像が、defaultでは黄緑のスケールとなってしまう -> pltのデフォルトでは、黄緑のスケールとなっているから

# In[2]:


img = cv2.imread('../src/lena.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(img)


# - cmapのデフォルトはこちらの"viridis"となっている(https://matplotlib.org/stable/tutorials/colors/colormaps.html)
# ![image.png](attachment:ce8d7492-23b1-4e3a-b5aa-824ca3e92448.png)

# ### これだけ覚えておきたいcmapを列挙

# In[27]:


cmaps = ['viridis', 'gray', 'gnuplot', 'binary']

plt.figure(figsize=[15, 3])
for idx, cmap in enumerate(cmaps):
    plt.subplot(1, len(cmaps), idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# ### cmapを全部列挙

# In[14]:


cmaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

plt.figure(figsize=[15, 3])
for idx, cmap in enumerate(cmaps):
    plt.subplot(1, len(cmaps), idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[24]:


cmaps = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges',
         'Reds','YlOrBr', 'YlOrRd', 'OrRd', 'PuRd',
         'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu',
         'PuBuGn', 'BuGn', 'YlGn']

plt.figure(figsize=[15, 12])
for idx, cmap in enumerate(cmaps):
    plt.subplot(len(cmaps)//5+1, 5, idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[25]:


cmaps = ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
         'pink', 'spring', 'summer', 'autumn', 'winter',
         'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat',
         'copper']

plt.figure(figsize=[15, 12])
for idx, cmap in enumerate(cmaps):
    plt.subplot(len(cmaps)//5+1, 5, idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[20]:


cmaps = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy',
         'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm',
         'bwr', 'seismic']

plt.figure(figsize=[15, 9])
for idx, cmap in enumerate(cmaps):
    plt.subplot(len(cmaps)//5+1, 5, idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[21]:


cmaps = ['twilight', 'twilight_shifted', 'hsv']

plt.figure(figsize=[15, 3])
for idx, cmap in enumerate(cmaps):
    plt.subplot(len(cmaps)//5+1, 5, idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[22]:


cmaps = ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
         'Set1', 'Set2', 'Set3', 'tab10', 'tab20',
         'tab20b','tab20c']

plt.figure(figsize=[15, 9])
for idx, cmap in enumerate(cmaps):
    plt.subplot(len(cmaps)//5+1, 5, idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[23]:


cmaps = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain',
         'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix',
         'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo',
         'nipy_spectral', 'gist_ncar']

plt.figure(figsize=[15, 12])
for idx, cmap in enumerate(cmaps):
    plt.subplot(len(cmaps)//5+1, 5, idx+1)
    plt.imshow(img, cmap=cmap), plt.axis('off'), plt.title(cmap)
plt.show()


# In[ ]:




