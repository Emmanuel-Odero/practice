import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
print('\n\nDatabase openned\n')


def update_record():  #provide the division and id where you would like to make the change
	base.execute('UPDATE employee_records set DIVISION="" WHERE ID=')
	base.commit()
	print("Employee record has been updated.")

update_record()

base.close()
print("\nDatabase has been closed.")