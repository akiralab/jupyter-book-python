#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://qiita.com/osanshouo/items/3c66781f41884694838b
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

fig = plt.figure()
ax = fig.add_subplot(111, aspect=1)

theta = np.linspace(0, 2*np.pi, 128)

def update(f):
    ax.cla() # ax をクリア
    ax.grid()
    ax.plot(np.cos(theta), np.sin(theta), c="gray")
    ax.plot(np.cos(f), np.sin(f), "o", c="red")

anim = FuncAnimation(fig, update, frames=np.pi*np.arange(0,2,0.25), interval=200)

# anim.save("c03.gif", writer="imagemagick")
# plt.close()
HTML(anim.to_html5_video())


# In[14]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.

ani.save("movie.mp4")

# or

writer = animation.FFMpegWriter(
    fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("movie.mp4", writer=writer)

plt.show()


# In[ ]:




