# -*- coding: utf-8 -*-

from urllib import request, parse
import json

serviceUrl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')
parms = dict()
parms['key'] = 42
parms['address'] = address
url = serviceUrl + parse.urlencode(parms)

uh = request.urlopen(url).read().decode()
info = json.loads(uh)

print(info['results'][0]['place_id'])
