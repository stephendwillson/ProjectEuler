"""
sdwillso
Common functionality for solving Project Euler problems.
"""
# pylint: disable=invalid-name
import math
import string
import collections
import itertools
import random


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

    return n * (n + 1) / 2


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


def get_least_common_multiple(a, b):
    """
    Calculate the least common multiple of 2 numbers, a and b.

    :type a: int
    :type b: int
    :rtype: int
    """

    return abs(a*b) // math.gcd(a, b)


def get_number_of_factors(n):
    """
    Find only the number of factors of a given number via prime factorization.
    Saves some time over getting a list of all factors and counting elements.

    :type n: int
    :rtype: int
    """

    prime_factors = get_prime_factors(n)

    num_factors = 1
    prev_factor = None
    factor_count = 0

    # Calculate number of factors using prime factorization
    for factor in prime_factors:

        if prev_factor is None:
            prev_factor = factor
            factor_count = 1
        elif prev_factor == factor:
            factor_count += 1
        else:
            num_factors *= (factor_count + 1)
            prev_factor = factor
            factor_count = 1

    num_factors *= (factor_count + 1)

    return num_factors


def get_factors(n):
    """
    Find all factors of a number.

    :type n: int
    :rtype: set[int]
    """

    factors = set()

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)

    # don't forget to add 1 and self as factors
    factors.add(1)
    factors.add(n)

    return factors


def get_proper_factors(n):
    """
    Find all factors of n except for self.

    :type n: int
    :rtype: set[int]
    """

    factors = get_factors(n)

    if n in factors:
        factors.remove(n)

    return factors


def get_prime_factors(n):
    """
    Find all prime factors of a number.

    :type n: int
    :rtype: list[int]
    """

    p_factors = []

    # Check for 2 as a factor
    while n % 2 == 0:
        p_factors.append(2)
        n //= 2

    # Check odd factors up to sqrt(n)
    for c in range(3, int(math.sqrt(n)) + 1, 2):
        while n % c == 0:
            p_factors.append(c)
            n //= c

    # If n is still greater than 2, it must be prime
    if n > 2:
        p_factors.append(n)

    return p_factors


def is_prime(n):
    """
    Test if a number is prime using the AKS (Agrawal-Kayal-Saxena) test.

    :param n: Number to be tested
    :type n: int
    :rtype: bool
    """

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    r = 5
    while r * r <= n:
        if n % r == 0 or n % (r + 2) == 0:
            return False
        r += 6
    return True


def is_prime_fast(n, k=5):
    """
    Test if a number is prime using Miller-Rabin primality test.
    This is a faster test but because it is probabalistic, there's a chance
    of some janky math with larger numbers.

    :param n: Number to be tested
    :type n: int
    :param k: Number of iterations. Higher values == more acc. Defaults to 5
    :type k: int, optional
    :rtype: bool
    """

    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Find r and d such that n = 2^r * d + 1
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # k iterations of Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x in (1, n - 1):
            continue

        for _ in range(r - 1):

            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
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


def get_primes_below_n(ceiling):
    """
    Get a list of all primes below the value of ceiling.
    Uses sieve of Eratosthenes.

    :param ceiling: Upper limit for prime search
    :type ceiling: int
    :return: Every prime below n
    :rtype: list[int]
    """

    # init empty list
    sieve = [True] * (ceiling + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(ceiling)) + 1):

        if sieve[i]:
            sieve[i*i::i] = [False] * ((ceiling - i*i) // i + 1)

    return [i for i in range(ceiling + 1) if sieve[i]]


def get_triangle_max_path_sum(t):
    """
    Find the sum of the vertical path through a number triangle with the
    highest max value.

    :param t: Number triangle
    :type t: list[int][int]
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
    :rtype: list[int][int]
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

    :type matrix: list[int|str][int|str]
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

    :type matrix: list[int][int]
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

    :type matrix: list[int|str][int|str]
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
