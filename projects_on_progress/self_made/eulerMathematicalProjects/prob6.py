'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def square(x):
	return x ** 2

def sumOfSquares(w):
	squaresList = []
	for  r in range(1, w + 1):
		s = square(r)
		squaresList.append(str(s))
	intSquares = [int(t) for t in squaresList]
	sumOfSquares = sum(intSquares)
	return sumOfSquares

def squareOfsum(w):
	numbers = [x for x in range(1, w + 1)]
	total = sum(numbers)
	sumSquared = total ** 2
	return sumSquared

inputedRange = int(input("\nInput the range you would like operate on:_"))
sumOfSquaresAns = sumOfSquares(inputedRange)
squareOfsumAns = squareOfsum(inputedRange)
print("The sum of the squares of the first " + str(inputedRange) + " natural numbers is " + str(sumOfSquaresAns))
print("The square of the sum of the first " + str(inputedRange) + " natural numbers is " + str(squareOfsumAns))
print("The difference between the sum of the squares of the first " + str(inputedRange) + " natural numbers and the square of the sum is " + str(squareOfsumAns - sumOfSquaresAns) + "\n")


