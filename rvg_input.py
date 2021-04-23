import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
def reverse_geo_locate():
 while True:
  lat = input("Latitude: ")
  long = input("Longitude: ")
  locator = Nominatim(user_agent='Geo_Locator')
  coordinates = lat,long
  location = locator.reverse(coordinates)
  print(f"Location: {location}")
reverse_geo_locate()
