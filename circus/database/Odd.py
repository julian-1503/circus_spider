from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

DeclarativeBase = declarative_base()

class Odd(DeclarativeBase):
    __tablename__ = 'odds'

    id = Column(Integer, primary_key=True)
    odd_value = Column('odd_value', String)
    recording_time = Column('recording_time', DateTime)

    outcome_id = Column(Integer, ForeignKey('outcome.id'))
    match_id = Column(Integer, ForeignKey('match.id'))

    outcome = relationship('Outcome', back_populates='odds')
    match = relationship('Match', back_populates='odds')

    def __repr__(self):
        return "<Odd({})>".format(self.odd_value)
