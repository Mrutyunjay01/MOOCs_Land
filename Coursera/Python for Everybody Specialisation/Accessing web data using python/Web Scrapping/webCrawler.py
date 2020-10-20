# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = input('Enter URL : ')
html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
