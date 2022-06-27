"""
sdwillso
Common functionality for solving Project Euler problems.
"""

import math
import string

# add up total for word where A=1, B=2, ..., Y=25, Z=26
def get_word_score(s):

    s = s.upper()
    score = 0
    
    for char in s:
        char_index = string.ascii_uppercase.find(char)
        if char_index != -1:
            score += char_index + 1 # A == [0] --> A == 1 score
            
    return score

# circular prime == all rotations of N are prime, ie 197: 197, 719, 971
def is_circular_prime(n):

    tmp = str(n)

    for i in range(0, len(tmp)):
        
        tmp = rotate(str(n), i)
        if not is_prime(int(tmp)):
            return False

    return True

# circular rotate string by N positions
def rotate(s, n):

    return s[n:] + s[:n]

def is_palindrome(s):

    return str(s) == str(s)[::-1]

# leap year checker
def is_leap_year(y):

    if y % 400 == 0:
        return True

    if y % 100 == 0:
        return False

    if y % 4 == 0:
        return True

    return False

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
