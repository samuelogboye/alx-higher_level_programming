#!/usr/bin/python3
"""Class definition of a City and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    A class that inherits from Base and links to the MySQL table cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    # foreign key constraint
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
