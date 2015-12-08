__author__ = 'YO_N'

import json
import urllib
sum=0.0
for item in (json.loads(((urllib.urlopen('http://python-data.dr-chuck.net/comments_192442.json')).read())))['comments']:
    sum+=int(item['count'])
print sum



# import json
# import urllib

# data = urllib.urlopen('http://python-data.dr-chuck.net/comments_192442.json')
# data = data.read()
# mData = json.loads(data)
# sum=0.0
# for item in mData['comments']:
# #    print 'Name: ', item['name']
# #    print 'Number: ', item['count']
#     sum+=int(item['count'])
# print sum
