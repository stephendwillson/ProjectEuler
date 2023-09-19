from utils import euler_lib


def main():

    # The smallest positive number that is evenly divisible by all of the
    # numbers from 1 to 20 is the least common multiple of those numbers.
    n = 20
    lcm = 1

    for i in range(2, n + 1):
        lcm = euler_lib.get_least_common_multiple(lcm, i)

    return lcm


if __name__ == "__main__":
    print(main())
