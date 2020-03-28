import sqlite3
import re

pattern = '\d{4}'
repatter = re.compile(pattern)

class CreateTable():
    def __init__(self):
        conn = sqlite3.connect('Data.sqlite3')
        c = conn.cursor()
        c.execute('create table if not exists OriginData(time text,Sec_Code integer,Sec_Name text,Stock_price real)')   
        #スクレイプしたデータの保存
        c.execute('create table if not exists SecCodeList(Sec_Code integer)')
        #調査する証券コード
        conn.commit
        conn.close

class SQLMatch():
    def __init__(self,dbname,target):

class Add_SecCode():
    def __init__(self,code):
        conn = sqlite3.connect('Data.sqlite3')
        c = conn.cursor()
        c.execute('select * from SecCodeUseage')
        for row in c:
            if row[0] == code and repatter.match(str(row[0])):
                c.execute("insert into SecCodeList values ?",(code,))
#        if SCValid:
                print("Success")
        print("Log Out from DB...")
        conn.commit
        conn.close

#CreateTable()

code = input()
result = repatter.match(code)

if result:
    Add_SecCode(int(code))