import geopy,argparse
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
parser = argparse.ArgumentParser(description="BruteForce Directory")
parser.add_argument('-lat','--latitude',metavar='',help="Latitude Coordinate(y)")
parser.add_argument('-long',"--longitude",metavar='',help="Longitude Coordinate(x)")
args = parser.parse_args()
def reverse_geo_locate(latgeo,longgeo):
 locator = Nominatim(user_agent=”myGeocoder”)
 coordinates = str(latgeo),str(longgeo)
 location = locator.reverse(coordinates)
 location.raw
 print(location)
reverse_geo_locate(args.latgeo,args.longgeo)

