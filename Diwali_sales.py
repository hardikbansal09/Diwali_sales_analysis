#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd #arrays 
import numpy as np #dataframe
import matplotlib.pyplot as plt #visualization data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns #visualization data


# In[14]:


df=pd.read_csv("E:\DS_DA\project\diwali sales\Diwali Sales Data.csv",encoding='unicode_escape')


# In[15]:


df.shape #rows and columns


# In[16]:


df.head() #top 5 rows


# In[17]:


df.info()


# In[18]:


#drop unrelated/blank columns,axis->vertical row,inplace->save in the same line
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[19]:


pd.isnull(df)


# In[20]:


pd.isnull(df).sum()


# In[23]:


df.shape


# In[25]:


df.dropna(inplace=True)
#drop null values


# In[27]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[28]:


df['Amount'].dtypes


# In[29]:


df.columns


# In[30]:


#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})


# In[31]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()


# In[32]:


# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis
# 

# # Gender
# 

# In[34]:


df.columns


# In[35]:


ax=sns.countplot(x='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[36]:


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# In[37]:


##AGE##


# In[38]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[39]:


# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# state

# In[40]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[41]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# Marital Status# 

# In[43]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# # Occupation

# In[45]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# #Product Category 

# In[47]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[48]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[49]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[50]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




