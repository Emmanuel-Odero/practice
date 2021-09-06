from sqlalchemy import create_engine

engine = create_engine('sqlite:///some.db')

#create_engine("postgresql://scott:tiger@localhost/test")

result = engine.execute("CREATE TABLE IF NOT EXISTS employee_records("
		"ID INT PRIMARY KEY NOT NULL,"
		"NAME TEXT NOT NULL,"
		"DIVISION TEXT NOT NULL,"
		"RATING INT NOT NULL)")

#it act like a dictionary object
row = result.fetchone()
#row['ID'] or row.ID gives the same query. row.keys() gives the table keys

#to close the connection 
result.close()

#to get a list of all the rows.
result.fetchall()


#to do multiple stuff
conn = engine.connect()
result = conn.execute("")
result.fetchall()
conn.close()

#alternative to doing multiple stuff
with engine.begin() as conn:
	conn.execute()
	conn.execute()

#Connection via the engine directly is called connectionless execution the engine connects and disconnect for us.
