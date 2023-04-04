"""
sdwillso
Common functionality for solving Project Euler problems.
"""
# pylint: disable=invalid-name
import math
import string
import collections
import itertools


def is_palindrome(s):
    """
    Check if string is a palindrome.

    :type s: string
    :rtype: bool
    """

    return str(s) == str(s)[::-1]


def is_leap_year(y):
    """
    Check if year is a leap year.

    :type y: int
    :rtype: bool
    """

    if y % 400 == 0:
        return True

    if y % 100 == 0:
        return False

    if y % 4 == 0:
        return True

    return False


def get_word_score(s):
    """
    Add up total for word where A=1, B=2, ..., Y=25, Z=26.

    :type s: string
    :rtype: int
    """

    s = s.upper()
    score = 0

    for char in s:
        char_index = string.ascii_uppercase.find(char)
        if char_index != -1:
            score += char_index + 1  # A == [0] --> A == 1 score

    return score


def rotate(s, n):
    """
    Rotate string by n positions.

    :type s: string
    :param n: Number of positions to rotate
    :type n: int
    :return: Rotated string
    :rtype: string
    """

    return s[n:] + s[:n]


def sum_digits(n):
    """
    Add up all the digits in a number.

    :type n: int
    :rtype: int
    """

    total = 0

    for digit in str(n):
        total += int(digit)

    return total


def get_triangle_number(n):
    """
    Add integers from 1 through n.

    :type n: int
    :rtype: int
    """

    triangle = 0
    for i in range(1, n + 1):
        triangle += i

    return triangle


def sum_of_squares(n):
    """
    Calculate sum of all squares from 1 through n.
    1^2 + 2^2 + ... + (n-1)^2 + n^2

    :type n: int
    :rtype: int
    """

    total = 0
    for i in range(1, n + 1):
        total += i * i

    return total


def square_of_sums(n):
    """
    Calculate the square of sums from 1 through n.
    (1 + 2 + ... + n-1 + n) ^ 2

    :type n: int
    :rtype: int
    """

    total = 0
    for i in range(1, n + 1):
        total += i

    return total * total


# get all factors, not just prime etc.
def get_factors(n):
    """
    Find all factors of a number.

    :type n: int
    :rtype: int array
    """

    factors = []

    if n <= 1:
        return factors

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)

            if n / i != i:
                factors.append(math.floor(n / i))

    return factors


def get_proper_factors(n):
    """
    Find all factors of n except for self.

    :type n: int
    :rtype: int array
    """

    factors = get_factors(n)

    if n in factors:
        factors.remove(n)

    return factors


def get_prime_factors(n):
    """
    Find all prime factors of a number.

    :type n: int
    :rtype: int array
    """

    p_factors = []

    c = 2
    while n > 1:

        if n % c == 0:
            p_factors.append(c)
            n /= c
        else:
            c += 1

    return p_factors


def is_prime(n):
    """
    Test if a number is prime.

    :type n: int
    :rtype: bool
    """

    # handle 1, 2, and all even numbers
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # odd numbers
    for i in range(3, 1 + math.floor(math.sqrt(n)), 2):
        if n % i == 0:
            return False

    return True


def is_circular_prime(n):
    """
    Determine if specified number is a circular prime. Circular prime == all
    rotations of N are prime.
    Ex. 197: 197, 719, 971.

    :type n: int
    :rtype: bool
    """

    tmp = str(n)

    for i in range(0, len(tmp)):

        tmp = rotate(str(n), i)
        if not is_prime(int(tmp)):
            return False

    return True


# get_triangle_max_path_sum
def get_triangle_max_path_sum(t):
    """
    Find the sum of the vertical path through a number triangle with the
    highest max value.

    :param t: Number triangle
    :type t: 2D list of ints
    :rtype: int
    """

    # collapse triangle upwards, updating bottom row with current maximums
    for i in range(len(t) - 1, 0, -1):

        # make new row of maximums of bottom 2 rows
        tmp = []
        for j in range(0, len(t[i-1])):
            tmp.append(t[i-1][j] + max(t[i][j], t[i][j+1]))

        # get rid of current bottom row
        # replace new bottom with updated maximums
        t.pop()
        t[-1] = tmp

    return t[0][0]


