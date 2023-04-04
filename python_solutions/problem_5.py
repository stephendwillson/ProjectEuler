import euler_lib


def main():

    # The smallest positive number that is evenly divisible by all of the
    # numbers from 1 to 20 is the least common multiple of those numbers.
    n = 20
    lcm = 1

    for i in range(2, n + 1):
        lcm = euler_lib.get_least_common_multiple(lcm, i)

    return lcm


def description():

    desc = """
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
    print(desc, end="")


PE_NAME = "SMALLEST MULTIPLE"
PE_SOLUTION = 232792560

if __name__ == "__main__":
    print(main())
