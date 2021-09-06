class Student:

	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()

	def show(self):
		return "Name: " + self.name + "\nRollno: " + str(self.rollno)

	class Laptop:
		def __init__(self, brand, cpu):
			self.brand = "HP"
			self.cpu = "i7"

s1 = Student('Marvin', 234)
s2 = Student('Joel', 412)

print(s1.show())