import urllib.request
import lxml.html
import sqlite3
import datetime
import time
from write_sqlite import SQLMatch
#from bs4 import BeautifulSoup as bs

class Scrape():
    def __init__(self,code):
        time.sleep(DELAY_TIME)
        url = "https://kabutan.jp/stock/?code="+str(code)
        soup = urllib.request.urlopen(url)
        dom = lxml.html.fromstring(soup.read())

        self.code = dom.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/span/text()')
        self.name = dom.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/text()')
        self.price = dom.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')

        dt_now = datetime.datetime.now()
        self.date = dt_now.strftime('%Y-%m-%d %H:%M')
        self.tuple_x = self.date,self.code[0],self.name[0],self.price[0]
#        print(tuple_x)
    
    def Record(self):
        print(self.tuple_x)
        if SQLMatch('OriginData',self.code):
            sql = "delete from Origindata where Sec_Code = ?"
            cur.execute(sql,self.code)
        sql = 'insert into OriginData values (?,?,?,?)'
        cur.execute(sql,self.tuple_x)



dbname = 'Data.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
DELAY_TIME = 1

list_code = []
for a in cur.execute('SELECT * FROM SecCodeList'):
    x, = a
    list_code.append(x)

for code in list_code:
    x = Scrape(code)
    x.Record()

cur.close()
conn.commit()
conn.close()