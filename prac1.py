#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as py
from scipy import stats 
import matplotlib
import matplotlib.pyplot as plt


# In[40]:


get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.style.use('ggplot')

data =[5.2,3.2,5.7,6.9,2.8,3.5,6.7,7.8,7.3,7.2,9.5,4.5,4.2,2.8,3.2,4.9,5.9,9.2,5.7,4.5];
print("Array is ",data);
plt.hist(data, bins=10, range=(0,10), edgecolor='black');
plt.show();


# In[41]:


mean = py.mean(data)
mean


# In[42]:


py.median(data)


# In[43]:


mode = stats.mode(data)

print("The modal value is {} with a count of {}".format(mode.mode[0], mode.count[0]))


# In[44]:


py.ptp(data)  


# In[45]:


py.var(data)


# In[46]:


py.std(data)


# In[47]:


stats.sem(data)


# In[ ]:




