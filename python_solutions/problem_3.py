"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import time

def main():


    target = 600851475143

    start_time = time.process_time()
    factors = get_prime_factors(target)
    end_time = time.process_time()

    print("time taken to get prime factors: {}".format(end_time - start_time))
    print("largest prime factor of {}: {}".format(target, factors))

def get_prime_factors(n):

    factors = list()

    i = 2
    while i <= n:
        if (n % i == 0):
            factors.append(i)
            n = n/i
        else:
            i += 1

    return max(factors)

main()
