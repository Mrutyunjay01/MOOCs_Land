import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter the xml url: ')
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
datastring = data.decode()
tree = ET.fromstring(datastring)
comment = tree.findall('comments/comment')
ans = 0
for cnt in comment:
    ans += int(cnt.find('count').text)
print(ans)
