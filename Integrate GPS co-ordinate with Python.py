import geopy
import folium

# for finding location by latitude and longitude
geolocator = geopy.Nominatim(user_agent="GetLoc")

locname = geolocator.reverse("26.92552825725126, 75.77955512259769")

print(locname)



#finding longitude and latitude by name of area
name = geolocator. Geocode("Mumbai")

#it will print latitude and longitude
print(name.latitude, name. Longitude)

