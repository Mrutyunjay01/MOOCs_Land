# -*- coding: utf-8 -*-

import json

data = '''
        [
                {
                        "id" : "001",
                        "x" : "2",
                        "name" : "Mrutyunjay"
                },
                {
                        "id" : "009",
                        "x" : "7",
                        "name" : "Chuck"
                }
        ]
'''

info = json.loads(data)
print('User count : ', len(info))
print(type(info))  # returns type as list
for item in info:
    #print(item)
    print('Name: ', item['name'])
    print('Id : ', item['id'])
    print('Attribute', item['x'])
    