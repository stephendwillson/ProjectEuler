import math

from utils import euler_lib


def main():

    n = 100

    fact = math.factorial(n)
    digit_sum = euler_lib.sum_digits(fact)

    return digit_sum


if __name__ == "__main__":
    print(main())