def get_recurring_decimal_cycle(numerator, denominator):
    """
    Find recurring cycle in the decimal for 'numerator / denominator' if
    one exists.

    :type numerator: int
    :type denominator: int
    :return: Numeric cycle if one exists
    :rtype: int, None
    """

    repeat = ""

    # remainder dictionary --> {remainder : position}
    rem_dict = {}

    # if remainder ever hits 0, there's no cycle
    remainder = numerator % denominator
    while (remainder != 0 and remainder not in rem_dict):

        rem_dict[remainder] = len(repeat)

        remainder *= 10
        repeat += str(remainder // denominator)

        remainder %= denominator

    if remainder == 0:
        return None

    return repeat[rem_dict[remainder]:]


def num_coin_combos(coins, target):
    """
    Find the total number of combinations of coins that add up to the target.

    :param coins: Possible coin values
    :type coins: int array
    :param target: Amount coins should add up to
    :type target: int
    :rtype: int
    """

    if target < 0 or len(coins) <= 0:
        return 0
    if target == 0:
        return 1

    return (
        num_coin_combos(coins[:-1], target)
        + num_coin_combos(coins, target - coins[-1])
    )


def count_lattice_paths(n, m):
    """
    Get number of paths from (0, 0) -> (m, n) only moving right or down.

    :type n: int
    :type m: int
    :rtype: int
    """
    # n x m lattice paths will always have n + m steps
    # out of n + m, count all possible downward steps
    # anything left is rightward
    return math.factorial(n + m) // math.factorial(n) // math.factorial(m)


def generate_number_spiral(ceiling):
    """
    Create a matrix of numbers that spiral outward from the center in a
    clockwise direction.

    :param ceiling: Maximum value for spiral
    :type m: int
    :return: Number spiral
    :rtype: 2D list of ints
    """

    # find dimensions needed for matrix...
    dim = int(math.ceil(math.sqrt(ceiling))) + 1

    # ...and allocate empty matrix
    spiral = [[None] * dim for _ in range(dim)]

    # stick a 1 in the center
    x = dim // 2
    y = dim // 2
    spiral[y][x] = 1  # type: ignore

    # consume steps until we've completed the matrix
    for i, step in enumerate(_outward_spiral_steps(), start=2):
        if i > ceiling:
            break

        x += step.dx
        y += step.dy
        spiral[y][x] = i

    # remove empty rows
    spiral = [x for x in spiral if any(x)]

    # transpose, remove empty rows, transpose back again
    spiral = zip(*spiral)
    spiral = [x for x in spiral if any(x)]
    spiral = list(zip(*spiral))

    return spiral


def _outward_spiral_steps():
    """
    Generate endless successive steps used to create a 2d outward number
    spiral.

    :yield: Tuple representing direction to move
    :rtype: (int, int)
    """
    Step = collections.namedtuple("Step", ["dx", "dy"])
    RIGHT = Step(1, 0)
    DOWN = Step(0, 1)
    LEFT = Step(-1, 0)
    UP = Step(0, -1)

    for n in itertools.count(start=1):
        if n % 2:
            yield RIGHT
            for _ in range(n):
                yield DOWN
            for _ in range(n):
                yield LEFT

        else:
            yield LEFT
            for _ in range(n):
                yield UP
            for _ in range(n):
                yield RIGHT


def get_longest_matrix_value(matrix):
    """
    Find the 'longest' value in a matrix of strings, ints, or a mix of both.

    :type matrix: 2D list of ints, strings, or a mix
    :return: Length of 'longest' value in matrix
    :rtype: int
    """
    m = 0

    for i in matrix:
        for j in i:

            if j is None:
                continue

            if len(str(j)) > m:
                m = len(str(j))
    return m


def get_matrix_diagonals_sum(matrix):
    """
    Find the sum along both diagonals of an n x n matrix.

    :type matrix: 2D list of ints
    :return: Sum along both diagonals.
    :rtype: int
    """

    d_sum = 0

    ceiling = len(matrix) - 1

    i = 0
    while i <= ceiling:
        d_sum += matrix[i][i]  # (0, 0) + (1, 1) + ... + (n-1, n-1) + (n, n)
        d_sum += matrix[i][ceiling - i]  # (0, n) + (1, n-1) + ... + (n, 0)
        i += 1

    # ...but we don't want to double-add the midpoint if one exists
    if len(matrix) % 2:
        midpoint = ceiling // 2
        d_sum -= matrix[midpoint][midpoint]

    return d_sum


def print_matrix(matrix):
    """
    Pretty print a matrix.

    :type matrix: 2D list of ints, strings, or a mix
    """

    if len(matrix) == 0:
        print("Matrix is empty!")
        return

    # get size of largest matrix element for padding prints
    padding = get_longest_matrix_value(matrix)

    # print it out
    p = ""
    for row in matrix:
        for ele in row:

            # number spiral matrices use None for empty entries
            if ele is None:
                ele = ' ' * padding

            # pad for pretty print
            p += f"{str(ele).rjust(padding, ' ')} "

        if p:
            print(p)
            p = ""
