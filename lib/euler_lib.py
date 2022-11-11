"""
sdwillso
Common functionality for solving Project Euler problems.
"""

import math
import string

# collapse triangle upwards, updating bottom row with current maximums
def get_triangle_max_path_sum(t):
    
    for i in range(len(t) - 1, 0, -1):
        
        # make new row of maximums of bottom 2 rows
        tmp = list()
        for j in range(0, len(t[i-1])):
            tmp.append(t[i-1][j] + max(t[i][j], t[i][j+1]))
        
        # get rid of current bottom row, replace new bottom with updated maximums
        t.pop() 
        t[-1] = tmp
    
    return t[0][0]

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
 
    if len(grid) == 0:
        print("Grid is empty!")

    p = ""
    for i in range(0, len(grid)):
        for ele in grid[i]:
            p += "{} ".format(ele)

        print(p)
        p = ""

# add up all the digits in n
def sum_digits(n):

    total = 0

    for digit in str(n):
        total += int(digit)

    return total

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

# get recurring cycle in the decimal for 'numerator / denominator' if one exists, otherwise return None
def get_recurring_decimal_cycle(numerator, denominator):
    
    repeat = ""

    # remainder dictionary --> {remainder : position}
    rem_dict = {}

    # if remainder ever hits 0, there's no cycle
    remainder = numerator % denominator
    while(remainder != 0 and remainder not in rem_dict):

        rem_dict[remainder] = len(repeat)

        remainder *= 10
        repeat += str(remainder // denominator)

        remainder %= denominator

    if(remainder == 0):
        return None
    else:
        return repeat[rem_dict[remainder]:]