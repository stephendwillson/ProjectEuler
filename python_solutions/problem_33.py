import fractions
import math


def main():

    # find curious fractions
    curious_fractions = get_curious_fractions()

    # multiply 'em all together
    prod = fractions.Fraction(1, 1)
    for fraction in curious_fractions:
        prod *= fraction

    # reduce product fraction to lowest common terms
    reduced_prod = prod / math.gcd(prod.numerator, prod.denominator)

    return reduced_prod.denominator


def is_curious_fraction(num, denom):
    """
    Check if a fraction meets the constraints provided in Problem 33.
    Fraction must be less than 1, contain 2 digits in both numerator and
    denominator, and can be simplified correctly by incorrectly cancelling
    one digit from both the numerator and denominator.

    :param num: Numerator of fraction to check
    :type num: int
    :param denom: Denominator of the fraction to check
    :type denom: int
    :rtype: bool
    """

    if num % 10 == 0 or denom % 10 == 0:
        return False

    fraction = fractions.Fraction(num, denom)
    num_digits = str(num)
    denom_digits = str(denom)

    for digit in num_digits:
        if digit in denom_digits:

            # naively simplify fraction
            new_num = int(num_digits.replace(digit, '', 1))
            new_denom = int(denom_digits.replace(digit, '', 1))
            new_fraction = fractions.Fraction(new_num, new_denom)

            if fraction == new_fraction:
                return True

    return False


def get_curious_fractions():
    """
    Generate a list of all curious fractions less than 1 that contain
    two digits in both the numerator and denominator.

    :return: List of curious fractions
    :rtype: List[fractions.Fraction]
    """

    curious_fractions = []

    for num in range(10, 100):  # 2 digits in num + denom
        for denom in range(num + 1, 100):

            if is_curious_fraction(num, denom):
                curious_fractions.append(fractions.Fraction(num, denom))

    return curious_fractions


if __name__ == "__main__":
    print(main())
