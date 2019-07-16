#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = ['q1', 'q2', 'q3', 'q4']
y = [10, 20, 30, 50]

plt.bar(x,y,color='r',width=0.5)
plt.grid(True)
plt.show()


# In[3]:


x = ['q1', 'q2', 'q3', 'q4']
y = [10, 20, 30, 50]

rect = plt.bar(x,y,color='r',width=0.5)
# plt.text(2,20,'test') # 在（2，20）的位置写字
for ind,item in enumerate(rect):
    _x = item.get_x()+0.15
    _y = item.get_height()+1
    plt.text(_x,_y,y[ind])
plt.ylim(0,60)  #更改y的范围
# plt.grid(True)
plt.show()


# In[4]:


plt.pie(y,labels=x)
plt.show()


# In[5]:


plt.pie(y,labels=x,autopct='%.1f%%')
plt.show()


# In[6]:


plt.axes(aspect=1)
plt.pie(y,labels=x,autopct='%.1f%%')
plt.show()


# In[11]:


plt.pie(y,labels=x,autopct='%.1f%%',explode=[0,0.2,0,0],shadow=True)
plt.show()


# In[ ]:




