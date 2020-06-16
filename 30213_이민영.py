#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[22]:


path = 'data1.csv'


# In[23]:


path


# In[24]:


df=pd.read_csv(path,encoding = 'cp949')


# In[25]:


df


# In[26]:


null_count = df.isnull().sum()


# In[27]:


df_null_count = null_count.reset_index()
df_null_count


# In[28]:


df_null_count.columns = ['메뉴','결측값']


# In[29]:


df_null_count


# In[30]:


df_2 = df_null_count.tail(2)


# In[31]:


df_2


# In[32]:


drop_columns = df_2['메뉴']


# In[33]:


drop_columns


# In[34]:


drop_columns.to_list()


# In[35]:


df[drop_columns]


# In[37]:


df_5=df.drop(drop_columns,axis=1)


# In[45]:


df_5.head(10)

