# -*- coding: utf-8 -*-

from urllib import request, parse
import json

url = input('Enter URL : ')
data = request.urlopen(url).read().decode()
#print(data)

info = json.loads(data)
total = 0
for item in info['comments']:
    total += item['count']
print(total)
