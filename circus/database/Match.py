from sqlalchemy import Column, Integer, String, DateTime
from circus.database.base import Base

class Match(Base):
    __tablename__ = 'match'

    id = Column(Integer, primary_key=True)
    match_name = Column('match_name', String)
    match_date = Column('recording_time', DateTime)

    def __repr__(self):
        return "<Match({})>".format(self.match_name)
