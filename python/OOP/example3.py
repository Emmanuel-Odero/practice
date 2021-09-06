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

	@classmethod
	def setRaiseAmount(cls, amount):
		cls.raiseAmount = amount

	@staticmethod
	def isWorkingDay(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



emp1 = Employee('Michael', "Ochara", 23000)
emp2 = Employee('Susan', "Onyango", 23000)

Employee.setRaiseAmount(2)

#x = str(emp1.raiseAmount())
#print(x)


import datetime

mydate = datetime.date(2016, 7, 10)

print(Employee.isWorkingDay(mydate))
