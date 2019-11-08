#!/usr/bin/python3
"""
list all 'cities' values from a database using sqlalchemy
args: [mysql username] [mysql password] [database name]
"""
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()
    for i in query:
        print("{}: ({}) {}".format(i[0].name, i[1].id, i[1].name))
    session.close()
