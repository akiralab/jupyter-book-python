#!/usr/bin/env python
# coding: utf-8

# # shutil
# - sh + utilから名称が来ている
# - ファイルのコピーや移動を自在に行うことができるツール

# In[1]:


import os, shutil
path = '../src/a/sample.txt'
os.path.exists(path)


# ### `../src/a/` -> `../src/b/`に移動させる

# In[2]:


src_path = '../src/a/sample.txt'
dst_dir = '../src/b/'

shutil.move(src_path, dst_dir)


# In[9]:


# 元のPathからは移動が完了していることが確認できる
print('移動元のディレクトリ--->', os.path.exists('../src/a/sample.txt'))
print('移動先のディレクトリ--->', os.path.exists('../src/b/sample.txt'))

