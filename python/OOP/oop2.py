class Computer:
	school = 'Manyatta'
	def __init__(self, cpu, ram):
		self.cpu = cpu
		self.ram = ram				#These are instance varible while those defined outside are static variables

	def config(self):
		print('This computer has been configed to ' + self.cpu + ' and ' + self.ram)

	@classmethod		#this when we want to use a variable like school in this case which is a static variable
	def info(cls):
		return cls.school

	@staticmethod
	def info2():
		print("Note that here we dont include anything in the brackets for static methods")

comp1 = Computer('i5', '16GB')	#Here we are creating the objects and everytime we create an object its normally created in head memory that we can investigate as follows id(object)
comp2 = Computer('i7', '24GB')	#Constructor creates the memory

comp1.config()
comp2.config()
print(Computer.info())
Computer.info2()