#!/usr/bin/python3
"""Class definition of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    A class that inherits from Base and links to the MySQL table states
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    # class attribute cities must represent a relationship with class City
    # (second argument to relationship() is backref, which adds a new
    # attribute to City called state)
    cities = relationship("City", backref="state", cascade="all, delete")
