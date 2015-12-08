__author__ = 'YO_N'

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Please, enter your adress: ')
    if len(address) <1:
        print "Nothing to search."
        break

    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address' : address})
    print "Retrieving url", url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved ', len(data), ' characters.'

    try:
        js = json.loads(str(data))
    except:
        js = None
    if 'status' not in js or js['status'] !='OK':
        print '====Failure To retrieve ===='
        print data
        continue

    #print json.dumps(js, indent = 4)
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'Latitude: ', lat, "Longitude: ", lng
    print js["results"][0]["formatted_address"]
