# coding=utf-8
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from sympy import primerange

list = ([i for i in primerange(2, 200000)])

print(len(list))
print(list[10000])