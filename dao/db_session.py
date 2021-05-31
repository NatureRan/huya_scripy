#coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:950608@121.43.148.210:3306/huya_scripy?charset=UTF8MB4", max_overflow=5, encoding="UTF-8")

class SessionBuilder(object):

    __session = None

    # 创建会话
    @classmethod
    def instance(self):
        if not SessionBuilder.__session:
            DBsession = sessionmaker(bind=engine)
            __session = DBsession()
            return __session
        

