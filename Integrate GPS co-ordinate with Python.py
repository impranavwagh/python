#!/usr/bin/env python
# coding: utf-8

# In[4]:


import geopy


# In[5]:


import folium


# In[9]:


geolocator = geopy.Nominatim(user_agent="GetLoc")


# In[10]:


locname = geolocator.reverse("26.92552825725126, 75.77955512259769")


# In[11]:


print(locname)


# In[ ]:





# In[14]:





# In[19]:


name = geolocator.geocode("Mumbai")


# In[20]:


#it will print latitude and longitude
print(name.latitude, name.longitude)


# In[ ]:




