#!/usr/bin/env python
# coding: utf-8

# In[38]:


from statistics import *
import pandas as pd


# In[39]:


data = pd.read_csv("/Users/administrator/Desktop/eurofxref-hist.csv")


# In[28]:


data.shape


# In[40]:


data


# In[41]:


data = data.drop(columns=['Unnamed: 42'])


# In[42]:


data


# In[43]:


list(data.columns)


# In[44]:


data.describe().round(4)


# In[ ]:





# In[ ]:




