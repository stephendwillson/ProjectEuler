import euler_lib


def main():

    num_primes = 10001

    return get_nth_prime(num_primes)


def get_nth_prime(n):

    count = 0
    i = 0

    while count < n:
        i += 1
        if euler_lib.is_prime(i):
            count += 1

    return i


def description():

    desc = """
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
    print(desc, end="")


PE_NAME = "10001ST PRIME"
PE_SOLUTION = 104743

if __name__ == "__main__":
    print(main())
