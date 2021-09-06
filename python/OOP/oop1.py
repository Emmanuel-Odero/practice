class Computer:
	def config(self):
		print("This is a 16GB computer.")
		

m1 = Computer()  #we have to create the object first

Computer.config(m1)  #These two produces the same result.
m1.config()				#computer().config()   these two have the same meaning
