import sqlite3

base = sqlite3.connect("F:/Inuse/Programming/SQL/sqlPractice/sqlite/lite.base")
print('\n\nDatabase openned\n')

def insert_record(ID, NAME, DIVISION, RATING):
	base.execute(''' INSERT INTO employee_records(ID, NAME, DIVISION, RATING)
		VALUES(?,?,?,?) ''', (ID, NAME, DIVISION, RATING))

	base.commit()         #this commits the changes we would like to make to the database

	print('\n' + NAME + ' has been added with id no ' + str(ID) + '.')


print('Insert data into employee_records table')
Id = int(input("Employee id no : "))
name = input('Employee name : ')
division = input('Employee division : ')
rating = int(input("Employee rating : "))


insert_record(Id, name, division, rating)

base.close()
print('\n\nDatabase closed')