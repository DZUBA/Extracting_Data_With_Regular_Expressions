import json
import urllib

while True:
    url = raw_input('Enter URL: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    print 'Retrieved', len(data), 'characters'
    info = json.loads(data)

    count = 0
    summary = 0
    key = info.get('comments')
    for item in key:
        count += 1
        summary += int(item['count'])

    print 'Count: ', count
    print 'Sum: ', summary