from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


engine = create_engine('mysql+pymysql://root:pss123er@10.0.0.49:3306/test')
DBSession = sessionmaker(bind=engine)


