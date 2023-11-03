import math

from utils import euler_lib


def main():

    # digits can be 1-9 and no repeated digits = 9! possible pandigital #s
    # max value of prod of two 5-digit #s = 9,999,800,001
    # 10 digits and not pandigital - only consider products up to sqrt(ceiling)
    ceiling = math.factorial(9)
    pandigitals = set()

    for multiplicand in range(3, int(math.sqrt(ceiling)) + 1):
        for multiplier in range(3, ceiling // multiplicand + 1):

            prod = multiplier * multiplicand
            mult_str = "".join([str(multiplier),
                                str(multiplicand),
                                str(prod)])

            if len(mult_str) != 9:
                continue

            if euler_lib.is_pandigital(mult_str):
                pandigitals.add(prod)

    return sum(pandigitals)


if __name__ == "__main__":
    print(main())
