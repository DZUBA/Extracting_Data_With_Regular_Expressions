import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter URL: ')
    if len(url) < 1 : break

    data = urllib.urlopen(url).read()
    tree = ET.fromstring(data)
    counts = tree.findall('comments/comment')
    print 'Retrieved',len(data),'characters'
    print len(counts)
    final_list = list()
    for item in counts:
        final_list.append(int(item.find('count').text))

    print sum(final_list)