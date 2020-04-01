import urllib.request
import lxml.html
import sqlite3
import datetime
import time
from write_sqlite import SQLMatch
import sqlite_ctrl
import re
#from bs4 import BeautifulSoup as bs

class Scrape():
    def __init__(self,code):
        time.sleep(DELAY_TIME)
        url = "https://kabutan.jp/stock/?code="+str(code)
        soup = urllib.request.urlopen(url)
        dom = lxml.html.fromstring(soup.read())

        self.code = dom.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/span/text()')
        self.name = dom.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/text()')
        p = dom.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')
        self.price = re.sub("\\D","",p[0])
        dt_now = datetime.datetime.now()
        self.date = dt_now.strftime('%Y-%m-%d %H:%M')
#        print(tuple_x)
    
    def Record(self):
        sqlite_ctrl.Update_OD(self.code,self.name,self.price)

DELAY_TIME = 1

data = sqlite_ctrl.Select_SCL()
allscl =data.ret()
scl = []
for code in allscl:
    x, = code
    scl.append(x)
print(scl)

for code in scl:
    x = Scrape(code)
    x.Record()

