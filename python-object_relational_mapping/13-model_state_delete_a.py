#!/usr/bin/python3
""" Deletes all states from db hbtn_0e_0_usa w/ an 'a' """


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_a(username, password, database_name):
    """ Listing states in db """
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    session.commit()

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    delete_states_with_a(username, password, database_name)
