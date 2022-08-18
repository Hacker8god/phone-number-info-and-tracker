from unittest import result
import phonenumbers
import folium
import opencage

#for country name
from num import number
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
location = geocoder.description_for_number(ch_number,"en")
print(geocoder.description_for_number(ch_number,"en"))

#for service provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))

#for location
from opencage.geocoder import OpenCageGeocode
key = 'ad48a37f012c45498d95d7da2c7d3cf5'
geocoder =OpenCageGeocode(key)
query =str(location)
results=geocoder.geocode(query)
print(results) 

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("trackedlocation.html")