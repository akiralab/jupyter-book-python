#!/usr/bin/env python
# coding: utf-8

# # [newspaper]
# 
# ### 概要
# - 記事をスクレイピングするためのライブラリ
# 
# ### 使い方
# - サイトのトップページから複数のページをまとめて取得する
# 
# ### 参考
# - https://github.com/codelucas/newspaper
# - [Pythonでスクレイピングによるニュース記事の取得と保存(CSVデータ)
# ](https://ai-inter1.com/webscraping_newspaper_2/)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ### newspaperをimportする

# In[2]:


# !pip3 install newspaper3k
import newspaper

# 必要ライブラリのインストール
# https://github.com/codelucas/newspaper/blob/master/requirements.txt


# ### CNNのサイトから記事を収集する
# - 一度buildすると、一定時間buildできない可能性あり

# In[3]:


cnn_paper = newspaper.build('http://cnn.com')


# In[4]:


for article in cnn_paper.articles:
    print(article.url)
    print(article.title)


# In[5]:


print(cnn_paper.size())


# In[ ]:





# In[ ]:





# In[6]:


article.download()


# In[7]:


# article.html
article.parse()


# In[8]:


article.authors


# In[9]:


article.publish_date


# In[10]:


article.text


# In[11]:


article.top_image


# In[12]:


# !pip install --user -U nltk
import nltk
nltk.download('punkt')
article.nlp()


# In[13]:


article.keywords


# In[14]:


article.summary


# ### hotなキーワードを探す

# In[15]:


newspaper.hot()


# In[16]:


newspaper.popular_urls()[:10]


# ### 試しに日経新聞をスクレイピングしてみる

# In[17]:


url = "https://www.nikkei.com/technology/ai/"


# In[18]:


website = newspaper.build(url)


# In[19]:


for item, article in enumerate(website.articles):
    website_article = website.articles[item]
    website_article_url = website_article.url
    try:
        website_article.download()
        website_article.parse()
        website_article.nlp()
        print("記事[" + str(item) + "]: "+ website_article_url +" : " + website_article.summary + "\n")
    except:
        print("記事[" + str(item) + "]: "+ website_article_url +" : " + "取得エラー" + "\n")
    continue


# In[ ]:




