"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

i = 1

for d in range(3, 10):
	while i % d == 0:
		d += 1
		if d == 10:
			print(i, 'is divisible by all!')
	i += 1