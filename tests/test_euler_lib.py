import os
import importlib
import pytest

import utils.euler_lib as euler_lib


def test_is_palindrome():

    assert euler_lib.is_palindrome(0)

    assert euler_lib.is_palindrome(11)
    assert euler_lib.is_palindrome(1234321)

    assert not euler_lib.is_palindrome(10)
    assert not euler_lib.is_palindrome(234321)
    assert not euler_lib.is_palindrome(123432)


def test_is_leap_year():

    # year 0 is a can of worms, just treating as a leap year like in Java
    assert euler_lib.is_leap_year(0)

    assert euler_lib.is_leap_year(4)
    assert euler_lib.is_leap_year(800)
    assert euler_lib.is_leap_year(1996)
    assert euler_lib.is_leap_year(2000)

    assert not euler_lib.is_leap_year(1)
    assert not euler_lib.is_leap_year(99)
    assert not euler_lib.is_leap_year(100)
    assert not euler_lib.is_leap_year(1500)
    assert not euler_lib.is_leap_year(1900)
    assert not euler_lib.is_leap_year(1994)


def test_get_word_score():

    assert 0 == euler_lib.get_word_score("")

    assert 1 == euler_lib.get_word_score("a")
    assert 1 == euler_lib.get_word_score("A")
    assert 13 == euler_lib.get_word_score("m")
    assert 13 == euler_lib.get_word_score("M")
    assert 26 == euler_lib.get_word_score("z")
    assert 26 == euler_lib.get_word_score("Z")

    assert 293 == euler_lib.get_word_score("testsomelongerstrings")

    # numerics, special characters, spaces all unsupported, don't count
    assert 0 == euler_lib.get_word_score("4")
    assert 18 == euler_lib.get_word_score("r4")
    assert 0 == euler_lib.get_word_score("?!?")
    assert 6 == euler_lib.get_word_score("4*a?b!c?3")
    assert 63 == euler_lib.get_word_score("s p a c e s")


def test_rotate():

    assert "" == euler_lib.rotate("", 3)
    assert "a" == euler_lib.rotate("a", 10)

    # test borders of 0 incl. negative
    assert "fabcde" == euler_lib.rotate("abcdef", -1)
    assert "abcdef" == euler_lib.rotate("abcdef", 0)
    assert "bcdefa" == euler_lib.rotate("abcdef", 1)
    assert "cdefab" == euler_lib.rotate("abcdef", 2)

    # rotate same length as string
    assert "abcdef" == euler_lib.rotate("abcdef", 6)

    # rotate greater than string length
    assert "cdefab" == euler_lib.rotate("abcdef", 8)

    assert " World!Hello," == euler_lib.rotate("Hello, World!", 6)


def test_sum_digits():

    assert 0 == euler_lib.sum_digits(0)
    assert 0 == euler_lib.sum_digits(0000000)

    assert 1 == euler_lib.sum_digits(1)
    assert 2 == euler_lib.sum_digits(1000000001)
    
    assert 3 == euler_lib.sum_digits(12)
    assert 10 == euler_lib.sum_digits(1234)


def test_get_triangle_number():

    # triangle number is 1 -> n, ignore n < 1
    assert 0 == euler_lib.get_triangle_number(-1)
    assert 0 == euler_lib.get_triangle_number(0)

    assert 1 == euler_lib.get_triangle_number(1)
    assert 15 == euler_lib.get_triangle_number(5)
    assert 500500 == euler_lib.get_triangle_number(1000)


def test_sum_of_squares():

    # sums squares 1 -> n, ignore n < 1
    assert 0 == euler_lib.sum_of_squares(-100)
    assert 0 == euler_lib.sum_of_squares(0)

    assert 1 == euler_lib.sum_of_squares(1)
    assert 5 == euler_lib.sum_of_squares(2)
    assert 14 == euler_lib.sum_of_squares(3)
    assert 338350 == euler_lib.sum_of_squares(100)


def test_square_of_sums():

    # square of sums for 1 -> n, ignore n < 1
    assert 0 == euler_lib.square_of_sums(-1)
    assert 0 == euler_lib.square_of_sums(0)

    assert 1 == euler_lib.square_of_sums(1)
    assert 9 == euler_lib.square_of_sums(2)
    assert 25502500 == euler_lib.square_of_sums(100)
    assert 250500250000 == euler_lib.square_of_sums(1000)


