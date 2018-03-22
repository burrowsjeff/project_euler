# coding=utf-8
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from sympy import primerange

list = ([i for i in primerange(2, 2000000)])

print(len(list))
print(sum(list))