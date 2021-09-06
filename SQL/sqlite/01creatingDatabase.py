import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
print('Database openned')

base.execute('''CREATE TABLE IF NOT EXISTS employee_records(
		ID INT PRIMARY KEY NOT NULL,
		NAME TEXT NOT NULL,
		DIVISION TEXT NOT NULL,
		RATING INT NOT NULL)''')
print('Table created')

base.close()
print('Database closed')