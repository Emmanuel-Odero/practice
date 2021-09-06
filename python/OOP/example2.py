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


emp1 = Employee('Michael', "Ochara", 23000)
emp2 = Employee('Susan', "Onyango", 23000)

emp1.raiseAmount = 1.05  # change the class variable RaiseAmount for instance emp1

emp1.applyRaise()
emp2.applyRaise()

print(emp1.pay)
print(emp2.pay)

print(emp1.__dict__)
print(emp2.__dict__)

print(Employee.numOfEmployees)