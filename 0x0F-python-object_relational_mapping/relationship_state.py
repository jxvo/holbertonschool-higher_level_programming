#!/usr/bin/python3
"""Module for State class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """A U.S. state stored in a database
    Attributes:
        cities (List[City]): list of cities in this state
        id (int): a unique ID for this record
        name (str): name of the state
    """
    def __init(self):
        pass

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")
