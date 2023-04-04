import euler_lib


def main():

    ceiling = 2000000

    primes = euler_lib.get_primes_below_n(ceiling)

    return sum(primes)


def description():

    desc = """
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
    print(desc, end="")


PE_NAME = "SUMMATION OF PRIMES"
PE_SOLUTION = 142913828922

if __name__ == "__main__":
    print(main())
