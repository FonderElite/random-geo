import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
latitude = input("Latitude: ")
longitude  = input("Longitude: ")
def reverse_geo_locate(lat,long): 
 locator = Nominatim(user_agent='Geo_Locator')
 coordinates = lat,long
 location = locator.reverse(coordinates)
 location.raw
 print(location)
reverse_geo_locate(latitude,longitude)
