import requests
import json
import urllib



class ISSData:

    def __init__(self, api_key):
        self.api_key = api_key

    def _call_api(self, url):
        self.site = "http://api.open-notify.org" + url
        response = urllib.request.urlopen(self.url)
        return response.json

    def location_of_ISS(self):
        url = '/iss-now.json'
        self._call_api(self, url)
        result = json.loads(response.read())
        location = result['iss_position']
        latitude = location['latitude']
        longitude = location['longitude']
        print('Latitude: ', latitude)
        print('Longitude: ', longitude)
        print(result)

    def people_on_iss(self, people):
        url = '/astros.json'
        self._call_api(self, url)
        result = json.loads(response.read())
        print('People in Space: ', result['number'])
        people = result['people']
        for p in people:
            print(p['name'])


print('location of ISS is currently: ')
location_of_ISS(self)
print('people currently residing in space: ' + people_on_iss(self, people))





