#!/usr/bin/python3
"""
create a 'state' and insert 'city' value using sqlalchemy
usage: [mysql username] [mysql password] [database name]
"""


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State
import sys

if __name__ == "__main__":
    """Create a state California with a city San Francisco"""
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    session.add(new_state)
    session.add(new_city)
    session.flush()
    session.commit()
    session.close()
