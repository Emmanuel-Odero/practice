import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
print('Database openned')


def read_table():
	data = base.execute("SELECT * FROM employee_records")
	print("These are employee records in the database.")
	for record in data:
		print("\nID     : " + str(record[0]))
		print("NAME   : " + str(record[1]))
		print("DIVISION : " + str(record[2]))
		print("RATING : " + str(record[3]))

read_table()

base.close()
print("\nDatabase closed")