import euler_lib


def main():

    n = 11

    t_primes = []
    i = 11
    while len(t_primes) < n:

        i += 2

        if euler_lib.is_left_right_truncatable_prime(i):
            t_primes.append(i)

    return sum(t_primes)


def description():

    desc = """
https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
    print(desc, end="")


PE_NAME = "TRUNCATABLE PRIMES"
PE_SOLUTION = 748317

if __name__ == "__main__":
    print(main())
