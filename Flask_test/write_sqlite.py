#===============================
#Regasy; Conversion to sqlite_ctrl.py
#2020-03-29/akata
#===============================
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
        print('Start... SQLM Process')
        conn = sqlite3.connect('Data.sqlite3')
        c = conn.cursor()
        c.execute("select * from ('%s')" % dbname)
        self.ret_val = bool(0)
        for row in c:
            if row[0] == target:
                self.ret_val = bool(1)
                print('True')
#        print("Log Out from DB...")
        conn.commit
        conn.close
        print('End...   SQLM Process')

class Add_SecCode():
    '''
        codeがSecCodeUseageに存在するか確認[SQLMatch()]
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
        print('Start... Add_SC Process')
        conn = sqlite3.connect('Data.sqlite3')
        c = conn.cursor()
        val = int(code)
        instanceU = SQLMatch('SecCodeUseage',code)
        if instanceU.ret_val:
            instanceL = SQLMatch('SecCodeList',code)
            if instanceL.ret_val:
                print("Error: Registered Code")
            else:
                print(val)
                print(type(val))
                c.execute("insert into SecCodeList values ('%d') " % val)
                print("Success")
        else:
            print("Error: Unused Code")
        print('End...   Add_SC Process')
        conn.commit()
        conn.close()

class UpdateData():
    def __init__(self,uptime,code,name,price):
        conn = sqlite3.connect('Data.sqlite3')
        c = conn.cursor()
        c.execute("insert into OriginData values (?,?,?,?) " (uptime,code,name,price))
        conn.commit()
        conn.close()

### Gabages
#4桁の数字か？
#if repatter.match(str(row[0])):
#SecCodeListにcodeを追加する
#CreateTable()
###
'''
code = input()
result = repatter.match(code)
print('================================')

if result:
    Add_SecCode(int(code))'''