import sqlite3

dbname = 'Data.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# terminalで実行したSQL文と同じようにexecute()に書く
cur.execute('SELECT * FROM SecCodeList')
l = []
# 中身を全て取得するfetchall()を使って、printする。
print(cur.fetchall())
for a in cur.execute('SELECT * FROM SecCodeList'):
    x, = a
    l.append(x)
print(l)
cur.close()
conn.close()