#coding:utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import BigInteger, Boolean, Date, DateTime, Integer, String, Text

Base = declarative_base()

class UserBarrage(Base):
    __tablename__ = 'user_barrage'
    id = Column(BigInteger, primary_key=True)
    room = Column(String(16))
    user_name = Column(String(64))
    barrage_content = Column(String(255))
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    expired = Column(Boolean)