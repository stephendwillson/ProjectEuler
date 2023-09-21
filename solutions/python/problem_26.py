from utils import euler_lib


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


if __name__ == "__main__":
    print(main())
