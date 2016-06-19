import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count_limit = raw_input('Enter count: ')
position = raw_input('Enter position: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
count = 0
tags_list = list()
while True:
    if count == int(count_limit):
        break
    for tag in tags:
        tags_list.append(str(tag.get('href', None)))
    url = tags_list[int(position) - 1]
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    tags_list = list()
    count += 1
    print url