#!/usr/bin/python3
""" Lists all states from db hbtn_0e_0_usa """


import MySQLdb
import sys

def list_states(username, password, database_name, host, port):
	""" Listing states in db """
	db = MySQLdb.connect(
		user=username,
		passwd=password,
		db=database_name,
		host=host,
		port=port
    )

	cursor = db.cursor()
	query = "SELECT * FROM states ORDER BY states.id"
	cursor.execute(query)

	results = cursor.fetchall()

	for state in results:
		print(state)

	cursor.close()
	db.close()

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	database_name = sys.argv[3]
	host = "localhost"
	port = 3306
	list_states(username, password, database_name, host, port)
