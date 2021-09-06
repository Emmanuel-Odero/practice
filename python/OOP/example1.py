class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@chefted.com"

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp1 = Employee('Michael', "Ochara", 20000)

print(emp1)
print(emp1.fullname())
print(Employee.fullname(emp1))