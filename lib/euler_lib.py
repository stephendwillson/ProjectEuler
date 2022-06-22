"""
sdwillso
Common functionality for solving Project Euler problems.
"""

import math


# get number of paths from (0, 0) -> (m, n) only moving right or down
def count_lattice_paths(n, m):

    # n x m lattice paths will always have n + m steps
    # out of n + m, count all possible downward steps, anything left is rightward
    return math.factorial(n + m) // math.factorial(n) // math.factorial(m)

# print n x m grid
def print_grid(grid): 
 
    n = len(grid)
    m = len(grid[0])

    if n == 0:
        print("Grid is empty!")

    p = ""
    for i in range(0, n): 
        for j in range(0, m): 
            p += "{} ".format(grid[i][j]) 
        
        print(p)
        p = ""

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

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)

            if n / i != i:
                factors.append(math.floor(n / i))
    
    return factors

# all factors except for self
def get_proper_factors(n):

    factors = get_factors(n)

    if n in factors:
        factors.remove(n)
    
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
