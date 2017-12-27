from sqlalchemy import *
from strategy.sqlBase import Base
import logging


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(125), nullable=false)

    @classmethod
    def to_dict(cls, row):
        if not row:
            return None

        d = {'id': row.id,
             'name': row.name
             }

        return d

    @classmethod
    def get(cls, session, user_id):
        row = session.query(cls).filter(cls.id == user_id).first()
        return cls.to_dict(row)

    @classmethod
    def update(cls, session, user_id, name):
        try:
            session.query(cls.id == user_id).update({cls.name: name})
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False

    @classmethod
    def add(cls, session, name):
        user = cls(name=name)

        session.add(user)
        try:
            session.commit()
            return user.id
        except Exception as e:
            logging.error(e)
            return None

    @classmethod
    def remove(cls, session, user_id):
        try:
            session.query(cls.id == user_id).delete()
            session.commit()
            return True
        except Exception as e:
            logging.error(e)
            return False
