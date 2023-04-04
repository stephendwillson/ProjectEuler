import euler_lib


def main():

    running_prime_count = 0
    max_prime_seq_len = 0

    max_product = 0

    for a in range(-1000, 1000):
        for b in range(-1001, 1001):

            n = 0
            while True:

                if not euler_lib.is_prime(n*n + a*n + b):
                    break

                running_prime_count += 1
                n += 1

            if running_prime_count > max_prime_seq_len:
                max_prime_seq_len = running_prime_count
                max_product = a * b
            running_prime_count = 0

    return max_product


def description():

    desc = """
https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 <= n <= 39. However, when n = 40,
40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41,
41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces
80 primes for the consecutive values 0 <= n <= 79. The product of the
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

            n^2 + an + b   where   |a| < 1000   and   |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""
    print(desc, end="")


PE_NAME = "QUADRATIC PRIMES"
PE_SOLUTION = -59231

if __name__ == "__main__":
    print(main())
