#===============================
#Rewrite of write_sqlite.py by SQLalchemy
#2020-04-01/akata
#===============================
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table,Column,Integer,String,Float
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///Data.sqlite3')
Base=declarative_base()

Session = sessionmaker(engine)
session = Session()

class OriginData(Base):
    __tablename__="OriginData" #テーブル名を指定
    time        =Column(String(255))
    Sec_Code    =Column(Integer,primary_key=True)
    Sec_Name    =Column(String(255))
    Stock_price =Column(Float)

class SecCodeList(Base):
    __tablename__="SecCodeList" #テーブル名を指定
    Sec_Code    =Column(Integer,primary_key=True)

class SecCodeUseage(Base):
    __tablename__="SecCodeUseage" #テーブル名を指定
    SecCodeUseage=Column(Integer,primary_key=True)

Base.metadata.create_all(engine)

class Insert_OD():
    def __init__(self,sec_code,sec_name,stock_p):
        self.code = sec_code[0]
        self.name = sec_name[0]
        self.p = stock_p
        dt = datetime.datetime.now()
        date = dt.strftime('%Y-%m%d %H%M')
        New_data=OriginData(time=date,Sec_Code=self.code,Sec_Name=self.name,Stock_price=self.p)
        print(New_data)
        session.add(New_data)
        session.commit()
        session.close()

class Update_OD():
    def __init__(self,code,name,price):
        print(code)
        test = session.query(OriginData).all()
        data = session.query(OriginData).filter(OriginData.Sec_Code=="2768").all()
        session.query(OriginData).filter(OriginData.Sec_Code==int(code[0])).delete()
        Insert_OD(code,name,price)
        session.commit()

class Select_OD():
    #get all data from db
    def __init__(self):
        data = session.query(OriginData).all()
        session.commit()

class Match_SCL():
    def __init__(self,target):
        data = session.query(SecCodeList).filter(SecCodeList.Sec_Code==target).all()
        self.ret_val = bool(0)
        if data is not None:
            self.ret_val = bool(1)
        session.commit()

class Insert_SCL():
    #insert to SecCodeList
    def __init__(self,sec_code):
        dt = datetime.datetime.now()
        New_data=SecCodeList(Sec_Code=sec_code)
        session.add(New_data)
        session.commit()

class Delete_SCL():
    def __init__(self,target):
        session.query(SecCodeList).filter(SecCodeList.Sec_Code==target).delete()
        session.commit()

class Update_SCL():
    #mode> None:Add(only not-match on DB),1:Delete
    def __init__(self,target,mode=None):
        if mode == None:
            if Match_SCL(target):
                pass
            else:
                Insert_SCL(target)
        else:
            if Match_SCL(target):
                Delete_SCL(target)
            else:
                pass
        session.commit()

class Select_SCL():
    #get all data from db
    def __init__(self):
        self.data = session.query(SecCodeList.Sec_Code).all()
        print(self.data)
        session.commit()
        session.close()

    def ret(self):
        return self.data