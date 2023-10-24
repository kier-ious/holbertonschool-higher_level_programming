#!/usr/bin/python3
""" Lists all states from db hbtn_0e_0_usa """


import MySQLdb
import sys


def list_cities(username, password, database_name):

    """ Listing states in db """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name,
        host=host,
        port=port
    )

    cursor = db.cursor()
    cursor.execute("""
        SELECT cities.id, cities.name, state.name
        FROM cities JOIN states ON cities.state_id = states.id
        ORDER BY cities.id""")

    results = cursor.fetchall()

    for city in results:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    list_cities(username, password, database_name)
