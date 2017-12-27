from sqlalchemy import *
from strategy.sqlBase import Base, DBSession


class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


session = DBSession()
new_user = User(id='6', name='liam')
session.add(new_user)
session.commit()
session.close()
