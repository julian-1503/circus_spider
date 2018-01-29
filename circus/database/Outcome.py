from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

class Outcome(DeclarativeBase):
    __tablename__ = 'outcome'

    id = Column(Integer, primary_key=True)
    outcome_name = Column('match_name', String)

    def __repr__(self):
        return "<Match({})>".format(self.match_name)
