#!/usr/bin/python3
""" Lists all states from db hbtn_0e_0_usa """


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, database_name):
    """ Listing states in db """
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = session.query(State).filter_by(state_id).first()

    if update_state:
        update_state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_id = int(sys.argv[4])
    new_name = sys.argv[5]
    list_states(username, password, database_name)
