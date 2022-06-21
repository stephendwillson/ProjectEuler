"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import time

import euler_lib


n = 600851475143

start_time = time.process_time()
factors = euler_lib.get_prime_factors(n)
end_time = time.process_time()

print("time to calculate: {}".format(end_time - start_time))
print("largest prime factor of {}: {}".format(n, max(factors)))
