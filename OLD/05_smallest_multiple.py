"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

i = 1
d = 3
done = 0

while done == 0:
	while i % d == 0:
		d += 1
		if d == 20:
			print(i, 'is divisible by all!')
			done = 1
	d = 3
	i += 1