# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = input('Enter the url: ')
html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
result = 0
for span in spans:
    result += int(span.contents[0])
    
print(result)