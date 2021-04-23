import random,argparse,requests
from geopy.geocoders import Nominatim
import time,geocoder
import json
from pprint import pprint
from random import uniform
parser = argparse.ArgumentParser(description="Random GeoLocation")
parser.add_argument('-a','--address',metavar='',help='Address')
parser.add_argument('-ak','--apikey',metavar='',help='API KEY')
args = parser.parse_args()
ip_stack_apikey = "255e2ed0c218837a05c2e33a7f0de38c"
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
   global latitude
   latitude = geo_json['latitude']
   global longitude
   longitude = geo_json['longitude']
   city = geo_json['city']
   print('''
╔═╗─┐ ┬┌─┐┬  ┌─┐┬─┐┌─┐  ╔╦╗┬ ┬┌─┐  ╦ ╦┌─┐┬─┐┬  ┌┬┐┬
║╣ ┌┴┬┘├─┘│  │ │├┬┘├┤    ║ ├─┤├┤   ║║║│ │├┬┘│   │││
╚═╝┴ └─┴  ┴─┘└─┘┴└─└─┘   ╩ ┴ ┴└─┘  ╚╩╝└─┘┴└─┴─┘─┴┘o
   ''')
   time.sleep(2)
   print('''
     ,o88~~88888888o,
   ,~~?8P  88888     8,
  d  d88 d88 d8_88     b
 d  d888888888          b
 8,?88888888  d8.b o.   8
 8~88888888~ ~^8888\ db 8
 ?  888888          ,888P
  ?  `8888b,_      d888P
   `   8888888b   ,888'
     ~-?8888888 _.P-~    
         ~~~~~~
''')   
   time.sleep(1.5)
   print('''
╔╦╗┬ ┬  ╔═╗┌─┐┌─┐   ╦  ┌─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
║║║└┬┘  ║ ╦├┤ │ │───║  │ ││  ├─┤ │ ││ ││││
╩ ╩ ┴   ╚═╝└─┘└─┘   ╩═╝└─┘└─┘┴ ┴ ┴ ┴└─┘┘└┘
''')
   pprint(geo_json)
   print('-------------------------------------------------------------------------')
 @staticmethod
 def newpoint():
  global x,y
  print('''
╦═╗┌─┐┌┐┌┌┬┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐┌┬┐┌─┐┌─┐
╠╦╝├─┤│││ │││ ││││  ║  │ ││ │├┬┘ ││││││├─┤ │ ├┤ └─┐
╩╚═┴ ┴┘└┘─┴┘└─┘┴ ┴  ╚═╝└─┘└─┘┴└──┴┘┴┘└┘┴ ┴ ┴ └─┘└─┘
''') 
  print("Generating Random Geolocation Coordinates...")
  for i in range(10):
   x,y = uniform(-180,180), uniform(-90, 90)
   time.sleep(1)
   print(f"Latitude:{x},Longitude:{y}")
map = GeoLocation(args.address)
map.my_location()
map.newpoint()
#End
