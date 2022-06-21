"""
sdwillso
Common functionality for solving Project Euler problems.
"""

import math

# add up all the digits in n
def sum_digits(n):

    total = 0

    for digit in str(n):
        total += int(digit)

    return total

# get length of longest collatz sequence
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# reduce to 1, counting steps to get there
def get_collatz_length(n):
    
    length = 1 

    while n > 1: 
        if n % 2 == 0:
            n = n/2
        else: 
            n = 3*n + 1

        length += 1

    return length

# 1 + 2 + ... + n-1 + n
def get_triangle_number(n):

    triangle = 0
    for i in range(1, n + 1):
        triangle += i

    return triangle


def sum_of_squares(n):

    total = 0
    for i in range(1, n + 1):
        total += i * i

    return total

def square_of_sums(n):

    total = 0
    for i in range(1, n + 1):
        total += i

    return total * total

# get all factors, not just prime etc.
def get_factors(n):

    factors = list()

    if n <= 1:
        return factors

    i = 1
    while i <= math.floor(math.sqrt(n)):
        if n % i == 0:

            if n / i == 0: # if divisors are equal
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n / i)

        i += 1

    return factors

# simple prime checker
def is_prime(n):

    # handle 1, 2, and all even numbers
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # odd numbers
    for i in range(3, 1 + math.floor(math.sqrt(n)), 2):
        if n % i == 0:
            return False

    return True

# composite number reduction
def get_prime_factors(n):

    p_factors = list()

    c = 2
    while n > 1:

        if n % c == 0:
            p_factors.append(c)
            n /= c
        else:
            c += 1

    return p_factors
