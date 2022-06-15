"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import sys

def largest_prime_factor(target):
    i = 2
    factors = []

    while i <= target:
        if (target % i == 0):
            factors.append(i)
            target = target / i
        else:
            i = i+1

    return max(factors)

test_num = 600851475143
print("The largest prime factor for {}: {}".format(test_num, largest_prime_factor(test_num)))
