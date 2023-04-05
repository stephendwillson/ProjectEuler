import euler_lib


def main():

    max_a = 1000
    max_b = 1000

    # compute the list of odd primes up to the max value of b
    tmp_prime_list = euler_lib.get_primes_below_n(max_b)
    prime_list = []
    for p in tmp_prime_list:
        if 2 < p < max_b and p % 2 == 1:
            prime_list.append(p)

    max_prime_seq_len = 0
    max_product = 0

    for a in range(-max_a, max_a + 1):
        for b in prime_list:

            # count number of consecutive primes
            n = 1
            while euler_lib.is_prime(n*n + a*n + b):
                n += 1

            if n > max_prime_seq_len:
                max_prime_seq_len = n
                max_product = a * b

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
