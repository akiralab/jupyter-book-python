#!/usr/bin/env python
# coding: utf-8

# # itertools
# - 時々しか使わないけれど、便利なツール

# ### 組み合わせを出力してくれる

# In[1]:


import itertools
p_list = [1, 2, 3, 4, 5]
list(itertools.combinations(p_list, 2))


# ### （例）Nある商品の中から、M個選んだ時の値段をリスト化する

# In[2]:


products = {
    'a' : 100,
    'b' : 500,
    'c' : 200,
    'd' : 400,
    'e' : 600,
    'f' : 1000,
    'g' : 2000,
    'h' : 5000,
}


# In[3]:


# 2つ選ぶ時
carts = list(itertools.combinations(products.keys(), 2))
print('---商品は全部で{}種類'.format(len(products)))
print('---組み合わせは全部で{}通り'.format(len(carts)))


# In[4]:


for cart in carts:
    bill = np.array([products[item] for item in cart]).sum()
    print('---組み合わせが{}の時、合計金額は{}円'.format(cart, bill))
    # break


# In[33]:


bills = {}
for cart in carts:
    bill = np.array([products[item] for item in cart]).sum()
    bills[cart] = bill


# In[41]:


sorted_bills = sorted(bills.items(), key=lambda x:x[1])

print('---もっとも安い組み合わせは、{}の時で、合計金額は{}円'.format(sorted_bills[0][0], sorted_bills[0][1]))
print('---もっとも高い組み合わせは、{}の時で、合計金額は{}円'.format(sorted_bills[-1][0], sorted_bills[-1][1]))


# In[ ]:




