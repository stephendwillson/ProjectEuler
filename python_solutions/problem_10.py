import math

import euler_lib


def main():

    ceiling = 2000000
    total = 2 # skip 2, only prime check odd #s

    for i in range(3, ceiling + 1, 2):
        if euler_lib.is_prime(i):
            total += i

    print("sum of primes below {}: {}".format(ceiling, total))

def description():

    desc = """
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
