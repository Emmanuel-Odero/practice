from sqlalchemy import create_engine

engine =  create_engine("sqlite:///del.db")

print("Add an employee to the database:")
#ident = int(input("What is the employee ID : "))
name = input("What is the name of employee : ")

with engine.begin() as conn:
	conn.execute("create table IF NOT EXISTS employee (ID integer primary key, emp_name varchar(30))")
	conn.execute("insert into employee(emp_name) values(:name)", name = name)

result = engine.execute("SELECT * FROM employee")

for row in result:
	print(row)

result2 = engine.execute("")