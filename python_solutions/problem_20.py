"""
https://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math
import time

def main():

    n = 100

    fact = factorial(n)
    digits = sum_digits(fact)
    
    print("{} factorial: {}".format(n, fact))
    print("sum of digits: {}".format(digits))

def factorial(n):

    fact = 1

    while n > 0:
        fact *= n
        n -= 1

    return fact

def sum_digits(n):

    total = 0

    n_str = str(n)
    for i in range(0, len(n_str)):
        total += int(n_str[i])

    return total
    
main()
