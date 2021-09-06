'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def primeNumber(number):					#Find a way to improve the primeNumber function since its taking long to run this script.
	count = 0
	for x in range(1, number+1):
		if number % x == 0:
			count = count + 1
			if count == 3:
				break
	if count == 2:
		prime= True
	else:
		prime = False
	return prime

def primeList(num):
	primes = []
	for x in range(1, 10000000000000000000000):
		if len(primes) < num:
			if primeNumber(x):
				primes.append(x)

		else:
			break
	return primes
	

inputed = int(input("Input the number of prime numbers you would like to output:_"))

count = 0
for p in primeList(inputed):
	count = count + 1
	print('No. ' + str(count) + ' prime number is ' + str(p))


