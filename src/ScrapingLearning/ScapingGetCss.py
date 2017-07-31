# just get from this one : https://github.com/REMitchell/python-scraping

#  nice right
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getSpan(url):
 try:
    html = urlopen(url)
 except HTTPError as e:
    print("Error url open %s",e.msg)
    return None

 try:
    bsObj = BeautifulSoup(html.read(),"lxml")
    nameList = bsObj.findAll("span", {"class":"green"})
    for name in nameList:
        print(name.get_text())
 except AttributeError as e:
    print("Error get span %s",e.msg)
    return None


getSpan("http://www.pythonscraping.com/pages/warandpeace.html")


