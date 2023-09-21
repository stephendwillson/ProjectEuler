from utils import euler_lib


def main():

    n = 1000  # 2^n

    total = euler_lib.sum_digits(2 ** n)

    return total


if __name__ == "__main__":
    print(main())
