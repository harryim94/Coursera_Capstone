#!/usr/bin/env python
# coding: utf-8

# ## Capstone project2

# In[54]:


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


# In[55]:


#Capture Data frame from wikipedia by using panda
df=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")[0]
df.head(5)


# In[56]:


#Data cleaning
#Notice my data is sorted by Borough
df=df[df.Borough != 'Not assigned'] #drop the cell with column of Borough contains Not assigned 
df=df.groupby(['Postal Code','Borough'])['Neighbourhood'].apply(",".join).reset_index() #Join neighbourhood which shares same borough
df['Neighbourhood']=np.where(df['Neighbourhood'] == 'Not assigned', df['Borough'], df['Neighbourhood'])#If neighbourhood has not assigned value, replace it with borough
df#print out the result


# In[57]:


df.shape


# In[ ]:


#Second part


# In[68]:


#read data and store in data frame
loca=pd.read_csv("https://cocl.us/Geospatial_data")
loca.head()


# In[71]:


#merge the data
df_merged=pd.merge(df,loca,on="Postal Code")
df_merged


# In[ ]:


#Third parts


# In[80]:


#capturing all the data for only toronto in borough
df=df_merged[df_merged.Borough.str.contains("Toronto")]
df


# In[82]:


#Clustering
toronto=folium.Map(location=[43.651070,-79.347015],zoom_start=10)
for latitude,longitude,borough,neighbourhood in zip(df['Latitude'],df['Longitude'],df['Borough'],df['Neighbourhood']):
    label = '{}, {}'.format(neighbourhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
    [latitude,longitude],
    radius=5,
    popup=label,
    color='blue',
    fill=True,
    fill_color='#3186cc',
    fill_opacity=0.7,
    parse_html=False).add_to(toronto)
toronto


# In[ ]:




