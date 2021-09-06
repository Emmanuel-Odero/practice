'''The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?'''

def Adjacent(m):
	adjacentValues = ['0']
	position = 0
	count = 0
	while adjacentValues[-1] != number[-m:]:
		value = number[count:count + m]
		adjacentValues.append(value)
		count += 1

	adjacentList = [int(x) for x in adjacentValues]

	return adjacentList


def maxFigProducts(lis):
	productsFull = []
	for x in lis:
		count = 1
		for y in str(x):
			if count == 1:
				product = 1 * int(y)
				count = count + 1
			else:
				product = product * int(y) 
		full = str(x) + "-" + str(product)
		productsFull.append(full)
	productLast = [int(m.split("-")[-1]) for m in productsFull ]
	maxProduct = max(productLast)
	
	for m in productsFull:
		if maxProduct == int(m.split("-")[-1]): 
			return (m.split("-")[0], maxProduct)


number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

	

print("The number below can be used to produce defined digit numbers from those adjacent to each other. For example we can produce 4-digit figures and perform operations on them to give the maximum number produced when grouped in in a certain digit number formart\n\n" + number)
print("\n")
inputed = int(input("Input the adjacent number of digits you would like to produce:_"))

#produce the adjacent digits list and name it Adjus
Adjus = Adjacent(inputed)


print("The adjacent " + str(inputed) + " digit-value you can get are\n " + str(Adjus))
print("\n")


#compute the max product of adjacent values and return a tuple of the producer value and the product it gives as maximum
adjacent, maxAdjProduct = maxFigProducts(Adjus)
print("The maximum product is " + str(maxAdjProduct) + " resulting from the products of adjacent values " + str(adjacent) + "\n\n")



