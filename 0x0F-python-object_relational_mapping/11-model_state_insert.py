#!/usr/bin/python3
"""A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
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

    # add the new state to the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # print the new state's id
    print(new_state.id)
