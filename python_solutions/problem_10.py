"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
import math

def main():

    ceiling = 2000000
    total = 2

    start_time = time.process_time()

    for i in range(3, ceiling + 1, 2):
        if (is_prime(i)):
            total += i

    end_time = time.process_time()
    
    print("time to find solution: {}".format(end_time - start_time))
    print("sum of primes below {}: {}".format(ceiling, total))

def is_prime(n):

    # handle 1, 2, and all even numbers
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # odd numbers - start at 3, test and increment by 2
    n_sqrt_floor = math.floor(math.sqrt(n))
    for i in range(3, 1 + n_sqrt_floor, 2):
        if n % i == 0:
            return False

    return True

main()
