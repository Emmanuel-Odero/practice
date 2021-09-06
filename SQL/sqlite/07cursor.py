#note that a cursor is used to make things much faster instead of querying a database
#directyly



import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
cursor = base.cursor()
print('\n\nDatabase openned\n')
print("cursor created.")

data = cursor.execute("SELECT * FROM employee_records")

for x in data:
	print('(',x[0], ":", x[1], ":", x[2], ":", x[3],')')

print("\n\nUsing fetchall to get data")
w =  data.fetchall()
print(w)  # why is it giving a blank list