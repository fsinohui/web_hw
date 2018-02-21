# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:35:51 2018

@author: Rayzel
"""

import random
from citipy import citipy
import pandas as pd
import requests as req
import json
import matplotlib.pyplot as plt

api_key = "afbde06f4217fea7175e8c03acbc3eac"
url = "http://api.openweathermap.org/data/2.5/weather?"
units = 'imperial'
query_url = url + "appid=" + api_key + "&units=" + units + "&q="

count = 0
lats = []
lngs = []

while count < 1200:
    lats.append(random.uniform(-90,90))
    lngs.append(random.uniform(-180,180))
    count = count+1
    
cities = ['london']
countries =['GB']
for lat, lng in zip(lats, lngs):
    cityid = citipy.nearest_city(lat, lng)
    city = cityid.city_name
    country = cityid.country_code
    cities.append(city)
    countries.append(country)
    
    
temp_data       = []
lon_data        = [] 
temp_data       = []
lat_data        = []
humidity_data   = []
cloud_data      = []
wind_data       = []

for city in cities:
    weather_json = req.get(query_url + city).json()
    try:
        temp_data.append(weather_json['main']['temp'])
        lon_data.append(weather_json['coord']['lon'])
        lat_data.append(weather_json['coord']['lat'])
        humidity_data.append(weather_json['main']['humidity'])
        cloud_data.append(weather_json['clouds']['all'])
        wind_data.append(weather_json['wind']['speed'])
    except:
        #print('no city found')
        cat='dog'

weather_data = {"lon": lon_data, 'temp':temp_data, 'lat':lat_data,'humidity':humidity_data, 'cloud':cloud_data, 'wind': wind_data}
weather_data = pd.DataFrame(weather_data)
weather_data.head()


weather_df = weather_data.drop_duplicates(keep='first')
weather_df.head()

# Build a scatter plot for each data type
plt.scatter(weather_data["lat"], weather_data["temp"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Temperature")
plt.xlabel("Latitude")
plt.show()

plt.scatter(weather_data["lat"], weather_data["humidity"], marker="o")
plt.title("Humidity in World Cities")
plt.ylabel("Humidity")
plt.xlabel("Latitude")
plt.show()

plt.scatter(weather_data["lat"], weather_data["cloud"], marker="o")
plt.title("Cloudiness in World Cities")
plt.ylabel("Cloudiness")
plt.xlabel("Latitude")
plt.show()

plt.scatter(weather_data["lat"], weather_data["wind"], marker="o")
plt.title("wind in World Cities")
plt.ylabel("Wind Speed")
plt.xlabel("Latitude")
plt.show()
    
    
    
    
    
    
    
    
    
    
    
 