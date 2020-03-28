import urllib.request
import lxml.html
#from bs4 import BeautifulSoup as bs

url = "https://kabutan.jp/stock/?code=2768"
soup = urllib.request.urlopen(url)

dom = lxml.html.fromstring(soup.read())

s = dom.xpath('string(/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/table/tbody/tr[3]/td[1]/span)')
print(s)