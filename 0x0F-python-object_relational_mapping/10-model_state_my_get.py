#!/usr/bin/python3
"""
print 'state' object matching string parameter using sqlalchemy
args: [mysql username] [mysql password] [database name] [state name]
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

    states = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).one_or_none()
    if states is not None:
        print(states.id)
    else:
        print('Not found')
    session.close()
