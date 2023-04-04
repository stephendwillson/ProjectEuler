import euler_lib


def main():

    ceiling = 1000000

    # circular prime can't contain these digits because at least one
    # rotation wouldn't be prime
    bad_digits = ['0', '2', '4', '5', '6', '8']

    total = 4  # count single digit primes so they're not excluded...
    for i in range(11, ceiling + 1, 2):  # ...and start loop appropriately

        digit_set = set(str(i))

        if any(digit in digit_set for digit in bad_digits):
            continue

        if euler_lib.is_circular_prime(i):
            total += 1

    return total


def description():

    desc = """
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""
    print(desc, end="")


PE_NAME = "CIRCULAR PRIMES"
PE_SOLUTION = 55

if __name__ == "__main__":
    print(main())
