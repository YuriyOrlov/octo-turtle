import urllib
from bs4 import *

url = raw_input('Enter web adress: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags=soup('span')
summa=0
for tag in tags:
    summa += int(tag.contents[0])
print summa
