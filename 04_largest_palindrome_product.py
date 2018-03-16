# coding=utf-8

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

a = 100
b = 100
p = []

def palindrome_check():
	result = str(a * b)
	reverse = result[::-1]
	if result == reverse:
		p.append(int(result))
		print('You found the palindrome', a * b, 'found with', a, '&', b)

for a in range(100,999):
	palindrome_check()
	for b in range(100, 999):
		palindrome_check()

print('The final palindrome was found to be', max(p))