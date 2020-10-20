# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

data =''' <stuff>
            <users>
                <user x='2'>
                    <id>001</id>
                    <name>Mrutyu</name>
                </user>
                <user x='3'>
                    <id>001</id>
                    <name>Biswal</name>
                </user>
            </users>
        </stuff>'''
stuff = ET.fromstring(data)
lst = stuff.findall('users/user') # go along the path
print(len(lst))

for item in lst:
    print(item.find('name').text)
    print(item.find('id').text)
    print(item.get('x'))
