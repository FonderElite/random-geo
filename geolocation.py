import random,argparse,requests
from geopy.geocoders import Nominatim
import time,geocoder
import json
from pprint import pprint
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
   latitude = geo_json['latitude']
   longitude = geo_json['longitude']
   city = geo_json['city']
   print('''
╦ ╦┌─┐┬─┐┬  ┌┬┐  ╔╦╗┌─┐┌─┐
║║║│ │├┬┘│   ││  ║║║├─┤├─┘
╚╩╝└─┘┴└─┴─┘─┴┘  ╩ ╩┴ ┴┴  
   ''')
   time.sleep(2)
   print('''

   180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
    |     |     |     |     |     |     |     |     |     |     |     |     |
90N-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90N
    |           . _..::__:  ,-"-"._        |7       ,     _,.__             |
    |   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|
    |>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                mt-2_|
60N-+  \_.:--.       `._ )`^-. "'       , [_/(                       __,/-' +-60N
    | '"'     \         "    _L        oD_,--'                )     /. (|   |
    |          |           ,'          _)_.\\._<> 6              _,' /  '   |
    |          `.         /           [_/_'` `"(                <'}  )      |
30N-+           \\    .-. )           /   `-'"..' `:._          _)  '       +-30N
    |    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |
    |              `._,   ""         |           \`'   \|   ?_)  {\         |
    |                 `=.---.        `._._       ,'     "`  |' ,- '.        |
000-+                   |    `-._         |     /          `:`<_|h--._      +-000
    |                   (        >        .     | ,          `=.__.`-'\     |
    |                    `.     /         |     |{|              ,-.,\     .|
    |                     |   ,'           \   / `'            ,"     \     |
30S-+                     |  /              |_'                |  __  /     +-30S
    |                     | |                                  '-'  `-'   \.|
    |                     |/                                         "    / |
    |                     \.                                             '  |
60S-+                                                                       +-60S
    |                      ,/            ______._.--._ _..---.---------._   |
    |     ,-----"-..?----_/ )      __,-'"             "                  (  |
    |-.._(                  `-----'                                       `-|
90S-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90S
''')
   time.sleep(1.5)
   print('''
╔╦╗┬ ┬  ╔═╗┌─┐┌─┐   ╦  ┌─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
║║║└┬┘  ║ ╦├┤ │ │───║  │ ││  ├─┤ │ ││ ││││
╩ ╩ ┴   ╚═╝└─┘└─┘   ╩═╝└─┘└─┘┴ ┴ ┴ ┴└─┘┘└┘
''')
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
   print('---------------------------------------------------------------------------')
 @staticmethod
 def reverse_geo(lat,long,language="en"):
  coordinates = f"{lat},{long}"
  time.sleep(1)
  try:

   reversed = app.reverse(coordinates, language=language).raw
   print('''
╔═╗┌─┐┌─┐┌─┐┌─┐┌┬┐┌─┐  ╔═╗┌─┐┌─┐╦  ┌─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
║ ╦├┤ │ ││  │ │ ││├┤   ║ ╦├┤ │ │║  │ ││  ├─┤ │ ││ ││││
╚═╝└─┘└─┘└─┘└─┘─┴┘└─┘  ╚═╝└─┘└─┘╩═╝└─┘└─┘┴ ┴ ┴ ┴└─┘┘└┘
''')
   pprint(reversed)
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
