# -*- coding: utf-8 -*-
import re
from urllib import request
from bs4 import BeautifulSoup

url = input('Enter URL : ')
html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# retrieve all the anchor tags
tags = soup('a')
for _ in range(7):
    
    urlS = tags[17].get('href')
    htmlS = request.urlopen(urlS).read()
    soupS = BeautifulSoup(htmlS, 'html.parser')
    tags = soupS('a')
    
target = re.findall('known_by_(\S+[.])', urlS)
ans = target[0][:-1]
print(ans)
