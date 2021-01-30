#!/usr/bin/env python
# coding: utf-8

# ## Capstone project2

# In[38]:


#Importing relavent lib
import numpy as np 
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import json 
from geopy.geocoders import Nominatim
import requests # 
from pandas.io.json import json_normalize 
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
import folium # map rendering library

print('Libraries imported.')


# In[39]:


#Capture Data frame from wikipedia by using panda
df=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")[0]
df.head(5)


# In[52]:


#Data cleaning
df=df[df.Borough != 'Not assigned'] #drop the cell with column of Borough contains Not assigned 
df=df.groupby(['Postal Code','Borough'])['Neighbourhood'].apply(",".join).reset_index() #Join neighbourhood which shares same borough
df['Neighbourhood']=np.where(df['Neighbourhood'] == 'Not assigned', df['Borough'], df['Neighbourhood'])#If neighbourhood has not assigned value, replace it with borough
df#print out the result


# In[53]:


df.shape


# In[ ]:




