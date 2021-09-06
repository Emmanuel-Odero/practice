def primeNumber(number):					#Find a way to improve the primeNumber function since its taking long to run this script.
	count = 0
	for x in range(1, number+1):
		if number % x == 0:
			count = count + 1
	if count == 2:
		prime= True
	if count !=2:
		prime = False
	return prime

def primeList(num):
	primes = []
	for x in range(1, 1000000000000000):
		if len(primes) < num:
			if primeNumber(x):
				print(x)
				primes.append(x)
		else:
			break
	return primes

print(primeList(100))