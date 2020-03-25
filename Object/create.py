from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/studb",encoding="utf8")

Base = declarative_base()  #生成orm基类

class User(Base):   #继承base基类
    __tablename__ = "t123"
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    address = Column(String(40))
Base.metadata.create_all(engine)
