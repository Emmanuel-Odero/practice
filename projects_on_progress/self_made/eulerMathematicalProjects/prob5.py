'''520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''



n = int(input("To find the smallest positive number that is evenly divisible by all of the numbers from 1 to : _"))

def smallestEvenlyDivisible(n):
	testRange = range(1, n + 1)
	w = range(1, 1000000000000000000000000000000000000000000000000)			
	for x in w:
		count = 0
		for y in testRange:
			if x % y == 0:
				count = count + 1
				if count == n:
					return x
for t in range(n):
	print(t , smallestEvenlyDivisible(t))