def test_get_least_common_multiple():

    # negatives and 0s
    assert 8 == euler_lib.get_least_common_multiple(-4, 8)
    assert 0 == euler_lib.get_least_common_multiple(0, 0)
    assert 0 == euler_lib.get_least_common_multiple(0, 10)

    # co-primes
    assert 15 == euler_lib.get_least_common_multiple(3, 5)

    # equals
    assert 7 == euler_lib.get_least_common_multiple(7, 7)

    # one is multiple of the other
    assert 12 == euler_lib.get_least_common_multiple(6, 12)

    # a big 'un
    assert 999999000000 == euler_lib.get_least_common_multiple(999999, 1000000)


def test_get_number_of_factors():

    # 0 and borders
    assert 0 == euler_lib.get_number_of_factors(-1)
    assert 0 == euler_lib.get_number_of_factors(0)
    assert 1 == euler_lib.get_number_of_factors(1)

    # primes
    assert 2 == euler_lib.get_number_of_factors(2)
    assert 2 == euler_lib.get_number_of_factors(3)
    assert 2 == euler_lib.get_number_of_factors(997)

    assert 3 == euler_lib.get_number_of_factors(4)
    assert 6 == euler_lib.get_number_of_factors(12)
    assert 9 == euler_lib.get_number_of_factors(36)
    assert 24 == euler_lib.get_number_of_factors(360)
    assert 16 == euler_lib.get_number_of_factors(1000)


def test_get_factors():

    # 0 and borders
    assert {} == euler_lib.get_factors(-1)
    assert {} == euler_lib.get_factors(0)
    assert {1} == euler_lib.get_factors(1)

    assert {1, 2} == euler_lib.get_factors(2)
    assert {1, 2, 4} == euler_lib.get_factors(4)
    assert {1, 2, 5, 10} == euler_lib.get_factors(10)
    assert {1, 97} == euler_lib.get_factors(97)


def test_get_proper_factors():

    # 0 and borders
    assert {} == euler_lib.get_proper_factors(-1)
    assert {} == euler_lib.get_proper_factors(0)
    assert {} == euler_lib.get_proper_factors(1)

    assert {1} == euler_lib.get_proper_factors(2)
    assert {1, 2} == euler_lib.get_proper_factors(4)
    assert {1, 2, 5} == euler_lib.get_proper_factors(10)
    assert {1} == euler_lib.get_proper_factors(97)


def test_get_prime_factors():

    # 0 and borders
    assert [] == euler_lib.get_prime_factors(-1)
    assert [] == euler_lib.get_prime_factors(0)
    assert [] == euler_lib.get_prime_factors(1)

    assert [2] == euler_lib.get_prime_factors(2)
    assert [3] == euler_lib.get_prime_factors(3)
    assert [2, 2] == euler_lib.get_prime_factors(4)
    assert [2, 5] == euler_lib.get_prime_factors(10)
    assert [97] == euler_lib.get_prime_factors(97)
    assert [2, 3, 5, 7] == euler_lib.get_prime_factors(210)


def test_is_prime():

    # 0 and borders
    assert not euler_lib.is_prime(-13)
    assert not euler_lib.is_prime(-1)
    assert not euler_lib.is_prime(0)
    assert not euler_lib.is_prime(1)

    assert euler_lib.is_prime(2)
    assert euler_lib.is_prime(3)
    assert not euler_lib.is_prime(4)
    assert not euler_lib.is_prime(100)
    assert euler_lib.is_prime(101)
    assert euler_lib.is_prime(9973)
    assert not euler_lib.is_prime(1000000)


def test_is_prime_fast():

    # 0 and borders
    assert not euler_lib.is_prime_fast(-13)
    assert not euler_lib.is_prime_fast(-1)
    assert not euler_lib.is_prime_fast(0)
    assert not euler_lib.is_prime_fast(1)

    assert euler_lib.is_prime_fast(2)
    assert euler_lib.is_prime_fast(3)
    assert not euler_lib.is_prime_fast(4)
    assert not euler_lib.is_prime_fast(100)
    assert euler_lib.is_prime_fast(101)
    assert euler_lib.is_prime_fast(9973)
    assert not euler_lib.is_prime_fast(1000000)


