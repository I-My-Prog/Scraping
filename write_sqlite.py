import sqlite3
import re

pattern = '\d{4}'
repatter = re.compile(pattern)

class CreateTable():
'''
テーブルを作成する
'''
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
'''
dbnameに指定されたDBにtarget(int)が存在するか調べる
返り値はブール型
'''
    def __init__(self,dbname,target):
        conn = sqlite3.connect('Data.sqlite3')
        c = conn.cursor()
        c.execute('select * from ?',(dbname,))
        for row in c:
            if row[0] == target:
                ret_val = bool(1)
            else:
                ret_val = bool(0)
        print("Log Out from DB...")
        conn.commit
        conn.close
        return ret_val

class Add_SecCode():
'''
codeがSecCodeUseageに存在するかつ４桁の数字か確認[SQLMatch()]
if ある：
    codeがSecCodeListに存在するか確認[SQLMatch()]
    if ある：
        エラーを表示する
    if ない：
        SecCodeListにcodeを追加する
if ない：
    エラーを表示する
返り値はなし
'''
    def __init__(self,code):
#4桁の数字か？
#if repatter.match(str(row[0])):
#SecCodeListにcodeを追加する
#   c.execute('insert into ? values ?',(dbname,target))
        pass

#CreateTable()

code = input()
result = repatter.match(code)

if result:
    Add_SecCode(int(code))