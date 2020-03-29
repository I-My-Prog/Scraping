import urllib.request
import lxml.html
import sqlite3
import time
#from bs4 import BeautifulSoup as bs
dbname = 'Data.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
DELAY_TIME = 1

list_code = []
for a in cur.execute('SELECT * FROM SecCodeList'):
    x, = a
    list_code.append(x)
for code in list_code:
    time.sleep(DELAY_TIME)
    url = "https://kabutan.jp/stock/?code="+str(code)
    soup = urllib.request.urlopen(url)
    dom = lxml.html.fromstring(soup.read())

    code = dom.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/span/text()')
    name = dom.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/text()')
    price = dom.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')
    print(code,name,price)

cur.close()
conn.close()