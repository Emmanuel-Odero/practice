import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
print('\n\nDatabase openned\n')

def delete_record():
	base.execute(""" DELETE FROM employee_records WHERE ID=8 """)
	base.commit()
	print("\nThe record has been deleted.")


delete_record()


base.close()
print("\nDatabase has been closed.")