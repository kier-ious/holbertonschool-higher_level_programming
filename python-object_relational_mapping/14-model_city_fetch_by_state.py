#!/usr/bin/python3
""" Deletes all states from db hbtn_0e_0_usa w/ an 'a' """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City


def cities_states(username, password, database_name):
    """ Listing states in db """
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
        echo=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states = session.query(City, State).join(State).order_by(City.id)

    for city, state in cities_states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    cities_states(username, password, database_name)
