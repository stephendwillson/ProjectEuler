import euler_lib


def main():

    n = 600851475143

    factors = euler_lib.get_prime_factors(n)

    print("largest prime factor of {}: {}".format(n, max(factors)))

def description():

    desc = """
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
