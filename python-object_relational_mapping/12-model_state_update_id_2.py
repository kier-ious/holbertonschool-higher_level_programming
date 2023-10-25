#!/usr/bin/python3
""" Lists all states from db hbtn_0e_0_usa """


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, database_name, state_id, new_name):
    """ Listing states in db """
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session. quey(State).filter(State.id == state_id).first()

    if state:
        state.name = new_name
        session.commit()
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_id = int(sys.argv[4])
    new_name = sys.argv[5]
    list_states(username, password, database_name, state_id, new_name)
