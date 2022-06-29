import math

import euler_lib


def main():

    ceiling = 2000000
    total = 2 # skip 2, only prime check odd #s

    for i in range(3, ceiling + 1, 2):
        if euler_lib.is_prime(i):
            total += i
    
    return total

def description():

    desc = """
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
    print(desc, end="")

pe_name = "SUMMATION OF PRIMES"
pe_solution = 142913828922

if __name__ == "__main__":
    print(main())
