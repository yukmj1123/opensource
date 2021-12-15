#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas


# In[97]:


import pandas as pd
import numpy as np
df = pandas.read_csv('C:/Users/82109/Desktop/daegu_test.csv', encoding='cp949')


# In[98]:


print(df.dtypes)


# In[102]:


print(df.groupby('spot')[['tourist1','tourist2','tourist3','tourist4']].mean())


# In[103]:


import matplotlib.pyplot as plt


# In[104]:


area_tourist = df.groupby('spot')[['tourist1','tourist2','tourist3','tourist4']].mean()


# In[105]:


area_tourist.plot()


# In[106]:


from sklearn.linear_model import LinearRegression


# In[107]:


from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# In[108]:


import numpy as np


# In[114]:


traindata = pd.read_csv('C:/Users/82109/Desktop/daegu_test.csv')
x = pd.DataFrame(traindata.spot, columns = traindata.spot )
y = pd.DataFrame(traindata.tourist1, columns = traindata.tourist1)


# In[115]:


x


# In[116]:


y


# In[ ]:




