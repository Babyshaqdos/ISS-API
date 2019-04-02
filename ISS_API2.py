import urllib
import json
import time


class ISSData:

    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    print('People in Space: ', result['number'])

    people = result['people']

    for p in people:
        print(p['name'], ' in ', p['craft'])

    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('Latitude: ', lat)
    print('Longitude: ', lon)

    # Find the location of the ISS
    url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # print result
    over = result['response'][1]['risetime']
    location = (time.ctime(over))


