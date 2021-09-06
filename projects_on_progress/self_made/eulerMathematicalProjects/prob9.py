'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 52
9 + 16 = 25 .

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

#define a funtion that takes a value and try retun values that form a pythgorean triplet
def tripletOfAdditionTotal(additionTotal):
	tripletList = []
	for x in range(1, additionTotal+ 1):
		for y in range(x+1, additionTotal):
			z = additionTotal - x - y
			if x*x + y*y == z*z:		
				triplet = [x, y, z]
				tripletList.append(triplet)
	return tripletList


inputed = input("Input the sum of pythogorean triplet you would like to produce:_")
while inputed != 'q':
		inputed = int(inputed)
		print(tripletOfAdditionTotal(inputed))
		inputed = input("Input the sum of pythogorean triplet you would like to produce:_")