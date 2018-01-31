from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from circus.database.base import Base

class Odd(Base):
    __tablename__ = 'odds'

    id = Column(Integer, primary_key=True)
    odd_value = Column('odd_value', String)
    odd_name = Column('odd_name', String)
    match_name = Column('match_name', String)

    def __repr__(self):
        return "<Odd({})>".format(self.odd_value)
