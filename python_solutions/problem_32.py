import math


def main():

    # digits can be 1-9 and no repeated digits = 9! possible pandigital #s
    # max value of prod of two 5-digit #s = 9,999,800,001
    # 10 digits and not pandigital - only consider products up to sqrt(ceiling)
    ceiling = math.factorial(9)
    pandigitals = set()

    for multiplicand in range(3, int(math.sqrt(ceiling)) + 1):
        for multiplier in range(3, ceiling // multiplicand + 1):

            prod = multiplier * multiplicand
            mult_str = "".join([str(multiplier),
                                str(multiplicand),
                                str(prod)])

            if len(mult_str) != 9:
                continue

            if is_pandigital(mult_str):
                pandigitals.add(prod)

    return sum(pandigitals)


def is_pandigital(pd):
    """
    Check if a number is 1-9 pandigital - makes use of all the digits
    1 to 9.

    :param pd: Integer to check for pandigitality
    :type pd: int
    :rtype: bool
    """

    digits = set(str(d) for d in range(1, 10))
    n_digits = set(str(pd))

    return len(n_digits) == len(digits) and n_digits == digits


def description():

    desc = """
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
    print(desc, end="")


PE_NAME = "PANDIGITAL PRODUCTS"
PE_SOLUTION = 45228

if __name__ == "__main__":
    print(main())
