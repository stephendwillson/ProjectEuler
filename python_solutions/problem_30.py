import math


def main():

    # ceiling = #_digits x 9^exp
    # ceiling = 5 * 9^5 = 295245

    exp = 5
    ceiling = 295245
    total = 0

    # calculate the value of 1 - 9 ^ exp up front to save time
    digit_powers = [math.pow(i, exp) for i in range(10)]

    for i in range(2, ceiling):

        i_total = 0
        for digit in str(i):
            i_total += digit_powers[int(digit)]

        if i_total == i:
            total += i

    return total


def description():

    desc = """
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""
    print(desc, end="")


PE_NAME = "DIGIT FIFTH POWERS"
PE_SOLUTION = 443839

if __name__ == "__main__":
    print(main())
