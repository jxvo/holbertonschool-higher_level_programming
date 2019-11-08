#!/usr/bin/python3
"""
list all 'state' and corresponding 'cities' values using sqlalchemy
usage: [mysql username] [mysql password] [database name]
"""
import sys
from relationship_city import Base, City
from relationship_state import State
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).all()
    for i in state:
        print(i.child)
    session.close()
