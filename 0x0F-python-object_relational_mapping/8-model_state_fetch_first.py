#!/usr/bin/python3
"""
Module to print the first 'state' instance inside a database using sqlalchemy
usage: [mysql username] [mysql password] [database name]
"""
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
