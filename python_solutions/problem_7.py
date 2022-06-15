"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import sys
import time
import math

def main():

    # the N in 'find the Nth prime'
    num_primes = 10001

    # time the slow 'naive' algorithm
    start_time = time.process_time()
    naive_prime = naive_solution(num_primes)
    end_time = time.process_time()
    
    print("'Naive' algorithm time: {}".format(end_time - start_time))
    print("Prime number #{}: {}".format(num_primes, naive_prime))
    
    

    # time the optimized algorithm
    start_time = time.process_time()
    optimized_prime = optimized_solution(num_primes)
    end_time = time.process_time()

    print("Optimized algorithm time: {}".format(end_time - start_time))
    print("Prime number #{}: {}".format(num_primes, optimized_prime))


# naive brute force solution
def naive_solution(num_primes):
    
    prime_count = 0
    n = 1 # skip 1
    
    while prime_count < num_primes:
        n += 1
        for i in range(2, n):
            if(n % i == 0):
                break
        else:
            prime_count += 1
    
    return n

# sane optimized solution
def optimized_solution(num_primes):
    
    prime_count = 0
    index = 0
    
    while prime_count < num_primes:
        index += 1
        if is_prime(index):
            prime_count += 1
    
    return index

def is_prime(n):

    # handle 1, 2, and all even numbers
    if n <= 1:
        return False
    if n == 2:
        return True
    if n >= 2 and n % 2 == 0:
        return False

    # odd numbers - start at 3, test and increment by 2
    n_sqrt_floor = math.floor(math.sqrt(n))
    for i in range(3, 1 + n_sqrt_floor, 2):
        if n % i == 0:
            return False

    return True

main()
