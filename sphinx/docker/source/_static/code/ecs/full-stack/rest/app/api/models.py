from sqlalchemy import Column, Integer, String

from .database import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    age = Column(Integer)
