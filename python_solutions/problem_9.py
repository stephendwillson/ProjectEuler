import math
import time

def main():

    triplet = get_triplet()

    # convert list to int for math.prod
    triplet = [int(i) for i in triplet]

    return math.prod(triplet)

# square sum relation: (a^2 + b^2 = c^2) == (c^2 = m^4 + n^4 + 2*m^2*n^2)
def get_triplet():

    c = 0
    m = 0

    while True:
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n

            if a + b + c == 1000:
                return [a, b, c]

        m += 1

    return None

def description():

    desc = """
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
    print(desc, end="")
pe_name = "SPECIAL PYTHAGOREAN TRIPLET"
if __name__ == "__main__":
    main()
