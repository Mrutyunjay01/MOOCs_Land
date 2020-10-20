# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

data =''' <person>
                <name>Mrutyunjay </name>
                <phone>934833067 </phone>
                <email hide='yes'/>
            </person>'''
            
tree = ET.fromstring(data)

print(tree.find('name').text)
print(tree.find('email').get('hide'))
