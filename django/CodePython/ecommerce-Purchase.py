
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom
ecom = pd.read_csv('ecommerce.txt')


# In[3]:


#Check the head of the DataFrame.
ecom.head(2)


# In[6]:


#How many rows and columns are there? 
len(ecom.columns)


# In[7]:


len(ecom.index)


# In[11]:


#How many people have English 'en' as their Language of choice on the website? 
ecom["Language"].value_counts()["en"]


# In[16]:


#How many people have English 'en' as their Language of choice on the website? 
ecom[ecom['Language']=="en"]["Language"].count()


# In[17]:


#How many people have English 'en' as their Language of choice on the website? 
ecom["Language"].value_counts().loc["en"]


# In[24]:


##How many people have the job title of "Lawyer" ? 
ecom[ecom["Job"]=="Lawyer"]["Job"].count()


# In[26]:


##How many people have the job title of "Lawyer" ? 
len(ecom[ecom["Job"]=="Lawyer"].index)


# In[31]:


#How many people made the purchase during the AM and how many people made the purchase during PM ? 
#ecom["AM or PM"].unique()
ecom["AM or PM"].value_counts()


# In[33]:


#What are the 5 most common Job Titles? 
ecom["Job"].value_counts().head(5)


# In[34]:


#What are the 5 most common Job Titles? 
ecom.groupby('Job').count().sort_values(by='Company', ascending=False)['Address'].head(5)


# In[37]:


#Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? 
ecom[ecom["Lot"]=="90 WT"]["Purchase Price"]


# In[39]:


#What is the email of the person with the following Credit Card Number: 4926535242672853 
ecom[ecom["Credit Card"]==4926535242672853]["Email"]


# In[50]:


#How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)].count()


# In[51]:


#How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
len(ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)].index)


# In[70]:


ecom["CC Exp Date"].loc[0][3:]


# In[74]:


ecom["CC Exp Date"].loc[0].split('/')[1]


# In[69]:


#How many people have a credit card that expires in 2025? 
len(ecom[ecom["CC Exp Date"].apply(lambda exp: exp[3:]=="25")].index)


# In[75]:


#How many people have a credit card that expires in 2025? 
ecom['ExpiryYear'] = ecom['CC Exp Date'].apply(lambda x: x.split('/')[-1]) #last element after / has year
ecom[ecom['ExpiryYear'] == '25'].count()['Lot']


# In[83]:


ecom["Email"].loc[0].split("@")[1]


# In[94]:


exemple = ecom["Email"].iloc[0]
exemple.split("@")[1]


# In[87]:


#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) 
ecom["Email"].apply(lambda pop: pop.split("@")[1]).value_counts().head(5)


# In[ ]:


#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) 
ecom['EmailHost'] = ecom['Email'].apply(lambda x: x.split('@')[-1])
ecom['EmailHost'].value_counts().sort_values(ascending=False).head(5)


# In[5]:


#What is the average Purchase Price? 
ecom["Purchase Price"].mean()


# In[8]:


#What were the highest and lowest purchase prices? 
ecom["Purchase Price"].max()


# In[9]:


ecom["Purchase Price"].min()


# In[89]:


ecom.columns


# In[88]:


ecom.info()

