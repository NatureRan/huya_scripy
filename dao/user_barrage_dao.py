#coding:utf-8

from dao.db_session import SessionBuilder
from models import UserBarrage

class UserBarrageDao(object):
    

    def __init__(self):
        self.db_session = SessionBuilder.instance()
    
    def save(self, userBarrage:UserBarrage):
        self.db_session.add(userBarrage)
        self.db_session.commit()