# -*- coding: utf-8 -*-

import json

data = '''{
        "name" : "Mrutyunjay Biswal",
        "phone" : {
                "type" : "int1",
                "number" : "9348833067"
        },
        "email" : {
                "hide" : "yes"
                }

        }'''
info = json.loads(data)
#print(type(info)) returns type dictionary

print('Name : ', info['name'])
print('Email : ', info['email']['hide'])
print('Phone: ', info['phone']['number'])
