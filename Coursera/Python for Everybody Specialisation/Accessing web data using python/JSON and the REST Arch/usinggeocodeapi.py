# -*- coding: utf-8 -*-

from urllib import request, parse, error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    
    if len(address) < 1 : break
    
    url = serviceurl + parse.urlencode({'address' : address})
    
    print('Retrieving : ', url)
    uh = request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved ', len(data), 'characters')
    
    try:
        js = json.loads(data)
        
    except:
        js = None
    
    print(js)    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Falied to retrieve')
        print(data)
        continue
    
    