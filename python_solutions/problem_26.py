import euler_lib


def main():

    long_denom = 0
    long_cycle_length = 0

    denom_ceiling = 1001

    # problem only asks for numerator == 1
    # in theory should work with any num / denom
    for num in range(1, 2):
        for denom in range(1, denom_ceiling):

            repeat = euler_lib.get_recurring_decimal_cycle(num, denom)
            if repeat is None:
                continue

            # keep track of numerator, denominator, and length of cycle for
            # longest found so far
            if len(repeat) > long_cycle_length:
                long_denom = denom
                long_cycle_length = len(repeat)

    return long_denom


def description():

    desc = """
https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2	    = 	0.5
    1/3	    = 	0.(3)
    1/4	    = 	0.25
    1/5	    = 	0.2
    1/6	    = 	0.1(6)
    1/7	    = 	0.(142857)
    1/8	    = 	0.125
    1/9	    = 	0.(1)
    1/10    = 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""
    print(desc, end="")


PE_NAME = "RECIPROCAL CYCLES"
PE_SOLUTION = 983

if __name__ == "__main__":
    print(main())