def test_is_circular_prime():

    # 0 and borders
    assert not euler_lib.is_circular_prime(-13)
    assert not euler_lib.is_circular_prime(-1)
    assert not euler_lib.is_circular_prime(0)
    assert not euler_lib.is_circular_prime(1)

    # single digit
    assert euler_lib.is_circular_prime(2)
    assert euler_lib.is_circular_prime(7)
    assert not euler_lib.is_circular_prime(8)

    # two digits
    assert euler_lib.is_circular_prime(11)
    assert euler_lib.is_circular_prime(13)
    assert euler_lib.is_circular_prime(31)
    assert not euler_lib.is_circular_prime(16)
    assert not euler_lib.is_circular_prime(61)

    # three+ digits
    assert not euler_lib.is_circular_prime(123)
    assert not euler_lib.is_circular_prime(312)
    assert not euler_lib.is_circular_prime(231)

    assert euler_lib.is_circular_prime(197)
    assert euler_lib.is_circular_prime(719)
    assert euler_lib.is_circular_prime(971)

    assert euler_lib.is_circular_prime(3779)
    assert euler_lib.is_circular_prime(9377)
    assert euler_lib.is_circular_prime(7937)
    assert euler_lib.is_circular_prime(7793)

    assert not euler_lib.is_circular_prime(12345)


def test_is_left_right_truncatable_prime():

    # 0 and borders
    assert not euler_lib.is_left_right_truncatable_prime(-13)
    assert not euler_lib.is_left_right_truncatable_prime(-1)
    assert not euler_lib.is_left_right_truncatable_prime(0)
    assert not euler_lib.is_left_right_truncatable_prime(1)

    assert euler_lib.is_left_right_truncatable_prime(2)

    # single digit prime and non-prime
    assert euler_lib.is_left_right_truncatable_prime(3)
    assert not euler_lib.is_left_right_truncatable_prime(6)

    # double digit prime and not prime
    assert not euler_lib.is_left_right_truncatable_prime(41)
    assert not euler_lib.is_left_right_truncatable_prime(15)
    assert euler_lib.is_left_right_truncatable_prime(23)

    # 3797, 797, 97, 7/379, 37, 3 all primes
    assert euler_lib.is_left_right_truncatable_prime(3797)

    # 9 not prime
    assert not euler_lib.is_left_right_truncatable_prime(9973)

    # only truncatable left to right, right to left ends up with 2 == not prime
    assert not euler_lib.is_left_right_truncatable_prime(233993)

    # 12 not prime
    assert not euler_lib.is_left_right_truncatable_prime(12345)


def test_get_primes_below_n():

    # 0 and borders
    assert [] == euler_lib.get_primes_below_n(-13)
    assert [] == euler_lib.get_primes_below_n(-1)
    assert [] == euler_lib.get_primes_below_n(0)
    assert [] == euler_lib.get_primes_below_n(1)

    assert [2] == euler_lib.get_primes_below_n(2)

    assert [2, 3] == euler_lib.get_primes_below_n(3)
    assert [2, 3, 5, 7] == euler_lib.get_primes_below_n(10)
    assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] == euler_lib.get_primes_below_n(30)
    assert [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] == euler_lib.get_primes_below_n(31)


def test_get_triangle_max_path_sum():

    # single level, 0 and borders
    triangle = [[-1]]
    assert -1 == euler_lib.get_triangle_max_path_sum(triangle)
    triangle = [[0]]
    assert 0 == euler_lib.get_triangle_max_path_sum(triangle)
    triangle = [[1]]
    assert 1 == euler_lib.get_triangle_max_path_sum(triangle)

    # negatives
    triangle = [
        [-1],
        [-2, 3]
    ]
    assert 2 == euler_lib.get_triangle_max_path_sum(triangle)

    # 1 -> 3
    triangle = [
        [1],
        [2, 3]
    ]
    assert 4 == euler_lib.get_triangle_max_path_sum(triangle)

    # 1 -> 3 -> 6
    triangle = [
        [1],
        [2, 3],
        [4, 5, 6]
    ]
    assert 10 == euler_lib.get_triangle_max_path_sum(triangle)

    # 1 -> 3 -> 6 -> 10
    triangle = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    assert 20 == euler_lib.get_triangle_max_path_sum(triangle)

    # 3 -> 7 -> 4 -> 9
    triangle = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]
    assert 23 == euler_lib.get_triangle_max_path_sum(triangle)


def test_get_recurring_decimal_cycle():

    # negatives
    assert None == euler_lib.get_recurring_decimal_cycle(-1, 2)
    assert "3" == euler_lib.get_recurring_decimal_cycle(-1, 3)
    assert "714285" == euler_lib.get_recurring_decimal_cycle(-5, 7)

    # 0 and borders
    assert None == euler_lib.get_recurring_decimal_cycle(0, 1)
    assert None == euler_lib.get_recurring_decimal_cycle(1, 0)
    assert None == euler_lib.get_recurring_decimal_cycle(0, -1)
    assert None == euler_lib.get_recurring_decimal_cycle(1, 1)

    assert None == euler_lib.get_recurring_decimal_cycle(1, 2)
    assert "3" == euler_lib.get_recurring_decimal_cycle(1, 3)
    assert None == euler_lib.get_recurring_decimal_cycle(1, 4)
    assert "142857" == euler_lib.get_recurring_decimal_cycle(1, 7)
    assert "714285" == euler_lib.get_recurring_decimal_cycle(5, 7)
    assert "142857" == euler_lib.get_recurring_decimal_cycle(22, 7)


def test_num_coin_combos():

    # 0 coins
    coins = []
    assert 0 == euler_lib.num_coin_combos(coins, 0)

    # 0 target and borders
    coins = [1, 2, 5]
    assert 0 == euler_lib.num_coin_combos(coins, -1)
    assert 0 == euler_lib.num_coin_combos(coins, 0)
    assert 1 == euler_lib.num_coin_combos(coins, 1)
    assert 2 == euler_lib.num_coin_combos(coins, 2)

    coins = [1, 5, 10, 25]
    assert 1 == euler_lib.num_coin_combos(coins, 2)
    assert 2 == euler_lib.num_coin_combos(coins, 5)
    assert 4 == euler_lib.num_coin_combos(coins, 10)


def test_count_lattice_paths():

    # no movement
    assert 1 == euler_lib.count_lattice_paths(0, 0)
    
    # only down
    assert 1 == euler_lib.count_lattice_paths(1, 0)
    assert 1 == euler_lib.count_lattice_paths(3, 0)

    # only right
    assert 1 == euler_lib.count_lattice_paths(0, 1)
    assert 1 == euler_lib.count_lattice_paths(0, 3)

    assert 2 == euler_lib.count_lattice_paths(1, 1)
    assert 3 == euler_lib.count_lattice_paths(2, 1)
    assert 3 == euler_lib.count_lattice_paths(1, 2)
    assert 6 == euler_lib.count_lattice_paths(2, 2)
    assert 10 == euler_lib.count_lattice_paths(2, 3)


def test_generate_number_spiral():

    # 0 and borders
    expected = [()]
    assert expected == euler_lib.generate_number_spiral(0)

    expected = [(1,)]
    assert expected == euler_lib.generate_number_spiral(1)

    expected = [(1, 2)]
    assert expected == euler_lib.generate_number_spiral(2)

    # complete 2x2
    expected = [
        (1, 2),
        (4, 3)
    ]
    assert expected == euler_lib.generate_number_spiral(4)

    # complete 3x3
    expected = [
        (7, 8, 9),
        (6, 1, 2),
        (5, 4, 3)
    ]
    assert expected == euler_lib.generate_number_spiral(9)

    # empty bottom left
    expected = [
        (1, 2),
        (None, 3)
    ]
    assert expected == euler_lib.generate_number_spiral(3)

    # empty top right
    expected = [
        (7, None, None),
        (6, 1, 2),
        (5, 4, 3)
    ]
    assert expected == euler_lib.generate_number_spiral(7)

    # empty bottom right
    expected = [
        (7, 8, 9, 10),
        (6, 1, 2, None),
        (5, 4, 3, None)
    ]
    assert expected == euler_lib.generate_number_spiral(10)


def test_get_longest_matrix_value():

    # empty
    matrix = []
    assert 0 == euler_lib.get_longest_matrix_value(matrix)

    # ints
    matrix = [
        [1, 22, 333],
        [4444, 55555, 666666],
        [7777777, 88888888, 999999999],
    ]
    assert 9 == euler_lib.get_longest_matrix_value(matrix)

    # strings
    matrix = [
        ["you", "say", "goodbye"],
        ["i", "say", "hello"],
        ["don't", "know", "why"],
    ]
    assert 7 == euler_lib.get_longest_matrix_value(matrix)

    # mix
    matrix = [
        ["one", 2, "three"],
        ["four", 55555, "six"],
        ["sleven", "ate", 999999999],
    ]
    assert 9 == euler_lib.get_longest_matrix_value(matrix)


def test_is_pandigital():

    assert euler_lib.is_pandigital(1)

    assert euler_lib.is_pandigital(1234)
    assert euler_lib.is_pandigital(1324)
    assert euler_lib.is_pandigital(4231)

    assert euler_lib.is_pandigital(123456789)
    assert euler_lib.is_pandigital(381654729)

    assert not euler_lib.is_pandigital(-1)
    assert not euler_lib.is_pandigital(0)

    assert not euler_lib.is_pandigital(2)

    assert not euler_lib.is_pandigital(11)
    assert not euler_lib.is_pandigital(122)
    assert not euler_lib.is_pandigital(113456789)