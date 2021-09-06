'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

'''def primeNumber(number):					#Find a way to improve the primeNumber function since its taking long to run this script.
	count = 0
	for x in range(2, number):
		if count < 1:
			if number % x == 0:
				count = count + 1
	if count == 0:
		prime= True
	else:
		prime = False
	return prime'''
def primeNumber(x):
	from math import sqrt
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

def primesListBelow(below):
	primes = [2]
	for x in range(3, 9999999999999999999999999999999999999999999999999999999999999999999):
		if primes[-1] < below:
			if primeNumber(x):
				print(x)
0				primes.append(x)
		else:
			break 
	primeList = [x for x in primes if x < below]	
	return primeList

maximum = int(input("\nFind the prime numbers and their sum below:_"))

#This is a list of prime numbers below the inputed maximum
primeListing = primesListBelow(maximum)

#print the prime numbers
print("\nThe prime numbers below " + str(maximum) + " are:_")
print(primeListing)

#print the sum of the prime numbers
totalPrimes = 0
for x in primeListing:
	totalPrimes = x + totalPrimes
print("\nThe sum of prime numbers below " + str(maximum) + " is "+ str(totalPrimes) + "\n")
