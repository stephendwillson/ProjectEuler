import math


def main():

    # https://en.wikipedia.org/wiki/Factorion

    # must be smaller than 9999999, sum(factorial of digits of 7*9!) = 2540160
    # pre-calculate factorials for 1-9 to save repeated calculations
    factorials = [math.factorial(i) for i in range(10)]
    ceiling = 7 * factorials[9]

    total = 0
    for i in range(3, ceiling):

        if sum(factorials[int(digit)] for digit in str(i)) == i:
            total += i

    return total


def description():

    desc = """
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
    print(desc, end="")


PE_NAME = "DIGIT FACTORIALS"
PE_SOLUTION = 40730

if __name__ == "__main__":
    print(main())
