class Employee:

	numOfEmployees = 0
	raiseAmount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@chefted.com"

		Employee.numOfEmployees = Employee.numOfEmployees + 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def applyRaise(self):
		self.pay = int(self.pay * self.raiseAmount)

class Developer(Employee):
	 
	 raiseAmount = 1.10

	 def __init__(self, first, last, pay, progLang):
	 	super().__init__(first, last, pay)
	 	self.progLang = progLang

class Manager(Employee):

	raiseAmount = 1.12

	def __init__(self, first, last, pay, employees):
	 	super().__init__(first, last, pay)
	 	if employees is None:
	 		self.employees = []
	 	else:
	 		self.employees = employees

	def add_emp(self, emp):
	 	if emp not in self.employees:
	 		self.employees.append(emp)

	def remove_emp(self, emp):
	 	if emp in self.employees:
	 		self.employees.remove(emp)

	def print_emp(self):
	 	for emp in self.employees:
	 		print("-->", emp.fullname())

	 		



emp1 = Employee('Michael', "Ochara", 23000)
emp2 = Employee('Susan', "Onyango", 23000)

mng = Manager("Sue", "Smith", 9000, [emp1])
mng.add_emp(emp2)
mng.print_emp()

print(isinstance(mng, Employee))
print(issubclass(Developer, Employee))