from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# find all related link
html = urlopen("http://en.wikipedia.org/wiki/Indonesia")
bsObj = BeautifulSoup(html,"lxml")

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

