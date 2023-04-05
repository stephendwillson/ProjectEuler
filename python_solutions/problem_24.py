import math


def main():

    ceiling = 1000000

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    permutation = []
    length = len(digits)

    for _ in range(length):

        # calculate the factorial for the remaining digits
        factorial = math.factorial(length - 1)

        # calculate the index of the digit to add to the permutation
        index = (ceiling - 1) // factorial

        # add the digit to the permutation and remove from the list of digits
        digit = digits[index]
        permutation.append(digit)
        digits.remove(digit)

        # adjust the ceiling and length for the next iteration
        ceiling = ceiling - (index * factorial)
        length = length - 1

    nth_permutation = int("".join(str(d) for d in permutation))

    return nth_permutation


def description():

    desc = """
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
    print(desc, end="")


PE_NAME = "LEXICOGRAPHIC PERMUTATIONS"
PE_SOLUTION = 2783915460

if __name__ == "__main__":
    print(main())
