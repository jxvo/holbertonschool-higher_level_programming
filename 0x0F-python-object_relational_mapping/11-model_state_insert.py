#!/usr/bin/python3
"""
insert a new state 'Louisiana' to a database using sqlalchemy
args: [mysql username] [mysql password] [database name]
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    session.close()
    get = session.query(State).filter(State.name == 'Louisiana').one()
    print(get.id)
