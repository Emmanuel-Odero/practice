'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

n = int(input("Input the figure you want to find it's prime factor:_"))

#Find a way to improve the primeNumber function since its taking long to run this script.

def primeNumber(number):					
	count = 0
	for x in range(1, number+1):
		if number % x == 0:
			count = count + 1
	if count == 2:
		prime= True
		print('[+] adding {} as a prime factor'.format(x))
	if count !=2:
		prime = False
		print(count)
	return prime

def primeFactors(n):
	primeDivisors = [x for x in range(1, n+1) if n % x == 0 if primeNumber(x)]
	return primeDivisors


print("The prime factors of " + str(n) + " are: ")

ans = primeFactors(n)
for t in ans:
	print(t)
print("The maximum prime factor is " + str(max(ans)))
	
