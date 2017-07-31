# just get from this one : https://github.com/REMitchell/python-scraping

#  nice right
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
 try:
    html = urlopen(url)
 except HTTPError as e:
    print("Error url open %s",e.msg)
    return None

 try:
    bsObj = BeautifulSoup(html.read(),"lxml")
    title = bsObj.body.h1
 except AttributeError as e:
    print("Error get h1 %s",e.msg)
    return None

 return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title == None:
 print("Title could not be found")
else:
 print(title)
