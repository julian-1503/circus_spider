from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from circus.database.base import Base

class Odd(Base):
    __tablename__ = 'odds'

    id = Column(Integer, primary_key=True)
    odd_value = Column('odd_value', String)
    outcome_name = Column('match_name', String)

    # match_id = Column(Integer, ForeignKey('match.id'))

    # match = relationship('Match', back_populates='odds')

    def __repr__(self):
        return "<Odd({})>".format(self.odd_value)
