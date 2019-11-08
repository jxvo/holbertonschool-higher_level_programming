#!/usr/bin/python3
"""Module for City class"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """A U.S. city stored in a database
    Attributes:
        id (int): a unique ID for this record
        name (str): name of the state
        state (State): state this city is in
        state_id (int): the ID of the state in which this state resides
    """
    def __init(self):
        pass

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
