import random,argparse,requests
from geopy.geocoders import Nominatim
import time,geocoder
import json
from pprint import pprint
parser = argparse.ArgumentParser(description="Random GeoLocation")
parser.add_argument('-a','--address',metavar='',help='Address')
parser.add_argument('-ak','--apikey',metavar='',help='API KEY')
args = parser.parse_args()
class GeoLocation:
 def __init__(self,address):
  self.address = address
 @staticmethod
 def my_location():
  send_url = f"http://api.ipstack.com/check?access_key={ip_stack_apikey}"
  geo_req = requests.get(send_url)
  if geo_req.status_code == 200 or geo_req.status_code < 399:
   json_info = geo_req.text
   geo_json = json.loads(json_info)
   country = geo_json['country_name']
   capital = geo_json['location']['capital']
   ip = geo_json['ip']
   continent = geo_json['continent_name']
   global latitude
   latitude = geo_json['latitude']
   global longitude 
   longitude = geo_json['longitude']
   city = geo_json['city']
   print('-------------------------------------------------------------------------')
   pprint(geo_json)
   print('-------------------------------------------------------------------------')

 def random_geo(self):
   global array
   array = []
   global app 
   app = Nominatim(user_agent="Sample")
   location = app.geocode(self.address).raw
   global latitude
   latitude = location["lat"]
   global longitude
   longitude = location["lon"]
   pprint(f"Coordinates: Latitude:{latitude}, Longitude:{longitude}")
 @staticmethod
 def reverse_geo(lat,long,language="en"):
  coordinates = f"{lat},{long}"
  time.sleep(1)
  try:
   reversed = app.reverse(coordinates, language=language).raw
   pprint(reversed)
   print('--------------------------Random ----------------------------------------')

  except:
   address_rev = reverse_geo(lat, long)
   pprint(address_rev)
   latitude = 36.723
   longitude = 3.188
   # get the address info
   address = get_address_by_location(latitude, longitude)
   # print all returned data
   pprint(address)
map = GeoLocation(args.address)
map.my_location()
map.random_geo()
map.reverse_geo(latitude,longitude)
