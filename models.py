from sqlalchemy import Column,String,JSON,Integer

from database import Base

class Posting(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,index=True)
    post = Column(JSON)
