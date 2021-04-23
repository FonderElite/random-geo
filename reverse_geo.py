import geopy
from colorama import Fore
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
def reverse_geo_locate(lat,long):
 locator = Nominatim(user_agent='Geo_Locator')
 coordinates = lat,long
 location = locator.reverse(coordinates)
 if location == None:
  print(f"{wi}{rd}Location=>{wi}None or Unidentified(Check Google Maps)")
 else:
  print(f"{wi}{gr}Location=>{wi}{location}")
