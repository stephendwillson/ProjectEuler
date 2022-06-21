"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
import math

import euler_lib


ceiling = 2000000
total = 2 # skip 2, only prime check odd #s

start_time = time.process_time()
for i in range(3, ceiling + 1, 2):
    if euler_lib.is_prime(i):
        total += i
end_time = time.process_time()

print("time to find solution: {}".format(end_time - start_time))
print("sum of primes below {}: {}".format(ceiling, total))
