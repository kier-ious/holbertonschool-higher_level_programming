#!/usr/bin/python3
""" Displays arg and all values in states from db where name matches arg """


import MySQLdb
import sys


def list_states_by_name(username, password, database_name, state_searched):

    """ Listing states in db """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name,
        host='localhost',
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
        WHERE name = '{}' ORDER BY states.id""".format(state_searched))

    results = cursor.fetchall()

    for state in results:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]
    list_states_by_name(username, password, database_name, state_searched)
