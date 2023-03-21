#!/usr/bin/env python
# coding: utf-8

# In[1]:


from geopy.geocoders import Nominatim


# In[2]:


geolocator = Nominatim(user_agent="geoapiExercises")
 
# Assign Latitude & Longitude
Latitude = "26.2314"
Longitude = "78.2053"
 
# Displaying Latitude and Longitude
print("Latitude: ", Latitude)
print("Longitude: ", Longitude)


# In[3]:


# Get location with geocode
location = geolocator.geocode(Latitude+","+Longitude)
 
# Display location
print("\nLocation of the given Latitude and Longitude:")
print(location)


# In[6]:


import pandas as pd 
import numpy as np
    
# Define a dictionary containing  data 
data = {'place':['jaipur junction', 'amber fort jaipur','hawa mahal jaipur','city palace jaipur','jantar mantar jaipur','ram mandir cinema jaipur','patrika gate jaipur','university of rajasthan jaipur']} 
    
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 
    
# Observe the result 
df 
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
   
# declare an empty list to store
# latitude and longitude of values 
# of city column
longitude = []
latitude = []
   
# function to find the coordinate
# of a given city 
def findGeocode(place):
       
    # try and catch is used to overcome
    # the exception thrown by geolocator
    # using geocodertimedout  
    try:
          
        # Specify the user_agent as your
        # app name it should not be none
        geolocator = Nominatim(user_agent="your_app_name")
          
        return geolocator.geocode(place)
      
    except GeocoderTimedOut:
          
        return findGeocode(place)    
    # each value from city column
# will be fetched and sent to
# function find_geocode   
for i in (df["place"]):
      
    if findGeocode(i) != None:
           
        loc = findGeocode(i)
          
        # coordinates returned from 
        # function is stored into
        # two separate list
        latitude.append(loc.latitude)
        longitude.append(loc.longitude)
       
    # if coordinate for a city not
    # found, insert "NaN" indicating 
    # missing value 
    else:
        latitude.append(np.nan)
        longitude.append(np.nan)
df["Longitude"] = longitude
df["Latitude"] = latitude
  
df


# In[ ]:




