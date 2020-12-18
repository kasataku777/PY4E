# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
position = input('Enter position: ')

cnt = int(count)
pos = int(position)
# Retrieve all of the anchor tag
while cnt > 0:

    tags = soup('a')
    # for tag in tags:
    # print(tag.get('href', None))
    lin = tags[pos-1].get('href', None)
    name = tags[pos-1].contents[0]
    html = urllib.request.urlopen(lin, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    cnt -= 1
print(name)
