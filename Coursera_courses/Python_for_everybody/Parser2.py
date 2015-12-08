import urllib
from bs4 import *

url = raw_input('Enter web adress: ')
cnt = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags=soup('a')
print 'Retrieving name: ', tags[pos-1].contents[0]
while cnt > 1:
    html = urllib.urlopen(tags[pos-1].get('href', None)).read()
    soup = BeautifulSoup(html)
    tags=soup('a')
    print 'Retrieving name: ', tags[pos-1].contents[0]
    cnt -= 1



#htmlmod = urllib.urlopen(urlmod).read()
#soup = BeautifulSoup(htmlmod)
#tagsmod=soup('a')
#for tag in tagsmod:
    #print tag.contents[0]
#    print tag.get('href', None)

"""
while cnt > 0:
    print 'Retrieving name: ', tags[pos-1].contents[0]
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags=soup('a')
    retr = tags[pos-1]


#for tag in tags:
    #print tag.contents[0]
#    print tag.get('href', [3])

"""