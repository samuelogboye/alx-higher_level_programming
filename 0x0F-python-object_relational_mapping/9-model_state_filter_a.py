#!/usr/bin/python3
"""A Script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # set up connection to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    for state in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
