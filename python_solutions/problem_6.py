from utils import euler_lib


def main():

    n = 100

    summed = euler_lib.sum_of_squares(n)
    squared = euler_lib.square_of_sums(n)
    delta = squared - summed

    return delta


if __name__ == "__main__":
    print(main())
