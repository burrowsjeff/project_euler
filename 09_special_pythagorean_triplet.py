# coding=utf-8
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

a = 1

while a <= 331:
	for b in range(a+1,332):
		if (a+b+(sqrt((a+b)^2))) == 1000:
			print('A =', a, 'B =', b, 'C =', (sqrt((a+b)^2)))
			break
	print(a)
	a += 1