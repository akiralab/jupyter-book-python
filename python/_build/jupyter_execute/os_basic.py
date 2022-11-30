#!/usr/bin/env python
# coding: utf-8

# # osの基本的な使い方
# 
# ### path操作系
# 1. os.path.exists()
# 2. os.path.join(DIR_NAME, ...)
# 3. os.makedirs(PATH, exist_ok=True)
# 4. os.rename(OLD_PATH, NEW_PATH)
# 5. os.listdir(PATH)
# 
# ### 検索系
# 6. os.walk(ROOT_DIR)

# In[1]:


import os


# ### 1. pathが存在するか確認する -> `os.path.exists(PATH)`

# In[2]:


os.path.exists('../src/sample.jpg')


# ### 2. pathを作成する -> `os.path.join(DIR_NAME, ...)`

# In[3]:


os.path.join('../src', 'test.txt')


# ### 3. ディレクトリを作成する -> `os.makedirs(PATH, exist_ok=True)`

# In[4]:


path = '../src/test'
os.makedirs(path, exist_ok=True)
os.path.exists(path)


# ### 4. ディレクトリもしくはファイルの名前を変更する -> `os.rename(OLD_PATH, NEW_PATH)`

# In[5]:


old_name = '../src/test'
new_name = '../src/test1'

os.rename(old_name, new_name)


# ### 5. ディレクトリのファイル名をリストアップする -> `os.listdir(DIR)`

# In[6]:


os.listdir('../')


# ### 6. ディレクトリ内部のroot, dir名, file名を一覧表示する -> os.walk(PATH)

# In[7]:


for (root, dirs, files) in os.walk('../python/'):
    print('root', root)
    print('---dirs', dirs)
    print('---files', files)
    print('-'*40)    


# In[ ]:





# In[ ]:





# In[ ]:




