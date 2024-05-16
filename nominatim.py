import requests
import json

def gps_coordinate(city):
    URL="https://nominatim.openstreetmap.org/search"
    params={"q":city,"format":"json"}
    response=requests.get(URL, params=params)
    places=json.loads(response.content)
    '''print(places[0]['display_name'])
    print(places[0]['lat'])
    print(places[0]['lon'])
    return (float(places[0]['lat'])), (float(places[0]['lon']))'''
  
gps_coordinate("Cairns")