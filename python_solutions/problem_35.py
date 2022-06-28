"""
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import euler_lib


n = 1000000

total = 0
for i in range(1, n + 1):
    if euler_lib.is_circular_prime(i):
        total += 1

print("circular primes below {}: {}".format(n, total))