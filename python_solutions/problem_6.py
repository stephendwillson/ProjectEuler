import euler_lib


def main():

    n = 100

    summed = euler_lib.sum_of_squares(n)
    squared = euler_lib.square_of_sums(n)
    delta = squared - summed

    print("Sum of squares: {}".format(summed))
    print("Square of sums: {}".format(squared))
    print("Delta: {} - {} = {}".format(squared, summed, delta))

def description():

    desc = """
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
