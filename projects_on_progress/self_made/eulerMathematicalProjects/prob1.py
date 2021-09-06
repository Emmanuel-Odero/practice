'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

import logging

logging.basicConfig(level=logging.DEBUG)

print("Find the sum of all the multiples of 3 or 5")
max_value = int(input("Below:_"))
logging.info('[+] calculating the values that are divisible')
divisible35 = [x for x in range(1, max_value) if x % 3 == 0 or x % 5 == 0]
for x in divisible35:
	print(x)

logging.info('[+] summing the divisibles')
totalOfDivisible35 = sum(divisible35)

print("The sum of all multiples of 3 or 5 below " + str(max_value) + " is " + str(totalOfDivisible35))

