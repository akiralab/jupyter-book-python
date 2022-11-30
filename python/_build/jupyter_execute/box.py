#!/usr/bin/env python
# coding: utf-8

# # Box
# - 深い階層を伴う辞書式配列に対してデータを引っ張ってくるときに便利
# - configなどに使用すると便利

# In[1]:


# !pip install python-box
from box import Box


# In[2]:


data = {
    "movies": {
        "Spaceballs": {
            "imdb stars": 7.1,
            "rating": "PG",
            "length": 96,
            "director": "Mel Brooks",
            "stars": [
                {"name": "Mel Brooks", "imdb": "nm0000316",
                    "role": "President Skroob"},
                {"name": "John Candy", "imdb": "nm0001006", "role": "Barf"},
                {"name": "Rick Moranis", "imdb": "nm0001548",
                 "role": "Dark Helmet"}
            ]
        }
    }
}


# In[3]:


box_data = Box(data)


# In[4]:


# 辞書式配列の深い階層の値もJSのように引っ張ってくることができる
box_data.movies.Spaceballs.director


# In[ ]:




