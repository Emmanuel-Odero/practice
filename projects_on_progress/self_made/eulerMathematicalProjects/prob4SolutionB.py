print("Find the largest palindrome (press q to exit)")
maxim = int(input("Input maximum product: "))
while maxim != "q":
	values = [str(x * y) for x in range(1, maxim) for y in range(x,maxim)]
	palindrome = [int(val) for val in values if val == val[::-1]]
	maxPalindrome = max(palindrome)
	print("Largest palindrome made from product of all value in the  range of " + str(maxim) + " is " + str(maxPalindrome) + "\n\n")
	maxim = input("Input maximum product: ")
	if maxim != "q":
		maxim = int(maxim)
	else :
		maxim =maxim