#!/usr/bin/python3
""" Lists all states from db hbtn_0e_0_usa """


import MySQLdb
import sys

def list_states(username, password, database_name, host, port):
	""" Listing states in db """
	try:
		db = MySQLdb.connect(
			username=sys.argv[1],
			password=sys.argv[2],
			database_name=sys.argv[3],
			host = "localhost",
			port = 3306
		)

		cursor = db.cursor()
		""" Execute SQL query """
		query = "SELECT * FROM states ORDER BY states.id ASC;"
		cursor.execute(query)

		results = cursor.fetchall()

		for state in results:
			print(state)

		cursor.close()
		db.close()

	except MySQLdb.Error as e:
		print("Error: ", e)

if __name__ == "__main__":
	username=sys.argv[1],
	password=sys.argv[2],
	database_name=sys.argv[3],
	list_states(username, password, database_name)
