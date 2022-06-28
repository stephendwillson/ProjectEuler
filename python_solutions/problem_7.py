import time
import math

import euler_lib

def main():

    num_primes = 10001

    start_time = time.process_time()
    prime = get_nth_prime(num_primes)
    end_time = time.process_time()

    print("time to calculate: {}".format(end_time - start_time))
    print("Prime number #{}: {}".format(num_primes, prime))

def get_nth_prime(n):
    
    count = 0
    i = 0
    
    while count < n:
        i += 1
        if euler_lib.is_prime(i):
            count += 1
    
    return i

def description():

    desc = """
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
