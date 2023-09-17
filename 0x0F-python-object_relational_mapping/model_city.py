#!/usr/bin/python3
"""A Python file that contains the class definition of a City and an
instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    A class that inherits from Base and links to the MySQL table cities
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    # foreign key constraint
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
