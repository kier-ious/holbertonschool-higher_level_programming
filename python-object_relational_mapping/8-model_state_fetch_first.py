#!/usr/bin/python3
""" Lists all states from db hbtn_0e_0_usa """


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def first_state(username, password, database_name):
    """ Listing states in db """
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).first()

    if first_state is not None:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    first_state(username, password, database_name)
