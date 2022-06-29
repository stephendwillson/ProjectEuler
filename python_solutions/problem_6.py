import euler_lib


def main():

    n = 100

    summed = euler_lib.sum_of_squares(n)
    squared = euler_lib.square_of_sums(n)
    delta = squared - summed

    return delta

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

pe_name = "SUM SQUARE DIFFERENCE"
pe_solution = 25164150

if __name__ == "__main__":
    print(main())
