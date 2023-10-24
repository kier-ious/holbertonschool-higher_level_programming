#!/usr/bin/python3
""" List all states that start with a cap N in db"""


import MySQLdb
import sys


def list_states_starting_with_N(username, password, database_name):

    """ Listing states in db """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name,
        host=host,
        port=port
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    results = cursor.fetchall()

    for state in results:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    list_states_starting_with_N(username, password, database_name, host, port)
