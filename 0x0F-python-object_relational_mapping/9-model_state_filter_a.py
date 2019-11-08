#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy
from sqlalchemy.orm import sessionmaker

"""
Module to filter objects containing 'a' inside a database using sqlalchemy
usage: [mysql username] [mysql password] [database name]
"""
if __name__ == "__main__":
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id.asc())

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
