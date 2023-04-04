import euler_lib


def main():

    # grid dimensions
    n = 1001
    m = 1001

    # maximum value of the spiral
    ceiling = n * m

    # make the spiral
    spiral = euler_lib.generate_number_spiral(ceiling)

    # voila
    d_sum = euler_lib.get_matrix_diagonals_sum(spiral)

    return d_sum


def description():

    desc = """
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
sdwillso NOTE: Numbers along diagonals from corner to corner are highlighted.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?

"""
    print(desc, end="")


PE_NAME = "NUMBER SPIRAL DIAGONALS"
PE_SOLUTION = 669171001

if __name__ == "__main__":
    print(main())
