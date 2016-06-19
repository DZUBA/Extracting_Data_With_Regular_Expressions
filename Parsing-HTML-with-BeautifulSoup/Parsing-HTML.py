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
    for tag in tags:
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        tags_list.append(str(tag.get('href', None)))
    url = tags_list[int(position) - 1]
    tags_list = list()
    count += 1
    if count == count_limit:
        break
    print url