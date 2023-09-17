#!/usr/bin/python3
"""A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # set up connection to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    query_x = \
        session.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for state in query_x:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
