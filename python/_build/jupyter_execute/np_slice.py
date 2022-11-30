#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# slice: [start:end:span]
a = np.arange(10)

# 全選択
print('a[:]', a[:])
# 前半のみ
print("a[:5] ", a[:5])
# 後半のみ
print('a[5:] ', a[5:])
# 間隔を2に設定
print('a[::2]', a[::2])


# In[3]:


from keras.datasets import mnist
(train_x, _), (_, _) = mnist.load_data()
image = train_x[0]
plt.imshow(image)
plt.axis('off')
print('shape:',image.shape)


# In[4]:


# 画像の右半分を白にする
image_left, image_right = np.zeros((2, 28, 28))
image_left[:, :14] = image[:, :14]
image_right[:, 14:] = image[:, 14:]

plt.subplot(121)
plt.imshow(image_left)
plt.axis('off')
plt.subplot(122)
plt.imshow(image_right)
plt.axis('off')


# In[5]:


# 画像を斜めにトリミング
# forでループもできるが、numpyを高速稼働させるためにsliceを使用
x = np.arange(28)
mask = np.ones((28,28))

for i in range(28):
    mask[i, :x[i]] = 0

plt.subplot(121)
plt.imshow(mask)
plt.subplot(122)
plt.imshow(mask*image)


# In[ ]:





# In[ ]:




