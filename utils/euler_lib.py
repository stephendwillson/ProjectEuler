"""
sdwillso
Common functionality for solving Project Euler problems.
"""

import math
import string
import collections
import itertools
import random


def is_palindrome(val, base=10):
    """
    Check if a string or integer is a palindrome.

    Optionally, specify a base to test if an integer is a palindrome in that base.

    :param val: Value to test for palindromicity.
    :type val: str or int
    :param base: Base to test int, defaults to 10.
    :type base: int, optional
    :rtype: bool
    """

    if isinstance(val, str):
        return val == val[::-1]

    digits = []
    if isinstance(val, int):

        while val > 0:
            digits.append(val % base)
            val //= base

        return digits == digits[::-1]

    return False


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

    if len(s) == 0:
        return s

    # make sure to handle number of rotations > input string length
    rotation = n % len(s)

    return s[rotation:] + s[:rotation]


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

    if n < 1:
        return 0

    return n * (n + 1) // 2


def sum_of_squares(n):
    """
    Calculate sum of all squares from 1 through n.
    1^2 + 2^2 + ... + (n-1)^2 + n^2

    :type n: int
    :rtype: int
    """

    if n < 1:
        return 0

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

    if n < 1:
        return 0

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

    # lcm involving 0 is always 0
    if a == 0 or b == 0:
        return 0

    return abs(a*b) // math.gcd(a, b)


def get_number_of_factors(n):
    """
    Find only the number of factors of a given number via prime factorization.
    Saves some time over getting a list of all factors and counting elements.

    :type n: int
    :rtype: int
    """

    if n < 1:
        return 0

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

    # no factors for negative numbers
    if n < 1:
        return {}

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

    # negatives, 0, and 1 have no proper factors
    if n < 2:
        return {}

    factors = get_factors(n)

    if n in factors:
        factors.remove(n)

    return factors


def get_prime_factors(n):
    """
    Find all prime factors of a number via trial division.

    :type n: int
    :rtype: list[int]
    """

    if n < 2:
        return []

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

    n_str = str(n)

    # check if the number itself is prime
    if not is_prime(n):
        return False

    primes = set()

    # check if all rotations of the number are prime
    for i in range(1, len(n_str)):

        rotated_n = int(rotate(n_str, i))

        # skip circular primes we've already tested
        if rotated_n in primes:
            continue

        if not is_prime(rotated_n):
            return False

        primes.add(rotated_n)

    return True


def is_left_right_truncatable_prime(n):
    """
    Test if a number is a prime that is truncatable both from left to right
    and right to left.

    :type n: int
    :rtype: bool
    """

    if not is_prime(n):
        return False

    # strip digits off the end
    tmp = n // 10
    while tmp > 0:
        if not is_prime(tmp):
            return False
        tmp //= 10

    # strip digits off the beginning
    length = len(str(n))
    while length > 1:
        n = int(str(n)[1:])
        length -= 1
        if not is_prime(n):
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

    if ceiling < 2:
        return []

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
    :type t: list[list[int]]
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
    :rtype: str, None
    """

    if denominator == 0:
        return None

    repeat = ""

    # deal with negatives
    numerator = abs(numerator)
    denominator = abs(denominator)

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
    :type coins: list of int
    :param target: Amount coins should add up to
    :type target: int
    :return: Total number of combinations
    :rtype: int
    """

    if target < 1:
        return 0

    # list to store number of combinations for each possible value of
    # target and each possible coin denomination
    combos = [0 for _ in range(target + 1)]

    # if the target is 0, there is one combination
    combos[0] = 1

    # update number of combinations for each possible value of target and
    # each possible coin denomination
    for coin in coins:
        for j in range(coin, target + 1):
            combos[j] += combos[j-coin]

    # last element of array will be total combos
    return combos[target]


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
    :rtype: list[tuple[int, int]]
    """

    if ceiling == 0:
        return [()]

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


def is_pandigital(n):
    """
    Check if a number is pandigital (contains all the digits from
    1 to the length of the number exactly once). Does not take into
    account 0s. Only considers base 10.

    :type n: int
    :rtype: bool
    """

    n_str = str(n)

    # grab every digit from 1 to length of test number
    digits = [str(x) for x in range(1, len(n_str) + 1)]

    return set(n_str) == set(digits)


def is_permutation(a, b):
    """
    Check if 'a' and 'b' are permutations of each other.

    :type a: int
    :type b: int
    :rtype: bool
    """

    str_a = sorted(str(abs(a)))
    str_b = sorted(str(abs(b)))

    return str_a == str_b
