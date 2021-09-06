import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
print('Database openned')

base.execute(''' INSERT INTO employee_records(ID, NAME, DIVISION, RATING)
		VALUES(4, 'James', 'Maintainace', 9) ''')

base.commit()         #this commits the changes we would like to make to the database

print('employee_added')

base.close()
print('Database closed')