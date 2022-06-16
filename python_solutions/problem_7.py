"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import time
import math

def main():

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

def naive_solution(num_primes):
    
    count = 0
    n = 1
    
    while count < num_primes:
        n += 1
        for i in range(2, n):
            if(n % i == 0):
                break
        else:
            count += 1
    
    return n

def optimized_solution(num_primes):
    
    count = 0
    i = 0
    
    while count < num_primes:
        i += 1
        if is_prime(i):
            count += 1
    
    return i

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
