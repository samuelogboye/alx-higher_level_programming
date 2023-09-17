#!/usr/bin/python3
"""A python file that contains the class definition of a State and an
instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    A class that inherits from Base and links to the MySQL table states
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
