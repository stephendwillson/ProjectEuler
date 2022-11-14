import math

import euler_lib


def main():

    n = 100

    fact = math.factorial(n)
    digit_sum = euler_lib.sum_digits(fact)
    
    return digit_sum

def description():

    desc = """
https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
    print(desc, end="")

pe_name = "FACTORIAL DIGIT SUM"
pe_solution = 648

if __name__ == "__main__":
    print(main())
