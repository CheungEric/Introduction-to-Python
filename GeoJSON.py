import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place = js['results'][0]['place_id']
    print('Place id', place)


    #print(json.dumps(js, indent=4)) - Use this to display the whole api formatted_address

    #lat = js["results"][0]["geometry"]["location"]["lat"] - use this to extract the latitude
    #lng = js["results"][0]["geometry"]["location"]["lng"] - use this to extract the longitude
    #print('lat', lat, 'lng', lng) - print lat and longitude
    #location = js['results'][0]['formatted_address'] - finds the formatted address
    #print(location)
