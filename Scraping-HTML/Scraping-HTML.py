import urllib
import re
from BeautifulSoup import *


url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
#print html
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
tags_list = list()
final_list = list()
for tag in tags:
    #stuff = str(tag.contents[0])
    tags_list.append(re.findall('[0-9]+', str(tag.contents[0])))
for i in tags_list:
    for n in i:
        final_list.append(int(n))
print sum(final_list)