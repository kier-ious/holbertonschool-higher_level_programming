#!/usr/bin/python3
""" Lists all cities by state from db hbtn_0e_0_usa """


import MySQLdb
import sys


def list_cities(username, password, database_name, state_name):
    """ Listing cities by state in db """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name,
        host="localhost",
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("""
        SELECT cities.name
        FROM cities LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY '{}'
        ORDER BY cities.id""".format(state_name))

    results = cursor.fetchall()

    cities = [city[0] for city in results]
    cities_str = ", ".join(cities)
    print(cities_str)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    list_cities(username, password, database_name, state_name)
