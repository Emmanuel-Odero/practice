import mysql.connector 

mydb = mysql.connector.connect(
		user='root',
		passwd='',
		host='localhost',
		port='3306')

print(mydb)