import random,argparse,requests,time,json,sys,reverse_geo
from pprint import pprint
from random import uniform
from colorama import Fore
from colorama import init
init(autoreset=True)
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
parser = argparse.ArgumentParser(description="Random GeoLocation")
parser.add_argument('-a','--address',metavar='',help='Address')
parser.add_argument('-ak','--apikey',metavar='',help='API KEY')
args = parser.parse_args()
ip_stack_apikey = "255e2ed0c218837a05c2e33a7f0de38c"
def slow_print(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
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
   slow_print('''
╔═╗─┐ ┬┌─┐┬  ┌─┐┬─┐┌─┐  ╔╦╗┬ ┬┌─┐  ╦ ╦┌─┐┬─┐┬  ┌┬┐┬
║╣ ┌┴┬┘├─┘│  │ │├┬┘├┤    ║ ├─┤├┤   ║║║│ │├┬┘│   │││
╚═╝┴ └─┴  ┴─┘└─┘┴└─└─┘   ╩ ┴ ┴└─┘  ╚╩╝└─┘┴└─┴─┘─┴┘o
   ''')
   time.sleep(2)
   print(wi + gr + '''
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
   slow_print('''
╔╦╗┬ ┬  ╔═╗┌─┐┌─┐   ╦  ┌─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
║║║└┬┘  ║ ╦├┤ │ │───║  │ ││  ├─┤ │ ││ ││││
╩ ╩ ┴   ╚═╝└─┘└─┘   ╩═╝└─┘└─┘┴ ┴ ┴ ┴└─┘┘└┘
''')
   pprint(geo_json)
   time.sleep(1.5)
   print('-------------------------------------------------------------------------')
 @staticmethod
 def newpoint():
  global x,y
  slow_print('''
╦═╗┌─┐┌┐┌┌┬┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐┌┬┐┌─┐┌─┐
╠╦╝├─┤│││ │││ ││││  ║  │ ││ │├┬┘ ││││││├─┤ │ ├┤ └─┐
╩╚═┴ ┴┘└┘─┴┘└─┘┴ ┴  ╚═╝└─┘└─┘┴└──┴┘┴┘└┘┴ ┴ ┴ └─┘└─┘
''') 
  slow_print("Generating Random Geolocation Coordinates...")
  for i in range(20):
   x,y = uniform(-90,90), uniform(-90, 90)
   time.sleep(0.1)
   print(f"Latitude:{x}<===>,Longitude:{y}")
   reverse_geo.reverse_geo_locate(x,y)
if __name__ == "__main__":
    map = GeoLocation(args.address)
    map.my_location()
    map.newpoint()
