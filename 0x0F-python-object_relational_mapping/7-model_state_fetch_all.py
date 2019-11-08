#!/usr/bin/python3
"""
Module to list all 'state' objects in a database using sqlalchemy
args: [mysql username] [mysql password] [database name]
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id.asc()):
        print("{}: {}".format(state.id, state.name))

    session.close()