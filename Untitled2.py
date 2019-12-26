#!/usr/bin/env python
# coding: utf-8

# In[15]:



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[16]:


df = [4,55,21,33,5,92,33,5,91,33,9,29,99,105,39,45,6,62,65,25,10,73,85,11,79,20,56,45,21,8,65,70,30]
print(df);
df.sort();
print("AFTER SORT:",df);


# In[17]:


sns.boxplot(data=df,color='y')
sns.swarmplot(data=df,color='b');


# In[20]:


sns.boxplot(data=df)
print("MINIMUM IS :",min(df));
print("MAXIMUM IS :",max(df));
df.sort();
print(sum(df))


# In[ ]:




