#!/usr/bin/python3

'''Module for model state'''

from sqlalchemy import Coumn, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    '''State class for SQLAlchemy ORM'''
    __tablename__ = 'states'
    id = Coumn(Integer, primary_key=True, nullable=False)
    name = Coumn(String(128), nullable=False)
