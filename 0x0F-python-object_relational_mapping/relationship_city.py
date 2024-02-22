#!/usr/bin/python3
'''
ORM class -state
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from model_state import State

class City(Base):
    '''Cities class to the table'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
