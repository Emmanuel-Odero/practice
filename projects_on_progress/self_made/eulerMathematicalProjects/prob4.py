'''palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers 
 is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''
h = int(input("Find the larges palindrome made form the product of numbers below:_"))
palindromes = max((x * y)for x in range(1, h) for y in range(x, h) if str(x * y) == str(x * y)[::-1])
print(palindromes)