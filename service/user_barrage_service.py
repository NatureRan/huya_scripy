#coding:utf-8

from sqlalchemy.sql.functions import user
from dao.user_barrage_dao import UserBarrageDao
from models import UserBarrage
from datetime import datetime

class UserBarrageService(object):
    def __init__(self):
        self.userBarrageDao:UserBarrageDao = UserBarrageDao()

    def saveUserBarrage(self, room:str, name:str, barrage:str):
        user_barrage:UserBarrage = UserBarrage()
        user_barrage.room = room;
        user_barrage.user_name = name
        user_barrage.barrage_content = barrage
        user_barrage.create_time = datetime.now()
        user_barrage.update_time = datetime.now()
        user_barrage.expired = False
        self.userBarrageDao.save(user_barrage)

