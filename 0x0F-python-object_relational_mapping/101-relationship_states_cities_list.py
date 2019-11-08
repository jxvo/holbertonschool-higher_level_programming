#!/usr/bin/python3
"""
list all 'state' and corresponding 'cities' values using sqlalchemy
usage: [mysql username] [mysql password] [database name]
"""
from sys import argv
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).options(joinedload(State.cities))

    for states in state:
        print("{}: {}".format(states.id, states.name))
        for i in range(len(states.cities)):
            print("\t{}: {}".format(
                states.cities[i].id, states.cities[i].name))

    session.close()
