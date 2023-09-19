from utils import euler_lib


def main():

    target = 500

    divisors = 0
    triangle = 0

    i = 0
    while divisors <= target:
        i += 1

        triangle = euler_lib.get_triangle_number(i)
        divisors = euler_lib.get_number_of_factors(triangle)

    return triangle


if __name__ == "__main__":
    print(main())
