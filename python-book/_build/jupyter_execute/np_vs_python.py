#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import time


# In[2]:


# Python vs Numpy
start = time.time()
data = np.arange(1000)
for i in range(1000):
    sum(data)
end = time.time()
t_python = (end - start) * 1000

start = time.time()
data = np.arange(1000)
for i in range(1000):
    np.sum(data)
end = time.time()

t_numpy = (end - start) * 1000

print('Numpy is {} times faster than Python-default method'.format(t_python/t_numpy))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('time(ms)')
plt.barh(np.arange(2), [t_python, t_numpy], tick_label=["Python", "Numpy"], color='b')


# In[3]:


# Numpy.mean() vs np.average() vs python sum()/len()
start = time.time()
data = np.arange(1000)
for i in range(1000):
    sum(data)/len(data)
end = time.time()
t_python = (end - start) * 1000

start = time.time()
data = np.arange(1000)
for i in range(1000):
    np.average(data)
end = time.time()

t_numpy_1 = (end - start) * 1000

start = time.time()
data = np.arange(1000)
for i in range(1000):
    np.mean(data)
end = time.time()

t_numpy_2 = (end - start) * 1000

print('Numpy(average) is {} times faster than Python-default method'.format(t_python/t_numpy))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('time(ms)')
plt.barh(np.arange(3), [t_python, t_numpy_1, t_numpy_2], tick_label=["Python", "Numpy(average)", "Numpy(mean)"], color='b')


# In[4]:


# Python vs Numpy
start = time.time()

a, b = 2, 3
data = np.zeros((128, 128))

for x in range(128):
    for y in range(128):
        if y >= a * x + b:
            data[x][y] = 1
t_python = (end - start) * 1000

end = time.time()

a, b = 2, 3
data = np.zeros((128, 128))

start = time.time()

x = np.arange(128)
y = a * x + b

for x in range(128):
    data[x][:int(y[x])] = 1

end = time.time()

t_numpy = (end - start) * 1000

print('Numpy is {} times faster than Python-default method'.format(t_python/t_numpy))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('time(ms)')
plt.barh(np.arange(2), [t_python, t_numpy], tick_label=["Python", "Numpy"], color='b')


# In[ ]:




